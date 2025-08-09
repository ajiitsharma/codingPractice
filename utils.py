import os
import argparse

class TestRunner:
    def __init__(self, solve_fn, description="Run test cases for solve(n, m)."):
        """
        :param solve_fn: Function to be tested (must take n, m as arguments).
        :param description: CLI description for argparse.
        """
        self.solve_fn = solve_fn
        self.description = description

    def read_test_cases(self, file_path):
        """Read test cases from input file."""
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        t = int(lines[0])
        return [tuple(map(int, line.split())) for line in lines[1:t+1]]

    def read_expected_results(self, file_path):
        """Read expected results from file."""
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def compare_results(self, test_cases, expected_results):
        """Compare computed results with expected results."""
        errors = []
        for idx, (n, m) in enumerate(test_cases):
            computed = self.solve_fn(n, m)
            expected = expected_results[idx]
            if str(computed) != expected:
                errors.append(
                    f"Test case {idx+1}: Input=({n}, {m}), "
                    f"Expected={expected}, Got={computed}"
                )
        return errors

    def compute_results(self, test_cases):
        """Compute results for all test cases."""
        return [str(self.solve_fn(n, m)) for n, m in test_cases]

    def run_from_cli(self):
        """Run the test runner from command line arguments."""
        parser = argparse.ArgumentParser(description=self.description)
        parser.add_argument("-i", "--input", required=True, help="Path to input file.")
        parser.add_argument("-o", "--output", help="Path to expected output file.")
        args = parser.parse_args()

        test_cases = self.read_test_cases(args.input)

        if args.output:
            if os.path.exists(args.output):
                # Compare mode
                expected_results = self.read_expected_results(args.output)
                if len(expected_results) != len(test_cases):
                    print("Error: Number of expected results does not match number of test cases.")
                    return
                errors = self.compare_results(test_cases, expected_results)
                if errors:
                    print("Mismatches found:")
                    for e in errors:
                        print(e)
                else:
                    print("All test cases passed!")
            else:
                # Save computed results to output file
                results = self.compute_results(test_cases)
                with open(args.output, "w") as f:
                    f.write("\n".join(results))
                print(f"Results saved to {args.output}")
        else:
            # Just print results
            results = self.compute_results(test_cases)
            print("\n".join(results))

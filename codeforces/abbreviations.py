'''
        https://codeforces.com/contest/2257/problem/A

        Creating Abbreviations
'''
def check_valid_abbreviation(words: list[str], tests: list[int]) -> str:
        '''
        returns YES if all tests strings as abbreviations are possible from words list else NO
        '''
        valid_first_chars = ''.join(list(set([w[0] for w in words])))

        test_first_chars = list(set(''.join(tests)))

        for c in test_first_chars:
                if not c.lower() in valid_first_chars:
                        return 'NO'

        return 'YES'

if __name__ == '__main__':
        N = int(input())

        for _ in range(N):
                W, T = list(map(int, input().strip().split()))
                words = []

                for j in range(W):
                        words.append(str(input()))

                tests = []
                for j in range(T):
                        tests.append(str(input()))

                result = check_valid_abbreviation(words, tests)

                print(result)
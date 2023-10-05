def solution(s):
    s_len = len(s)
    def check(s):
        for i in range(s_len//2):
            cnt = 0
            tmp = s[:i+1]
            for j in range(i+1, s_len, i+1):
                tmp2 = s[j:j+len(tmp)]
                if tmp2 == tmp:
                    cnt += 1
                else:
                    break
                if j == s_len - (i+1):
                    cnt += 1
                    return cnt
        return 1
    # move string
    for i in range(s_len):
        ans = check(s)
        if ans != 1:
            return ans
        s = s[1:] + s[0]
    return 1

"""
'abcabcabcabc' -> 4
'bcabcabcabca' -> 4
"""

if __name__ == '__main__':
    s = "abcabcabcabc"
    # s = "abcabcabcab"
    # s = "abcdefghijk321abcdefghijk32"
    # s = "bcabcabcabca"
    print(solution(s))
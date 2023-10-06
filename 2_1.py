def solution(n, b):
    def _numberToBase(n, b):
        if n == 0:
            return '0'
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        digits = digits[::-1]
        ans = ''
        for i in range(len(digits)):
            ans += str(digits[i])
        # print(ans)
        return ans

    def _to_len(z, n_len):
        len_diff = n_len - len(z)
        if len_diff > 0:
            z = '0' * len_diff + z
        return z

    def alg(n, b):
        n_len = len(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z = int(x, b) - int(y, b)
        z = _numberToBase(z, b)
        z = _to_len(z, n_len)
        return z

    tmp = [n]
    dup_tmp = []
    while True:
        # print("Progress: {}".format(len(tmp)), end='\r')
        ans = alg(tmp[-1], b)
        if ans in tmp:
            dup_idx = tmp.index(ans)
            if dup_idx in dup_tmp:
                return len(dup_tmp)
            else:
                dup_tmp.append(dup_idx)
        tmp.append(ans)
            
if __name__ == "__main__":
    n = '1211'
    b = 10
    print(solution(n, b))
    n = '210022'
    b = 3
    print(solution(n, b))
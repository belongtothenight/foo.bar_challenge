def solution(xs):
    def _max_current_product(xs):
        max_product = 1
        zero_count = 0
        for x in xs:
            if x != 0:
                max_product *= x
            else:
                zero_count += 1
        if zero_count == len(xs):
            return 0
        zero_flag = True if zero_count > 0 else False
        return max_product, zero_flag
    max_product, zero_flag = _max_current_product(xs)
    if max_product < 0:
        xs.sort()
        max_product = 1
        xs_neg = [x for x in xs if x < 0]
        xs_pos = [x for x in xs if x > 0]
        xs_neg_len = len(xs_neg)
        xs_pos_len = len(xs_pos)
        xs_neg_flag = True
        xs_pos_flag = True
        for i in range(0, xs_neg_len, 2):
            if i+1 < xs_neg_len:
                max_product *= xs_neg[i] * xs_neg[i+1]
                xs_neg_flag = False
        for i in range(xs_pos_len):
            max_product *= xs_pos[i]
            xs_pos_flag = False
        if xs_neg_flag and xs_pos_flag:
            if zero_flag:
                max_product = 0
            else:
                max_product = xs_neg[-1]
        if xs_neg_len == 1 and xs_pos_len == 1:
            max_product = xs_neg[0] * xs_pos[0]
    return str(max_product)

if __name__ == "__main__":
    # xs = [2, 0, 2, 2, 0]
    # print(solution(xs))
    # xs = [-2, -3, 4, -5]
    # print(solution(xs))
    # xs = [-2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5, -2, -3, 4, -5]
    # print(solution(xs))
    # xs = [-200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, -200, -300, 400, -500, 0, 0]
    # print(solution(xs))
    # xs = [1, 1, 1, 1, 1, 0]
    # print(solution(xs))
    # xs = [-1, -1, -1, -1, -1, 0]
    # print(solution(xs))
    # xs = [0]
    # print(solution(xs))
    # xs = [-1]
    # print(solution(xs))
    xs = [-1, 0]
    print(solution(xs))
    # xs = [-10]
    # print(solution(xs))
    xs = [-10, 1]
    print(solution(xs))
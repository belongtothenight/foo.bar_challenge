def solution(map):
    def _map_remove_obstacle(map):
        # generates a list of all possible maps
        # first check the current shortest path
        # then try to remove one obstacle along the path
        # keep record of all records until the shortest path is found or all possible maps are generated
        pass

    def _move(map, dir, steps):
        idx1 = steps[0][1]
        idx2 = steps[0][0]
        if dir == 'top':
            idx1 -= 1
        elif dir == 'left':
            idx2 -= 1
        elif dir == 'right':
            idx2 += 1
        elif dir == 'bottom':
            idx1 += 1
        else:
            pass
        tmp_step = [idx2, idx1]
        # ! check if out of range
        if idx1 < 0 or idx2 < 0:
            return tmp_step, False
        # ! check if index valid
        try:
            tmp_step_val = map[idx1][idx2]
        except:
            return tmp_step, False
        # ! check if visited
        if tmp_step in steps:
            return tmp_step, False
        # ! check if wall
        if tmp_step_val == 0:
            return tmp_step, True
        else:
            return tmp_step, False

    maze_h = len(map)
    maze_w = len(map[0])
    steps = [[maze_w-1, maze_h-1]]
    step_cnt = 1
    while True:
        #! find top, left, right, bottom for 0
        top_flag = False
        left_flag = False
        right_flag = False
        bottom_flag = False
        #* evaluate direction (top, left, right, bottom)
        top_tmp_step, top_flag = _move(map, 'top', steps)
        left_tmp_step, left_flag = _move(map, 'left', steps)
        right_tmp_step, right_flag = _move(map, 'right', steps)
        bottom_tmp_step, bottom_flag = _move(map, 'bottom', steps)
        #* check direction
        if top_flag:
            steps.insert(0, top_tmp_step)
            step_cnt += 1
        elif left_flag:
            steps.insert(0, left_tmp_step)
            step_cnt += 1
        elif right_flag:
            steps.insert(0, right_tmp_step)
            step_cnt += 1
        elif bottom_flag:
            steps.insert(0, bottom_tmp_step)
            step_cnt += 1
        #* check if reach the end
        if steps[0] == [0, 0]:
            return step_cnt


if __name__ == "__main__":
    # map = [[0, 1, 1, 0],
    #        [0, 0, 0, 1],
    #        [1, 1, 0, 0],
    #        [1, 1, 1, 0]]
    map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(solution(map))
    # map = [[0, 0, 0, 0, 0, 0],
    #        [1, 1, 1, 1, 1, 0],
    #        [0, 0, 0, 0, 0, 0],
    #        [0, 1, 1, 1, 1, 1],
    #        [0, 1, 1, 1, 1, 1],
    #        [0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print(solution(map))
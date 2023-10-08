def solution(map):
    def _depth_search(map):
        def __option_coordinate(coordinate):
            options = []
            if coordinate[0] != 0: # up
                options.append((coordinate[0] - 1, coordinate[1]))
            if coordinate[0] != len(map) - 1: # down
                options.append((coordinate[0] + 1, coordinate[1]))
            if coordinate[1] != 0: # left
                options.append((coordinate[0], coordinate[1] - 1))
            if coordinate[1] != len(map[0]) - 1: # right
                options.append((coordinate[0], coordinate[1] + 1))
            return options
        map_w = len(map[0])
        map_h = len(map)
        for i in range(map_h):
            print(map[i])
        start_point = (0, 0)
        end_point = (map_h - 1, map_w - 1)
        steps = [[start_point]]
        search_depth = 0
        while True:
            layer_cnt = 0
            for step in steps[search_depth]:
                options = __option_coordinate(step)
                #* remove wall
                tmp = []
                for op in options:
                    if map[op[0]][op[1]] == 1:
                        tmp.append(op)
                for op in tmp:
                    options.remove(op)
                #* remove visited
                tmp = []
                for op in options:
                    for i in range(len(steps)):
                        if op in steps[i]:
                            tmp.append(op)
                for op in tmp:
                    options.remove(op)
                #* reach the end
                if end_point in options:
                    return len(steps) + 1
                if len(steps) == search_depth + 1:
                    steps.append([])
                steps[search_depth + 1].extend(options)
                if len(steps[search_depth]) > 1:
                    layer_cnt += 1
                    if layer_cnt > (len(steps[search_depth])-1):
                        search_depth += 1
                        layer_cnt = 0
                else:
                    search_depth += 1
    
    def _wall_finder(map, mode="all"):
        #* List out the wall that is next to the path
        map_w = len(map[0])
        map_h = len(map)
        walls = []
        if mode == "path":
            for i in range(map_h):
                for j in range(map_w):
                    if map[i][j] == 1:
                        if i != 0: #* up
                            if map[i - 1][j] == 0:
                                walls.append((i, j))
                        if i != map_h - 1: #* down
                            if map[i + 1][j] == 0:
                                walls.append((i, j))
                        if j != 0: #* left
                            if map[i][j - 1] == 0:
                                walls.append((i, j))
                        if j != map_w - 1: #* right
                            if map[i][j + 1] == 0:
                                walls.append((i, j))
        elif mode == "all":
            for i in range(map_h):
                for j in range(map_w):
                    if map[i][j] == 1:
                        walls.append((i, j))
        return walls
    
    depth_list = []
    walls = _wall_finder(map)
    search_times = len(walls)
    print("Found {} walls".format(search_times))
    walls.insert(0, (0, 0))
    search_times += 1
    for idx, wall in enumerate(walls):
        print("Searching {}/{}".format(idx + 1, search_times))
        if idx == 0:
            depth_list.append(_depth_search(map))
        else:
            map[wall[0]][wall[1]] = 0
            depth_list.append(_depth_search(map))
            map[wall[0]][wall[1]] = 1
        print("Depth list: {}".format(depth_list))
    return min(depth_list)


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
    # map = [[0, 0],
    #        [1, 0]]
    map = [[0, 0], [1, 0]]
    print(solution(map))
    # map = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    #        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    #        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    #        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    #        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
    map = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
    print(solution(map))
    # map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(map))
    # map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(map))
    # map = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(map))
    map = [[0, 0, 0, 0, 1],
           [1, 0, 1, 1, 0],
           [1, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 1], [1, 0, 1, 1, 0], [1, 0, 0, 0, 0]]
    print(solution(map))

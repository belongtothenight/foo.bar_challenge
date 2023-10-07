def solution(map):
    def _simple_map(map):
        def __move(map, dir, steps):
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
            top_tmp_step, top_flag = __move(map, 'top', steps)
            left_tmp_step, left_flag = __move(map, 'left', steps)
            right_tmp_step, right_flag = __move(map, 'right', steps)
            bottom_tmp_step, bottom_flag = __move(map, 'bottom', steps)
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

    def _gen_nodes(map):
        nodes = []
        map_w = len(map[0])
        map_h = len(map)
        for idx_i in range(map_w):
            for idx_j in range(map_h):
                if map[idx_i][idx_j] == 0:
                    idx1_top = idx_i-1
                    idx2_top = idx_j
                    idx1_left = idx_i
                    idx2_left = idx_j-1
                    idx1_right = idx_i
                    idx2_right = idx_j+1
                    idx1_bottom = idx_i+1
                    idx2_bottom = idx_j
                    try:
                        val_top = map[idx1_top][idx2_top]
                    except:
                        val_top = 1
                    try:
                        val_left = map[idx1_left][idx2_left]
                    except:
                        val_left = 1
                    try:
                        val_right = map[idx1_right][idx2_right]
                    except:
                        val_right = 1
                    try:
                        val_bottom = map[idx1_bottom][idx2_bottom]
                    except:
                        val_bottom = 1
                    if idx1_top < 0 or idx2_top < 0 or idx1_top >= map_w or idx2_top >= map_h:
                        val_top = 1
                    if idx1_left < 0 or idx2_left < 0 or idx1_left >= map_w or idx2_left >= map_h:
                        val_left = 1
                    if idx1_right < 0 or idx2_right < 0 or idx1_right >= map_w or idx2_right >= map_h:
                        val_right = 1
                    if idx1_bottom < 0 & idx2_bottom < 0 or idx1_right >= map_w or idx2_right >= map_h:
                        val_bottom = 1
                    if (val_top == 0 and val_bottom == 0) or (val_left == 0 and val_right == 0):
                        continue
                    if (val_top == 0 or val_left == 0 or val_right == 0 or val_bottom == 0):
                        nodes.insert(0, [idx_i, idx_j])
        # print(nodes)
        return nodes

    def _find_shortest_path(nodes):
        def __is_connected(node1, node2):
            # * check if node1 and node2 are connected
            # * return True if connected, False if not
            if (node1[0] == node2[0]):
                return True, abs(node2[1]-node1[1])
            elif(node1[1] == node2[1]):
                return True, abs(node2[0]-node1[0])
            else:
                return False, 0
        shortest_path = []
        shortest_path_step_cnt = 0
        possible_paths = []
        possible_paths_step_cnt = []
        nodes_stepped_on_flag = [True] + [False]*(len(nodes)-1)
        while False in nodes_stepped_on_flag:
            availabe_nodes = nodes.copy()
            tmp_path = [nodes[0]]
            tmp_path_step_cnt = 1
            while [0, 0] not in tmp_path:
                try:
                    availabe_nodes.remove(tmp_path[-1])
                except:
                    pass
                tmp_possible_steps = []
                tmp_possible_steps_step_cnt = []
                for idx, node in enumerate(availabe_nodes):
                    is_connected, step = __is_connected(tmp_path[0], node)
                    if is_connected:
                        tmp_possible_steps.append(node)
                        tmp_possible_steps_step_cnt.append(step)
                if len(tmp_possible_steps) == 0:
                    break
                # * left first searching, prefer unvisited node
                for idx, step in enumerate(tmp_possible_steps):
                    if step not in tmp_path:
                        nodes_stepped_on_flag[nodes.index(step)] = True
                        tmp_path.insert(0, step)
                        tmp_path_step_cnt += tmp_possible_steps_step_cnt[idx]
                        break
            possible_paths.append(tmp_path)
            possible_paths_step_cnt.append(tmp_path_step_cnt)
        shortest_path_step_cnt = min(possible_paths_step_cnt)
        shortest_path_idx = possible_paths_step_cnt.index(shortest_path_step_cnt)
        shortest_path = possible_paths[shortest_path_idx]
        return shortest_path, shortest_path_step_cnt

    def _map_remove_obstacle(map, path):
        #* generate all maps from removing one wall along the path
        map_w = len(map[0])
        map_h = len(map)
        #* sum all walls along the path
        walls = []
        for idx, step in enumerate(path):
            idx1_top = step[0]-1
            idx2_top = step[1]
            idx1_left = step[0]
            idx2_left = step[1]-1
            idx1_right = step[0]
            idx2_right = step[1]+1
            idx1_bottom = step[0]+1
            idx2_bottom = step[1]
            try:
                val_top = map[idx1_top][idx2_top]
            except:
                val_top = 0
            try:
                val_left = map[idx1_left][idx2_left]
            except:
                val_left = 0
            try:
                val_right = map[idx1_right][idx2_right]
            except:
                val_right = 0
            try:
                val_bottom = map[idx1_bottom][idx2_bottom]
            except:
                val_bottom = 0
            if idx1_top < 0 or idx2_top < 0 or idx1_top >= map_w or idx2_top >= map_h:
                val_top = 0
            if idx1_left < 0 or idx2_left < 0 or idx1_left >= map_w or idx2_left >= map_h:
                val_left = 0
            if idx1_right < 0 or idx2_right < 0 or idx1_right >= map_w or idx2_right >= map_h:
                val_right = 0
            if idx1_bottom < 0 & idx2_bottom < 0 or idx1_right >= map_w or idx2_right >= map_h:
                val_bottom = 0
            if val_top == 1:
                walls.append([idx1_top, idx2_top])
            if val_left == 1:
                walls.append([idx1_left, idx2_left])
            if val_right == 1:
                walls.append([idx1_right, idx2_right])
            if val_bottom == 1:
                walls.append([idx1_bottom, idx2_bottom])
        walls = list(set([tuple(t) for t in walls]))
        #* map remove walls
        maps = [map]*len(walls)
        for idx, wall in enumerate(walls):
            print(wall)
            maps[idx][wall[0]][wall[1]] = 0
            for a in tmp_map:
                print(a)
            print("Generated {} maps.".format(len(maps)), end='\r')
        return maps

    def _complex_map(map):
        # 1. Use map to generate nodes
        # 2. Use nodes to perform path finding, shortest.
        # 3. Use the found path to generate maps by removing obstacles
        # 4. Repeat 1-2 until shortest path is found or all possible maps are generated
        step_hist = []
        nodes = _gen_nodes(map)
        print("Generated {} nodes: {}".format(len(nodes), nodes))
        path, step_cnt = _find_shortest_path(nodes)
        print("Shortest path: {} with {} steps.".format(path, step_cnt))
        step_hist.append(step_cnt)
        obj_removed_maps = _map_remove_obstacle(map, path)
        print("Generated {} maps.".format(len(obj_removed_maps)))
        for obj_removed_map in obj_removed_maps:
            nodes = _gen_nodes(obj_removed_map)
            path, step_cnt = _find_shortest_path(nodes)
            step_hist.append(step_cnt)
            print("Progress: {}%".format(len(step_hist)/len(obj_removed_maps)*100))
        return min(step_hist)
    
    # return _simple_map(map)
    return _complex_map(map)


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
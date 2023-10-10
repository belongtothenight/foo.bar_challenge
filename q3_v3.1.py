# A* Algorithm
# Reference: https://www.youtube.com/watch?v=JtiK0DOeI4A
# This is a working version with PriorityQueue (not available in Python 2.7)
from queue import PriorityQueue

def solution(map):
    class Spot:
        def __init__(self, x, y, val):
            self.x = x
            self.y = y
            self.is_wall = True if val == 1 else False
            self.is_path = True if val == 0 else False
            self.is_open = False
            self.is_closed = False

        def update_neighbors(self, map_spot):
            self.neighbors = []
            self.map_w = len(map_spot[0])
            self.map_h = len(map_spot)
            if self.x > 0:
                up = map_spot[self.y][self.x - 1]
                if not up.is_wall:
                    self.neighbors.append(up)
            if self.x < self.map_w - 1:
                down = map_spot[self.y][self.x + 1]
                if not down.is_wall:
                    self.neighbors.append(down)
            if self.y > 0:
                left = map_spot[self.y - 1][self.x]
                if not left.is_wall:
                    self.neighbors.append(left)
            if self.y < self.map_h - 1:
                right = map_spot[self.y + 1][self.x]
                if not right.is_wall:
                    self.neighbors.append(right)

        def get_pos(self):
            return (self.x, self.y)

    def h(p1, p2): #* Manhattan distance
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def reconstruct_path(came_from, current, path):
        path.append(current.get_pos())
        while current in came_from:
            current = came_from[current]
            path.append(current.get_pos())
        return path[::-1]

    def a_star(start, end, map_as):
        path = []
        cnt = 0
        open_set = PriorityQueue()
        open_set.put((0, cnt, start))
        came_from = {}
        g_score = {spot: float("inf") for row in map_as for spot in row}
        g_score[start] = 0
        f_score = {spot: float("inf") for row in map_as for spot in row}
        f_score[start] = h(start.get_pos(), end.get_pos())
        open_set_hash = {start} #* For checking if a spot is in the open set
        while not open_set.empty():
            current = open_set.get()[2]
            open_set_hash.remove(current)
            if current == end:
                #* Reconstruct path
                return reconstruct_path(came_from, end, path)
            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                    if neighbor not in open_set_hash:
                        cnt += 1
                        open_set.put((f_score[neighbor], cnt, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.is_open = True
            if current != start:
                current.is_closed = True
        return [] #* No path found
    
    def perform_a_star_search(map_pss, print_text=False):
        #* Initialize
        map_w = len(map_pss[0])
        map_h = len(map_pss)
        start = (0, 0)
        end = (map_h - 1, map_w - 1)
        #* Print map
        if print_text:
            print("Map:")
            for row in map_pss:
                print(row)
        #* Update entire map
        for y in range(map_h):
            for x in range(map_w):
                map_pss[y][x] = Spot(x, y, map_pss[y][x])
        #* Update neighbors
        for y in range(map_h):
            for x in range(map_w):
                map_pss[y][x].update_neighbors(map_pss)
        #* A* Algorithm
        path = a_star(map_pss[start[0]][start[1]], map_pss[end[0]][end[1]], map_pss)
        if print_text:
            print("Path:")
            print(path)
        #* Restore map
        for y in range(map_h):
            for x in range(map_w):
                map_pss[y][x] = 0 if map_pss[y][x].is_path else 1
        return len(path)
    
    def wall_finder(map_wf, mode="path"):
        #* List out the wall that is next to the path
        map_w = len(map_wf[0])
        map_h = len(map_wf)
        walls = []
        if mode == "path":
            for i in range(map_h):
                for j in range(map_w):
                    if map_wf[i][j] == 1:
                        if i != 0: #* up
                            if map_wf[i - 1][j] == 0:
                                walls.append((i, j))
                        if i != map_h - 1: #* down
                            if map_wf[i + 1][j] == 0:
                                walls.append((i, j))
                        if j != 0: #* left
                            if map_wf[i][j - 1] == 0:
                                walls.append((i, j))
                        if j != map_w - 1: #* right
                            if map_wf[i][j + 1] == 0:
                                walls.append((i, j))
        elif mode == "all":
            for i in range(map_h):
                for j in range(map_w):
                    if map_wf[i][j] == 1:
                        walls.append((i, j))
        return walls
    
    step_list = []
    wall_list = wall_finder(map, mode="path")
    search_times = len(wall_list)
    # print("Found {} walls".format(search_times))
    wall_list.insert(0, (0, 0))
    search_times += 1
    for idx, wall in enumerate(wall_list):
        # print("Searching {}/{}".format(idx + 1, search_times))
        if idx == 0:
            step_list.append(perform_a_star_search(map, print_text=False))
        else:
            map[wall[0]][wall[1]] = 0
            step_list.append(perform_a_star_search(map, print_text=False))
            map[wall[0]][wall[1]] = 1
    # print("Step list: {}".format(step_list))
    return min(step_list)

if __name__ == "__main__":
    # [[0, 1, 1, 0],
    #  [0, 0, 0, 1],
    #  [1, 1, 0, 0],
    #  [1, 1, 1, 0]]
    map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(solution(map))
    # [[0, 0, 0, 0, 0, 0],
    #  [1, 1, 1, 1, 1, 0],
    #  [0, 0, 0, 0, 0, 0],
    #  [0, 1, 1, 1, 1, 1],
    #  [0, 1, 1, 1, 1, 1],
    #  [0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print(solution(map))
    # map = [[0, 0],
    #        [1, 0]]
    map = [[0, 0], [1, 0]]
    print(solution(map))
    # [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    #  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #  [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    #  [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    #  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    #  [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    #  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
    map = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
    print(solution(map))
    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(map))
    # [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    map = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(map))
    # [[0, 0, 0, 0, 1],
    #  [1, 0, 1, 1, 0],
    #  [1, 0, 0, 0, 0]]
    map = [[0, 0, 0, 0, 1], [1, 0, 1, 1, 0], [1, 0, 0, 0, 0]]
    print(solution(map))
    # [[0, 0, 0],
    #  [1, 1, 0],
    #  [0, 0, 0],
    #  [0, 1, 0],
    #  [0, 0, 0]]
    map = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(solution(map))

import os
import sys
import queue


class State(object):
    goal_state = [[0 for i in range(3)] for j in range(3)]
    for i in range(1, 9):
        goal_state[(i - 1) // 3][(i - 1) % 3] = i
    goal_state[2][2] = 0

    def __init__(self, state, parent, direction, move=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.direction = direction

    def __lt__(self, other):
        return self.h() + self.g() < other.h() + other.g()

    def __str__(self):
        return str(self.state)

    def __eq__(self, other):
        flag = True
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != other.state[i][j]:
                    flag = False
        return flag

    def __hash__(self):
        return hash(str(self.state))

    # hamming distance
    def h(self):
        sum = 0
        for i in range(3):
            for j in range(3):
                temp = self.state[i][j]
                sum += abs(i - temp // 3)
                sum += abs(j - temp % 3)
        return sum

    def g(self):
        return self.move

    def next_moves(self, move):
        # 0,1,2,3 represents LEFT,RIGHT,UP,DOWN
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    x = i
                    y = j

        if x in [0, 1]:
            new_state = [i[:] for i in self.state]
            new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]
            yield State(new_state, self, "DOWN", move)
        if x in [1, 2]:
            new_state = [i[:] for i in self.state]
            new_state[x - 1][y], new_state[x][y] = new_state[x][y], new_state[x - 1][y]
            yield State(new_state, self, "UP", move)
        if y in [0, 1]:
            new_state = [i[:] for i in self.state]
            new_state[x][y + 1], new_state[x][y] = new_state[x][y], new_state[x][y + 1]
            yield State(new_state, self, "RIGHT", move)
        if y in [1, 2]:
            new_state = [i[:] for i in self.state]
            new_state[x][y - 1], new_state[x][y] = new_state[x][y], new_state[x][y - 1]
            yield State(new_state, self, "LEFT", move)


class Puzzle(object):
    def __init__(self, init_state, goal_state):
        # You may add more attributes as necessary
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = list()
        self.solvable = True

    def solve(self):
        x1, y1 = 0, 0
        x2, y2 = 1, 0
        if self.init_state[x1][y1] == 0:
            y1 = 1
        if self.init_state[x2][y2] == 0:
            y2 = 1
        opp_init_state = [i[:] for i in self.init_state]
        opp_init_state[x1][y1], opp_init_state[x2][y2] = opp_init_state[x2][y2], opp_init_state[x1][y1]

        frontier = queue.PriorityQueue()
        frontier.put(State(self.init_state, None, None))

        opp_frontier = queue.PriorityQueue()
        opp_frontier.put(State(opp_init_state, None, None))

        explored = set()
        opp_explored = set()

        current_move = 0

        while frontier:
            opp_current = opp_frontier.get()
            if opp_current.state == self.goal_state:
                return ["UNSOLVABLE"]

            current = frontier.get()
            #
            # if current_move % 1000 == 0:
            #     print(current_move)

            if current.state == self.goal_state:
                while current.direction:
                    self.actions.append(current.direction)
                    current = current.parent
                return reversed(self.actions)
            current_move += 1
            for state in current.next_moves(current_move):
                if state not in explored:
                    frontier.put(state)

            explored.add(current)

            for state in opp_current.next_moves(current_move):
                if state not in opp_explored:
                    opp_frontier.put(state)
            opp_explored.add(opp_current)

        return ["UNSOLVABLE"]


if __name__ == "__main__":
    # do NOT modify below
    if len(sys.argv) != 3:
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        raise IOError("Input file not found!")

    init_state = [[0 for i in range(3)] for j in range(3)]
    goal_state = [[0 for i in range(3)] for j in range(3)]
    lines = f.readlines()

    i, j = 0, 0
    for line in lines:
        for number in line:
            if '0' <= number <= '8':
                init_state[i][j] = int(number)
                j += 1
                if j == 3:
                    i += 1
                    j = 0

    for i in range(1, 9):
        goal_state[(i - 1) // 3][(i - 1) % 3] = i
    goal_state[2][2] = 0

    puzzle = Puzzle(init_state, goal_state)
    ans = puzzle.solve()

    with open(sys.argv[2], 'a') as f:
        for answer in ans:
            f.write(answer + '\n')








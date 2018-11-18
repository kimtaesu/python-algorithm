"""
     4
    / \
   1   5
  / \   \
 2   3   9
"""

vertice = [4, 1, 5, 2, 3, 9]
adj_list = {}
adj_list[4] = [1, 5]
adj_list[1] = [2, 3]
adj_list[5] = [9]
adj_list[2] = []
adj_list[3] = []
adj_list[9] = []

queue = []
visited = []


def bfs(start):
    queue.append(start)

    while len(queue) > 0:
        print(queue, queue[len(queue)-1])
        cur = queue.pop()
        for neighbor in adj_list[cur]:
            if not neighbor in visited:
                queue.insert(0, neighbor)
        visited.append(cur)

bfs(4)
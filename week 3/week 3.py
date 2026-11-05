#task 1
from collections import deque
graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def bfs(start, goal):
	q=deque([(start,[start])]); seen={start}
 
	while q:
		node,path=q.popleft()
		if node==goal: return path
		for n in graph[node]:
			if n not in seen:
				seen.add(n); q.append((n,path+[n]))
    
def dfs(start, goal):
	stack=[(start,[start])]; seen=set()
 
	while stack:
		node,path=stack.pop()
		if node==goal: return path
		if node in seen: continue
		seen.add(node)
		for n in reversed(graph[node]): stack.append((n,path+[n]))
  
print(bfs("A","G")); print(dfs("A","G"))


#task 2


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

def dls(node, goal, limit, path):
    if node == goal:
        return FOUND, path

    if len(path) - 1 == limit:
        if graph[node]:
            return CUTOFF, None
        else:
            return FAILURE, None

    cutoff_occurred = False

    for successor in graph[node]:
        if successor in path:
            continue
        
        status, result_path = dls(
            successor,
            goal,
            limit,
            path + [successor]
        )

        if status == FOUND:
            return FOUND, result_path

        if status == CUTOFF:
            cutoff_occurred = True

    if cutoff_occurred:
        return CUTOFF, None

    return FAILURE, None

def iddfs(start, goal, max_depth):
    limits_attempted = []

    for limit in range(max_depth + 1):
        limits_attempted.append(limit)

        status, path = dls(
            start,
            goal,
            limit,
            [start]
        )

        if status == FOUND:
            return status, path, limits_attempted

        if status == FAILURE:
            return status, None, limits_attempted

    return CUTOFF, None, limits_attempted

print("DEPTH-LIMITED SEARCH")

for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])

    print(
        f"Limit={limit}, "
        f"Status={status}, "
        f"Path={path}"
    )

print("ITERATIVE DEEPENING DFS")

for max_depth in [1, 2, 3, 4]:
    status, path, limits = iddfs("A", "G", max_depth)

    print(
        f"Max depth={max_depth}, "
        f"Status={status}, "
        f"Path={path}, "
        f"Limits attempted={limits}"
    )


#task 3


graph = {
    "A": {"B": 1, "C": 5},
    "B": {"D": 2, "E": 1},
    "C": {"F": 2, "G": 7},
    "D": {},
    "E": {"G": 1},
    "F": {},
    "G": {},
}

def ucs(start, goal):
    nodes = [(0, [start])]
    visited = []
    while nodes:
        best = nodes[0]
        for node in nodes:
            if node[0] < best[0]:
                best = node
        nodes.remove(best)
        cost, path = best
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            visited.append(node)
            for next_node in graph[node]:
                new_cost = cost + graph[node][next_node]
                nodes.append((new_cost, path + [next_node]))

path, cost = ucs("A", "G")
print("path =", path, "hops =", len(path) - 1, "cost =", cost)
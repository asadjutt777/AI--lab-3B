import heapq

GRAPH = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)],
         "C": [("G", 3)], "G": []}
H = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def astar(graph, h, start, goal, verbose=True):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded, log = [], []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            log.append(f"  skip stale {node} (g={g}, best={best[node]})")
            continue
        if node == goal:
            log.append(f"  pop {node}: g={g} h={h[node]} f={f}  -> GOAL (not counted)")
            return g, path, expanded, log
        log.append(f"  pop {node}: g={g} h={h[node]} f={f}  -> EXPAND")
        expanded.append(node)
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
                log.append(f"     push {nxt}: g={g}+{w}={ng}, h={h[nxt]}, f={ng + h[nxt]}")
            else:
                log.append(f"     reject {nxt}: g={ng} >= best {best[nxt]}")
        frontier = sorted((e[0], e[1], e[2]) for e in pq)
        log.append("     frontier (f,g,node): " + str(frontier))
    return None, None, expanded, log

def path_cost(graph, path):
    total = 0
    for u, v in zip(path, path[1:]):
        total += dict(graph[u])[v]
    return total

def true_remaining(graph, goal):
    def go(n):
        if n == goal:
            return 0
        opts = [w + go(v) for v, w in graph[n]]
        return min(opts) if opts else float("inf")
    return {n: go(n) for n in graph}


def report(title, h):
    print(f"\n{title} h={h}")
    cost, path, exp, log = astar(GRAPH, h, "S", "G")
    print("\n".join(log))
    print(f"returned cost={cost}  path={'->'.join(path)}  "
          f"independent sum={path_cost(GRAPH, path)}")
    print(f"expanded ({len(exp)}): {exp}")
    return cost, path, exp

if __name__ == "__main__":
    hstar = true_remaining(GRAPH, "G")
    print("True remaining cost h*:", hstar)
    print("Admissible (h<=h*):", {n: H[n] <= hstar[n] for n in H})
    print("Consistency h(u)<=w+h(v):")
    for u, es in GRAPH.items():
        for v, w in es:
            print(f"  {u}->{v}: {H[u]} <= {w}+{H[v]}={w + H[v]}  {H[u] <= w + H[v]}")

    a = report("Task 1: A* (supplied h)", H)
    u = report("Task 2: UCS (h=0)", {n: 0 for n in H})
    h_bad = dict(H); h_bad["C"] = 10
    print(f"\nOverestimate check: h(C)=10 vs h*(C)={hstar['C']}")
    o = report("Task 3: A* with h(C)=10", h_bad)

    print("\nSummary")
    print(f"{'Run':<14}{'Path':<12}{'Cost':<6}{'Expanded':<6} Nodes")
    for name, r in [("A* (h)", a), ("UCS (h=0)", u), ("A* h(C)=10", o)]:
        print(f"{name:<14}{'->'.join(r[1]):<12}{r[0]:<6}{len(r[2]):<6} {r[2]}")
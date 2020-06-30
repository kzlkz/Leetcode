

## Calculate the minimal dist from start to target
def BFS(Node start, Node target):
    q = deque([])
    visited = set()

    q.append(start)
    visited.add(start)
    step = 0

    while q:
        sz = len(q)

        for i in range(sz):
            cur = q.popleft()
            if cur == target:
                return step
            
            for x in cur.adj:
                q.append(x)
                visited.add(x)
        
        step += 1
    

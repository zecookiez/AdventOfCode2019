lines = open("input.txt", "r").read().split()
edges = [line.split() for line in lines]

def solve(arr):

    # Create 2 adjacency list -- one for directed/undirected graph

    adj = {}, {}
    for i, j in arr:
        adj[0][i] = adj[0].get(i, []) + [j]
        adj[1][i] = adj[1].get(i, []) + [j]
        adj[1][j] = adj[1].get(j, []) + [i]

    dist = {"COM": 0} # Keep track of shortest distances

    def helper(node, dir):
        for neighbor in adj[dir].get(node, []):
            if dist.get(neighbor, 1e9) <= dist[node]: # Only visit further if distance is shorter
                continue
            dist[neighbor] = dist[node] + 1 # Update distance
            helper(neighbor, dir) # Explore further

    # Part 1
    helper("COM", 0)
    tot = sum(dist.values())
    
    # Part 2
    dist = {"YOU": 0}
    helper("YOU", 1)

    return tot, dist["SAN"] - 2
    
p1, p2 = solve(arr)

print "Answer: %d for part 1, %d for part 2" % (p1, p2)

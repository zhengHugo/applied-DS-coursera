# Applications
## Preferential Attachment Model
### Degree Distributions
The **degree distribution** of a graph is the probability distribution of the degrees over the entire network.

Plot of the degree distribution of this network
```python
degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = 
    [list(degrees.values()).count(i) / float(nx.number_of_nodes(G)) 
    for i in degree_values]

import malplotlib.pyplot as plt
plt.bar(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()
```

### Degree Distributions in Real Networks
Degree distribution looks like a straight line when on a log-log scale. 
**Power law:** $P(k) = Ck^{-\alpha}$

### Preferential Attachment Model
- Start with two nodes connected by an edge
- At each time step, add a new node with an edge connecting it to an existing node
- Choose the node to connect to at random with probability proportional to each node's degree
- The probability of connecting to a node $u$ of degree $k_u$ is $k_u/\sum_jk_j$

### Preferential Attachment in NetworkX
`barabasi_albert_graph(n, m)` returns a network with `n` nodes. Each new node attaches to `m` existing nodes according to the Preferential Attachment model.

## Small World Networks
### Path Length and Clustering
Social networks tend to have high clustering coeffient and small average path length.

### Small World Model
**Motivation:** Real networks exhibit high clustering coeffient and small average shortest paths. Can we think of a mode that achieves both of these properties?

Small-world model:
- Start with a ring of $n$ nodes, where each node is connected to its $k$ nearest neighbors.
- Fix a parameter $p\in[0,1]$
- Consider each edge $(u,v)$. With probability $p$, select a node $w$ at random and rewire the edge $(u,v)$ so it becomes $(u,w)$

### Small World Model in NetworkX
`watts_strogatz_graph(n, k, p)` returns a small world network with `n` nodes, starting with a ring lattice with each node connected to its `k` nearest neighbors, and reviewing probability `p`.


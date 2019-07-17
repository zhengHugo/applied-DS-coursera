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

## Link Prediction
**Triadic closure:** the tendency for people who share connections in a social network to become connected
### Measure I: Common Neighbors
The number of common neighbors of nodes $X$ and $Y$ is 
$$
\text{comm\_neigh}(X,Y)=|N(X)\cap N(Y)|
$$
where $N(X)$ is the set of neighbors of node $X$

### Measure II: Jaccard Coefficient
Number of common neighbors normalized by the total number of neighbors
$$
\text{jacc\_coeff}(X,Y)=\frac{|N(X)\cap N(Y)|}{|N(X)\cup N(Y)|}$$

### Measure III: Resource Allocation
Fraction of a "resource" that a node can send to another through their common neighbors.

The Resource Allocation index of nodes $X$ and $Y$ is 
$$
\text{res\_alloc}(X,Y)=\sum_{u\in N(X) \cap N(Y)}\frac{1}{|N(u)|}$$

### Measure IV: Adamic-Adar Index
Similar to resource allocation index, but with log in the denominator.

The Adamic-Adar index of nodes $X$ and $Y$ is 
$$
\text{adamic\_adar}(X,Y)=\sum_{u\in N(X)\cap N(Y)}\frac{1}{\log(|N(u)|)}
$$

### Measure V: Preferential Attachment
Product of the node's degree.
$$
 \text{pref\_attach}(X,Y)=|N(X)||N(Y)|
$$

### Community Structure
Some measures consider the community structure of the network for link prediction

Assume the nodes in this network belong to different communities (sets of nodes)

### Measure VI: Community Common Neighbors
Number of common neighbors with bonus for neighbors in same community.

The Common Neighbor Soundarajan-Hopcroft score of nodes $X$ and $Y$ is:<br>
$$
\text{cn\_soundarajan\_hopcroft}(X,Y)=|N(X)\cap N(Y)|+\sum_{u\in N(X)\cap N(Y)}f(u)
$$
where 
$$
f(u)=
\begin{cases} 
    1, &u \text{ in same community as } X \text{ and }Y \\ 
    0, & \text{otherwise}   
\end{cases}
$$

### Measure VII: Community Resource Allocation
Similar to resource allocation index, but only considering nodes in the same community

The Resource Allocation Soundarajan-Hopcroft scre of nodes $X$ and $Y$ is:
$$
\text{ra\_soundarajan\_hopcroft}(X,Y)=\sum_{u\in N(X)\cap N(Y)}\frac{f(u)}{|N(u)|}
$$





# Influence Measures and Network Centralization
## Degree and Closeness Centrality
### Note Centrality
Centrality measures identify the most important nodes in a network:
- Influential nodes in a social network
- Nodes that disseminate information to many nodes or prevent epidemics
- Hubs in a transportation network
- Important pages on Web
- Nodes that prevent the network from breaking up
### Centrality Measures
- Degree centrality
- Closeness centrality
- Betweenness centrality
- Load centrality
- Page rank
- Katz centrality
- Percolation centrality
### Degree centrality
Assumption: Important nodes have many connections

The most basic measure of centrality: number of neighbors

Undirected networks: use degree <br>
Directed networks: use in-degree or out-degree

### Degree Centrality - Undirected Networks
$C_{deg}(v) = \frac{d_v}{|N|-1}$, where $N$ is the set of nodes in the network and $d_v$ is the degree of node $v$.

### Degree Centrality - Directed Networks
$C_{indeg}(v) = \frac{d^{in}_v}{|N|-1}$, where $N =$ set of the network, $d^{in}_v =$ the in-degree of node $v$

$C_{outdeg}(v) = \frac{d^{out}_v}{|N|-1}$, where $N =$ set of the network, $d^{out}_v =$ the out-degree of node $v$

### Closeness centrality
Assumption: important nodes are close to other nodes

$C_{close}(v)=\frac{|N|-1}{\Sigma_{u\in N \setminus \{v\}}d(v,u)}$

### Disconnected Nodes
How to measure the closeness centrality of a node when it cannot reach all othoer nodes?

**Option I:** Consider only nodes that L can reach

$C_{close}(L)=\frac{|R(L)|}{\Sigma_{u\in R(L)}d(L,u)}$, where $R(L)$ is the set of nodes L can reach.

**Problem:** centraliy of I is too high for a node that can only reach one other node!

**Option II:** Consider only nodes that $L$ can reach and normalize by the fraction of nodes $L$ can reach:

$C_{close}(L) = [\frac{|R(L)|}{|N|-1}]\frac{|R(L)|}{\Sigma_{u\in R(L)}d(L,u)}$

## Betweenness Centrality
**Assupmtion:** important nodes connect other notes

$C_{btw}(v) = \Sigma_{s,t\in N}\frac{\sigma_{s,t}(v)}{\sigma_{s,t}}$, where 
- $\sigma_{s,t} =$ the number of shortest paths between nodes $s$ and $t$.
- $\sigma_{s,t}(v) =$ the number of shortest paths between nodes $s$ and $t$ that pass through node $v$

### Betweenness Centrality - Normalization
**Normalization:** betweenness centrality values will be larger in graphs with many nodes. To control for this, we divide centrality values by the number of pairs of nodes in the graph (excluding $v$):
- $\frac{1}{2}(|N|-1)(|N|-2)$ in undirected graphs
- $(|N|-1)(|N|-2)$ in directed graphs

### Betweenness Centrality - Complexity
Computing betweenness centrality of all nodes can be very computationally expensive. Depending on the algorithm, this computation can take up to $O(|N|^3)$ time.

**Approximation:** rather can computing betweenness centrality based on all pairs of nodes $s,t$, we can approximate it based on a sample of nodes.

### Betweenness Centrality - Subsets

### Betweenness Centrality - Edges
$C_{btw}(e)=\sum_{s,t\in N}\frac{\sigma_{s,t}(e)}{\sigma_{s,t}}$, where
- $\sigma_{s,t}=$ the number of shortest paths between nodes $s$ and $t$.
- $\sigma_{s,t}=$ the number of shortest paths between nodes $s$ and $t$ that pass through edge $e$.

## Basic Page Rank
Developed by Google founders to measure the importance of webpages from the hyperlink network structure.

PageRank assigns a score of importance to each node. Important nodes are those with many in-links from important pages.

- $n=$ number of nodes in the network
- $k=$ number of steps

1. Assign all nodes a PageRank of $\frac{1}{n}$
2. Perform the *Basic PageRank Update Rule* $k$ times.

**Basic PageRank Update Rule:** Each node gives an equal share of its current PageRank to all the nodes it links to.

## Scaled Page Rank
### Interpreting PageRank

### PageRank Problem
**Random walk of k steps with damping parameter $\alpha$: Start on a random node, then:
- <font color='red'> With probability $\alpha$</font>: choose an outgoing edge at random and follow it to the next node.
- <font color='red'> With probability $1-\alpha$</font>: choose a node at random and go to it.

Repeat $k$ times.

The **Scaled PageRank** of $k$ steps and damping factor $\alpha$ of a node $n$ is the probability that a random walk with damping factor $\alpha$ lands on a $n$ after $k$ steps.

## Hubs and Authorities
Given a query to a search engine:
- **Root**: set of highly relevant web pages - potential *autorities*
- Find all pages that link to a page in root - potential *hubs*
- **Base**: root nodes and any node that links to a node in root
- Consider all edges connecting nodes in the base set
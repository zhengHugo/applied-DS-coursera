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




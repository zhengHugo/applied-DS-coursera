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




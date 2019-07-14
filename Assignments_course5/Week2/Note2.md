# Network Connectivity
## Clustering Coefficient
### Triadic Closure
**Triadic Closure:** The tendency for people who share connections in a social network to become connected

**Local clustering coefficient of a node:** Fraction of pairs of the node's friends that are friends with each other

### Global Clustering Coefficient
Measuring clustering on the whole network

**Approach I:** Average local clustering coefficient over all nodes in the graph

**Approach II:** Percentage of "open triads" that are triangles in a network
- Transitivity = (3*Number of closed triads) / (Number of open triads)

### Transitivity vs. Average Clustering Coefficient
Both measure the tendency for edges to form triangle. 
Transitivity weights nodes with large degree higher.

## Distance Measures
### Paths
- Path: A sequence of nodes connected by an edge
### Distance
- Distance between two nodes: the length of the shortest path between them
- Breadth-first search: a systematic and efficient procedure for computing distances from a node to all other nodes in a large network by "discovering" nodes in layers

How to characterize the distance between all pairs of nodes in a graph? 
- Average distance
- Diameter: maximum distance between any pair of nodes
- Eccentricity: the largest distance between the node n and all other nodes
- Radius of a graph: the minimum eccentricity in the graph

How to summarize the distances between all pairs of nodes in a graph
- Periphery: the set of nodes that have eccentricity equal to the diameter
- Center: the set of nodes that have eccentricity equal to the radius

## Connected Components
### Conneted Graphs
An undirected graph is **connected** if, for every pair nodes, there is a path between them.
### Graph Components
**Connected component:**
A subset of nodes such that:
- Every node in the subset has a path to every other node.
- No other node has a path to any node in the subset
### Connectivity in Directed Graphs
A directed graph is **strongly connected** if, for every pair nodes u and v, there is a directed path from u to v and a directed path from v to u.

A directed graph is **weakly connected** if replacing all directed edgeds with undirected edges produces a connected undirected graph.

**Strongly connected component:**
A subset of nodes such that:
- Every node in the subset has a directed path to every other node
- No other node has a directed path to and from every node in the subset

**Weakly connected component:**
The connected components of the graph after replacing all directed edges with undirected edges

## Network Robustness
- **Network Robustness:** the ability of a network to maintain its general structure properties when it faces failures or attacks
- **Type of attacks:** removal of nodes or edges
- **Structural propertities:** connectivity

### Disconnecting a Graph
What is the smallest number of nodes that can be removed from this graph in order to disconnect it?

What is the smallest number of edges that can be removed from this graph in order to disconnect it?

Robust networks have large minimum node and edge cuts





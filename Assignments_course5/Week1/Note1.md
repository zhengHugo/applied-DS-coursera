# Why Study Networks and Basics on NetworkX
## Network Definition and Vocabulary
- Network (or Graph)
  - Nodes (or Vertices)
  - Edges (or Links or Ties)
  - (Mostly) Symmetric relationships
### Weighted Networks
### Signed Networks
Some networks can carry information about friendship and antagoism based on conflict or disagreement.
### Other Edge Attributes
Edges can carry many other labels or attributes
### MultiGraphs
A pair of nodes can have different types of relationships simultaneously

## Node and Edge Attributes
See the notebook
- Adding node and edge attributes
- Accessing node attributes

## Bipartite Graphs
`from networkx.algorithms import bipartite`
- Checking if a graph is bipartite
- Checking if a set of nodes is a bipartition of a graph
- Getting each set of nodes of a bipartite graph
### Projected Graphs
**L-Bipartite graph**: Network of nodes in group L, where a pair of nodes is connected if they have a common neighbor in R in the bipartite graph

Similar definition for R-Bipartite graph projection

**L-Bipartite weighted graph projection**: An L-Bipartite graph projection with weights on the edges that are proportional to the number of common neighbors between the nodes
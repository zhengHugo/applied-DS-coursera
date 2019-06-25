# Unsupervised Machine Learning
## Introduction
- Unsupervised learning involves tasks that operate on datasets __without__ labeled responses or target values
- Instead, the goal is to capture interesting structure or information
  
Applications of unsurpervised learning:
- Visualize structure of a complex dataset
- Density estimation to predict probability of evetns
- Compress and summarize the data
- Extract features for supervised learning
- Discover important clusters or outliers
  
### Two major types of unsupervised learning methods
- Transformations
  - Processes that extract or compute information
- Clustering
  - Find groups in the data
  - Assign every point in the dataset to one of the groups
  
### Transformation: Density Estimation

## Dimensionality Reduction and Manifold Learning
### Dimensionality Reduction
- Finds an approximate version of your dataset using fewer features
- Used for exploring and visualizing a dataset to understand grouping or relationships
- Often visualized using a 2-dimensional scatterplot
- Also used for compression, finding features for supervised learning

## Clustering: Finding a way to divide a dataset into groups ('clusters')
- Data points within the same cluster should be 'close' or 'similar' in some way
- Data Points in different clusters should be 'far apart' or 'different'
- Clustering algorithms output a cluster membership index for each data point:
  - Hard clustering: each data point belongs to exactly one cluster
  - Soft (or fuzzy) clustering: each data point is assigned a weight, score, or probability of membership for each cluster

### K-means Clustering
The k-means algorithm

 __**Initialization**__<br>
 Pick the number of clusters *k* you want to find. <br>
Then pick *k random* points to serve as an initial guess for the cluster centers.

__**Step A**__<br>
Assign each data point to the nearest cluster center.

__**Step B**__<br>
Update each cluster center by replacing it with the mean of all points assigned to that cluster (in step A)

__**Repeat steps A and B**__ until the centers converge to a stable solution

### Limitations of k-means
- Works well for simple clusters that are same size, well-seperated, globular shapes
- Does not do well with irregular, complex clusters
- Variants of k-means like k-medoids can work with categorical features

### Agglomerative Clustering Example

### Linkage Criteria for Agglomerative Clustering
- Ward's method
  - Least increase in total variance (around cluster centroids)
- Average linkage
  - Average distance between clusters
- Complete linkage
  - Max distance between clusters

### Hierarchical Clustering
### DBSCAN Clustering
- Unlike k-means, you don't need to specify # of clusters
- Relatively efficient - can be used with large datasets 
- Identifies likely noise points

### Clustering Evaluation
- With ground truth, existing label can be used to evaluate cluster quality
- Without groud truth, evaluation can be difficult: multiple clusterings may be plausible for a dataset
- Consider task-based evaluation: Evaluation clustering according to performance on a task that __does__ have an objective basis for comparison
- __Example__: the effectiveness of clustering-based features for a superviased learnig task
- Some evaluation heuristics exist (silhouette) but these can be unreliable


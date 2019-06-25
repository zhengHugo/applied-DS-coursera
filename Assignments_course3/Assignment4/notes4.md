# Week 4
## Naive Bayes Classifiers
### Naive Bayes Classifiers: a simple, probabilistic classifier family
- These classifiers are called 'Naive' because they assume that features are conditionally independent, given the class
- In other words, they assume that, for all instances of a given class, the features have little/no correlation with each other
- Highly efficient learning and prediction
- But generalization performance may worse than more sophisticated learning methods.
- Can be competitive for some tasks.

### Naive Bayes Classifier Types
- Bernoulli: binary features (e.g. word presence/absence)
- Multinomial: discrete features (e.g. word counts)
- Gaussian: continuous/real-valued features
  - Statistics computed for each class:
    - For each feature: mean, standard deviation
- See the Applied Text Mining course for more details on the Bernoulli and Multinomial Naive Bayes models
### Gaussian Naive Bayes Classifier
### Naive Bayes classifier: Pro and Cons
Pros:
- Easy to understand
- Simple, efficient parameter estimation
- Works well with high dimentional data
- Often useful as a baseline comparison against more sophisticated methos
  
Cons:
- Assumption that features are conditionally independent given the class is not realistic
- As a result, other classifier types often have better generalization performance
- Their confidence estimates for predictions are not very accurate

## Random Forests
- An ensemble of trees, not just one tree
- Widely used, very good results on many problems
- `sklearn.ensemble` module:
  - Classification: `RandomForestClassifier`
  - Regression: `RandomForestRegressor`
- One decision tree -> Prone to overfitting
- Many decision trees -> More stable, better generalization
- Ensemble of trees should be diverse: introduce random variation into tree-building.
  
### Random Forest `max_features` Parameter
- Learning is quite sensitive to `max_features`
- Setting `max_features = 1` leads to forests with diverse, more complex trees
- Setting `max_features = <close to number of features>` will lead to similar forests with simpler trees

### Random Forest: Pros and Cons
Pros:
- Widely used, excellent prediction performance on many problems
- Doesn't require carefull normalization of features or extensive parameter tuning.
- Like decision trees, handles a mixture of feature types
- Easily parallelized across multiple CPUs
  
Cons:
- The resulting models are often difficult for humans to interpret
- Like decision trees, random forests may not be a good choice for very high-dimensional tasks (e.g. text classifiers) compared to fast, accurate linear model.
  
### Random Forests: RandomForestClassifier Key Parameters
- `n_estimators`: number of trees to use in ensemble (default: 10)
  - Should be large for larger datasets to reduce overfitting (but uses more computation)
- `max_features`: has a strong effect on performance. Influences the diversity of trees in the forest
  - Default works well in practice, but adjusting may lead to some further gains
- `max_depth`: controls the depth of each tree (default: None. Splits until all leaves are pure)
- `n_jobs`: How many cores to use in parallel during training
- Choose a fixed setting for the `random-state parameter` if you need reproducible results
  
## Gradient Boosted Decision Trees
- Training builds a series of small decision trees
- Each tree attempts to correct errors from the previous stage
- The learning rate controls how hard each new tree tries to correct remaining mistakes from previous round
  - High learning rate: more complex trees
  - Low learning rate: simpler trees

### GBDT: Pros and Cons
Pros:
- Often best off-the-shelf accuracy on many problems
- Using model for prediction requires only modest memory and is fast
- Doesn't require careful normalization of features to perform well
- Like dicision trees, handles a mixture of feature types

Cons:
- Like random forests, the models are often difficult for human to interpret
- Requires careful tuning of the learning rate and other parameters
- Training can require significant computation
- Like decision trees, not recommended for text classification and other problems with very high dimensional sparse features, for accuracy and computational cost reasons

### GBDT: GradientBoostingClassifier Key Parameters
- `n_estimators`: sets # of small decision trees to use (weak learners) in the ensemble
- `learning_rate`: controls emphasis on fixing errors from previous iteration
- The above two are typically tuned together
- `n_estimators` is adjusted first, to best exploit memory and CPUs during training, then other parameters.
- `max_depth` is typically set to a small value (e.g. 3-5) for most applications

## Neural Network
### Neural Networks: Pros and Cons
Pros:
- They form the basis of state-of-the-art models and can be formed into advanced architectures taht effectively capture complex features given enough data and computation

Cons:
- Larger, more complex models require significant training time, data, and cunstomization
- Careful preprocessing of the data is needed
- A good choice when the features are of similar types, but less so when features of very different types

### Neural Nets: MLPClassifier and MLPRegressor Important Parameters
- `hidden_layer_sizes`: sets the number of hidden layers (number of elements in list), and number of hidden units per layer (each list element). Default: 100
- `alpha`: controls weight on the regularization penalty that shrinks weights to zero. Default: alpha = 0.0001
- `activation`: controls the nonlinear function used for the activation function, including: `'relu'`(default), `'logistic'`, `'tanh'`

## Deep Learning
### Deep Learning Summary
- Deep learning architectures combine a sophisticated automatic feature extraction phase with a supervised learning phase
- The feature extraction phase uses a hierarchy of multiple feature extraction layers
- Starting from primitive, low-level features in the initial layer, each feature layer's output provides the input features to the next highter feature layer
- All features are used in the final supervised learning model

### Pros and Cons of Deep Learning
Pros:
- Powerful: deep learning has achieved significant gains over other machine learning approaches on many difficult learning tasks, leading to state-of-the-art performance across many different domains
- Does effective automatic feature extraction, reducing the need for guesswork and heuristics on this key problem
- Current software provides flexible architecture that can be adopted for new domains fairly easily

Cons:
- Can require huge amount of training data
- Can require huge amount of training power
- Architectures can be complex and often must be highly tailored to a specific application
  
## Data Leakage
- When the data you're using to train contains information about what you're trying to predict
- Introducing information about the target during training that would not legitimately be available during actual use
- Obvious examples
  - Including the label to be predicted as feature
  - Including test data with training data
- If your model performance is too good to be true, it probably is and likely due to "giveaway" features

### More Subtle Examples of Data Leakage
- Prediction target: will user stay on site, or leave?
  - Giveaway feature: total session length, based on information about future page visits
- Predicting if a user on a financial site is likely to open an account
  - An account number field that's only filled in once the user does open an account
- Diagnostic test to predict a medical condition
  - The existing patient dataset contains a binary variable that happens to mark whether they had surgery for that condition
  - Combination of missing diagnosis codes that are not be available while the patient's condition was still being studied
  - The patient ID could contain information about specific diagnosis paths (e.g. for routine visit vs specialist)
  - The patient ID could contain information about specific diagnosis paths (e.g. for routine visit vs specialist)
- Any of these leaked features is hightly predictive of the target, but not legitimately available at the time prediction needs to be done

### Other Examples of Data Leakage
Leakage in training data:
- Performing data preprocessing using parameters or results from analyzing the entire dataset: Normalizing and rescaling, detecting and removing outliers, estimating missing values, feature selection
- Time-series datasets: using records from the future when computing features for the current prediction
- Errors in data values/gathering or missing variable indicators (e.g. the special value 999) can encode information about missing data that reveals information about the future

Leakage in features:
- Removing variables that are not legitimate without also removing variables that encode the same or related information (e.g. diagnosis info may still exist in patient ID)
- Reversing of intentional randomization or anoymization that reveals specific information about e.g. users not legitimately available in actual use

Any of the above could be present in any external data joined to the training set

### Detecting Data Leakage
- Before building the model
  - Exploratory data analysis to find surprises in the data
  - Are there features very highly correlated with the target value?
- After building the model
  - Look for surprising features behavior in the fitted model
  - Are there features with very high weights, or high information gain?
  - Simple rule-based models like decision trees can help with features like account numbers, patient IDs
  - Is overall model performance surprisingly good compared to known results on the same dataset, or for similar problems on similar datasets?
- Limited real-world deployment of the trained model
  - Potentially expensive in terms of development time, but more realistic
  - Is the trained model generalizing well to new data
  

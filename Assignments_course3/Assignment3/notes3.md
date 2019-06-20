# Week 3
## Classifier Decision Functions
- Each classifier score value per test point indicates how confidently the classifier predicts the positive class or the negative class
### Predicted Probability of Class Membership
- Typical rule: choose most likely class
- Adjusting threshold affects predictions of classifier
- Higher threshold results in a more conservative classifer
### Varying the Decision Threshold
- Different precision and recall values correspond to different decision thresholds
  
## Precision-Recall & ROC Curve
### Precision-Recall Curves
X-axis: Precision <br>
Y-axies: Recall <br>

Top right corner:
- The "idea" point
- Precision = 1.0
- Recall = 1.0

"Steepness" of P-R curvers is important:
- Maximize precision
- while maximizing recall
### ROC Curves
X-axis: False Positive Rate <br>
Y-axis: True Positive Rate <br>

Top left corner:
- The "ideal" point
- False positive rate of zero
- True positive rate of one

"Steepness" of ROC curves is important:
- Maximize the true positive rate
- while minimizing the false positiver rate

## Multi-Class Evaluation
- Multi-class evaluation is an extension of the binary case.
  - A collection of true vs predicted binary outcomes, one per class
  - Confusion matrices are especially useful
  - Classification report
- Overall evaluation metrics are averages across classes
    - But there are different ways to average multi-class results
    - The support for each class is important to consider
- Multi-label classification: each instance can be have multiple label (not covered)
### Multi-Class Confusion Matrix

### Micro vs Macro Average
**Macro-average:**
- Each class haas equal weight
1. Compute metric within each class
2. Average resulting metrics across classes

**Micro-average**
- Each instance has equal weight
- Large classes have most influence
1. Aggregrate outcomes across all classes
2. Compute metric with aggregate outcomes

- If the classes have about the same number of instances, macro- and micro-average will be about the same.
- If some classes are much larger (more instances) than others, and you want to:
  - Weight your metric toward the largest ones, use micro-averaging.
  - Weight your metric toward the smallest ones, use macro-averaging.
- If the micro-average is much lower than the macro-average then examine the larger classes for poor metric performance.
- If the macro-average is mush lower than the micro-average then examine the smaller classes for poor metric performance.

## Regression Evaluation
### Regression Metrics
- Typically r2_score is enough
  - Reminder: computes how well future instances will be predicted
  - Best possible score is 1.0
  - Constant prediction score is 0.0
- Alternative metrics include:
  - mean_absolute_error (absolute difference of target & predicted values)
  - mean_squared_error (squared difference of target & predicted values)
  - median_absolute_error (robust to outliers)
### Dummy Regressor
As in classification, comparison to a 'dummy' prediction model that uses a fixed rule can be useful. For this, sckit.learn provides __dummy regressors__.

The DummyRegressor class implements four simple baseline rules for regression, using the strategy parameter:
- mean predicts the mean of the training target values.
- median predicts the median of the training target values.
- quantile predicts a user-provided quantile of the training target values (e.g. value at the 75th percentile)
- constant predicts a custom constant value provided by the user

## Model Selection: Optimizing Classifiers for Different Evaluation Metrics
### Model Selection Using Evaluation Metrics
- Train/test on same data
  - Single metric
  - Typically overfits and likely won't generalize well to new data
  - But can serve as asanity check: low accuracy on the training set may indicate an implementation problem
- Single train/test split
  - Single metric
  - Speed and simplicity
  - Lack of variance information
- K-fold cross-validation
  - K train-test splits
  - Average metric overall splits
  - Can be combined with parameter grid search: GridSearchCV (def. cv=3)
### Training, Validation, and Test Framework for Model Selection and Evaluation
- Using only cross-validation or a test set to do model selection may lead to more subtle overfitting / optimistic generalization estimates
- Instead, use three data splits:
  1. Training set (model building)
  2. Validation set (model selection)
  3. Test set (final evaluation)
- In practice:
  - Create an initial training/test split
  - Do cross-validation on the training data for model/parameter selection
  - Save the held-out test set for final model **evaluation**

# Week 3
## Merging Data Sets
When we adding a column to a datafram, the length of the list should be consistant with the number of rows in the dataframe.
Otherwise we have to add 'None' to tell pandas where to add these value in. 

We can speicify the index of the value so that the list can be applied to the dataframe.
Pandas will fill the missing value with 'None' 

- Full outer join (union)
- Inner join (intersection)

- merge(df1, df2, how='outer', left_index=True, right_index=True)

- multi-indexing, multiple columns

## Pandas Idioms
- Chain indexing: generally bad practice
- think carefully if you need chain indexing, which looks like ']['

- Method chaining is good

## Group by
- groupby('column_name')
- groupby(function)
- agg({'column_name': func_name})
- apply
- Example:
```python
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#        
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))
```
## Scale
- ratio scale
- interval scale
- ordinal scale
- nominal scale

- `df['column_name].astype('category')`
```python
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)

```


## Time Series and Date Functionality
- Timestamp
- Period
- DatetiemIndex
- PeriodIndex
- Timedeltas


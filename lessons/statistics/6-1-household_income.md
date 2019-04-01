# [Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

## Code 

Using `InterpolateSample()` from the book code:
```
def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.loc[41, 'log_upper'] = log_upper
    
    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample
```
I used the following to answer the posed questions:

```
log_sample = InterpolateSample(income_df, log_upper=6.0)
sample = np.power(10, log_sample)
cdf = thinkstats2.Cdf(sample)
mean_income = cdf.Mean()
print("Mean income: ",mean_income)
median_income = cdf.Value(.5)
print("Median income: ", median_income)
inc_skewness = PearsonMedianSkewness(sample)
print("Skewness factor: ", inc_skewness)
inc_below_mean = cdf.Prob(cdf.Mean())
print("The percentage of households reporting incomes below the mean is: ",inc_below_mean * 100)
```
Output:
```
Mean income:  74278.70753118755
Median income:  51226.45447894046
Skewness factor:  0.7361258019141782
The percentage of households reporting incomes below the mean is:  66.0005879566872
```
If we change the `InterpolateSample()` to have a log_upper of 7.0 to simulate 10 million, the output becomes: 
```
Mean income:  124267.39722164671
Median income:  51226.45447894046
Skewness factor:  0.39156450927742087
The percentage of households reporting incomes below the mean is:  85.65630665207664
```
So the upper bound affects the mean income and the skewness, but not the median.
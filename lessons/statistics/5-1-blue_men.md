# [Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

## Code
```
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

# 2.54 cm per inch
upper_lim=(6*12 + 1)*2.54
lower_lim = (5*12 + 10) * 2.54
p_upper_lim_or_lower = dist.cdf(upper_lim)
p_lower_lim_or_lower = dist.cdf(lower_lim)
print('''Probability of male between 5'10" and 6'1" ''')
print(p_upper_lim_or_lower-p_lower_lim_or_lower)

```
The probability of male height between 5'10" and 6'1" is about 34.27%.
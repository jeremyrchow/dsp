# [Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

## Code 

```
import numpy as np
rand_array=np.random.random(1000)

rand_pmf=thinkstats2.Pmf(rand_array)
thinkplot.Pmf(rand_pmf)
thinkplot.Config(xlabel='Random Value', ylabel='PMF')

rand_cdf=thinkstats2.Cdf(rand_array)
thinkplot.Cdf(rand_cdf)
thinkplot.Config(xlabel='Random Value', ylabel='CDF')
```

![](https://github.com/jeremyrchow/dsp/blob/master/prework/statistics/graphs/rand_num_pmf.png)

![](https://github.com/jeremyrchow/dsp/blob/master/prework/statistics/graphs/rand_num_cdf.png)

The PMF plot suggests there's about a .001 probability for each value, which seems correct given that we have 1000 random numbers. The CDF graph also suggests that the distribution adds up linearly, therefore it seems uniform.
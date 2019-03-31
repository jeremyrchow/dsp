# [Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

## Code
```
import sys
import nsfg
import math

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live_births = preg[preg.outcome == 1]
first_born = live_births[live_births.birthord == 1]
non_first = live_births[live_births.birthord != 1]

print("Cohen's D for weight of firstborn and non-firstborn babies:")
print(CohenEffectSize(first_born['totalwgt_lb'],non_first['totalwgt_lb']))
print("Cohen's D for pregnancy length of firstborn vs. non-firstborn babies:")
print(CohenEffectSize(first_born['wksgest'],non_first['wksgest']))
```

Cohen's D for weight difference between firstborn and non-firstborn babies is .08867, and the D for the pregnancy length is 0.0454. To be statistically significant, the 'D' must be .2 or higher.
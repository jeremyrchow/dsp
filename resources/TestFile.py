from collections import defaultdict
import pprint as pp

food_list = 'spam spam spam egg'.split()
food_count = dict()
#for food in food_list:
#	food_count[food] += 1

food_count = defaultdict(int)

for food in food_list:
	food_count[food] += 1

print (food_count)
pp.pprint(food_count,width = 2)
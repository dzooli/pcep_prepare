"""
  Example of useage of map()
"""
from pprint import pprint

mylist = range(10)
mapped_list = map(lambda x: bool(x % 2 == 0), mylist)

for i in mapped_list:
    print(i)

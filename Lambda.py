# normal function
# def my_function(x, y):
#     return x + y
#lambda function

# my_function = lambda x, y: x + y
# print(my_function(4,6))

#sort list by lambda function:
# list = ["Duong", "Manh", "Quan"]
# print(sorted(list))
# print(sorted(list, key = lambda x: len(x)))

#filter(func, iterable)
lst = [1,2,3,4,5,6]
print(lst)
new_list = list(filter(lambda x: x%2==0, lst))
print(new_list)

#map(func, iterables) => apply something to other oject in list
lst = [1,2,3,4,5,6]
new_list = list(map(lambda x: x + 3 , lst))
print(new_list)

#reduce(func, iterable)
from functools import reduce
lst = [1,2,3,4,5,6]
result =  reduce(lambda x,y: x + y, lst)
print(result)
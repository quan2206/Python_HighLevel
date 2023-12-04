# name = "Quan"
# print("I am " + name)

"""Method 1"""
# string module operator %
name = "Manh Quan"
weight = 9.2
my_string = "My name's %s. I am %.2f kg" % (name, weight)
print(my_string)

"""Method 2.format() function""" 

name = "Min"
loc =  "HaNoi"

print("My name's {}, I am from {},{}".format(name, loc, " hahaha"))

dict = {"name": "Quan", "loc": "DaNang", "weight": "55kg"}
print("My name's {my_dict[name]}, I am from {my_dict[loc]},My weight {my_dict[weight]}".format(my_dict = dict))


#############################
acc = 0.782365
print("Accuracy: {}".format(acc))
print("Accuracy: {:.3f}".format(acc))

"""Method 3  f string"""
name = "Quan"
loc = "GiaLai"

print(f"My name's {name}, I am from {loc}")
print(f"accuracy: {acc:.2f}")

""" Method 4 : Template string"""
from string import Template
name = "Linh"
template = Template("Hellp, $name.") # using $ character
print(template.substitute(name=name))
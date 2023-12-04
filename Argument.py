import argparse

#create parser
parser = argparse.ArgumentParser(

)
#positional arguments
# parser.add_argument("x", type= int)
# parser.add_argument("y", type = int)

# optional arguments
parser.add_argument("--x", type= int, )
parser.add_argument("--y", type = int, default=20)

#get info
args = parser.parse_args()

print("x = ",args.x)
print("y = ",args.y)
print("Sum = x + y =", args.x + args.y)
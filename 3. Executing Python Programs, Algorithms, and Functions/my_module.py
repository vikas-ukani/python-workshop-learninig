import math

""" 

This function will return the factorial number of given numberand return it.. 
"""


def compute(a):
    return ([math.factorial(x) for x in a])


result = 0
# Loop 1 to 10
for i in range(1, 11):
    result += i

if __name__ == "__main__":
    print(__name__)
    print("__main__")
    print(result)

from module import maths
print("IMPORTING MATHS MODULE")
print(maths.add(5,10))
print(maths.div(5,10))
print(maths.mul(5,10))
print(maths.sub(5,10))

from module.maths import add, div, mul, sub
print("IMPORTING FUNCTIONS FROM MATHS MODULE")
print(add(5,10))
print(div(5,10))
print(mul(5,10))
print(sub(5,10))


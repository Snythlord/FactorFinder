from ast import Num
import numbers


Number=int(input("Enter a Number to factorize: "))
factors=[]
for i in range(1,Number+1):
    if Number%i==0:
       factors.append(i)

print ("Factors of {} = {}".format(Number,factors))
if Number & 1 in factors:
    print ("This is prime")
else:
    print ("This is Composite. ")
#first n term of gemotric progression

a = int(input("enter value of a:"))
r = int(input("enter value of r:"))
n = int (input ("enter value of n:"))
for i in range (1,n+1):
    t_n = a*r**(i-1)
    print(t_n)

# geting the first n terms of geometric progression
a = int(input("enter the value of a:"))
r = int(input("enter the value of r:"))
n = int (input("enter the value of r:"))
if(r>1):
    s_n =(a*(r**n))/(r-1)
else:
    s_n =(a*(r**n))/(1-r)
    print("sum of n terms:",s_n)

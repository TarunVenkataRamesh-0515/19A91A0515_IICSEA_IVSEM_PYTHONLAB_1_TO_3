"""
Implement a python script to compute
distance between two points taking inp from the user (Pythagorean Theorem)
"""
x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,y1),"and",(x2,y2),"is : ",result)

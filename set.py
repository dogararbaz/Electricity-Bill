# Set retain the unique values
# max = max value in set  min = min value in set   and  len = length of set
s=set()   # This a set
"""print(type(s))
a = ["Ali"] # This is a list
c = set(a)
print(type(c))
s.add(1)
a=s.add(2)
print(s)"""

a=input("Enter A 1st Set Number:")
b=input("Enter A 2nd Set Number:")
c= set(a)
d=set(b)
print("Intersetion Of A and B Is:",c.intersection(d))
print("Union:",c.union(d))
print("Disadjoint:",c.isdisjoint(d))
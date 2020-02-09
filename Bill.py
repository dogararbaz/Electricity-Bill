print("\t Electricity Bill")
cr=int(input("Enter Current Reading:"))
pr=int(input("Enter Previous Reading:"))
u=cr-pr
print("Unit Consume:",u)
if u <= 100:
    uc=5.79
elif u>100 and u<=200:
    uc=8.11
elif u>201 and u<=300:
    uc=10.20
elif u>301 and u<=700:
    uc=17.60
else:
    uc=20.70
print("Cost Per Unit:",uc)
print("Electricity Cost:",u*uc)

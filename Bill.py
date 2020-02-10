print("\n\t\t Electricity Bill\n")
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
ec=uc*u
print("Electricity Cost:",ec)
print("\n\t\t\tTaxes & Others\n")
e=ec*0.015
print("E-Duty:",e)
print("TV-Fee:35")
gst=ec*0.35
print("GST:",gst)
njs=ec*0.012
print("NJS:",njs)    # I am not Confirm This Rate Please Change It When You Sure
sur=ec*0.05
print("FC-SUR:",sur) # I am not Confirm This Rate Please Change It When You Sure
total=ec+e+35+gst+njs+sur
print("Total Payable Bill:",total)

# Dictonay is a key value pairs
# "Type"  is used to show the type.
d1={"Asad":"Burger", "Arbaz": "Shawarma" , "Kashi":"Pizza"}
print(d1)
print(d1["Arbaz"]) #Call Specific item
d2={"Asad":"Burger", "Dogar":{"B":"Egg" , "Lunch" :"Kulcha" }} # Dictonary into Dictonary
d2["Kashi"]="Khana" # update dictonary
d2[1]= "ok" # Dic with Intergers
d3 = d2.copy()  #Used to return copy
del d3["Asad"] # Remove the key in dictonary

d2={"Asad":"Burger", "Dogar":{"B":"Egg" , "Lunch" :"Kulcha" }}
print(d2.get("Asad")) # Call the value or also use pop instead of get
d2.update({"Saad":"Call"}) #Update the dictonary
print(d2.keys()) # Show The Keys
print(d2.items()) # print the item of key value pair

square={1:1, 2:4, 3:9, 4:16, 5:25}
print(square.pop(2))
square.clear() # Clear the dictonary

print(square)
# Create A Dictonary and take input from the user and return the meaning of the word from the dictonary
print("Dictonary")
print("Chose The Word: 1.Computer 2.Google 3.School 4.University")
a=input("Enter A Word:")

d1={"Computer":"Computer is a machine which perform a specific task.", "Google":"Google is search engine","School":"In School Children completes their early education","University":"In University we learn many things about our life as well as study"}
print(d1[a])

d2={"Ali":"Water"}
print(type(d2))
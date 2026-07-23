a = 10
b = 3

print(a + b) #Addition
print(a - b) #Subtraction
print(a * b) #Multiplication
print(a / b) #Division
print(a // b)#Floor Division
print(a % b) #Modulus
print(a ** b)#Power

#Comparison Operators
age = 20
print (age == 18) #Equal to 
print (age != 18) #Not Equal to 
print (age > 18)  #Greater than
print (age < 18)  #Less than
print (age >= 20) #Greater than equal to 
print (age <= 20) #Less than equal to 

#Logical Operators

age = 22
has_id_card = True

print (age >= 18 and has_id_card)
print (age >= 18 or has_id_card)
print (not has_id_card)

#Type Casting

age= input("Apni age likhein: ")
print(type(age))

age =  int(age)
print(type(age))
print(age+5)

#Conditional Statements - if / elif /else

#Simple if
age = 20

if age >= 18:
    print("Aap vote de sakte hain")

#If-else
age = 15    

if age >= 18:
    print("Aap vote de sakte hain")
else:
    print("Aap vote nhi de sakte hain") 

#If-elif-else           
age = 15 

if age >= 18:
    print("Aap vote de sakte hain")
elif age == 15:
    print("Aap kisi bhi vote de sakte hain")
else:
    print("Aap vote nhi de sakte hain")


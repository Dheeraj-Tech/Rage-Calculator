''' What is New In this Version ?
1>Loading Bar Added
2> Added 3 New Operations -> Modulus,Exponentiation and Floor Division''' # <-For Developers

#Loading Bar Program(copied)
#Pls Download tqdm from pip if not installed by -> pip install tqdm
from tqdm import tqdm 

for i in tqdm (range (1000), desc="Loading..."): 
	pass

#Prefixes
print('''            |||||||||||||||||||||||||||||||||||||||||||||||||Welcome To Detto Calculatio||||||||||||||||||||||||||||||||||||||||||||||
                                                                                                                                                Version - 1.02.B''')
print(''' What is New In the Version 1.02.B ?
1>Loading Bar Added 
2> Added 3 New Operations -> Modulus,Exponentiation and Floor Division''')#<-For Users
#The types of operations
print('''
All the Possible Operations :
1} Addition(+)
2}Subtraction(-)
3}Multiplication(*)
4}Division(/)
5}Modulus(%)
6}Expotentiation(**)
7}Floor Divsion(//)
''')

#Program For The Calculator
a = int(input("Enter The First Number "))
b = int(input("Enter The Second Number "))
c = input("Enter The Operation You want to do ")
if c == "+"or c == "Addition"or c == "ADDITION"or c == "addition"or c == "Add"or c == "ADD"or c == "add" :
        print(a+b)

elif c == "-"or c == "Subtraction"or c == "SUBTRACTION"or c == "subtarction"or c == "Subtract"or c == "SUBTRACT"or c == "subtract" :
      print(a-b)
      print ("If your value is opposite,then try interchanging your value")
      
elif c == "*"or c == "Multiplication"or c == "MULTIPLICATION"or c == "multiplication"or c == "Multiply"or c == "MULTIPLY"or c == "multiply" :
      print(a*b)
      
elif c == "/"or c == "Division"or c == "DIVISION"or c == "division"or c == "Division"or c == "DIVISION"or c == "division" :
      print(a/b)
      print("If your value is opposite,then try interchanging your value")
      
elif c == "%"or c == "Modulus"or c == "MODULUS"or c == "modulus" :
      print(a%b)
      print("If your value is opposite,then try interchanging your value")
      
elif c== "**"or c == "Exponentiation"or c == "EXPOTENTIATION"or c == "exponentiation":
      print(a**b)
      print("If your value is opposite,then try interchanging your value")
      
elif c== "//"or c == "Floor Division"or c == "FLOOR DIVISION"or c == "floor division":
      print(a//b)
      print("If your value is opposite,then try interchanging your value")
else :
        print("The following Operation is Invalid")
#For Developers,
# Dear Coders, This is not a Copyright Version and hereby allow to use this programming for further use.
#Happy Coding,
#Dheeraj,
#13
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
      
 
     
      

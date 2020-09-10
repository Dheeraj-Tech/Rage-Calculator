"""What's new in this *Major version* ?
1> Added Greeting at the Start of Calculator with Name 
2> Added Greeting at the End of Calculation
3> Now Calculator asks about itself
4>The Calculator Never Ends after Giving the Result
Tip : Ctrl+C to stop the Calculator""" # <- For Developers

#Prefixes
print('''            |||||||||||||||||||||||||||||||||||||||||||||||||Welcome To Detto Calculatio||||||||||||||||||||||||||||||||||||||||||||||
                                                                                                                                                Version -> 2.03.C''')
print ("""What's new in this *Major version* ?
1> Added Greeting at the Start of Calculator with Name 
2> Added Greeting at the End of Calculation
3> Now Calculator asks about itself
4>The Calculator Never Ends after Giving the Result
Tip : Ctrl+C to stop the Calculator""") # <- For Users

#Greetings
name =  (input("What is Your Name Sir/Madam ? "))
print ("Hello "+ name, ", Nice to meet you. Let's get Started")

#The types of operations
print('''
These Are All the Possible Operations :
1} Addition(+)
2}Subtraction(-)
3}Multiplication(*)
4}Division(/)
5}Modulus(%)
6}Expotentiation(**)
7}Floor Divsion(//)
You can write the sign or the name
''')

# Program For The Calculator
while True :
    a = int(input("Enter The First Number "))
    b = int(input("Enter The Second Number "))
    c = input("Enter The Operation You want to do ")
    
    if c == "+"or c == "Addition"or c == "ADDITION"or c == "addition"or c == "Add"or c == "ADD"or c == "add" :
        print(a+b)
        print(" Thank You",name)
        print("Re-Running....")
        print("Press Ctrl+C to Stop")

        i =  input("Did You liked my Calculator ? Y/N ")
        if i == "Y" :
                     print ("Thank You!!") 
        elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
        else :
                     print ("Pls Give answer in Y or N")    
    
    elif c == "-"or c == "Subtraction"or c == "SUBTRACTION"or c == "subtarction"or c == "Subtract"or c == "SUBTRACT"or c == "subtract" :
      print(a-b)
      print ("If your value is opposite,then try interchanging your value")
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
              
      i =  input("Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                    print ('''Pls Give answer in Y or N
                            ''')
      
    elif c == "*"or c == "Multiplication"or c == "MULTIPLICATION"or c == "multiplication"or c == "Multiply"or c == "MULTIPLY"or c == "multiply" :
      print(a*b)
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
        
      i =  input("Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')     
      
    elif c == "/"or c == "Division"or c == "DIVISION"or c == "division"or c == "Division"or c == "DIVISION"or c == "division" :
      print(a/b)
      print("If your value is opposite,then try interchanging your value")
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
              
      i =  input("Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
 
    elif c == "%"or c == "Modulus"or c == "MODULUS"or c == "modulus" :
      print(a%b)
      print("If your value is opposite,then try interchanging your value")
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
              
      i =  input("Did You liked my Calculator ? Y/N")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')    
      
    elif c== "**"or c == "Exponentiation"or c == "EXPOTENTIATION"or c == "exponentiation":
      print(a**b)
      print("If your value is opposite,then try interchanging your value")
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
              
      i =  input("Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
      
    elif c== "//"or c == "Floor Division"or c == "FLOOR DIVISION"or c == "floor division":
      print(a//b)
      print("If your value is opposite,then try interchanging your value")
      print(" Thank You",name)
      print("Re-Running....")
      print("Press Ctrl+C to Stop")
              
      i =  input("Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Thank You!!") 
      elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
    else :
        print("The following Operation is Invalid")
        print(" Thank You",name)
        print("Re-Running....")
        print("Press Ctrl+C to Stop")
              
        i =  input("Did You liked my Calculator ? Y/N ")
        if i == "Y" :
                     print ("Thank You!!") 
        elif i == "N" :
                     print ("Sorry,We Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')      
#For Developers,
# Dear Coders, This is not a Copyright Version and hereby allow to use this programming for further use.
#Happy Coding,
#Dheeraj,
#13
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
                    

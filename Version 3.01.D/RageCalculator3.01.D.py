"""What is New In this Version
1>Comparisons Operators also added
2>Introducing - "Dettio",your all new Virtual Assistant that will guide you through My Calculator
""" # <- For Developers
#Prefixes
print('''           ||||||||||||||||||||||||||||||||||||||||||||||||Welcome To Rage Calculator||||||||||||||||||||||||||||||||||||||||||||||
                                                                                                                                                Version -> 3.01.D''')
print("""What is New In this Version
1>Comparisons Operators also added
2>Introducing - "Dettio",your all new Virtual Assistant that will guide you through My Calculator
""") # <- For Users 
#Greetings
print("Hello, I am Dettio, your Virtual Assistant ")
name =  (input("Dettio - What is Your Name Sir/Madam ? "))
print ("Dettio - Hello "+ name, ", Nice to meet you. Let's get Started")

#The types of operations
print('''Dettio -                                           
These Are All the Possible Arithmetics :                                                       
1} Addition(+)                                                                                   
2}Subtraction(-)                                                                                      
3}Multiplication(*)                                                                               
4}Division(/)                                                                               
5}Modulus(%)                                                                                     
6}Expotentiation(**)                                                                        
7}Floor Divsion(//)                                                                                  
You can write the sign or the name                                                    
 ''')
print(''' Dettio - 
  These are all the Possible Comparisons :
  1}Greater than (>)
  2}Smaller than (<) 
  3}Greater than or equal to (>=)
  4}Lesser than or equal to ( <=)
  5}Equal to (=) 
  6}Not Equal to (!=))

#Program for asking for Operation or Comparison 
while True :
  ask = input("Dettio - What do you want to do ?(Comparison or Arithmetic)")
  #Comparison Operators
  if ask == "Comparison" or ask == "comparison" :
    comp = int(input("Dettio - Write The First Number " ))
    comp2 = int(input("Dettio - Write The Second Number " ))
    print("Dettio -  Remember, First Number is comparised with the Second")
    Comparisonask = input("Dettio - Write your Comparison Operator ")
    if Comparisonask == ">" :
        print (comp > comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    elif Comparisonask== "<" :
        print (comp < comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    elif Comparisonask== ">=" :
        print (comp >= comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    elif Comparisonask== "<=" :
        print (comp <= comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    elif Comparisonask=="=" :
        print(comp==comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    elif Comparisonask== "!=" :
        print(comp!=comp2)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

    else :
          print ("Dettio -  The Comparison Operator you are writing is either wrong,not supported by us or more likely to be a wrong sign")
  elif ask == "arithmetic"or ask == "Arithmetic" :      
    a = int(input("Dettio - Enter The First Number "))
    b = int(input("Dettio - Enter The Second Number "))
    c = input("Dettio - Enter The Operation You want to do ")
    if c == "+"or c == "Addition"or c == "ADDITION"or c == "addition"or c == "Add"or c == "ADD"or c == "add" :
        print(a+b)
        print("Dettio -  Thank You!!",name)
        print("Re-Running....")
        print("Dettio -  Press Ctrl+C to Stop")

        i =  input("Dettio - Did You liked my Calculator ? Y/N ")
        if i == "Y" :
                     print ("Dettio - Thank You!!") 
        elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
        else :
                     print ("Pls Give answer in Y or N")    
    
    elif c == "-"or c == "Subtraction"or c == "SUBTRACTION"or c == "subtarction"or c == "Subtract"or c == "SUBTRACT"or c == "subtract" :
      print(a-b)
      print ("Dettio - If your value is opposite,then try interchanging your value")
      print(" Dettio - Thank You",name)
      print("Re-Running....")
      print("Dettio - Press Ctrl+C to Stop")
              
      i =  input("Dettio - Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                    print ('''Pls Give answer in Y or N
                            ''')
      
    elif c == "*"or c == "Multiplication"or c == "MULTIPLICATION"or c == "multiplication"or c == "Multiply"or c == "MULTIPLY"or c == "multiply" :
      print(a*b)
      print(" Dettio - Thank You",name)
      print("Re-Running....")
      print("Dettio - Press Ctrl+C to Stop")
        
      i =  input("Dettio - Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')     
      
    elif c == "/"or c == "Division"or c == "DIVISION"or c == "division"or c == "Division"or c == "DIVISION"or c == "division" :
      print(a/b)
      print("Dettio - If your value is opposite,then try interchanging your value")
      print("Dettio -  Thank You!!",name)
      print("Re-Running....")
      print("Dettio -  Press Ctrl+C to Stop")
              
      i =  input("Dettio - Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
 
    elif c == "%"or c == "Modulus"or c == "MODULUS"or c == "modulus" :
      print(a%b)
      print("Dettio - If your value is opposite,then try interchanging your value")
      print(" Dettio - Thank You",name)
      print("Re-Running....")
      print("Dettio - Press Ctrl+C to Stop")
              
      i =  input("Dettio - Did You liked my Calculator ? Y/N")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')    
      
    elif c== "**"or c == "Exponentiation"or c == "EXPOTENTIATION"or c == "exponentiation":
      print(a**b)
      print("Dettio - If your value is opposite,then try interchanging your value")
      print(" Dettio - Thank You",name)
      print("Re-Running....")
      print("Dettio - Press Ctrl+C to Stop")
              
      i =  input("Dettio - Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
      
    elif c== "//"or c == "Floor Division"or c == "FLOOR DIVISION"or c == "floor division":
      print(a//b)
      print("Dettio - If your value is opposite,then try interchanging your value")
      print(" Dettio - Thank You",name)
      print("Re-Running....")
      print("Dettio - Press Ctrl+C to Stop")
              
      i =  input("Dettio - Did You liked my Calculator ? Y/N ")
      if i == "Y" :
                     print ("Dettio - Thank You!!") 
      elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
    else :
        print("Dettio - The following Operation is Invalid")
        print(" Dettio - Thank You",name)
        print("Re-Running....")
        print("Dettio - Press Ctrl+C to Stop")
              
        i =  input("Dettio - Did You liked my Calculator ? Y/N ")
        if i == "Y" :
                     print ("Dettio - Thank You!!") 
        elif i == "N" :
                     print ("Dettio - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')
  else : 
      print("Dettio - The Operation you want to do is Invalid")                
#For Developers,
# Dear Coders, This is not a Copyright Version and hereby allow to use this programming for further use.
#Happy Coding,
#Dheeraj,
#13

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

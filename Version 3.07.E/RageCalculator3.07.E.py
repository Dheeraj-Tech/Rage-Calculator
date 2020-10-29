""" What's new in this version(For Developers) :
1>Variables now have a meaningful name for proper understandment
"""
#Prefixes
print('''            |||||||||||||||||||||||||||||||||||||||||||||||||Welcome To Rage Calculator||||||||||||||||||||||||||||||||||||||||||||||
                                                                                                                                                Version -> 3.07.E''')
print("""What is New In this Version :
1>Now Input Decimal Numbers for Calculation
2>Short Outputs, Gives easier viewing to users
3>"Dettio" has upgraded to "Darweig"
""") # <- For Users 
#Greetings
print("Hello, I am Darweig, your Virtual Assistant ")
name =  (input("Darweig - What is Your Name Sir/Madam ? "))
print ("Hello "+ name, ", Nice to meet you. Let's get Started")

#The types of operations
print('''                                                                                
These Are All the Possible Arithmetics :     |             These are all the Possible Comparisons :                                        
1} Addition(+)                               |             1}Greater than (>)                                          
2}Subtraction(-)                             |             2}Smaller than (<)                                              
3}Multiplication(*)                          |             3}Greater than or equal to (>=)                                          
4}Division(/)                                |             4}Lesser than or equal to ( <=)                                    
5}Modulus(%)                                 |             5}Equal to (=)                                         
6}Expotentiation(**)                         |             6}Not Equal to (!=)                                    
7}Floor Divsion(//)                          |                                                        
                                          You can write the sign or the name 
''')


#Program for asking for Operation or Comparison 
while True :
  ask = input("Darweig - What do you want to do ?(Comparison or Arithmetic) ")
  #Comparison Operators
  if ask == "Comparison" or ask == "comparison" :
    comp = float(input("Darweig - Write The First Number " ))
    comp2 = float(input("Darweig - Write The Second Number " ))
    print("Darweig -  Remember, First Number is comparised with the Second")
    Comparisonask = input("Darweig - Write your Comparison Operator ")
    if Comparisonask == ">" :
        print (comp > comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")
        
        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    elif Comparisonask== "<" :
        print (comp < comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    elif Comparisonask== ">=" :
        print (comp >= comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    elif Comparisonask== "<=" :
        print (comp <= comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    elif Comparisonask=="=" :
        print(comp==comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    elif Comparisonask== "!=" :
        print(comp!=comp2)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')

    else :
          print ("Darweig -  The Comparison Operator you are writing is either wrong,not supported by us or more likely to be a wrong sign")
          #Arithmetic Operations Code 
  elif ask == "arithmetic"or ask == "Arithmetic" :      
    firstnumber = float(input("Darweig - Enter The First Number "))
    secondnumber = float(input("Darweig - Enter The Second Number "))
    arithmeticask = input("Darweig - Enter The Operation You want to do ")
    if arithmeticask == "+"or arithmeticask == "Addition"or arithmeticask == "ADDITION"or arithmeticask == "addition"or arithmeticask == "Add"or arithmeticask == "ADD"or arithmeticask == "add" :
        prfloat(firstnumber+secondnumber)
        print("Darweig -  Thank You!!",name)
        print("Re-Running....")
        print("Darweig -  Press Ctrl+C to Stop")

        inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                     print ("Pls Give answer in Y or N")    
    
    elif arithmeticask == "-"or arithmeticask == "Subtraction"or arithmeticask == "SUBTRACTION"or arithmeticask == "subtarction"or arithmeticask == "Subtract"or arithmeticask == "SUBTRACT"or arithmeticask == "subtract" :
      print( firstnumber-secondnumber)
      print ("Darweig - If your value is opposite,then try interchanging your value")
      print(" Darweig - Thank You",name)
      print("Re-Running....")
      print("Darweig - Press Ctrl+C to Stop")
              
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                    print ('''Pls Give answer in Y or N
                            ''')
      
    elif arithmeticask == "*"or arithmeticask == "Multiplication"or arithmeticask == "MULTIPLICATION"or arithmeticask == "multiplication"or arithmeticask == "Multiply"or arithmeticask == "MULTIPLY"or arithmeticask == "multiply" :
      print( firstnumber*secondnumber)
      print(" Darweig - Thank You",name)
      print("Re-Running....")
      print("Darweig - Press Ctrl+C to Stop")
        
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')     
      
    elif arithmeticask == "/"or arithmeticask == "Division"or arithmeticask == "DIVISION"or arithmeticask == "division"or arithmeticask == "Division"or arithmeticask == "DIVISION"or arithmeticask == "division" :
      print( firstnumber/secondnumber)
      print("Darweig - If your value is opposite,then try interchanging your value")
      print("Darweig -  Thank You!!",name)
      print("Re-Running....")
      print("Darweig -  Press Ctrl+C to Stop")
              
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
 
    elif arithmeticask == "%"or arithmeticask == "Modulus"or arithmeticask == "MODULUS"or arithmeticask == "modulus" :
      print( firstnumber%secondnumber)
      print("Darweig - If your value is opposite,then try interchanging your value")
      print(" Darweig - Thank You",name)
      print("Re-Running....")
      print("Darweig - Press Ctrl+C to Stop")
              
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')    
      
    elif arithmeticask == "**"or arithmeticask == "Exponentiation"or arithmeticask == "EXPOTENTIATION"or arithmeticask == "exponentiation":
      print( firstnumber**secondnumber)
      print("Darweig - If your value is opposite,then try interchanging your value")
      print(" Darweig - Thank You",name)
      print("Re-Running....")
      print("Darweig - Press Ctrl+C to Stop")
              
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
      
    elif arithmeticask == "//"or arithmeticask == "Floor Division"or arithmeticask == "FLOOR DIVISION"or arithmeticask == "floor division":
      print( firstnumber//secondnumber)
      print("Darweig - If your value is opposite,then try interchanging your value")
      print(" Darweig - Thank You",name)
      print("Re-Running....")
      print("Darweig - Press Ctrl+C to Stop")
              
      inputlike = input("Darweig - " + name +", Did You liked my Calculator ? Y/N ")
      if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
      elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
      else :
                     print ('''Pls Give answer in Y or N
                            ''')      
    else :
        print("Darweig - The following Operation is Invalid")
        print(" Darweig - Thank You",name)
        print("Re-Running....")
        print("Darweig - Press Ctrl+C to Stop")
              
        inputlike =  input("Darweig - " +name+ ", Did You liked my Calculator ? Y/N ")
        if inputlike == "Y" or inputlike == "y" :
                     print ("Darweig - Thank You!!") 
        elif inputlike == "N" or inputlike == "n" :
                     print ("Darweig - Sorry,I Will Try to Improve")
        else :
                    print ('''Pls Give answer in Y or N
                            ''')
  else : 
      print("Darweig -  The Comparison Operator you are writing is either wrong,not supported by us or more likely to be a wrong sign")
      
#For Developers,
# Dear Coders, This is not a Copyright Version and I hereby allow to use this programming for further use.
#Happy Coding,
#Dheeraj,
#13
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

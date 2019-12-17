### HELLOWORLD VERSION 2, TESTING IF STATEMENTS ###

print ("Welcome to HelloWorld Version 2")
print ("")
print ("Please type your name:") 
name1 = input()  
print ("Hello, ", name1, " !")
print ("The name ", name1, " has ", len(name1), "characters, that is pretty neat!"  )    
print ("Now please enter your age: ")
age1 = input()   
if int(age1) < 18:
    print(name1, "! Congratulations!!!! You still have enough time left to enjoy life" )
if int(age1) >= 18:
    print(name1, "! Your best years are behind you :(" )

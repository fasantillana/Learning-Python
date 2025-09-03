print("Hello World")
print("What is your name?")  # Ask for their name
my_name = input(">")
print("It is good to meet you, " + my_name)
print("The length of your name is:")
print(len(my_name))
print("What is your age?")  # Ask for their age
my_age = input(">")
#The code below works like PEMDAS where parenthesis will be evaluated first. 
#The function int(my_age) is taking my string value and converting it to interger, then it adds +1
#The function str() then converts my interger number back to string before it concactinates it 
print("You will be " + str(int(my_age) + 1) + " in a year.")

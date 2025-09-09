#Exercise 3
line = "Processor board ID FAL127990LA"
line1, line2, line3, line4 =line.split() #the variable 'line' is being split by whitespace into 4 different string variables
print(line4) #printing one of the 4 string variables that was split
linesplit = line.split() #splitting a sequence of strings will place all of them into a list[]
print(linesplit) #printing the whole list
print(linesplit[3]) #printing part of the list (position 3)



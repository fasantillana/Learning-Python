#Exercise 3 - Extracting serial number from string
line = "Processor board ID FAL127990LA"
line1, line2, line3, line4 =line.split() #the variable 'line' is being split by whitespace into 4 different string variables
print(line4) #printing one of the 4 string variables that was split
linesplit = line.split() #splitting a sequence of strings will place all of them into a list[]
print(linesplit) #printing the whole list
print(linesplit[3]) #printing part of the list (position 3)


#Exercise 4 - membership check on the 'line'variable
print('Processor board ID' in line)


#Exercise 5 - Concatenation 
ip_addr = '10.12.17.1'
mac_addr = '0024.c4e9.48ae'

print('String Concatenation\n' + (ip_addr) + ' --> ' + (mac_addr)) #printing without using f-strings
print(f'f-string \n {ip_addr} --> {mac_addr}') #printing using f-strings
print('Format Method \n {} --> {}'.format(ip_addr, mac_addr)) #printing useing the .format() method







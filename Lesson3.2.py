'''
a. Create a Python program that reads in the file named show_ip_int_brief.txt.
b. Loop over the file contents (in some way) and find the address that belongs to the "10.220" network. 
Note, since we have not talked about regular expressions yet, you can use simple string checks for finding this address.
c. Once you find the line containing the "10.220.x.x" address, extract both the interface name and the IP address. 
d. Save these two items to variables named "intf_name" and "ip_addr". Print these variables out to standard output.
'''
#a : Read file named 'show_ip_int_brief.txt'
with  open("show_ip_int_brief.txt") as f:
    file = f.readlines()
    #b - Looping over the file to find 10.220
    for line in file: 
        if "10.220" in line: #While looping through lines, if a line contains 10.220, do the following...
            print(line) # print the line
            line0 = line.split() # take that line which is a string and split contents into a list 

            #c - Extracting Interface and IP from the list and assigning as variables
            intf_name = line0[0] 
            ip_addr = line0[1]
            
            #d - printing the assigned variables
            print(intf_name)
            print(ip_addr)
            



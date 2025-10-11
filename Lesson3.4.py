'''
4. Create a Python program that reads the file named show_ip_int_brief.txt. 
a. Loop over the contents of this file (in some way).

From the contents of this file, find all of the interfaces that are assigned an IP address. 
You can assume that any IP address will start with "10.".

From this, create a list of all of the assigned IP addresses. 
Additionally, create a list of all the interfaces containing an IP address. 
The order of these two lists should match. 
In other words, the first IP address should correspond to the first interface in the interfaces list.

Print both of these lists out to standard output.

'''

with open ("show_ip_int_brief.txt") as f:
    file = f.readlines()
    for x in file: #a - looping over the contents of the file
        if "10" in x: #b - if 10 is in a line(x) 
            print(x)
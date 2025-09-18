'''3. Create a list of five IP addresses. Print the initial list of addresses.
a. Use the .append() method to add an IP address onto the end of the list
b. Use the .extend() method to add two more IP addresses to the end of the list.
c. Use list concatenation to add two more IP addresses to the end of the list.
d. Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.
e. Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
f. Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.'''

#List of five IP addresses. Print the list
ip_list = ['10.0.0.1', '192.168.0.1', '127.0.0.5', '224.20.45.3', '8.3.3.7']
print(ip_list)

#a
ip_list.append('129.98.80.5')

#b
ip_list.extend(['2.2.2.5'])

#c
ip_list = ip_list + ['7.7.7.7', '4.4.4.4']

#d
print(ip_list)
print(ip_list[0])
print(ip_list[-1])

#e
ip_list.pop(0)
ip_list.pop()

#f
ip_list = ['2.2.2.2'] + ip_list
print(ip_list)
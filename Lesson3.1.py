'''1. This exercise expands on the subnet calculations from lesson2, exercise1.

Create a base address variable and set it to "192.168.254.". Prompt a user to enter a subnet prefix length that ranges between 25 to 30 
(i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). 
Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number and the broadcast address).

Use a loop to print out all of the subnet network numbers. For example, if your prefix length is 26, then your program should print out the following:

​Subnets:
 Number of subnets: 4
 Subnet Number: 192.168.254.0
 Subnet Number: 192.168.254.64
 Subnet Number: 192.168.254.128
 Subnet Number: 192.168.254.192

Your program should print out the following:
     a. The number of hosts in the subnet.
     b. The total number of subnets and the network number for each of the subnets
     c. The first and last host address in just the first subnet'''

#The setup: Imported from Lesson 2 - Exercise 1
base_addr = '192.168.254.'
submask1 = int(input('Please insert subnet prefix length within range 25-30:\n >')) #prompted user for slash notation and saved as int
borrowed_bits = submask1 - 24 # needed to calculate sub-networks
hosts = 2**(32 - submask1) - 2 # this is the calculation i use when subnetting. 2 to the power of unused bits minus 2 for Network and Broadcast
subnets = 2**borrowed_bits # amount of subnets, 2 to the power of borrowed bits.
bitlist = [128, 64, 32, 16, 8, 4, 2, 1]
octet = list(range(256))#created a list containing 0-255 in case I need it later on. 
net1 = octet[0]
net2 = net1 + bitlist[borrowed_bits - 1]
# a
print(f'there are {hosts} available hosts in your given subnet')
# b
print(f'the first network number is {base_addr}{net1} \nThe second network starts at {base_addr}{net2}')
#c
print(f'the first host address of the first subnet is {base_addr}{net1 + octet[1]} \n the last available host address is {base_addr}{net2 - 2}')

#Implementing a Loop to show all network subnet numbers

while net1 < octet:
    print(net1)
    net1 = net1 + bitlist[borrowed_bits - 1]
    



#Kirk Byers' Lesson 2 - Exercise 1
base_addr = '192.168.254.'
submask1 = int(input('Please insert subnet prefix length within range 25-30:\n >')) #prompted user for slash notation and saved as int
borrowed_bits = submask1 - 24 # needed to calculate sub-networks
hosts = 2**(32 - submask1) - 2 # this is the calculation i use when subnetting. 2 to the power of unused bits minus 2 for Network and Broadcast
subnets = 2**borrowed_bits # amount of subnets, 2 to the power of borrowed bits.
bitlist = [128, 64, 32, 16, 8, 4, 2, 1]
octet = list(range(256))#created a list containing 0-255 in case I need it later on. 
net1 = octet[0]
net2 = net1 + bitlist[borrowed_bits - 1]
print(f'there are {hosts} available hosts in your given subnet')
print(f'the first network number is {base_addr}{net1} \nThe second network starts at {base_addr}{net2}')
print(f'the first host address of the first subnet is {base_addr}{net1 + octet[1]} \n the last available host address is {base_addr}{net2 - 2}')

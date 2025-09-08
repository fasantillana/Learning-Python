#Exercise 1 - IP Table
sf_gw1 = "172.31.255.1/24"
sf_gw2 = input('what is your gw2 IP address?:\n>')
headerline = '-' * 20
header1 = 'sf_gw1'
header2 = 'sf_gw2'
print(f'{header1:^20}{header2:^20}"\n"{headerline:^} {headerline:^}"\n"{sf_gw1:^20}{sf_gw2:^20}')

#Exercise 2 - Data Center Location 
# a. Use the .upper() method to convert the data center location to all upper case. Print this variable out.
dc_location = 'Ashburn    '
print(dc_location.upper())
# b - whitespace
print('strip off whitespace:')
print(f'before: {repr(dc_location)}')
print(f'after: {repr(dc_location.strip())}')
print(f'Method Chaining:\n {repr(dc_location.upper().strip())}')

#Exercise 3 - Extracting Information from a string
somevar ="test"
anothervar= "wow"
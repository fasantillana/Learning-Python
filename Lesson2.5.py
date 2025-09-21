"""5. Create a variable named 'intf' using the following string (from 'show ip interface brief' on a Cisco router):
a. intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

b. split() this variable into fields based on white-space and save this to a variable named intf_fields.

c. From this new 'intf_fields' variable, create variables named intf_name, intf_ip_addr, intf_status, intf_protocol 
and match the corresponding fields from the above output (the first two fields and the last two fields, respectively).

d. Print out each of these four variables and their corresponding values.

e. Create booleans indicating whether both line status and line protocol are in the 'up' state. Print these booleans to the screen."""

#a
intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

#b
intf_fields = intf.split()
print(intf_fields)

#c
intf_name = intf_fields[0]
intf_ip = intf_fields[1]
intf_status = intf_fields[-2]
intf_protocol = intf_fields[-1]

#d 
print(f"{intf_name} \n {intf_ip} \n {intf_status} \n {intf_protocol}")

#e
print("up" in intf_protocol)
print("up" in intf_status )

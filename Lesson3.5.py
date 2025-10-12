'''
 a. Create a Python program that reads the file named junos_show_arp.txt. 
 b. From this Junos ARP information, extract all of the IP address to MAC-address bindings. 
 c. Convert the MAC address format from '06:1a:97:b0:c4:89' to '06-1a-97-b0-c4-89'
 d. Print all of these pairings out to standard output.
'''
#a - opened the file
with open("junos_show_arp.txt") as f:
    #b - extracting IP to MAC bindings
    file = f.readlines()
    for line in file:
        if ":" in line:
            line = line.replace(":", "-") #c - Converted the MAC Address from containg : to containging -
            print(line) #printed the line

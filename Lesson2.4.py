'''Using a context manager, open the file named "show_arp.txt". Read the contents of this file in (using the f.readlines() method) and save the file contents to a variable named 'show_arp'.
a. Print out the Python data type of 'show_arp' variable.
b. Print out the length of the 'show_arp' variable.
c. Print out the header line from the 'show_arp' variable.
d. Print out both the first and the last line of the tabular data from the 'show_arp' variable.
e. Split the header line into fields using the .split() method. Save this into a variable named fields. Print out this 'fields' variable.
f. Print out the Python data type of this 'fields' variable.
g. Print out the current number of entries in the 'fields' variable.
h. Print out the first field and the last field.

If you print out the fields variable you will observe that some fields are unneeded or incorrect (due to the splitting on whitespace).

For example, there are fields containing 'Age' and '(min)', but that is only one column in the tabular output. Similarly, 'Hardware' and 'Addr' were split into two fields, 
but there is only one corresponding column in the table output.

Consequently, you should delete the field containing '(min)' from the list. Similarly, you should combine the 'Hardware' and 'Addr' entries into a single field named 'Hardware_Addr'. 
At the end of your modifications, you should only see the following six fields in the 'fields' variable.
['Protocol', 'Address', 'Age', 'Hardware_Addr', 'Type', 'Interface']
Finally, print out the fields variable after you have made the above corrections.
'''
with open('show_arp.txt') as f:
    show_arp = f.readlines()

    #a
    print(show_arp)

    #b
    print(len(show_arp))

    #c
    print (show_arp[0])

    #d
    print(show_arp[1], show_arp[-1])

    #e
    fields = show_arp[0].split()
    print(fields)
    #f
    print(type(fields))

    #g
    print(len(fields))

    #h
    print(fields[0],fields[-1])

    #corrections / modifications
    fields.pop(3)
    fields.pop(4)
    fields[3] = 'Hardware_Addr' #there was probably a more efficient way to combine. Will revisit in the future
    print(fields)



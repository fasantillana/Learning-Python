#Kirk Byers' PyNet Learning Python : Lesson 2 Exerice 2 

#opened the file show_version.txt as read-only and passed all the output onto variable 'data'
f = open("show_version.txt")
data = f.readline() #using f.readline over .read() would print just the first line

# the following is not a valid way to use pring:  print(f.readline())
print(data)
print(type(data))
f.close()

#Doing the same task as above but this time I am using with to create a context manager (which is useful to contain errors
with open("show_version.txt") as f: 
    data=f.readline()
    print(data)
    print(type(data))


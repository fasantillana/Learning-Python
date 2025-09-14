#Kirk Byers' PyNet Learning Python : Lesson 2 Exerice 2 

#opened the file show_version.txt as read-only and passed all the output onto variable 'data'
f = open('show_version.txt', mode='r')
data = f.read()

print(f.readline())
print(type(data))
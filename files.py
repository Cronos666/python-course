#opens file as "file" ( file name, atribiutes) atribiutes: r - read,    a - append, w - write, x - create, t - text, b - binary
file = open("LICENSE", "rt") 
print(file.read())
file.close()
#append file
file = open("demofile", "at")
file.write("Live long and prosper.")
file.close()
#read file
f = open("demofile", "rt")
print(f.read())
f.close()
#delete file
import os
os.remove("demofile")
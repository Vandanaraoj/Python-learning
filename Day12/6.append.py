file=open("write.txt", 'a')
file.write("This is an appended line\n")
file.write("Python programming is fun")
file.close()

file=open("write.txt", 'r')
content=file.read()
print(content)
file.close()
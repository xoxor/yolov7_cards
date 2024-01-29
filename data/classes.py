file = open("classes.txt","r")
lines = [line.rstrip() for line in file]
print(lines)
print(len(lines))
file.close()
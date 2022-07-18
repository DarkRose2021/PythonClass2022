# fileio
# 'r' read = stream in at the beginning of the file
# 'w' write = stream out at the beginning of the file
#'a' append = stream out at the end of the file

file = open('test1.txt', 'w')
file.write('hello, world\n')
file.write('thanks for visiting')
file.close()

file1 = open('test1.txt', 'r')
content = file1.read()
file1.close()
print(content)

file2 = open('test1.txt', 'a')
file2.write('\nand now for something completely different')
file2.close()

with open('test1.txt', 'w') as file3:
    file3.write('i overwrite everything')
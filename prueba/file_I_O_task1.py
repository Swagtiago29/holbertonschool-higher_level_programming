#!/usr/bin/python3

content = '''text
Hello, world! 
Welcome to file I/O in Python.'''
with open("txt_folder/example.txt", "w") as f:
    f.write(content)

with open("txt_folder/example.txt", "r") as f2:
    print(f2.read())
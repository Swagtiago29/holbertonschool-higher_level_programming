#!/usr/bin/python3

content = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vel blandit magna, ac aliquam elit. Donec vehicula, nibh eget accumsan placerat, orci turpis imperdiet nisl, non semper magna leo id ligula. Curabitur vehicula pretium nibh non condimentum.'''
with open("txt_folder/source.txt", "w") as f:
    f.write(content)

with open("txt_folder/source.txt", "r") as f1:
    text_file1 = f1.read()

with open("txt_folder/destination.txt", "w") as f2:
        f2.write(text_file1)

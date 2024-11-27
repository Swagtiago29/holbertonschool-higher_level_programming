#!/usr/bin/python3

with open("txt_folder/words.txt", "w") as f:
    f.write("ola amigos, como me gusta python3 lol xd")

with open("txt_folder/words.txt", "r") as f2:
    content = f2.read()

list = content.split()
print(f"Palabras: {len(list)}")
print(f"Letras: {len(content)}")
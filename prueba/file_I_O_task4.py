#!/usr/bin/python3
import re

content = '''The moon hung brightly in the night sky, casting a silver glow over the calm landscape. As the moon rose higher, the sky darkened, revealing countless stars that twinkled like tiny diamonds. The sky was clear, and the moon seemed to smile down upon the world. In the distance, the stars sparkled even more vividly, a beautiful display against the deep blue sky. The moon's light reflected off the water, creating a mirror image of the star-filled sky.'''
with open("txt_folder/test_lookfor.txt", "w")as f:
    f.write(content)
try:
    user_input = input("Looking for?: ")
    file_name = input("Inside?: ")
    with open(f"txt_folder/{file_name}", "r") as f1:
        text_test = f1.read()
    list_text = text_test.split()
    counter = 0
    for i in list_text:
        if i == user_input:
            counter = counter + 1
    print(f"found {user_input}: {counter} times")
except(FileNotFoundError):
    print("File not found")
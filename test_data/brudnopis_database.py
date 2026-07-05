import os

pwd = os.getcwd()
root = os.listdir(pwd)
file_names = []
directories = list()

files_contents = list()
for file in root:
    directories.append(f"{pwd}/{file}")

for file in directories:
    with open(f"{file}", "r", encoding="utf-8") as file:
        files_contents.append(file.read())


for content in files_contents:
    print(f"{content}\n")
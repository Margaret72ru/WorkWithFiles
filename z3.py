import os

dict = []
dir_for_files = "files"
for filename in os.listdir(dir_for_files):
    with open(os.path.join(dir_for_files, filename), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        dict.append((filename, len(lines), lines))
dict.sort(key=lambda s: s[1])

with open('file.txt', 'w', encoding='utf-8') as f:
    for item in dict:
        f.write(item[0] + "\n")
        f.write(str(item[1]) + "\n")
        f.writelines(item[2])
        f.write("\n")

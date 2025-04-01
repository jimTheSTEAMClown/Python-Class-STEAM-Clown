# Opening File Handles and reading data from files
# You can get the following files with wget
# sudo wget -O text-flie-matrix.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-matrix.txt
# sudo wget -O text-file-mail-very-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-very-short.txt
print('''
This Lab is about opening a file handle, and 
printing the file handle.

Hint: Check out W3Schools File Handling
- https://www.w3schools.com/python/python_file_handling.asp
      ''')
# Challenge 1
# Describe the parts of the file handle
print('''
Challenge # 1
----------------------------------------------------
Can you explain each part of the file handle? 

What does the following parts of the file handle mean?
1) _io.TextIOWrapper 
2) name='matrix.txt' 
3) mode='r' 
4) encoding='UTF-8'>
      
Hint: https://www.w3schools.com/python/python_file_handling.asp
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
-------------------------------------------------''')
# What does the following parts of the file handle mean?
# 1) _io.TextIOWrapper 
# 2) name='text-file-matrix.txt' 
# 3) mode='r' 
# 4) encoding='UTF-8'>
# print('The parts of a file handle are:')
# -----------------------------
xfile = open('text-file-matrix.txt')
print(xfile)
print('''
-------------------------------------------------''')

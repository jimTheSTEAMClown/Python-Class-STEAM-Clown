# Opening File Handles and reading data from files
# What happends if the file does not exist?
# You can get the following file with wget
# sudo wget -O text-flie-matrix.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-matrix.txt
# sudo wget -O text-file-mail-very-short.txt https://raw.githubusercontent.com/jimTheSTEAMClown/Python-Class-STEAM-Clown/refs/heads/main/text-file-mail-very-short.txt

print('''
This Lab is about opening a file handle, and 
printing the file handle.

Hint: Check out W3Schools File Handling
- https://www.w3schools.com/python/python_file_handling.asp
      ''')
# -----------------------------
print('''
Challenge
----------------------------------------------------

What happends if the file does not exist? 
- Try opening a file that does not exist... 
Like "text-file-matrix2.txt"

Can you open a diffrent file? 
- Try opening the file "text-file-very-short.txt"
---
''')
# -------------------------------------------------
print('''Answer to Challenge
-------------------------------------------------''')
# Try opening a file that does not exist... Like "matrix2.txt"
xfile = open('text-file-matrix.txt')
print(xfile)
print('''
-------------------------------------------------''')


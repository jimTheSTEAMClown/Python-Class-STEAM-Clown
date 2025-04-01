# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, printing line by line, and striping the 
extra /n at the end of a line in a file
      ''')
# Challenges
print('''
Challenge #1
----------------------------------------------------
#1 - Edit the code below to not print 
     the extra "\\n" on each line
Hint: Use a String Method that will "strip" a character. 
- https://www.w3schools.com/python/python_strings_methods.asp

#2 - Edit the code below to open the text-file-mail-very-short.txt file
---
''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')
# -----------------------------
fhand = open('text-file-matrix.txt')
for line in fhand:
	print(line)
print('Done')
print('''
-------------------------------------------------''')

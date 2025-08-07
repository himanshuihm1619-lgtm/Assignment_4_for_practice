# Assignment_4_for_practice

# Assignment 4: Files, Exceptions, and Errors in Python

This assignment covers **Module 5: File Handling, Exceptions, and Error Management in Python**, and includes two tasks:

---

## 📌 Task 1: Read a File and Handle Errors

### Description:
This task demonstrates how to **read specific lines from a file** and handle the **FileNotFoundError** exception if the file does not exist.
```python
### Code Snippet:

print("Reading file content:")
samplefile = 'sample.txt'

try:
    file1 = open('sample.txt', 'r')
    line1 = file1.readline()
    print("Line 1:", line1)
    line2 = file1.readline()
    print("Line 2:", line2 + "\n")

except FileNotFoundError:
    print(f"Error: The file '{samplefile}' was not found.")

file1.close()

Example Output:

Reading file content:
Line 1: Hello, world.
Line 2: Welcome to Python.

#Or if the file doesn't exist:
#Error: The file 'sample.txt' was not found.

📌 Task 2: Write and Append Data to a File
Description:
This task allows the user to:
Write new content to a file named output.txt
Append additional content to the same file
Read and display the final content of the file

Code Snippet:

x = str(input("Enter text to write to the file: "))
file2 = open('output.txt','w')
file2.write(x + '\n')
print("Data successfully written to output.txt.")
file2.close()

y = str(input("Enter additional text to append: "))
file3 = open('output.txt','a')
file3.write(y + '\n')
print("Data successfully appended.")
file3.close()

print("Final content of output.txt:")
file4 = open('output.txt','r')
reading_file4 = file4.read()
print(reading_file4)
file4.close()

Example Run:

Enter text to write to the file: Python is fun.
Data successfully written to output.txt.
Enter additional text to append: I love coding.
Data successfully appended.
Final content of output.txt:
Python is fun.
I love coding.


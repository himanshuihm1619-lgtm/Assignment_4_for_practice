'''
ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
'''
print("Reading file content:")
samplefile = 'sample.txt'

try:
    file1 = open('sample.txt', 'r')
    line1 = file1.readline()
    print("Line 1:",line1 )

    line2 = file1.readline()
    print("Line 2:", line2 + "\n")

except FileNotFoundError:
    print(f"Error: The file '{samplefile}' was not found.")

file1.close()

# Task 2: Write and Append Data to a File
x = str(input("Enter text to write to the file: "))
file2 = open('output.txt','w')
writing_file2 = file2.write(x +'\n')
print("Data successfully written to output.txt.")
file2.close()

y = str(input("Enter additional text to append: "))
file3 = open('output.txt','a')
append_file3 = file3.write(y + '\n')
print("Data successfully appended.")
file3.close()

print("Final content of output.txt:")
file4 = open('output.txt','r')
reading_file4 = file4.read()
print(reading_file4)
file4.close()
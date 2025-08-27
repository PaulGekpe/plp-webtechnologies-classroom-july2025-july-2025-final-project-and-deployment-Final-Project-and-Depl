"""
File Handling and Exception Handling Assignment
Author: Paul Kelechi Gekpe
Date: 27 August 2025
Description: Demonstrates writing to and reading from a file in Python,
with proper exception handling and best practices.
"""
try:
    # ---Writing to a file---
    # 'w' mode creates the file if it doesn't exist, or overwrites if it does
    with open("my_file.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is my phython assignment on file handling.\n")
        file.write("Practising both write and read operations!\n")
         # --- Reading from the file ---
    # 'r' mode opens the file for reading
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Content:\n" + content)
except FileNotFoundError:
    # Happens if the file path is wrong or missing
    print("Error: The file was not found.")
except PermissionError:
    # Happens if we don't have the rights to access the file
    print("Error: You do not have permission to access this file.")
except Exception as e:
     # Catches any other unexpected exceptions
     print(f"An unexpected error occurred: {e}")
finally:
     # Always runs, whether an error happened or not
    print("File operation completed.")
# using readlines()
open_file = open('file.txt', 'r')
File_lines = open_file.readlines()
print("\n File content:/n")
print(File_lines)
open_file.close()

# using strip
print("/n File content after removing newline character:")
File_lines = [i.strip() for i in File_lines]
print([i.strip() for i in File_lines])
open_file.close()

# without using strip
print("\n File content with newline character:")
print(File_lines)
#Add .txt extension to the 1st file that dont have any extension, note: the script has to be in the root directory /Users/admin/python/test
import os
# Set the root directory 
root = '/Users/admin/python/test'
# Update the root directory to the current working directory
root = os.getcwd()
# Iterate over files in the current directory
for file in os.listdir('.'):
 # Check if the current item is not a file, and if so, continue to the next iteration
    if not os.path.isfile(file):
       continue

 # Split the file name into its head (path) and tail (extension)
head, tail = os.path.splitext(file)
   # Check if the file has no extension
if not tail:
# Construct source and destination paths
   src = os.path.join (root, file)
   dst = os.path.join (root, file + '.txt')
# Check if the destination file does not already exist
   if not os.path.exists(dst):
     # Rename the source file to the destination file
      os.rename(src, dst)

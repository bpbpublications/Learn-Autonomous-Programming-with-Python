#Run each of these pieces separately

import os
objCWD = os.getcwd()
print("The current working directory is:", objCWD)


import os
if not os.path.exists('Test Folder'):
    os.mkdir('Test Folder')


import os
try:
    os.rmdir('Test Folder')
except Exception as e:
   	print(f"An error occurred: {e}")

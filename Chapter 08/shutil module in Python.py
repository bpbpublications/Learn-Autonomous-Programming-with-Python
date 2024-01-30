#Run each of these pieces of code separately

import shutil
source = "Shutil_Test.xlsx"
destination ="Copy-Shutil_Test.xlsx"
dest = shutil.copy(source, destination)


import shutil
source = "Shutil_Test.xlsx"
destination = "Move_Test/"
dest = shutil.copy(source, destination)

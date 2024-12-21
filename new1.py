import new
print(new.x)

#or
from new import x
print(x)

#or
from new import subtraction_from_my_side as s
data=s(30,20)
print(data)

#or
import new as n
print(n.x)

#collection of module in  a folder is called package.
#module means file in a folder
#collection of packages in a folder,so that folder is called library
#in python2 we need to make empty file named as __init__.py, to 
# understand interpreter that it is a package

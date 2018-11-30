#Pickle it
#demonstrates pickling and shelving data

import pickle
import shelve
import dbm


print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["clausen", "heinz", "vlassic"]

objfile = open("picklez.dat", "wb")

#pickle.dump
#requires two arguments: data to pickle and the file in which to store it

pickle.dump(variety,objfile)
pickle.dump(shape,objfile)
pickle.dump(brand,objfile)
objfile.close()

#pickleload() function. takes one argument: the file from which the load the next pickled object

print("\nUnpickling lists.")
objfile = open("picklez.dat", "rb")
variety = pickle.load(objfile)
shape = pickle.load(objfile)
brand = pickle.load(objfile)

# pickle.load() is reading the object to produce the list, and assigns the list to the object.

#print
print(variety)
print(shape)
print(brand)
objfile.close()

print("/nShelving lists.")
s = shelve.open("picklez.dat")
#---------------------------------------#
#Traceback error#
#see below# 

Traceback (most recent call last):
  File "C:/_PythonClass/Assignment07/Module07/Pickle_It.py", line 41, in <module>
    s = shelve.open("picklez.dat")
  File "C:\Users\rlarge\AppData\Local\Programs\Python\Python37-32\lib\shelve.py", line 243, in open
    return DbfilenameShelf(filename, flag, protocol, writeback)
  File "C:\Users\rlarge\AppData\Local\Programs\Python\Python37-32\lib\shelve.py", line 227, in __init__
    Shelf.__init__(self, dbm.open(filename, flag), protocol, writeback)
  File "C:\Users\rlarge\AppData\Local\Programs\Python\Python37-32\lib\dbm\__init__.py", line 88, in open
    raise error[0]("db type could not be determined")
dbm.error: db type could not be determined


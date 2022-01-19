'''This is a static file which just reads binary data from \'counterfile.bin\'

DATA
----
file : imported from .main
fh : file handle of the file 'counterfile.bin'
count : number of times your computer was turned on
        This is read from binary file 'counterfile.bin'''

import pickle, os
file = os.path.join( os.getcwd(), 'counterfile.bin' )
if os.path.exists(file):
    fh=open(file, 'rb')
    count=pickle.load(fh)
    fh.close()
else:
    count=0
'''The main file which has to be run during system startup.

DATA
----
file : the link to the file 'counterfile.bin'
counterfile : file handle of the file 'counterfile.bin'
count : number of times your computer was turned on
        This is read from binary file 'counterfile.bin' 
        (and also it is incremented and dumped)

Windows
-------
Put the link of this file in \"onf.cmd\" and put that file in \'shell:startup\''''
# All the numbers are steps of '### Programming Logic used' in 'README.md'
# https://github.com/ShobanChiddarth/counter/blob/main/README.md
import os
file = os.path.join(os.path.dirname(__file__), 'counterfile.bin') # The file which the 
# count has to be stored as binary
if __name__=='__main__':
    import pickle
    if os.path.exists(file): # 1
        counterfile=open(file, 'rb')
        count=pickle.load(counterfile) # The count
        # (the number of times your system was turned on)
    else: # 2
        counterfile=open(file, 'wb')
        count=0
        pickle.dump(count, counterfile)

    counterfile.close() # 3
    count+=1 # 4
    counterfile=open(counterfile.name, mode='rb+') # 5

    # 6
    counterfile=open(file, 'wb')

    pickle.dump(count, counterfile) # 7

    counterfile.close() # 8

# This file simply counts number of times it was run.
# Developed from project https://github.com/shobanchiddarth/counter
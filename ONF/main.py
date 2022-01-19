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
import os
file = os.path.join( os.getcwd(), 'counterfile.bin' ) # The file which the 
# count has to be stored as binary
if __name__=='__main__':
    import pickle
    if os.path.exists(file):
        counterfile=open(file, 'rb')
        count=pickle.load(counterfile) # The count
        # (the number of times your system was turned on)
    else:
        counterfile=open(file, 'wb')
        count=0
        pickle.dump(count, counterfile)
    counterfile.close()
    os.remove(file)
    count+=1
    counterfile=open(file, 'wb')
    pickle.dump(count, counterfile)
    counterfile.close()

# This file simply counts number of run.
# Developed from project https://github.com/shobanchiddarth/counter (yet to be published)
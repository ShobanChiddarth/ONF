'''The main file which has to be run during system startup.

DATA
----
files : the list of links to the files where the data is stored ('counterfile.bin')
counterfile : file handle of the file 'counterfile.bin'
count : number of times your computer was turned on
        This is read from binary file 'counterfile.bin' 
        (and also it is incremented and dumped)

Windows
-------
Put the link of this file in \"onf.cmd\" and put that file in \'shell:startup\''''


import os
file = os.path.join(os.path.dirname(__file__), 'counterfile.bin') 

if __name__=='__main__':
    import pickle
    if os.path.exists(file): 
        counterfile=open(file, 'rb')
        count=pickle.load(counterfile)
    else:
        counterfile=open(file, 'wb')
        count=0
        pickle.dump(count, counterfile)

    counterfile.close() 
    count+=1 
    counterfile=open(counterfile.name, mode='rb+') 

    
    counterfile=open(file, 'wb')

    pickle.dump(count, counterfile) 

    counterfile.close() 

# This file simply counts number of times it was run.
# Developed from project https://github.com/shobanchiddarth/counter
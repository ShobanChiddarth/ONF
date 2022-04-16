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
# from . import config
import config
import pickle

d = config.load_deque_of_files()

for item in d:

    count=config.load_val(item)
    count+=1

    with open(item, mode='wb') as fh:
        fh.write(pickle.dumps(count))



# This file simply counts number of times it was run.
# Developed from project https://github.com/shobanchiddarth/counter
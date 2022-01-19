import pickle, os
from .main import file
if os.path.exists(file):
    fh=open(file, 'rb')
    count=pickle.load(fh)
    fh.close()
else:
    count=0
import pickle, os
from .main import file
if os.path.exists(file):
    count=pickle.load(open(file, 'rb'))
else:
    count=0
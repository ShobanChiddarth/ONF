import os
file = os.path.join( os.getcwd(), 'counterfile.bin' )
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
    os.remove(file)
    count+=1
    counterfile=open(file, 'wb')
    pickle.dump(count, counterfile)
    counterfile.close()
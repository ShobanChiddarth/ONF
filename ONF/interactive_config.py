# from .config import *
from tkinter import filedialog
from config import *
from pprint import pprint



def main():

    print('Files that store the system turn on count are')
    deque_of_files=load_deque_of_files()
    pprint(list(deque_of_files))
    while True:
        choice=input('Do you want to change anything [Y/n]?')[0].strip().lower()
        if choice=='y':
            print('''File choose modes
    0 : create new file (save as)
    1 : open and overwrite existing file''')
            fileChooseMode=int(input('Enter file choose mode : '))
            if fileChooseMode == 0:
                
                filename=filedialog.asksaveasfilename(
                                        defaultextension='.bin',
                                        filetypes=[('Binary file', '*.bin'), 
                                                    ('Data file', '*.dat'), 
                                                    ('All binary files', '*')],
                                                    title='Choose a binary file to store system on off count')
                print(filename)
                deque_of_files.append(filename)
                flushoverwite(deque_of_files)
            elif fileChooseMode == 1:
                append_to_deque_open()

            elif choice=='n':
                break
            else:
                print('Wrong input')
                continue



main()

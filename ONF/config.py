from tkinter import filedialog
import os
import pickle
from collections import deque

_folder=os.path.dirname(__file__)
BackupDequeFilePath=os.path.join(_folder, 'deque_of_backups.bin')
default_filepath = os.path.join(_folder, 'counterfile.bin')


def load_val(file=default_filepath):
    if os.path.exists(file):
        with open(file, 'rb') as fh:
            return pickle.loads(fh.read())
    else:
        with open(file, 'wb') as fh:
            fh.write(pickle.dumps(0))
            return 0

def load_deque_of_files():
    if os.path.exists(BackupDequeFilePath):
        with open(BackupDequeFilePath, 'rb') as fh:
            deque_of_files=pickle.loads(fh.read())
            if default_filepath not in deque_of_files:
                deque_of_files.appendleft(default_filepath)
            return deque_of_files
    else:
        with open(BackupDequeFilePath, 'wb') as fh:
            deque_of_files=deque([default_filepath])
            fh.write(pickle.dumps(deque_of_files))
            return deque_of_files



def flushoverwite(item, filepath=BackupDequeFilePath):
    with open(filepath, 'wb') as fh:
        fh.write(pickle.dumps(item))
    


def append_to_deque_saveas():
    deque_of_files=load_deque_of_files()
    deque_of_files.append(
        filedialog.asksaveasfilename(confirmoverwrite=True,
                                        defaultextension='.bin',
                                        filetypes=[('Binary file', '*.bin'), 
                                                    ('Data file', '*.dat'), 
                                                    ('All binary files', '*')],
                                                    title='Choose a binary file to store system on off count')
                            )
    flushoverwite(deque_of_files)


def append_to_deque_open():
    deque_of_files=load_deque_of_files()
    deque_of_files.append(
        filedialog.askopenfilename(
                                    defaultextension='.bin',
                                    filetypes=[('Binary file', '*.bin'), 
                                                ('Data file', '*.dat'), 
                                                ('All binary files', '*')],
                                    title='Open a binary file to overwrite system on off count'
                                    )
                            )
    flushoverwite(deque_of_files)

            
# ONF - System on and off counter

This is a small package with which you can count the number of times your computer was turned on.

### Requirements
1. Python 3
2. Windows computer (Windows 10 is preffered)

### Installation
1. Copy the folder [ONF](.\ONF)
2. Paste it in 'site-packages'
   
   To open 'site-packages'
   Run this piece of code in python
   
   ```python
   import sys, webbrowser
   for folder in sys:
      if folder.endswith('site-packages'):
          webbrowser.open(folder)
   ```

3. Open 'static.py' and ', 'main.py' from the folder you just pasted in 'site-packages'
4. Create a text file 'counterfile.bin' in the folder
5. Right click and copy as path

   ![copy-as-path](Assets\Images\copy-as-path.png)

6. Delete the file
7. Replace `"link-to-counterfile.bin"` in 'static.py' and 'main.py'

   Don't miss out the `r`.

   Finally it should look like
   ```python
   file = r"C:\Users\Admin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\ONF\counterfile.bin"
   ```

The following is only for windows computers

8. Open [onf.cmd](.\Assets\onf.cmd) in a text editor
9. Open the folder 'ONF' in 'site-packages' that you just pasted
10. Copy the folder link from address bar

   ![explorer-addressbar-01](Assets\Images\explorer-addressbar-01.png)
   ![explorer-addressbar-02](Assets\Images\explorer-addressbar-02.png)

11. Replace ```"link-to-folder-ONF"``` in [onf.cmd](.\Assets\onf.cmd) with the copied link
12. Copy the file [onf.cmd]
13. Open Windows Explorer (Using Win+E)
14. In the address bar, type "shell:startup" and hit enter
   ![explorer-addressbar-03](Assets\Images\explorer-addressbar-03.png)
15. Paste the [onf.cmd](.\Assets\onf.cmd) file you just copied

You are all set. Whenever your computer starts up, it will be counted.
To know the count, run this piece of code in python
```python
from ONF import count
print(count)
```


#### Non-Windows computers
Please refer to other sources to know about files to be opened during system startup.
After you are ok with opening "main.py" on system startup,
```python
from ONF import count
print(count)
```
works for you.
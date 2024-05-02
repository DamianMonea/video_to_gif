# Prerequisites:

In order to run this program you NEED to have the 'ffmpeg' tool installed.
You can install 'ffmpeg' in several ways:
- Windows: You can install [Chocolatey](https://chocolatey.org/install) first and then use the command 'choco install ffmpeg' to install it. Make sure you run this command in an administrator PowerShell window
- MacOS: Use 'homebrew' to install 'ffmpeg' using the command 'brew install ffmpeg'.

If you are prompted to accept anything when installing 'ffmpeg', you can accept it by pressing 'y' and then the ENTER key.

# How to run the program:

### Step 1:

Put all of the videos that you want to convert to GIFs into the 'input' folder.

### Step 2:

Run the script with one of the following commands:

Convert everything in the 'input' folder to GIFs with this command:

```python
python3 main.py
```

Convert everything in the 'input' folder to GIFs AND delete the input files with this command:

```python
python3 main.py -c
```

Convert everything in the 'input' folder to GIFs with a specified target FPS:

```python
python3 main.py --fps 60
```

In the previous command we are specifying the FPS to be 60, but you can specify other values and if you don't pass this parameter, the default FPS value is 30FPS.

Also, you can combine the two parameters if you want/need to:

```python
python3 main.py -c --fps 60
```

This will create GIFs with the target FPS and then will delete the input files from the input folder.

### Step 3:

Enjoy!
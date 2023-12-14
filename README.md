# FileEncrypter
## How it works:
It works based on two lists of tuples that follows this format:

```[(Directory researched, [directories in the researched directory])]```
```[(Directory researched, [files in the researched directory])]```

It starts from the current working directory ((where the application is located)), and reach all the folders and their files, we do this at the ```resources.py```
```getFilesAndDirectories(startingDirectory)``` function, after that we call this same function passing different directories to it, until we do not have any 
directorie to check anymore. ((There is very little code to read and everything is well commented so, feel free to read the code)).

After that, we have a list of all the files that we've reached in our research and their corresponding directories, so we can file by file encrypting its contents. We've used SHA256 as the encryption method and encrypts text files and the binaries.

I've tested a lot and works pretty well, ((it really breaks all kinda of files reachable)), but if you finds anything to change, fell free to make a pull request, or a fork! And remember, use it for study purposes only, don't get in trouble, peace ✌️.

## How to run it:
Make sure you do have hashlib installed:

```pip install hashlib```

Place it at the desired folder, and run:

((Be careful with your current working directory choice))

```python3 main.py```

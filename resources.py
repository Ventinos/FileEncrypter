import hashlib as hl
import os

def getFilesAndDirectories(directory):
    # Creating our lists:
    visibleDirectories = []
    visibleFiles = []

    # Listing all the visible directories and visible files from directory:
    for d in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, d)):
            visibleDirectories.append(d)
        elif os.path.isfile(os.path.join(directory, d)):
            visibleFiles.append(d)

    return (directory,visibleDirectories), (directory, visibleFiles)

def encodeVisibleFiles(visibleFiles):
    for pair in visibleFiles:
        for file in pair[1]:
            try:
                encodeTextFile(pair[0],file)
            except UnicodeDecodeError as e:
                encodeBinaryFile(pair[0], file)

def encodeTextFile(directory, file):
    hashObj = hl.sha256()
    with open(directory+f'/{file}', 'r+') as currentFile: 
        lines = currentFile.readlines()

        for i, line in enumerate(lines):
            hashObj.update(line.encode('utf-8'))
            lines[i] = hashObj.digest().decode('utf-8')

        currentFile.seek(0)
        currentFile.truncate()

        currentFile.writelines(lines)

def encodeBinaryFile(directory, file):
    hashObj = hl.sha256()
    with open(directory+f'/{file}', 'rb+') as currentFile:
        content = currentFile.read()

        hashObj.update(content)
        currentFile.seek(0)
        currentFile.truncate()

        currentFile.write(hashObj.digest())


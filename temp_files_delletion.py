import os

JV = 'C:\\Users\\user\\Desktop\\folder\\Pytest'

for folderName, subfolders, filenames in os.walk(JV):
    for file in filenames:
        if file.startswith('~'):
            os.unlink(os.path.join(folderName, file))

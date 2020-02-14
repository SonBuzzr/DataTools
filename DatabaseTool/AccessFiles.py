import os
import time

from datetime import datetime
from Logger import SMLogger

FILEPATH = r'D:\temp'
EXT = '.log'
filesFound = []

# Delete files that are older than 7 Days
def remove_files(args):
    now = time.time()
    old = now - 60  # Remove files that are created 7 Days ago
    for file in args:
        if os.stat(file).st_ctime < old:
            print("Removing file {}".format(args))
            SMLogger('Remove Files', 'fileremove.log', file)

        # if os.stat(str(args)).st_ctime < old:
        #     print("Removing file {}".format(args))
        #     SMLogger('Remove Files', 'fileremove.log', args)
    #     # print(args)
    #     #
    #     # os.remove(args)


# List all the files in the given directory
def get_files(*args):

    for root, dirs, files in os.walk(args[0]):
        for file in files:
            # print(file)
            if file.endswith(EXT):
                file_read = os.path.join(root, file)
                # converting timestamp to readable format
                # print(datetime.fromtimestamp(os.stat(file_read).st_ctime))
                filesFound.append(file_read)



get_files(FILEPATH, EXT)
# remove_files(fileList)

for file in filesFound:
    SMLogger('Found Files', 'filefound.log', file)
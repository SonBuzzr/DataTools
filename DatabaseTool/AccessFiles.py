import os
import time

from datetime import datetime
from Logger import SMLogger

FILEPATH = r'D:\temp'
EXT = '.log'


# Delete files that are older than 7 Days
def remove_files(args):
    now = time.time()
    old = now - (60)  # Remove files that are created 7 Days ago

    if os.stat(args).st_ctime < old:
        print("Removing file {}".format(args))
        remove_logger = SMLogger('Remove Files', 'file_remove.log', args)
        # os.remove(args)


# List all the files in the given directory
def get_files(*args):
    for root, dirs, files in os.walk(args[0]):
        for file in files:
            # print(file)
            if file.endswith(EXT):
                file_read = os.path.join(root, file)
                # print(file_read)
                # converting timestamp to readable format
                # print(datetime.fromtimestamp(os.stat(file_read).st_ctime))
                remove_files(file_read)


get_files(FILEPATH, EXT)

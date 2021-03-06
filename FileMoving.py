import shutil
import os
from os import path
# This module is used to move files around for extraction. Obviously the folder names will be different, and you may not even need to use this section.
# For the project at hand the folders had four subfolders.

def dirCheckMove(src,dest,dirname,filename, subfolder = False, subOne = '', subTwo = ''):
    count = 0 # Used in case there is a duplicate file name. 
    dirCheck = os.path.isdir(src + dirname)
    if (dirCheck == True):
        files = os.listdir(src + dirname)
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + dirname + f, dest + dirname)
          


def fileMover(filename):
    src = # Source Path + filename + '/'
    dest = #Destination Path
    dirCheckMove(src,dest, r'.../', filename)  #The ... represents the subfolder needed to be passed in. 
    dirCheckMove(src,dest, r'.../', filename)
    dirCheckMove(src,dest, r'.../', filename)
    dirCheckMove(src,dest, r'.../', filename)
    dirCheckMove(src,dest, r'.../', filename)
    dirCheckMove(src,dest, r'.../', filename)
    
    

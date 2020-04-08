import shutil
import os
from os import path
# This module is used to move files around for extraction. Obviously the folder names will be different, and you may not even need to use this section.
# For the project at hand the folders had four subfolders, thus the 'LAC_A', 'MET_A', ect..

def dirCheckMove(src,dest,dirname,filename, subfolder = False, subOne = '', subTwo = ''):
    count = 0
    isdir01_ACCTG01 = os.path.isdir(src + dirname)
    if (isdir01_ACCTG01 == True):
        files = os.listdir(src + dirname)
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + dirname + f, dest + dirname)
          shutil.rmtree(os.path.join(src, dirname))


def fileMover(filename):
    src = r'Project directory ' + filename + '/'
    dest = src
    count = 0;
    dirCheckMove(src,dest, r'LAC_A/', filename)
    dirCheckMove(src,dest, r'LAC_I/', filename)
    dirCheckMove(src,dest, r'LAC_S/', filename)
    dirCheckMove(src,dest, r'MET_A/', filename)
    dirCheckMove(src,dest, r'MET_I/', filename)
    dirCheckMove(src,dest, r'MET_S/', filename)
    
    

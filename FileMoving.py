import shutil
import os
from os import path
# This module is used to move files around for extraction. Obviously the folder names will be different, and you may not even need to use this section.
# For the project at hand the folders had four subfolders, thus the 'LAC_A', 'MET_A', ect..


def fileMover(filename):
    src = r'Project directory ' + filename + '/'
    dest = src
    count = 0;
    isdirLAC_A = os.path.isdir(src + r'LAC_A/')
    if (isdirLAC_A == True):
        files = os.listdir(src + r'LAC_A/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + r'LAC_A/' + f, dest)
        shutil.rmtree(os.path.join(src, r'LAC_A/'))
    isdirLAC_I = os.path.isdir(src + r'LAC_I/')
    if (isdirLAC_I == True):
        files = os.listdir(src + r'LAC_I/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + r'LAC_I/' + f, dest)
        shutil.rmtree(os.path.join(src, r'LAC_I/'))
    isdirLAC_S = os.path.isdir(src + r'LAC_S/')
    if (isdirLAC_S == True):
        files = os.listdir(src + r'LAC_S/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) +'.pdf')
            shutil.move(src + r'LAC_S/' + f, dest)
        shutil.rmtree(os.path.join(src, r'LAC_S/'))
    isdirMET_A = os.path.isdir(src + r'MET_A/')
    if (isdirMET_A == True):
        files = os.listdir(src + r'MET_A/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + r'MET_A/' + f, dest)
        shutil.rmtree(os.path.join(src, r'MET_A/'))
    isdirMET_I = os.path.isdir(src + r'MET_I/')
    if (isdirMET_I == True):
        files = os.listdir(src + r'MET_I/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + r'MET_I/' + f, dest)
        shutil.rmtree(os.path.join(src, r'MET_I/'))
    isdirMET_S = os.path.isdir(src + r'MET_S/')
    if (isdirMET_S == True):
        print("Success!!!!!!!!")
        files = os.listdir(src + r'MET_S/')
        for f in files:
            if path.exists(src + f):
                fixFile = f[:-3]
                count = count + 1
                os.rename(src + f, src + fixFile + '_' + str(count) + '.pdf')
            shutil.move(src + r'MET_S/' + f, dest)
        shutil.rmtree(os.path.join(src, r'MET_S/'))
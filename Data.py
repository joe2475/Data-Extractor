import os
import shutil
import json
import os.path
from os import path
import subprocess
from pdfrw import PdfReader, PdfWriter
import FileMoving
import JsonData
sourcce = r'Source Directory'

def get_hash(filename):  # Gets hash from the json file. Used for decrypting ZIP Files.
    with open(filename) as g:
        json_file = json.load(g)
        hash = json_file['MD5HashCode'] # "MD5HashCode will vary depending on where to password is stored in the json file
        return hash


def pdfMetaDataAdd(filename, title, author, date ,keywords, jsonFile): # Adds desired metadata to the pdf file.
    os.chdir(source + ' '   + jsonFile)
    src = source  + jsonFile+ '/'
    dest = r'Destination directory'
    trailer = PdfReader(filename+'.pdf')
    date = date.replace("/", '-')
    date = date.replace(":", "_")
    trailer.Info.Title = title
    trailer.Info.Author = author
    trailer.Info.Created = date
    trailer.Info.Modified = date
    trailer.Info.Subject = keywords
    newFile = author + "_"+ filename +  "_" + date + '.pdf'
    PdfWriter(newFile, trailer=trailer).write() #Creates a new pdf with the metadata inserted
    shutil.move(src + '/' + newFile, dest)



def exctract_zip(fileN, passW): # Decypts and unzips the files.
    zip_file = fileN
    print(fileN)
    password = passW
    path_7zip = r"7-zip exe location"
    path_working = r'Directory of zip folders'
    outfile_name = fileN
    os.chdir(path_working)
    subprocess.call([path_7zip, 'x', '-r', '-y', '-p' + password, '-o %s' % os.path.normpath(filename[:-4]), outfile_name], shell=True)




if __name__ == "__main__":
    password = ""
    directory = os.fsencode(source)
    for file in os.listdir(directory):
        os.chdir(directory)
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            password = get_hash(filename)
            print("Password collected")



        elif filename.endswith(".zip"):
            exctract_zip(filename, password)
            print(filename + ' has been extracted and moved!')  # Used for conformation
            FileMoving.fileMover(filename[:-4])
            JsonData.json_write(filename[:-4]+'.json')
            print("Metadata added and moved")
            continue

        elif filename.endswith(".gz"):
            continue





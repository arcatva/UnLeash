"""
 ___  ___   ________    ___        _______    ________   ________   ___  ___     
|\  \|\  \ |\   ___  \ |\  \      |\  ___ \  |\   __  \ |\   ____\ |\  \|\  \    
\ \  \\\  \\ \  \\ \  \\ \  \     \ \   __/| \ \  \|\  \\ \  \___|_\ \  \\\  \   
 \ \  \\\  \\ \  \\ \  \\ \  \     \ \  \_|/__\ \   __  \\ \_____  \\ \   __  \  
  \ \  \\\  \\ \  \\ \  \\ \  \____ \ \  \_|\ \\ \  \ \  \\|____|\  \\ \  \ \  \ 
   \ \_______\\ \__\\ \__\\ \_______\\ \_______\\ \__\ \__\ ____\_\  \\ \__\ \__\
    \|_______| \|__| \|__| \|_______| \|_______| \|__|\|__| \_________\\|__|\|__|
                                                                                                                                                                                                                                     
Unleash recursively extracting file
zhefu_zhang@dell.com
Version 0.1
"""

import os, gzip, tarfile, zipfile

ArchivedFilesExtend = ['tar','gz','zip','rar'] # customize the supported extend types
PATH = os.getcwd() 

def WalkFiles():
    global DictArchivedFilesMapping
    DictArchivedFilesMapping = {} 
    for Ext in ArchivedFilesExtend: # initialize keys of dict
        DictArchivedFilesMapping[Ext] = []
    for CurDir, Dirs, Files in os.walk(PATH): # walk all dirs and subdirs and list Files
        for File in Files:
            CompletePath = os.path.join(CurDir,File) # join File and CurDir as CompletePath
            for Extend in ArchivedFilesExtend: 
                if CompletePath.endswith(Extend):
                    DictArchivedFilesMapping[Extend].append(CompletePath) # append CompletePath respectively into the extend list of the dict
      
def JudgeDict():
    Judge = all(value == [] for value in DictArchivedFilesMapping.values())
    return Judge   # TRUE if all lists are empty in all types of file

def Extract():
    for ZipFile in DictArchivedFilesMapping['zip']:
        print("----Extracting", ZipFile)
        with zipfile.ZipFile(ZipFile) as zip:
            zip.extractall(path=os.path.dirname(ZipFile))
        print("--Removing", ZipFile)    
        os.remove(ZipFile)
                       
    # def UnTar():
    #     for GzFile in DictArchivedFilesMapping['gz']:
    #         gzip.decompress(GzFile)
    #         os.remove(GzFile)
    # def ...


if __name__ == "__main__":
    WalkFiles()
    while JudgeDict() is not True:
        Extract()
        WalkFiles()
    else:
        print("All Completed!")
    

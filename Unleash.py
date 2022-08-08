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
Version 1.1
"""

import os, rarfile, tarfile, zipfile, gzip

ArchivedFilesExtend = ['tar','gz','zip','rar','tgz'] # customize the supported extend types
PATH = os.getcwd() # set working dir

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
    if DictArchivedFilesMapping['zip']:
        extract.UnZip()
    if DictArchivedFilesMapping['gz']:
        extract.UnGz()
    if DictArchivedFilesMapping['tar']:
        extract.UnTar()
    if DictArchivedFilesMapping['rar']:
        extract.UnRar()
    if DictArchivedFilesMapping['tgz']:
        extract.UnTgz()
            
class extract:
    @staticmethod
    def UnZip():
        for ZipFile in DictArchivedFilesMapping['zip']:
            print("----Extracting", ZipFile)
            with zipfile.ZipFile(ZipFile) as zip:
                zip.extractall(path=os.path.dirname(ZipFile))
            zip.close()
            print("--Removing", ZipFile)
            os.remove(ZipFile)
    @staticmethod
    def UnTar():        
        for TarFile in DictArchivedFilesMapping['tar']:
            print("----Extracting", TarFile)
            Tarfile = tarfile.open(TarFile)
            Tarfile.extractall()
            Tarfile.close()
            os.remove(TarFile)
    @staticmethod
    def UnGz():
        for GzFile in DictArchivedFilesMapping['gz']:
            print("----Extracting", GzFile)
            Gzfile = gzip.GzipFile(GzFile)
            gzip.decompress(GzFile)
            Gzfile.close()
            print("--Removing", GzFile)
            os.remove(GzFile)
    @staticmethod
    def UnRar():
        for RARFile in DictArchivedFilesMapping['rar']:
            print("----Extracting", RARFile)
            RARfile = rarfile.RarFile(RARfile)
            RARfile.extractall()
            print("--Removing", RARFile)
            os.remove(RARFile)
    @staticmethod        
    def UnTgz():        
        for TgzFile in DictArchivedFilesMapping['tgz']:
            print("----Extracting", TgzFile)
            Tgzfile = tarfile.open(TgzFile)
            Tgzfile.extractall()
            print("--Removing", TgzFile)
            os.remove(TgzFile)

def main():
    WalkFiles()
    while JudgeDict() is not True:
        Extract()
        WalkFiles()
    else:
        print("All Completed!")

if __name__ == "__main__":
    main()
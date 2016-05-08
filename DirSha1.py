import hashlib
import os


def GetDirFile(dir_path):
    os.chdir(dir_path)
    WalkGen = os.walk(os.getcwd())
    FileList = []
    for i in WalkGen:
        for j in i[2]:
            FileList.append(i[0] + "\\" + j)
    return FileList


def HashFile(file_path):
    file = open(file_path, 'rb')
    hash = hashlib.sha1()
    while True:
        bin = file.read(40960)
        if not bin:
            break
        hash.update(bin)
    sha1 = hash.hexdigest()
    return sha1


def GetSize(file_path):
    file = open(file_path, 'rb')
    file.seek(0, 2)
    size = file.tell()
    file.close()
    return size


def Sha1ADir(dir_path):
    print("*\tStart parser file in ", "[", dir_path, "]", sep="")
    FileList = GetDirFile(dir_path)
    print("*\tFinish parser file in ", "[", dir_path, "]", sep="")
    FileDict = {}
    print("*\tStart sha1 file in ", "[", dir_path, "]", sep="")
    for i in FileList:
        FileDict[i] = (HashFile(i), GetSize(i))
    print("*\tFinish sha1 file in ", "[", dir_path, "]", sep="")
    return FileDict


import os
import argparse
import shutil
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Source folder containing the files")
    parser.add_argument("destination", help="Destination folder to organize files")
    args = parser.parse_args()
    source = args.source
    dest = args.destination
    os.chdir(source)
    os.getcwd()

    os.listdir()

    list_ext = []
    for i in os.listdir():
        ext = i.split(".")[-1]
        if ext not in list_ext:
            list_ext.append(ext) 

    print(list_ext)

    

    path = dest

    try:
        shutil.rmtree(path)
        os.mkdir(path)
    except:
        os.mkdir(path)

    for ex in list_ext:
        os.mkdir(path+"\\"+ex)
        for fl in os.listdir():
            if ex in fl:
                shutil.copy(fl,path+"\\"+ex)

    print(path)





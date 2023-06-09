import os

def get_files_recursively(directory):
    if not directory:
        directory = input("Enter directory: ")
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        if dirpath[0] == "." or "__" in dirpath:
            pass
        for filename in filenames:
            if filename[0] == "." or "git" in filename or "TODO" in filename:
                pass
            else:
                files.append(os.path.join(dirpath, filename))
    return files

def show_dict(dct:dict, indent=0):
    for k,v in dct.items():
        if type(v) == dict:
            show_dict(v, indent=(indent+2))
        else:
            print((" "*indent)+ f"{k}: {v}")

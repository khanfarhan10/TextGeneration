import tensorflow as tf
import numpy as np
import os
import time
import sqlite3
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

ROOT_DIR=os.getcwd()

def search_file(filename,directory):
    files=find(filename, directory)
    if len(files)>1:
        print("Warning, Multiple Files Found, Selecting First Entry of :",files)
    return files[0]    
    
filename='shakespeare.txt'
data_file=filename if os.path.exists(filename) else search_file(filename=filename, directory=os.path.join(ROOT_DIR,"data"))

path_to_file = data_file




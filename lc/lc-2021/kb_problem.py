# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:20:18 2017

@author: xyin
"""


#### interview question with Kabbage



import json
import sys

# line = '{"Header": {"UserID": "XYZ", "RawData": {"Transaction": {"Date": "2015-02-02", "Amount": 300.00}}}}'

def printKeyValue(tree, parent):
    keys = getKeys(tree)
#    print(keys)
    for key in keys:
        if isinstance(tree[key],dict):
            print(parent + '_' + key)
            printKeyValue(tree[key], parent + '_' + key)
        else:
#            print(key + ':' + str(tree[key]))
            print(parent + '_' + key)
            
    
    
def getKeys(dict):
    key_list = []
    for key, value in dict.items():
        key_list.append(key)
    return(key_list)

def main():
    for line in sys.stdin:
        jsonDict = json.loads(line)
        for key, value in jsonDict.items():
            print(key)
            printKeyValue(jsonDict[key], key)

if __name__ == '__main__':
    main()
    
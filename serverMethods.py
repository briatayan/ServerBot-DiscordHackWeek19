#This code will routinely add servers to the servers users can be matched with.

#Server A & B would like to be added to the dictionary. A is already on the dictionary How do you do that?
#Step 1. Create a function with an if statement checking to see if the server is on the dictionary.
#step 2. If the server is on the dictionary, reject it. If the server is not on the dictionary add it to the dictionary.


# name = "Jame Cage White Server"
# tag = "very, cool, much, swag"
# Description = "A james cage white server"
#
# serverlist =	{
#   "server": {"tags": "wow, aliance, pvp, clan", "Description": "This server is a Wow server for an aliance clan!"}
#   }
#
# serverlist["name1"]= {"tags": "filler", "Description": "Just like half of Dragon Ball"}

import json
import os.path
from os import path

filename = "server_list.json"

### SERVER HELPER FUNCTIONS ###

def writeData(newVal):
    if path.exists(filename):
        with open(filename, "w") as write_file:
            json.dump(newVal, write_file)
        write_file.close()
    else:
        with open(filename, "w") as write_file:
            json.dump(newVal, write_file)
        write_file.close()

def initList(newVal):
    with open(filename, "w") as write_file:
        json.dump(newVal, write_file)
    write_file.close()

def getData():
    if path.exists(filename):
        with open(filename, "r") as load_file:
            data = json.load(load_file)
        load_file.close()
        return data
    else:
        return None

### SERVER FUNCTIONS ###

def serveradd (serverID, name, tag, description):
    isAdded = False
    newVal = {serverID : {"name" : name, "tags" : tag, "Description" : description}}
    serverlist = getData()
    if serverlist is None:
        initList(newVal)
        isAdded = True
        return isAdded
    if str(serverID) in serverlist:
        return isAdded
    else:
        serverlist.update(newVal)
        writeData(serverlist)
        isAdded = True
        return isAdded

def serverremove(serverID):
    isRemoved = False
    serverlist = getData()
    if str(serverID) in  serverlist:
        serverlist.pop(str(serverID))
        writeData(serverlist)
        isRemoved = True
        return isRemoved
    else:
        return isRemoved

def serveredit(serverID, key, newVal):
    serverID = str(serverID)
    isEdited = False
    serverlist = getData()
    if serverID in serverlist:
        serverlist[serverID][key] = newVal
        writeData(serverlist)
        isEdited = True
        return isEdited
    else:
        return isEdited

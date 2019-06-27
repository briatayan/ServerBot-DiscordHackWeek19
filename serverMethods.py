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

import helperMethods

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


#    adds a server to the JSON file database -- all args need to be strings, returns
#    True if the item was added, False if it wasn't (this can be used to determine
#    the response from the bot, and is the same format in the rest of the functions)


def serverAdd (serverID, name, tag, description):
    isAdded = False
    # initializes new item to be inserted into dictionary
    newVal = {serverID : {"name" : name, "tags" : tag, "Description" : description}}
    # gets dictionary from JSON file, all keys and values are strings
    serverlist = getData()
    # adds newVal to new server_list file if the file doesn't exist
    if serverlist is None:
        initList(newVal)
        isAdded = True
        return isAdded
    # returns false if already in serverlist
    if serverID in serverlist:
        return isAdded
    else:
    # adds newVal to serverlist, updates JSON, and returns True
        serverlist.update(newVal)
        writeData(serverlist)
        isAdded = True
        return isAdded

#    removes a server from the serverlist -- serverID is also a string, returns
#    True if it was successfully removed, False if not.

def serverRemove(serverID):
    isRemoved = False
    # gets serverlist from JSON file
    serverlist = getData()
    # checks if serverID is in the serverlist, if True, then pop serverID off the
    # dictionary and reutrn True, return False otherwise
    if serverID in  serverlist:
        serverlist.pop(serverID)
        writeData(serverlist)
        isRemoved = True
        return isRemoved
    else:
        return isRemoved

#    edits a server when given a key to be edited and its new value -- all
#    arguments are strings, and returns True if successfully edited, False if not

def serverEdit(serverID, key, newVal):
    isEdited = False
    # gets serverlist from JSON file
    serverlist = getData()
    if serverID in serverlist:
        # if the server is found in the list, then set the given key to the new value
        serverlist[serverID][key] = newVal
        writeData(serverlist)
        isEdited = True
        return isEdited
    else:
        return isEdited

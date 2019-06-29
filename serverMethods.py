#This code will routinely add servers to the servers users can be matched with.

#Server A & B would like to be added to the dictionary. A is already on the dictionary How do you do that?
#Step 1. Create a function with an if statement checking to see if the server is on the dictionary.
#step 2. If the server is on the dictionary, reject it. If the server is not on the dictionary add it to the dictionary.

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

# uses variation of selection sort to sort by percentage matched
def sortResults(result):
    for i in range(len(result)):
        max = i
        for key in result[i].keys():
            maxKey = str(key)
        for j in range(i + 1, len(result)):
            for key in result[j].keys():
                key = str(key)
                currPerc = result[j][key]["percentageMatched"]
                maxPerc = result[max][maxKey]["percentageMatched"]
                if currPerc > maxPerc:
                    max = j
                    maxKey = key
        result[i], result[max] = result[max], result[i]
    return result

### SERVER FUNCTIONS ###

#    adds a server to the JSON file database -- all args need to be strings, returns
#    True if the item was added, False if it wasn't (this can be used to determine
#    the response from the bot, and is the same format in the rest of the functions)


def serverAdd (serverID, name, tag = None, description = None, inviteURL = None):
    isAdded = False
    # initializes new item to be inserted into dictionary
    newVal = {serverID : {"name" : name, "tags" : tag, "description" : description, "invite" : inviteURL}}
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
    # dictionary and return True, return False otherwise
    if serverID in serverlist:
        try:
            del serverlist[serverID]
            writeData(serverlist)
        except KeyError:
            pass
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

#    searches the serverlist for servers that share tags with the given tags --
#    tags is a string of comma-separated tags, and the function returns a List
#    of all servers that are found that match at least one tag.

def serverSearch(tags):
    # gets the tags as a string and splits each tag into a list
    tags = helperMethods.tagsplit(tags, ",")
    result = []
    serverlist = getData()
    # for each item in the serverlist, worst case is O(n)
    for key, val in serverlist.items():
        # initializes default value for match percent, match count, matched flag
        matchPercent = 0
        matchCount = 0
        matchedTag = False
        # gets the number of tags that the current server has
        serverTagLength = len(helperMethods.tagsplit(val["tags"], ","))
        # makes new key val pair to be inserted into list
        newItem = dict({key : val})
        # for each tag in the given set of tags
        for tag in tags:
            # count how many of the tags match the tags of the server
            if tag in val["tags"]:
                matchCount += 1
                # set matched flag as true
                matchedTag = True
        # after counting all the matched tags, if any
        if matchedTag:
            # calculate percentage of given tags that match the server's tags
            matchPercent = int((matchCount / serverTagLength) * 100)
            # update new key val pair with percentage
            newItem[key].update(dict(percentageMatched = str(matchPercent)))
            # add new key val pair to result list
            result.append(newItem)
    sortResults(result)
    return result

### OTHER HELPER FUNCTIONS ###

#    Returns corresponding serverID when given a server name -- returns ID as
#    an integer if found, None if not found

def getServerID(serverName):
    serverID = None
    serverlist = getData()
    # checks each server in server list, in the worst case, will run for O(n) time
    for key, val in serverlist.items():
        # if a matching name is found, break the loop
        if serverName == val["name"]:
            serverID = key
            break
    return serverID

#This code will routinely add servers to the servers users can be matched with.

#Server A & B would like to be added to the dictionary. A is already on the dictionary How do you do that?
#Step 1. Create a function with an if statement checking to see if the server is on the dictionary.
#step 2. If the server is on the dictionary, reject it. If the server is not on the dictionary add it to the dictionary.

name = "Jame Cage White Server"
tag = "very, cool, much, swag"
Description = "A james cage white server"

serverlist =	{
  "server": {"tags": "wow, aliance, pvp, clan", "Description": "This server is a Wow server for an aliance clan!"}
  }

serverlist["name1"]= {"tags": "filler", "Description": "Just like half of Dragon Ball"}



def serveradd ():
    if "name" in serverlist:
        print("Sorry,this server already exsists on the list. Try appending to the server with !serverchange")

    else:
        serverlist[name]= {"tags": tag, "Description": Description}
        print("You're in! Your server will appear on our list shortly")

serveradd()

#print(serverlist)

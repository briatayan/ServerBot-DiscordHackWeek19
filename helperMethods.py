# tags = "world of warcraft, pvp, pve, aliance, hunter, tank, titan, warlock, shadowbringer, destiny, final fantasy, player versus enemy, player versus player, lol, laugh out loud"

#tag split function
def tagsplit (tags, sep):
    x = tags.split(sep)
    # removes empty strings
    x = list(filter(None, x))
    i = 0
    # removes all trailing and beginning whitespace
    while i < len(x):
        x[i] = x[i].strip()
        i += 1
    return x

def formatMessage(result):
    message = "Here are some servers we think you would like based on your tags:"
    for i in range(len(result)):
        for key, value in result[i].items():
            name = value["name"]
            tags = value["tags"]
            description = value["description"]
            percentageMatched = value["percentageMatched"]
            invite = value["invite"]
            serverInfo = "\n**Percentage Matched: " + percentageMatched+  "**\nServer Name: " + name + "\nTags: " + tags +\
             "\nDescription: " + description + "\nInvite Link: " + invite + "\n\n"
            message += serverInfo
    return message

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

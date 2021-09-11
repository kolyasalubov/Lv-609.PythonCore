def are_you_playing_banjo(name):
    
    if name[0] == 'R' or name[0] == 'r':
        result = " plays banjo"
    else:
        result = " does not play banjo"
    
    name = name + result
    return name
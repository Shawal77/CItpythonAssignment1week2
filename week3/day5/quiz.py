def surprising_function(value):
    thing = 0
    for counter in range(value+1):
        thing = thing + counter
    return thing

print(surprising_function(5))

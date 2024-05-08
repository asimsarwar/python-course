myDict = {
    "fast": "In a Quick Manner",
    "jack": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'jack': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "John": "Friend",
    "Leo": "Friend",
    "jack": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("jack")) # Prints value associated with key "jack"
print(myDict["jack"]) # Prints value associated with key "jack"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("jack2")) # Returns None as jack2 is not present in the dictionary
print(myDict["jack2"]) # throws an error as jack2 is not present in the dictionary
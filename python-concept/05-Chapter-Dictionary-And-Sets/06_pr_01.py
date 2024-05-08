myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Product": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Word from above mentioned options\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
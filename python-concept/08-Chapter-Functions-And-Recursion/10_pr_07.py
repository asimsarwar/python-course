def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Asim is a good      "
n = remove_and_split(this, "Asim")
print(n)
# print(this)
# print(this.strip())

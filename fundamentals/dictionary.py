# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure

mydict = {
    "one" : 1,
    "two" : 2,
    3: "three",
    4.5: ['four', 'point', 'five'],
    "one": "uno"  # this will overwrite the previous value for the key "one"
}

print(mydict)


# dictionaries are accessed via keys

print(mydict["one"])  # this will print "uno"
print(mydict[3])  # this will print "three"
# you can also set dictionary data by creating a new key

mydict["five"] = 5
print(mydict)
# Trying to access a nonexistent key will produce an error
#print(mydict["ten"])  # this will cause an error

# To avoid this, you can use the "in" operator to see if a key exists

print("ten" in mydict)  # False
print("one" in mydict)  # True
# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())  # this will print a list of all the keys in the dictionary
print(mydict.values())  # this will print a list of all the values in the

# You can also iterate over all the items in a dictionary
for key, value in mydict.items():
    print(f"{key} : {value}")

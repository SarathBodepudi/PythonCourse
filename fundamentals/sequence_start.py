# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 2, 3, 4, 5]
print(mylist)
print(len(mylist))

mylist = [1, 2, 3, "four", "five", 6.0]
print(mylist)

print(mylist[0])  # access the first element
print(mylist[3])  # access the fourth element
print(mylist[-1])  # access the last element
#print(mylist[-10])
print(mylist[1:4])  # access a slice of the list (from index 1 to 3)
print(mylist[:3])  # access the first three elements
print(mylist[3:])  # access from the fourth element to the end

print("==========================")  # access every second element
print(mylist[::2])  # access every second element


# add a list to another list
mylist = [1, 2, 3, "four", "five", 6.0]
mylist2 = [7, 8, 9]
mylist.extend(mylist2)
print(mylist)
print(mylist + mylist2)  # this creates a new list that is the concatenation of the two lists

# use slices to get parts of a sequence


# you can use slices to reverse a sequence
print("============ reverse string ==============")
print(mylist[::-1])  # this creates a new list that is the reverse of the original list

# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership

# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 5:
    print(f"x is currently {x}")
    x += 1

print("---------------------------------")
# define a for loop
for x in range(6):
    print(f"x is currently {x}")

print("---------------------------------")
#answer = input("Should I stop? ")
# while answer.lower() != "yes":
#     print(answer)
#     answer = input("Should I stop? ")

# use a for loop over a collection
print("---------------------------------")
my_list = ["a", "b", "c", "d", "e"]
for item in my_list:
    print(item)

print("---------------------------------")
# use the break and continue statements
for x in range(10):
    if x == 3:
        print("skipping 3")
        continue
    if x == 8:
        print("stopping at 8")
        break
    print(x)
print("---------------------------------")
# using the enumerate() function to get an index and an item

my_list = ["a", "b", "c", "d", "e"]
for index, item in enumerate(my_list):
    print(f"index: {index} item: {item}")
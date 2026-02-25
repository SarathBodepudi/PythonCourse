# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 10, 100

# conditional flow uses if, elif, else
if x < y:
    print("x is less than y")
    print("this is another statement in the if block")
elif x == y:
    print("x and y are equal")  
else:
    print("x is greater than y")
# conditional statements let you use "a if C else b"
print("---------------------------------")
message = "x is less than y" if x < y else "x is greater than or equal to y"  # pylint: disable=invalid-name
print(message)
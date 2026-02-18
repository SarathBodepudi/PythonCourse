age = int(input("Enter your age: "))


decades = age / 10
print("You are", decades, "decades old.")

decades = age // 10
print("You are", decades, "full decades old.")

decades_remainder = age % 10
print("You have lived", decades_remainder, "years into your current decade.")

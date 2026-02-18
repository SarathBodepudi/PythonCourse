temp = int(input("Enter temperature in Fahrenheit: "))

if temp >= 90:
    print("It's a hot day.")
    print("Stay home and drink plenty of water.")
elif temp >= 70:
    print("It's a warm day.")
    print("Wear light clothing.")
elif temp >= 50:
    print("It's a cool day.")
    print("Wear a jacket.")
else:
    print("It's a cold day.")
    print("Wear warm clothes.")

forecast = input("Enter the weather forecast (rainy/sunny): ")
if forecast.lower() == "rainy":
    print("Take an umbrella.")
else:
    print("Enjoy your day!")

isSunny = False
isRainy = False


if temp >= 80 and forecast.lower() == "sunny":
    print("It's a great day for the beach!")
if temp < 40 or forecast.lower() == "rainy":
    print("Stay indoors and keep warm.")
if forecast.lower() == "sunny":
    isSunny = True
elif forecast.lower() == "rainy":
    isRainy = True


if(isSunny):
    print("The sun is shining brightly!")
elif(isRainy):
    print("Don't forget your raincoat!")
else:
    print("The weather is moderate today.")
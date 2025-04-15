n = int(input("Please enter the weather (in °C): "))
print("So the weather is:", n, "°C")

if n <= -10:
    print("It is very cold in your area! Wear as many jackets, hoodies, and sweatshirts as you can.")
elif n <= 20:
    print("It's cold! You’ll need a very warm jacket, hoodie, or sweatshirt.")
elif n <= 30:
    print("Kinda warm — denim, t-shirt, pants... wear whatever you're comfy with.")
elif n >= 50:
    print("It's **very** hot! Please wear cotton clothes and stay hydrated.")
else:
    print("Weather is moderate. Dress comfortably!")


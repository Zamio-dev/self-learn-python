print("\nConditional statements with real world examples")
print("---------------------------------------------------------------\n")


# ---- 1. Greet someone differently based on the time of day ----
print(">>> Time of day greeting")
hour = int(input("What time is it now (0-23)? "))

if 5 <= hour < 12:
    print("Morning! Good vibes so far.")
elif 12 <= hour < 17:
    print("Afternoon. You're halfway through the day.")
elif 17 <= hour < 21:
    print("Evening. Time to wind down.")
else:
    print("Late night. You up?")
print()


# ---- 2. Can they get a driver's license? ----
print(">>> Driver's license check")
age = int(input("Enter age: "))

if age < 16:
    print("Nope, too young. Come back when you're older.")
elif age < 18:
    print("You can get a learner's permit, but not a full license yet.")
elif age < 65:
    print("Yep, you're eligible for a regular license.")
else:
    print("You're eligible, but some states want extra vision tests for seniors.")
print()



# ---- 3. ATM withdrawal ----
print(">>> ATM withdrawal")
balance = 5000
amount = int(input("How much do you want to withdraw? "))

if amount <= 0:
    print("You can't take out nothing or negative money. Think again.")
elif amount % 100 != 0:
    print("ATMs only give you notes in multiples of 100.")
elif amount > balance:
    print("Insufficient balance. You only have ₹5000.")
else:
    balance -= amount
    print(f"Taken ₹{amount}. Remaining balance: ₹{balance}")
print()


# ---- 4. What to wear based on weather ----
print(">>> Weather-based decision")
temp = int(input("Outside temperature (°C): "))
raining = ((input("Is it raining? (y/n): ").lower() == "y") if temp <= 25 else False )

if temp >= 35:
    print("Hot as hell. Shorts, t-shirt, sunscreen.")
elif temp >= 25:
    wear = "t-shirt and jeans" if not raining else "t-shirt, jeans, and an umbrella"
    print(f"Nice weather. Wear {wear}.")
elif temp >= 15:
    print("Mild. A light jacket and pants should work.")
else:
    print("Cold. Jacket, scarf, maybe gloves if you're feeling it.")
print()



# ---- 5. Password login with nested checks ----
print(">>> Login check")
username = "sameer"
password = "hello123"
attempts = 3

print("Login required:\n")
for attempt in range(attempts):
    uname = input(f"Attempt {attempt+1}/{attempts} — username: ")
    pwd = input("               password: ")

    if uname != username:
        print("  Wrong username.")
    elif pwd != password:
        print("  Wrong password.")
    else:
        print("  Login successful. Welcome back.")
        break
else:
    print("\n  You used all your attempts. Account locked for now.")
print()


# ---- 6. match/case — cleaner than a wall of if/elif ----
print(">>> match/case — mode selector")
mode = input("Pick a mode: drive / sleep / airplane / none: ").strip().lower()

match mode:
    case "drive":
        print("Phone is in driving mode. Notifications muted.")
    case "sleep":
        print("Do not disturb is on. Lights off.")
    case "airplane":
        print("Wi-Fi and mobile data disabled.")
    case "none":
        print("Normal mode. Everything is available.")
    case _:
        print("That's not a mode I know. Try again.")
print()

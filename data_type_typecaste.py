# Data types and typecasting
# I am learning python
# Like Appu, Lakshmi, Aranmula, Mavelikara etc.

print("====>  Types and Typecasting  <====\n")

# ========== 1. INTEGER (int) — whole numbers ==========
# Like counting elephants in a temple festival
appu_age = 25              # Appu's age in Puthukkad
lakshmi_age = 30           # Lakshmi's age in Varkala
shope_price = 150          # Price of a mundu in Mattancherry

print(f"{appu_age=}  type: {type(appu_age)}")
print(f"{lakshmi_age=}  type: {type(lakshmi_age)}")
print(f"{shope_price=}  type: {type(shope_price)}")

# ========== 2. FLOAT — numbers with decimal ==========
# Like exact distance or temperature
vel_mavelikara = 84.5      # Distance from Mavelikara to Thrissur (km)
cardamom_rate = 1250.75    # Price of cardamom per kg in Kochi market
temp_thrissur = 34.8       # Temperature in Thrissur today

print(f"\n{vel_mavelikara=}  type: {type(vel_mavelikara)}")
print(f"{cardamom_rate=}  type: {type(cardamom_rate)}")
print(f"{temp_thrissur=}  type: {type(temp_thrissur)}")

# ========== 3. STRING — anything in quotes ==========
name = "Aranmula"          # A place name
place = "Attingal"         # Another place
greeting = "Namskaram!"   # hello

print(f"\n{name=}  type: {type(name)}")
print(f"{place=}  type: {type(place)}")
print(f"{greeting=}  type: {type(greeting)}")

# ========== 4. BOOLEAN — True or False ==========
is_weekend = True          # Is it weekend? Yes!
is_sunny = False           # Is it sunny? No, monsoon leavo
is_moved_in = True         # Has Appu moved to Kochi? Yes

print(f"\n{is_weekend=}  type: {type(is_weekend)}")
print(f"{is_sunny=}  type: {type(is_sunny)}")
print(f"{is_moved_in=}  type: {type(is_moved_in)}")

# ========== 5. LIST — an ordered list of things ==========
# Like a shopping list for Onam
onan_shopping = ["pookalam", "kasavu mundu", "banana chips", "avial"]
bank_friends = ["Appu", "Niran", "Sibu", "Rahul"]

print(f"\n{onan_shopping=}  type: {type(onan_shopping)}")
print(f"{bank_friends=}  type: {type(bank_friends)}")

# ========== 6. DICTIONARY — key-value pairs ==========
# Like a phone book or ID card
appu_info = {"name": "Appu", "age": 25, "city": "Mavelikara", "phone": "9876543210"}
houseboat = {"name": "Swathi", "capacity": 12, "route": "Alleppey to Kollam"}

print(f"\n{appu_info=}  type: {type(appu_info)}")
print(f"{houseboat=}  type: {type(houseboat)}")

# ========== 7. SET — unique items, no duplicates ==========
# Like your temple visit list — no place visited twice
visit_places = {"Aranmula", "Thrissur", "Kochi", "Aranmula"}
# Notice Aranmula is there twice but set removes the duplicate!

print(f"\n{visit_places=}  type: {type(visit_places)}")
# When I print, Aranmula will appear only once. Set removes duplicates automatically.

# ========== 8. TUPLE — a list that CANNOT be changed ==========
# Like fixed coordinates — you can't change where the temple is!
# Temples are permanent, that's why tuple.
temple_coords = (9.2, 76.3)              # Latitude and longitude of Padmanabhaswamy Temple
rivers = ["Periyar", "Pamba", "Chalakkudy", "Bharathapuzha"]

# In a tuple you write with () not []
kerala_districts = ("Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alleppey",
                     "Kottayam", "Idukki", "Ernakulam", "Thrissur", "Palakkad",
                     "Malappuram", "Kozhikode", "Wayanad", "Kannur", "Kasaragod")
# That's all 14 districts in a tuple. Once written, no district will be removed or added.

print(f"\n{temple_coords=}  type: {type(temple_coords)}")
print(f"{kerala_districts=}  type: {type(kerala_districts)}")
# Try: kerala_districts[0] = "Mavelikara" — 💥 Error! Tuple is immutable, can't change.

# ========== 9. BYTES — raw data (used in networking) ==========
# When you send a message from Kochi to London, data is sent as bytes
appu_message = b"Hello from Kochi"
print(f"\n{appu_message=}  type: {type(appu_message)}")

# ========== 10. NONE — means "nothing here" ==========
# Like an empty parking spot. The spot exists, but nothing is in it.
appu_mobile = None  # Appu doesn't have a mobile phone yet. Mobile = None.
houseboat_status = None  # This houseboat is not yet built. Status = None.

print(f"\n{appu_mobile=}  type: {type(appu_mobile)}")
print(f"{houseboat_status=}  type: {type(houseboat_status)}")

# ========== 11. TYPECASTING — changing one type to another ==========
# Like changing a mundu into a t-shirt. Same person, different form.

print("\n\n====>  TYPECASTING EXAMPLES  <====\n")

# ---- int to float ----
# Like changing 100 rupees into 100.50. You have more precision now.
appu_budget = 100
print(f"Appu had {appu_budget} rupees -> now it's {float(appu_budget)} (same value, now decimal)")

# ---- float to int ----
# Like rounding your cardamom rate down. You lose the paise.
cardamom_price = 1250.75
print(f"Cardamom price was {cardamom_price} -> rounded down to {int(cardamom_price)}")
# Note: int() just cuts the decimal, it does NOT round. 1250.99 becomes 1250, not 1251.

# ---- string to int ----
# Like reading a bus number "15" and actually using it as a number
bus_number = "15"
print(f"Bus number string '{bus_number}' -> converted to number {int(bus_number)}")
print(f"Now I can do math: 15 + 10 = {int(bus_number) + 10}")

# ---- string to float ----
# Like reading a weight "65.5" from a weighing scale
weight_str = "65.5"
print(f"Weight string '{weight_str}' -> converted to float {float(weight_str)}")

# ---- int to str ----
# Like putting your age on a form. Forms need text, not numbers.
lakshmi_age = 30
print(f"Lakshmi's age {lakshmi_age} (int) -> as string '{str(lakshmi_age)}'")
# Why? Because in a form you write "30" not the number 30. String "30" not int 30.

# ---- bool to int ----
# True = 1, False = 0. Python thinks this way inside.
print(f"True as int -> {int(True)}")   # 1
print(f"False as int -> {int(False)}") # 0

# ---- int to bool ----
# 0 = False, anything else = True. Like: empty wallet = no money = False.
print(f"0 as bool -> {bool(0)}")       # False — empty wallet
print(f"1 as bool -> {bool(1)}")       # True — you have money!
print(f"100 as bool -> {bool(100)}")   # True

# ---- list to tuple ----
# Like turning a shopping list into a permanent record.
shopping_list = ["banana", "chips", "tea"]
print(f"Shopping list (list): {shopping_list}")
print(f"Same things as tuple: {tuple(shopping_list)}")
# Now this is frozen. Can't add or remove. Like engraving on stone.

# ---- tuple to list ----
# Like un-freezing a frozen record.
districts_tuple = ("Thrissur", "Kottayam", "Kollam")
print(f"Dists (tuple): {districts_tuple}")
print(f"Dists (list):  {list(districts_tuple)}")
# Now you can add a new district if needed.

# ---- string to list (split) ----
# Like breaking a sentence into individual words.
sentence = "Hello from Mavelikara"
print(f"Split a sentence into words: {sentence.split()}")
# You get: ['Hello', 'from', 'Mavelikara']

# ---- list to string (join) ----
# Like gluing words back into a sentence.
words = ["Hi", "I", "am", "from", "Kochi"]
joined = " ".join(words)
print(f"Join words into sentence: '{joined}'")

# ---- set — what happens if you convert list with duplicates ----
duplicate_list = ["Kochi", "Thrissur", "Kochi", "Mavelikara", "Thrissur"]
unique_places = set(duplicate_list)
print(f"List with duplicates: {duplicate_list}")
print(f"After set (duplicates removed): {unique_places}")
# Kochi and Thrissur appear only once now. Set is unique.

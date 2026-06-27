print("\nLoops — when you need to repeat something, over and over")
print("---------------------------------------------------------------\n")


# ---- 1. for loop — go through a shopping list ----
print(">>> Shopping list - for loop")
groceries = ["milk", "eggs", "bread", "butter", "cheese"]
print("Things to grab:\n")
for item in groceries:
    print(f"  ☐  {item}")
print("\nDone. Put it in the cart or check it off.")
print()


# ---- 2. for + enumerate — show items with a position number ----
print(">>> Task list with priorities 'enumerate' is used.")
tasks = ["reply to emails", "call to check job openings", "pick up dry cleaning", "learn new stuff"]
for i, task in enumerate(tasks, start=1):
    print(f"  {i}.  {task}")
print()


# ---- 3. for with range — count down before takeoff ----
print(">>> Rocket countdown (just for fun)")
for i in range(3, 0, -1):
    print(f"  {i}...")
print("  🚀 Liftoff!\n")


# ---- 4. for + sum — add up bills ----
print(">>> Split the dinner bill")
bills = [13, 105, 37, 12, 44, 10]  # what each person ate
total = 0
for bill in bills:
    total += bill

avg = total / len(bills)
print(f"  Total bill:  ₹{total} for #{len(bills)} Person")
print(f"  Per person:  ₹{avg:.2f}")
print()


# ---- 5. for with zip — match names to their scores ----
print(">>> People who ate and price")
friends_names = ["Anoop", "Sihaj", "Naseeb", "Binoy", "Mathew", "Nadish"]
print("  Name       Price\n")
for name, bill in zip(friends_names, bills):
    print(f"  {name:<10} {bill}")
print()


# ---- 6. while + break — collect names until user says stop ----
print(">>> Name collector - while,break,for")
names = []
print("  I'll keep asking for names. Type 'done' when you're finished.\n")
while True:
    name = input("  Name: ")
    if name.lower() == "done":
        break
    if name:
        names.append(name)

print(f"\n  You entered {len(names)} names:")
for name in names:
    print(f"    • {name}")
print()


# ---- 7. for + else — finish something with no interruptions ----
print(">>> Parking spot checker - forelse")
spots = ["free", "free", "occupied", "free", "occupied"]
found = False

for i, spot in enumerate(spots):
    if spot == "free":
        print(f"  Spot {i+1} is free. Park here.")
        found = True
        break

if not found:
    print("  No spots left. Drive around.")
else:
    print("  We found a spot and didn't run into any dead ends.")
print()


# ---- 8. nested for loop — show a simple calendar grid ----
print(">>> Mini calendar for a 7-day week - for, if else")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
events = ["Wed", "Sat"]  # which days have something planned

for day in days:
    if day in events:
        print(f"  {day}: ⚡ has an event")
    else:
        print(f"  {day}: 🟢 clear")
print()


# ---- 9. list comprehension — do something to every item ----
print(">>> Convert names to uppercase")
upper = [name.upper() for name in friends_names]
print(f"  Original:  {friends_names}")
print(f"  Uppercase: {upper}")
print()


# ---- 10. list comprehension with a filter ----
print(">>> Keep only even numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"  All:     {numbers}")
print(f"  Evens:   {evens}")
print()


# ---- 11. dict comprehension ----
print(">>> Word length lookup")
words = ["hello", "world", "python", "is", "great", "hello"]
lengths = {word: len(word) for word in words}
print(f"  {lengths} \n Items found in it {len(lengths)}")
print()

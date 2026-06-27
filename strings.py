
print("====>  String Operations  <====\n")

# ========== 1. BASIC STRING SLICING ==========

# Syntax: string[start:end] — from start to end-1

message = """
hi how are you
i think things will get better
"""
print(f"--- Original message ---\n{message=}")

# First 10 characters — like reading the first line of a letter
print(f"\nFirst 10 chars: {message[:10]=}")

# From index 5 to end — like starting from the 6th letter
print(f"From index 5: {message[5:]=}")

# Last 5 characters — like reading the last few words of a note
print(f"Last 5 chars: {message[-5:]=}")
# Negative index means "from the end". -1 is last char, -2 is second last, etc.

# Last 7 chars going backwards (note: [start:stop] where stop is exclusive)
print(f"From -1 to -7: {message[-1:-7]=}")
# This goes from the last char BACKWARDS, but Python slicing always goes forward.
# So [-1:-7] gives empty because you're going backwards but slicing goes forward.
# To get chars from end in reverse, use [::-1] or [-7::-1]

# ========== 2. CASE CONVERSION ==========

# upper() — convert everything to uppercase
# Like shouting. All letters become BIG.
name = "mavelikara"
print(f"\n--- Case conversion ---\n{message.upper()=}")

# lower() — convert everything to lowercase
# Like whispering. All letters become small.
print(f"lower: {message.lower()=}")

# title() — first letter of each word is uppercase
# Like giving everyone a name tag
print(f"title: {message.title()=}")
# "Hi How Are You I Think Things Will Get Better"

# capitalize() — only the very first letter is uppercase
# Like only the chief guest gets a name tag
small = "hello from kerala"
print(f"capitalize: {small.capitalize()=}")
# "Hello from kerala" — only H is capital

# swapcase() — flip caps and non-caps
# Like swapping mundu and shirt
mixed = "hELLO kERALA"
print(f"swapcase: {mixed.swapcase()=}")
# "Hello Kerala" — every cap becomes small, every small becomes cap

# ========== 3. STRIP — REMOVE EXTRA SPACES ==========

# strip() — remove spaces from BOTH sides
# Like trimming the edges of a picture frame
text = "   hello   kochi   "
print(f"\n--- Strip ---")
print(f"Original: '{text}'")
print(f"strip():   '{text.strip()}'")
# "'hello kochi'" — spaces gone from both sides

# lstrip() — remove spaces from LEFT only
# Like pushing everything to the right
left_text = "   hello"
print(f"lstrip():  '{left_text.lstrip()}'")
# Spaces only from the left

# rstrip() — remove spaces from RIGHT only
# Like pushing everything to the left
# Very useful when reading files — each line has \n at the end
right_text = "hello   "
print(f"rstrip():  '{right_text.rstrip()}'")

# reading a file line by line
# Each line from a file has "\n" (newline) at the end
# You use rstrip() to remove that trailing newline
file_line = "Appu lives in Kochi\n"
print(f"File line without newline: '{file_line.rstrip()}'")
# Now you get "Appu lives in Kochi" without the hidden newline

# ========== 4. FIND AND COUNT ==========

# find() — find where a word starts (returns index or -1 if not found)
# Like looking for a house in a street
sentence = "Appu lives in Mavelikara near the temple"
print(f"\n--- Find ---")
print(f"'lives' found at index: {sentence.find('lives')=}")  # 5
print(f"'kochi' found at index: {sentence.find('kochi')=}")  # -1 (not found!)

# index() — same as find but gives ERROR if not found (use find for safety)
# I am using find because it's safer. If word not found, find returns -1, index crashes.

# count() — how many times does a word appear?
# Like counting how many elephants are in Thrissur Pooram
text = "hi how are you and i think you will do well"
print(f"\n--- Count ---")
print(f"'you' appears: {text.count('you')=}")  # 2
print(f"'a' appears: {text.count('a')=}")      # 2
print(f"'z' appears: {text.count('z')=}")      # 0 — doesn't exist!

# ========== 5. STARTSWITH and ENDWITH ==========

# startswith() — does the string start with this?
# Like checking if a houseboat is going to Alleppey
email = "appu@gmail.com"
print(f"\n--- Startswith and Endswith ---")
print(f"Email starts with 'appu': {email.startswith('appu')=}")  # True
print(f"Email starts with 'lakshmi': {email.startswith('lakshmi')=}")  # False

# endswith() — does the string end with this?
# Like checking if a file is a PDF or Word doc
print(f"Email ends with '.com': {email.endswith('.com')=}")  # True
print(f"Email ends with '.org': {email.endswith('.org')=}")  # False

# Real world: checking file extensions
filename = "report.pdf"
if filename.endswith(".pdf"):
    print("This is a PDF file")  # Yes!

# ========== 6. REPLACE ==========

# replace() — replace one word with another
# Like changing "banana" to "mango" on a menu
menu = "We serve banana chips, banana fry, and banana shake"
new_menu = menu.replace("banana", "mango")
print(f"\n--- Replace ---")
print(f"Old menu: {menu}")
print(f"New menu: {new_menu}")
# "We serve mango chips, mango fry, and mango shake"

# You can also limit how many replacements
limited = menu.replace("banana", "mango", 1)
print(f"Replace only first: {limited}")
# "We serve mango chips, banana fry, and banana shake"
# Only first "banana" changed. Rest stays same.

# ========== 7. SPLIT — BREAK STRING INTO LIST ==========

# split() — break a sentence into individual words
# Like breaking a banana into pieces
sentence = "Hello from Mavelikara"
words = sentence.split()
print(f"\n--- Split ---")
print(f"Words: {words=}")
# ['Hello', 'from', 'Mavelikara']

# split with delimiter — split by a specific character
# Like cutting a string at specific marks
csv_line = "Appu,25,Mavelikara"
parts = csv_line.split(",")
print(f"Split by comma: {parts=}")
# ['Appu', '25', 'Mavelikara']

# Real world: parsing CSV data
# When you open an Excel file, it's stored as CSV with commas
# You split by comma to get each column

# ========== 8. JOIN — GLUE LIST INTO STRING ==========

# join() — combine list of words into one string
# Like putting banana pieces back into a bunch
words = ["Hi", "I", "am", "from", "Kerala"]
joined = " ".join(words)
print(f"\n--- Join ---")
print(f"Joined: '{joined}'")
# "Hi I am from Kerala"

# Real world: creating CSV
headers = ["name", "age", "city"]
csv_header = ", ".join(headers)
print(f"CSV header: {csv_header}")
# "name, age, city"

# You can join with any character
numbers = ["1", "2", "3", "4"]
pipe_joined = " | ".join(numbers)
print(f"Pipe joined: {pipe_joined}")
# "1 | 2 | 3 | 4"

# ========== 9. IN OPERATOR — CHECK IF WORD EXISTS ==========

# 'in' — check if a substring exists
# Like checking if your name is on the guest list
name = "Aranmula"
print(f"\n--- In operator ---")
print(f"'Aru' in 'Aranmula': {'Aru' in name}")   # True
print(f"'Kerala' in 'I am from Kerala': {'Kerala' in 'I am from Kerala'}")  # True

# 'not in' — check if a substring does NOT exist
print(f"'X' in 'Hello': {'X' in 'Hello'}")        # False
print(f"'X' not in 'Hello': {'X' not in 'Hello'}") # True

# Real world: email validation
email = "appu@gmail.com"
if "@" in email:
    print("This looks like an email address")  # Yes, @ is present

# ========== 10. ISDIGIT, ISALPHA, ISALNUM — WHAT TYPE OF CHARACTERS? ==========

# isdigit() — are all characters digits? (0-9)
# Like checking if a form field is a number
print(f"\n--- Character checks ---")
print(f"'42'.isdigit(): {'42'.isdigit()}")      # True — pure number
print(f"'42.5'.isdigit(): {'42.5'.isdigit()}")  # False — has a dot!
print(f"'abc'.isdigit(): {'abc'.isdigit()}")    # False — letters, not numbers

# isalpha() — are all characters letters? (a-z, A-Z)
# Like checking if a field accepts only letters
print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")     # True
print(f"'Hello 123'.isalpha(): {'Hello 123'.isalpha()}")  # False — has space and numbers

# isalnum() — are all characters alphanumeric? (letters + numbers, no spaces/symbols)
# Like checking if a username has only letters and numbers
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")     # True
print(f"'Hello 123'.isalnum(): {'Hello 123'.isalnum()}")   # False — has space

# password validation
password = "MyPass123"
if password.isalnum():
    print("Password has only letters and numbers (no special chars)")
else:
    print("Password has special characters (space, !, @ etc)")
# "MyPass123" is alnum, so it passes. Good for simple systems.

# ========== 11. ZFILL — PAD WITH ZEROS ==========

# zfill() — add zeros at the beginning to reach a certain length
# Like making a parking spot number always 4 digits: 0007, 0042, etc.
print(f"\n--- Zfill ---")
print(f"'7'.zfill(4): {'7'.zfill(4)}")      # "0007" — like room number 7 padded to 4 digits
print(f"'42'.zfill(4): {'42'.zfill(4)}")     # "0042"
print(f"'123'.zfill(4): {'123'.zfill(4)}")   # "0123"

# Real world: timestamps
hour = 5
minute = 3
print(f"Time: {str(hour).zfill(2)}:{str(minute).zfill(2)}")
# "05:03" — not "5:3" which looks ugly

# ========== 12. CENTER, LJUST, RJUST — ALIGNMENT ==========

# center() — put text in the middle of a space
# Like centering a picture on a wall
print(f"\n--- Alignment ---")
text = "MENU"
print(f"center(30, '-'): {text.center(30, '-')}")
# "---------MENU-----------" — 30 chars wide, text in center, padded with -

# ljust() — left justify (pad on right)
# Like pushing text to the left side of a table
name = "Appu"
print(f"ljust(15): '{name.ljust(15)}'")
# "Appu           " — text on left, spaces fill the rest

# rjust() — right justify (pad on left)
# Like pushing numbers to the right side of a table
score = 95
print(f"rjust(5): '{str(score).rjust(5)}'")
# "   95" — number on right, spaces fill the left

# Real world: making a table
print(f"\n--- Making a table ---")
print(f"{'Name':<15}{'Age':>5}{'City':<10}")
print(f"{'Appu':<15}{25:>5}{'Mavelikara':<10}")
print(f"{'Lakshmi':<15}{30:>5}{'Thrissur':<10}")
print(f"{'Niran':<15}{28:>5}{'Kochi':<10}")
# Output:
# Name           AgeCity
# Appu           25Mavelikara
# Lakshmi        30Thrissur
# Niran          28Kochi

# ========== 13. ESCAPE CHARACTERS — SPECIAL MEANINGS ==========

# \" — escaped quote (include a quote inside a quoted string)
# Like saying "hello" inside quotes — you need to escape the inner quotes
print(f"\n--- Escape characters ---")
print('He said "Namskarang" to me')
# Without escape: He said "Namskarang" to me

# \n — newline (go to next line)
# Like pressing Enter on a keyboard
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

# \t — tab (horizontal space)
# Like pressing the Tab key
print("Name\tAge\tCity")
print("Appu\t25\tMavelikara")
# Output (with actual tab spacing):
# Name    Age     City
# Appu    25      Mavelikara

# \\ — escaped backslash (include a real backslash)
# Like when you need to show a path in Windows: C:\Users\Appu
print("Path: C:\\Users\\Appu\\Documents")
# Output: Path: C:\Users\Appu\Documents

# ========== 14. LEN — LENGTH OF STRING ==========

# len() — how many characters are in a string?
# Like counting how many words are in a namaskaram
print(f"\n--- Len ---")
name = "Kochi"
print(f"len('Kochi'): {len(name)}")  # 5 — K-o-c-h-i, 5 letters

# Real world: checking password length
password = "Hello123"
if len(password) >= 8:
    print("Password is long enough (8+ characters)")
# len("Hello123") = 8, so it passes!

# ========== 15. STRING FORMATTING — BEAUTIFUL OUTPUT ==========

# F-string with format spec — combine value + formatting
# Like printing a price with 2 decimal places
print(f"\n--- F-string formatting ---")
price = 19.5
print(f"Price: ₹{price:.2f}")  # ₹19.50 — .2f means 2 decimal places

# Thousands separator — like salary
salary = 50000
print(f"Monthly salary: ₹{salary:,.2f}")  # ₹50,000.00

# Percentage
marks = 85.5
print(f"Exam marks: {marks:.1f}%")  # 85.5%

# ========== 16. .FORMAT() METHOD — ANOTHER WAY TO FORMAT ==========

# format() — put values into a string template
# Like filling blanks in a form
name = "Appu"
age = 25
city = "Mavelikara"
print(f"\n--- .format() ---")
print("My name is {} and I'm {} years old, from {}".format(name, age, city))
# "My name is Appu and I'm 25 years old, from Mavelikara"

# You can also use numbered placeholders
print("{0} lives in {1}. {0} is {2} years old.".format(name, city, age))
# "{0}" = first arg (name), "{1}" = second (city), "{2}" = third (age)
# Output: Appu lives in Mavelikara. Appu is 25 years old.

# ========== 17. % FORMATTING — OLD SCHOOL (BUT YOU'LL SEE IT) ==========

# %s = string, %d = integer, %f = float
# Like the old way of doing things. Still works, still used.
print(f"\n--- % formatting (old school) ---")
name = "Lakshmi"
age = 30
print("My name is %s and I'm %d years old" % (name, age))
# "My name is Lakshmi and I'm 30 years old"

# %f for decimals
temp = 34.8
print("Today's temperature: %0.1f°C" % temp)
# "Today's temperature: 34.8°C"

def string_to_number(s):
    hash = 0
    for c in s:
        hash = 31 * hash + ord(c)
    return hash

items = [
    ["apple", "1.69"],
    ["banana", "0.59"],
    ["orange", "1.99"]
]

input_name = input("Enter name: ").strip()

found = False
for item in items:
    if item[0].lower() == input_name.lower():
        print("Price:", item[1])
        found = True
        break

if not found:
    print("Name not found.")

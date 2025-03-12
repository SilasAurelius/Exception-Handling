# Dictionaries

kitchen = {
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf",
    "Blender": "Counter"
}

print(kitchen)

print(kitchen["Spoons"])

# .get() lets me safely check a dictionary without crashing the program if the element is not there.
location_of_toaster = kitchen.get("Toaster", "Not Found")
print(location_of_toaster)

community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM"
}

# Adding a key value pair:
community_center["Cooking"] = "1 PM"
print(community_center)

# Writing over a value: 
community_center["Yoga"] = "7:30 AM"
print(community_center)

# pop()
inventory = {
    "Apple": 30,
    "Oranges": 20,
    "Bananas": 15
}
removed_item = inventory.pop("Oranges")
print(removed_item) # Output: 20
print(inventory) # The key Oranges is gone.

# popitem()
user_data = {"name": "Alice", "age": 30, "city": "New York"}
removed_item = user_data.popitem()
print(removed_item) # Output: ('city', 'New York')

# del keyword
book_shelf = {"Fiction": 10, "Non-Fiction": 7, "Mystery": 5}
del book_shelf["Non-Fiction"]
print(book_shelf)

# clear() clears the entire dictionary
session_data = {"user id": 12345, "status": "active", "theme": "dark"}
session_data.clear()
print(session_data) # session_data is now empty

# items() Returns a view object that displays a list of dictionary's key-value tuple pairs.
book_ratings = {"1994": 4.5, "To Kill a Mockingbird": 4.8, "Brave New World": 4.3}
for book, rating in book_ratings.items():
    print(f"{book} has a rating of {rating}")
    
# keys() returns a view object that displays a list of all the keys in the dictoinary.
user_profile = {"name": "Alice", "age": 30, "email": "alice@example.com"}
for key in user_profile.keys():
    print(key)
    
# values() returns a view object that displays a list of all the values in the dictionary.
for values in user_profile.values():
    print(values)
    
# update() - updates the key values.
default_settings = {"theme": "light", "notifications": "on"}
user_settings = {"theme": "dark"}
default_settings.update(user_settings)
print(default_settings) # Output: {"theme": "dark", "notifications": "on"}

# setdefault() returns the value of a specified key. If the key does not exist, setdefault inserts the key with the specified default value.
stock = {"apples": 30, "oranges": 20}
stock.setdefault("bananas", 0)
print(stock) # Output: {"apples": 30, "oranges" 20, "bananas": 0}

# Original exhibit information
museum_exhibit = {
    "Ancient Vase": ["Greece", "Egypt"],
    "Renaissance Painting": ["Italy", "France"]
}

# Creating a shallow copy  -- A shallow copy creates a referrence to a list, not a brand new dictionary with its own key value pairs.
exhibit_copy = museum_exhibit.copy()

# exhibit_copy = {
#   "Ancient Vase": reference to value of "Ancient Vase" key in original dictionary,
#   "Renaissance Painting": ["Italy", "France"]
# }  


# Adding a new country to the "Ancient Vase" list in the copied dictionary
exhibit_copy["Ancient Vase"].append("China")

print("Original Exhibit: ", museum_exhibit)
print("Copied Exhibit:", exhibit_copy)


# adding to a dictionary:
museum_exhibit["Renaissance Painting"] = "Japan"
print(museum_exhibit)


student = {"name": "Silas", "age": 36, "school": "Coding Temple"}
print(student)
print(f"\n{student}")
print(len(student)) # Will return 3 because I have 3 keys in the dictionary.

for key in student.items(): # items() will print the key and the value.
    print(key)
    
captials = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

print(f"\n{captials}")

if captials.get("Japan"):
    print("That capital exists.")
else:
    print("that capital doesn't exits.")
    
captials.update({"USA": "Detroit"})
print(captials["USA"])
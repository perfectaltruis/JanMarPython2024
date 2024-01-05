# CHANGING CASE IN A STRING WITH METHODS
# In Python we can change the case of a string using methods
# let's start with title method

name = "ada lovelace"
print(name + "  : Normal Output")  # At this line name variable is printed as it is

# at this line all starting letters of a variable name are changed to upper
# The . after name in name.title() tell python to make title() method act on
# variable name

print(name.title() + "  : First letter name is capitalized")

print(name.lower() + "  : Lower case name")  # lower case letters
print(name.upper() + "  : Upper case name")  # upper case letters

print(len(name))  # output the length of the name

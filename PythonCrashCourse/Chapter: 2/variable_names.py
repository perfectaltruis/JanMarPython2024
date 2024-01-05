# Chapter 2 aims to show how to use variable and data types
# So here are some naming conversion to follow while naming
# variables in Python.

rule_number_one = (
    "\tVariable names can Only contain letters, number and underscores.\n"
    "\tThey can start with letter, and underscores and not with a number.\n"
    "\tFor instance, You can call a variable message_1 and not 1_message, or -Message"
)

rule_number_two = (
    "\tSpaces are not allowed in variable names but underscores\n"
    "\tcan be used to separate words in long or short variable names.\n"
    "\tFor instance, 'greeting_message' will work but 'greeting message' would cause an error"
)

rule_number_three = (
    "\tAvoid using python keywords and function names as variable names;\n"
    "\tThat is do not use that python has reserved for particular python programming purpose\n"
    "\tFor instance, Do not use a word 'print' as a variable name."
)
rule_number_four = (
    "\tVariable names should be short but descriptive; \n"
    "\tFor instance 'name' is better than 'n', \n"
    "\t'student_name' is better than 's_n'"
)

print("\nNaming and Using Variables in Python:\n")
print("1:" + rule_number_one + "\n")
print("2:" + rule_number_two + "\n")
print("3:" + rule_number_three + "\n")
print("4:" + rule_number_four + "\n")


# Do not worry about "\n" and "\t" I will explain them in string_01.py file

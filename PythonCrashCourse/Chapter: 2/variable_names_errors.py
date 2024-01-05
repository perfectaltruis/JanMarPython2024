# From variable_names.py File
# let's see some variable name error.
# I will create a variable and then print a misspelled name of the variable

languages = "My Best programming language is python"
print(language)

# This will generate an error and the python interpreter do its best to find where the error is.
# The interpreter provide a traceback when the program cannot run successfully

#  Traceback (most recent call last):
#  File "variable_names_errors.py", line 2, in <module>
#  print(language)
#  NameError: name 'language' is not defined

# This traceback shows that language variable is not defined and it is at the line 6 of your codes
# But also it shows a name that you might be required to enter to correct the error.

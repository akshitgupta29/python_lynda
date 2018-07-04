# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print (f)

# # re-declaring the variable works
f = 'def'
print (f)

# # ERROR: variables of different types cannot be combined
print ('this is a string ' + str(123))

# Global vs. local variables in functions
def trial():
    global f
    f = "inside"
    print (f)
    
trial()
f='outside2'
print (f)

# del f
f = 'outside'
print (f)
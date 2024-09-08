# First thing, you need to add the correct file extension. For Python files that is ".py" (or ".ipynb" for Python notebooks)

# All of the following needs to be done in the terminal, also make sure to have installed git (https://git-scm.com/downloads) before using those commands!
#=====================================================================================================
# Now, I'll create a markdown (.md) file in which I'll explain how to use each of the following
# git init

# git clone https://github.com/nehabear/myfirstpy

# cd myfirstpy

# git add .

# git commit -m "git is confusing tbh"

# git push
#=========================================================================================================

firstnumber = input('input number pls: ') # Python doesn't use the ";" delimiter, instead it relies on indentation (tabs and/or spaces)

try:
    firstnumber = int(firstnumber)
except ValueError:
    print("That's not a number dumbdumb!")
    exit()

print('you have chosen first number as: ' + str(firstnumber))

secondnumber = input('input second number por favor: ')

try:
    secondnumber = int(secondnumber)
except ValueError:
    print("That's not a number dumbdumb!")
    exit()

print('you have chosen second number as: ' + str(secondnumber))

operand = input('pick your operand (+ , - , * or /) : ')

if operand == '+':
    result = firstnumber + secondnumber
elif operand == '-':
    result = firstnumber - secondnumber
elif operand == '*':
    result = firstnumber * secondnumber
elif operand == '/':
    result = firstnumber / secondnumber
else :
    print('you are big dumbdumnb')
    exit()
print('you have chosen: ' + str(firstnumber) + operand + str(secondnumber))

print('your result is: ' + str(result))

# Nice job! For a first program it's great ;)

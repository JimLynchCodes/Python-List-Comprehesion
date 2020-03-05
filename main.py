# This project is meant to be a simple demonstration of Python's "List Comprehensions"

# In a nutshell, list comprehensions allow you to write the equivalent of a "for loop" in a clean one-liner.

nums = [1, 2, 3, 4, 5]

# Regular "For Loop" Method
doublesForLoop = []
for x in nums:
  doublesForLoop.append(x * 2)

# List Comprehension Method
doublesListComprehension = [x * 2 for x in nums]

# Notice how in the regular for loop method we first write the looping logic (for x in nums) and then the code to execute for each iteration (x * 2).

# Notice how the list comprehension just reverses the order of the two and puts them on the same line!

print(doublesForLoop)
print(doublesListComprehension)

# So, if you didn't fully understand Python's list comprehesions before, hopefully this helps you! abs

# Happy coding!
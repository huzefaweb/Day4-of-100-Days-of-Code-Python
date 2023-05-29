"""
100 days of Python course
DAY 4
"""

# the elements in lists called row-3 contain ascii emoticons
# to simulate squares
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

# this is not the Python map function - variable named map for
# easier understanding of how a list called map contains lists
# called row1-3 and when printed using f-string shows a basic
# 3 x 3 array
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# the first int is the row, the second int is the column
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

# remembering that indices start at zero we position the X
map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

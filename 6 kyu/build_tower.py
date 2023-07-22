# Build Tower Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A
# tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]


# MY SOLUTION

def tower_builder(n_floors):
    if n_floors == 0:
        return []
    else:
        final_tower = []
        tower = ["*"]
        for i in range(0, n_floors):
            counter = len(tower[-1])
            tower.append(("*" * counter) + ("*" * 2))
        for i in tower:
            final_tower.append(i.center(len(max(tower)) - 2))

        return final_tower[:-1]


# DEMONSTRATION

print(tower_builder(3))

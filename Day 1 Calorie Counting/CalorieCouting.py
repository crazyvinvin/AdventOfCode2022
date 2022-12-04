import os
def get_file_path(filename):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, filename)

def get_elf_array():

    elves = []
    elves.append(0)

    with open(get_file_path("input.txt"), "r") as input:
        for line in input:
            if line != "\n":
                elves[-1] += int(line)
            else:
                elves.append(0)
    
    return elves


elves = get_elf_array()
elves.sort(reverse=True)

print("elves: " + str(elves))
print("heighest calories: " + str(elves[0]))

calorie_top_three = 0
for i in range(3):
    calorie_top_three += elves[i]

print("accumulated top 3: " + str(calorie_top_three))






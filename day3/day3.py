import string
import re
# Part 1
with open('day3-input.txt', 'r') as f:
    rucksacks = f.readlines()

value_string = '{}{}'.format(string.ascii_lowercase, string.ascii_uppercase)

sum = 0
for r in [r.strip() for r in rucksacks]:
    compartment1 = r[0:int((len(r)+1)/2)]
    compartment2 = r[int((len(r)+1)/2):]
    share = list(set(compartment1).intersection(compartment2))
    sum += value_string.index(share[0]) + 1 # index starts at 0
print(sum)

# Part 2
sum = 0
with open('day3-input.txt', 'r') as f:
    rucksacks = [r.strip() for r in f.readlines()]
    for i in range(0, len(rucksacks), 3):
        sacks = rucksacks[i:i+3]
        share = list(set(sacks[0]).intersection(sacks[1]).intersection(sacks[2]))
        #print(share)
        sum += value_string.index(share[0]) + 1 # index starts at 0
print(sum)
with open('day1-input.txt', 'r') as f:
    elves = f.read().split('\n\n')
elves = [e.split('\n')for e in elves ]
calorie_list = []
for elf in elves:
    calorie_list.append(sum([int(e) for e in elf if e]))
    # if calories > most:
    #     most = calories

print(sum(sorted(calorie_list)[-3:]))
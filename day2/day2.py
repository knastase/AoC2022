with open('day2-input.txt', 'r') as f:
    strategy = f.readlines()

score_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_list = ['AY', 'BZ', 'CX']
tie_list = ['AX', 'BY', 'CZ']
lose_list = ['AZ', 'BX', 'CY']

points = 0
for s in strategy:
    # # Part 1
    result = s.strip().split(' ')
    check = ''.join(result)
    if check in win_list:
        points += 6
        
    elif check in tie_list:
        points += 3
    else:
        points += 0
    points += score_dict[result[1]]
print(points)

points = 0
for s in strategy:
    result = s.strip().split(' ')
    check = ''.join(result)
    # # Part 2
    if result[1] == 'X':
        for r in lose_list:
            if r[0] == result[0]:
                points += score_dict[r[1]]
                break
    elif result[1] == 'Y':
        points += 3
        for r in tie_list:
            if r[0] == result[0]:
                points += score_dict[r[1]]
                break
    else:
        points += 6
        for r in win_list:
            
            if r[0] == result[0]:
                points += score_dict[r[1]]
                break

print(points)

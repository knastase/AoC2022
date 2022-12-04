with open('day4-input.txt', 'r') as f:
    assignments = [r.strip() for r in f ]

    encompass = 0
    overlap = 0
    for a in assignments:
        coverage = []
        for assignment in a.split(','):
            coverage.append([i for i in range([int(i) for i in assignment.split('-')][0], \
                [int(i) for i in assignment.split('-')][1]+1 )])
        # Part 1
        if set(coverage[0]).issubset(coverage[1]):
            encompass += 1
        elif set(coverage[0]).issuperset(coverage[1]):
            encompass += 1
            
        # Part 2
        if set(coverage[0]).intersection(coverage[1]):
            overlap += 1

print(encompass)
print(overlap)
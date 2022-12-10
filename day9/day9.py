with open('test-input.txt', 'r') as f:
    moves = [c.strip() for c in f.readlines()]

position = 0
for m in moves:
    d, num = m.split(' ')
    print(d, num)
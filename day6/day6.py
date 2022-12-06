with open('input.txt', 'r') as f:
    chars = f.read()

marker = 14
markers = [4, 14] # 4 consectutive chars for start and 14 for message
for m in markers:
    for i in range(0,len(chars)):
        marker = chars[i:i+m]
        if len(set(marker)) == len(list(marker)):
            print('Part {}: {}'.format(markers.index(m)+1, i+m))
            break
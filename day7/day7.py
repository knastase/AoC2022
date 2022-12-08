with open('input.txt', 'r') as f:
    cmds = [c.strip() for c in f.readlines()]

position = ''
dirs = {}

for cmd in cmds:
    c = cmd.split(' ')
    if c[0] == '$':
        if c[1] == 'cd':
            if c[2] == '..':
                # print('move up')
                position = '/'.join(position.split('/')[:-2]) +'/'
            elif c[2] == '/':
                # print('move to root')
                position = '/'
            else:    
                # print(f'move into {c[2]}')
                position += c[2] + '/'
                if not position in dirs:
                    dirs[position] = 0
        elif c[1] == 'ls':
            pass
            # print('list_dir')
            
    elif c[0] == 'dir':
        pass
        # print(f'directory {c[1]}')
    else:
        if not position in dirs:
            dirs[position] = 0
        for i in range(0, len(position[0:].split('/'))):
            p = '/'.join(position.split('/')[:i+1]) + '/'         
            if '//' == p[-2:]:
                continue
            
            dirs['/'.join(position.split('/')[:-i])+'/'] += int(c[0])
            #print(f'file {c[1]} size {c[0]}')


d = 0
for key, val in dirs.items():
    # print(key, val)
    if val <= 100000:
        d += val
print(f'Part 1: {d}')

# Part 2
ans = 30000000 - (70000000 - dirs['/'])
ds = []
for key, val in dirs.items():
    if val >= ans:
        ds.append(val)
print('Part 2: {}'.format(sorted(ds)[0]))
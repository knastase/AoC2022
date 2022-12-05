import re

crate_dict1 = {}
crate_dict2 = {}

def move_single_crate(crate_dict, src, dst):
    c = crate_dict[src].pop(0)
    crate_dict[dst].insert(0, c)

    return crate_dict

def move_multi_crate(crate_dict, src, dst, num_crates):
    c = crate_dict[src][0:num_crates]
    for i in range(num_crates-1,-1,-1):
        del(crate_dict[src][i])
    crate_dict[dst] = c + crate_dict[dst]

    return crate_dict

with open('input.txt', 'r') as f:
    crates, moves = f.read().split('\n\n')

for cd in [crate_dict1, crate_dict2]:
    for i in range(1,10):
        cd[int(i)] = []

    for line in crates.split('\n')[:-1]:
        m = re.findall('\[\w\]|\s{4}', line)
        for idx, match in enumerate(m):
            if not match.strip() == '':
                cd[idx+1].append(match.strip())

# ex: move 1 from 4 to 1
for move in moves.split('\n'):
    m = re.findall('\d+', move)
    num_crates, src, dst = [int(i) for i in m]
    
    # Part 1
    for n in range(0,num_crates):
        crate_dict1 = move_single_crate(crate_dict1, src, dst)

    # Part 2
    crate_dict2 = move_multi_crate(crate_dict2, src, dst, num_crates)

print(''.join([i[0] for i in crate_dict1.values()]).replace('[','').replace(']',''))
print(''.join([i[0] for i in crate_dict2.values()]).replace('[','').replace(']',''))
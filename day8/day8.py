import numpy
with open('input.txt', 'r') as f:
    trees = [c.strip() for c in f.readlines()]

length = len(trees[0])
all_trees = ''.join(trees)
visible = []
v_score = {}
for idx, t in enumerate(all_trees):
    
    if idx - length < 0 or idx + length >= len(all_trees):
        visible.append(t)
    else:
        trees_in_way = {'up':[], 'down':[], 'left':[], 'right':[]}
        for i in range(idx+length, len(all_trees), length):
            trees_in_way['down'].append(all_trees[i])
        for i in range(idx-length, -1, 0-length):
            trees_in_way['up'].append(all_trees[i])

        for i in range(idx+1, idx+(length-(idx%length)), 1):
            trees_in_way['right'].append(all_trees[i])
        for i in range(idx-1, idx-(idx%length+1), -1):
            trees_in_way['left'].append(all_trees[i])

        v_score[f'{idx}-{t}'] = trees_in_way
        for key, vals in trees_in_way.items():
            nums = [int(v) for v in vals]
            if not nums:
                nums.append(-1)
            if nums and int(t) > max(nums):
                visible.append(t)
                break
                
        #print(idx, t, trees_in_way)
print('Part 1: {}'.format(len(visible)))

high_score = {'key': '', 'val': 0}

for key, vals in v_score.items():
    idx, num = key.split('-')
    score = []
    for direction in vals:
        count = 0
        for tree in vals[direction]:
            if int(tree) < int(num):
                count += 1
            else:
                count += 1
                break
        score.append(count)
    final_score = numpy.prod(score)
    if final_score > high_score['val']:
        high_score['val'] = final_score
        high_score['key'] = key
print('Part 2: {}'.format(high_score['val']))
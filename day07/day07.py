from collections import defaultdict

dirs = defaultdict(int)
cwd = []


def p1(lines):
    p1_ans = 0
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                cwd.pop()
            else:
                cwd.append(words[2])
        elif words[0] == 'dir' or words[1] == 'ls':
            continue
        else:  # files
            size = int(words[0])  # size
            for i in range(1, len(cwd)+1):
                dirs['/'.join(cwd[:i])] += size  # Add size to all current and parent paths

        # print('cwd', cwd)
        # print('dirs', dirs)

    for v in dirs.values():
        if v <= 100000:
            p1_ans += v

    return p1_ans


def p2(lines):
    p2_ans = 1e9

    max_possible = 40000000
    total_used = dirs['/']
    need_free = total_used - max_possible

    for v in dirs.values():
        if v >= need_free:
            p2_ans = min(p2_ans, v)

    return p2_ans


# with open('data/input_temp.txt') as f:
with open('data/input.txt') as f:
    # lines = f.readlines()
    lines = [(line.strip()) for line in f.readlines()]
    print('p1 ans:', p1(lines))
    print('p2 ans:', p2(lines))

# print(dirs)
# print(cwd)
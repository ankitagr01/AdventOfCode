curr_crt = [['?' for _ in range(40)] for _ in range(6)]


def p1check(cycle, x):
    val = 0
    if (cycle - 20) % 40 == 0:
        val = cycle * x
    return val


def p1(lines):
    p1_ans = 0
    x=1
    dcyc = 0

    for line in lines:
        if line.startswith('noop'):
            # start of cycle
            dcyc = dcyc + 1
            val = p1check(dcyc,x)
            p1_ans += val

        else:
            action, step = line.strip().split()
            step = int(step)

            dcyc += 1
            val = p1check(dcyc, x)
            p1_ans += val

            dcyc += 1
            val = p1check(dcyc, x)
            p1_ans += val

            x += step

    return p1_ans


def p2_crt(cycle, x):
    global curr_crt
    curr_cycle = cycle-1
    curr_crt[curr_cycle//40][curr_cycle%40] = ('#' if abs(x-(curr_cycle%40))<=1 else ' ')


def p2(lines):

    p2_ans = 0
    x=1
    dcyc = 0

    for line in lines:
        if line.startswith('noop'):
            # start of cycle
            dcyc = dcyc + 1
            p2_crt(dcyc,x)

        else:
            action, step = line.strip().split()
            step = int(step)

            dcyc +=1
            p2_crt(dcyc, x)

            dcyc+=1
            p2_crt(dcyc, x)

            x += step

    return p2_ans


# with open('data/input_temp.txt') as f:
with open('data/input.txt') as f:
    lines = [(line.strip()) for line in f.readlines()]
    print('p1 ans:', p1(lines))
    print('p2 ans:', p2(lines))
    # print(curr_crt)

    for c in range(6):
        print(''.join(curr_crt[c]))

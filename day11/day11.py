from tqdm import tqdm
from copy import deepcopy

M_ITEMS = []
OPERATIONS = []
OP = []
DIV = []
TRUE = []
FALSE = []


def parse_input(data):
    global M_ITEMS, OPERATIONS, DIV, TRUE, FALSE

    for monkey in data.split('\n\n'):
        id, items, op, div, true, false = monkey.split('\n')
        M_ITEMS.append([int(i) for i in items.split(':')[1].split(',')])
        words = op.split()
        op = ''.join(words[-3:])
        OPERATIONS.append(op)
        DIV.append(int(div.split()[-1]))
        TRUE.append(int(true.split()[-1]))
        FALSE.append(int(false.split()[-1]))

    print('M_ITEMS', M_ITEMS)
    print('OPERATIONS', OPERATIONS)
    print('DIV', DIV)
    print('TRUE', TRUE)
    print('FALSE', FALSE)


def p1():
    global M_ITEMS, OPERATIONS, DIV, TRUE, FALSE, OP
    M_ITEMS_P1 = deepcopy(M_ITEMS) # as M_Items is also needed for P2, making a copy
    count = [0 for i in range(len(M_ITEMS_P1))]

    for t in tqdm(range(20)):
        for m in range(len(M_ITEMS_P1)):
            for item in M_ITEMS_P1[m]:
                old = item
                item = eval(OPERATIONS[m])  # as operation has old as a variable
                item = (item // 3)

                if item % DIV[m] == 0:
                    M_ITEMS_P1[TRUE[m]].append(item)
                else:
                    M_ITEMS_P1[FALSE[m]].append(item)

                count[m] += 1

            M_ITEMS_P1[m] = []

    c = sorted(count, reverse=True)
    return c[0] * c[1]


def p2():
    global M_ITEMS, OPERATIONS, DIV, TRUE, FALSE
    # START = deepcopy(M_ITEMS)

    # as there can be thousands of items because of increasing order,
    # the processing time is huge.
    # hence we need to reduce it
    # so we divide the item by the divisors that we have (19,13,5,7,17,2,3,11)
    # and only keep the remainder to check for the divisibility
    # hence we reduce each item by the factor below:
    factor = 1
    for x in DIV:
        factor *= x

    count = [0 for _ in range(len(M_ITEMS))]
    # M_ITEMS = deepcopy(START)
    for t in tqdm(range(10000)):
        for m in range(len(M_ITEMS)):
            for item in M_ITEMS[m]:
                old = item
                item = eval(OPERATIONS[m])

                item %= factor

                if item % DIV[m] == 0:
                    M_ITEMS[TRUE[m]].append(item)
                else:
                    M_ITEMS[FALSE[m]].append(item)

                count[m] += 1

            M_ITEMS[m] = []

    c = sorted(count, reverse=True)
    return c[0] * c[1]


if __name__ == '__main__':
    # with open('data/input_temp.txt') as f:
    with open('data/input.txt') as f:
        # lines = [(line.strip()) for line in f.readlines()]
        # lines = [(line.strip()) for line in f.read()]
        lines = f.read().strip()
        print(lines)
        parse_input(lines)
        print('p1 ans:', p1())
        print('p2 ans:', p2())

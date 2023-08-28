t = int(input())
lines, columns = [], []
for i in range(t):
    x, y = input().split()
    lines.append(int(x))
    columns.append(int(int(y)))

for i in range(t):
    for l in range(lines[i]):
        for box in range(3):
            if box == 0 or l == lines[i]:
                print('*', end='', flush=True)
                for c in range(columns[i]):
                    if c == columns[i]-1:
                        print('***')
                    else: print('***', end='', flush=True)
            else:
                print('*', end='', flush=True)
                for c in range(columns[i]):
                    for line in range(1, 4):
                        if line == 0 or line%3 == 0:
                            print('*', end='', flush=True)
                        else:
                            print('.', end='', flush=True)
                print()
    print('*', end='', flush=True)
    for c in range(columns[i]):
        print('***', end='', flush=True)
    print('\n')
t = int(input())
lines, columns = [], []
for i in range(t):
    x, y = input().split()
    lines.append(int(x))
    columns.append(int(int(y)))

for i in range(t):
    for l in range(lines[i]):
        if(l % 2 == 0):
            for c in range(columns[i]):
                if(c % 2 == 0):
                    print('*', end='', flush=True)
                else: print('.', end='', flush=True)
        else:
            for c in range(columns[i]):
                if(c % 2 != 0):
                    print('*', end='', flush=True)
                else: print('.', end='', flush=True)
        print()
    print()
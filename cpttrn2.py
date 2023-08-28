t = int(input())
lines, columns = [], []
for i in range(t):
    x, y = input().split()
    lines.append(int(x))
    columns.append(int(int(y)))

for i in range(t):
    for l in range(lines[i]):
        if l == 0 or l == lines[i]-1:
            for c in range(columns[i]):
                print('*', end='', flush=True)
        else:
            print('*', end='')
            for c in range(1, columns[i]-1):
                print('.', end='')
            if columns[i] > 1:
                print('*', end='', flush=True)
        print()
    print()
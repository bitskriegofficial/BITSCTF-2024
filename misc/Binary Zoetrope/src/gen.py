with open('./flag.txt', 'r') as f:
    flag = f.readlines()

with open('./noise.txt', 'r') as r:
    noise = r.readlines()

for offset in range(15, 1556):
    data = [line[offset:offset + 320] for line in flag]

    for i in range(240):
        for j in range(320):
            if data[i][j] == '0':
                noise[i] = noise[i][:j] + ('1' if noise[i][j] == '0' else '0') + noise[i][j + 1:]

    frame = ''.join(line for line in noise)

    filename = './data/' + f'{offset - 15}'.zfill(4) + '.txt'
    with open(filename, 'w') as r:
        r.write(frame)
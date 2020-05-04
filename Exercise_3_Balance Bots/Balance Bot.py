import collections
import re

bots = collections.defaultdict(list)

outputs = dict()
# here we  are taking input as .txt file
lines = open('input3.txt')
rules = [line.split() for line in lines]  # input3.txt is file name

while rules:
    for r in rules:
        if r[0] == 'value':
            bots[int(r[5])].append(int(r[1]))
            rules.remove(r)

        else:
            a = int(r[1])
            if len(bots[a]) == 2:
                bots[a].sort()
                low, high = bots[a]
                if r[5] == 'bot':
                    bots[int(r[6])].append(low)
                else:
                    outputs[int(r[6])] = low
                if r[10] == 'bot':
                    bots[int(r[11])].append(high)
                else:
                    outputs[int(r[11])] = high
                rules.remove(r)

for n, value in bots.items():
    if value == [17, 61]:
        print("# Answer of part 1")
        print("bot which compares value-17 and value-61 microchips is =", n)
        break

print("\n# Answer of part 2")
print("The product of the microchip values is", outputs[0] * outputs[1] * outputs[2])



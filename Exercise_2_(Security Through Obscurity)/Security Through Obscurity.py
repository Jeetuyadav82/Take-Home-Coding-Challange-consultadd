def five_most_common(phrases):
    letters_dict = {}

    for p in phrases:
        for c in p:
            if c not in letters_dict:
                letters_dict[c] = -1
            else:
                letters_dict[c] -= 1

    flattened = [(j, i) for i, j in letters_dict.items()]
    flattened.sort()
    top5 = [j[1] for j in flattened][:5]
    return top5


def parse_encrypted(s):
    sum_sector_ids = 0
    tmp = s.split('-')
    letters = tmp[:-1]
    sec_id, checksum = tmp[-1][:-1].split('[')
    top5 = "".join(five_most_common(letters))

    if top5 == checksum:
        return int(sec_id)
    else:
        return 0


def test_1():
    rooms = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]"""

    sum_sec = 0
    for r in rooms.split('\n'):
        sum_sec += parse_encrypted(r.strip())
    assert sum_sec == 1514


def solution_part1():
    print("kindlt enter the string of room id followed by one extra empty line :-")

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    rooms = '\n'.join(lines)

    sum_sec = 0
    for r in rooms.split('\n'):
        sum_sec += parse_encrypted(r.strip())
    return sum_sec

if __name__ == '__main__':
    
    test_1()
    sum_of_real_id=solution_part1()
    print("sum of the sector IDs of the real rooms = ",sum_of_real_id)

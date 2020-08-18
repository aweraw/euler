from itertools import combinations

def confirm(d1,d2):
    return (((0 in d1 and 1 in d2) or (0 in d2 and 1 in d1)) and # 01
            ((0 in d1 and 4 in d2) or (0 in d2 and 4 in d1)) and # 04
            ((0 in d1 and (9 in d2 or 6 in d2)) or (0 in d2 and (9 in d1 or 6 in d1))) and # 09
            ((1 in d1 and (6 in d2 or 9 in d2)) or (1 in d2 and (6 in d1 or 9 in d1))) and # 16
            ((2 in d1 and 5 in d2) or (2 in d2 and 5 in d1)) and # 25
            ((3 in d1 and (6 in d2 or 9 in d2)) or (3 in d2 and (6 in d1 or 9 in d1))) and # 36
            ((4 in d1 and (9 in d2 or 6 in d2)) or (4 in d2 and (9 in d1 or 6 in d1))) and # 49
            (((6 in d1 or 9 in d1) and 4 in d2) or ((6 in d2 or 9 in d2) and 4 in d1)) and # 64
            ((8 in d1 and 1 in d2) or (8 in d2 and 1 in d1))) # 81

dice = list(combinations((0,1,2,3,4,5,6,7,8,9), 6))

answer = 0

while dice:
    die1 = dice.pop()
    answer += sum(int(confirm(die1, die2)) for die2 in dice)

print answer
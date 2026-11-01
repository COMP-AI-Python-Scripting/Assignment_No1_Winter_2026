
for i, upper in enumerate (range(ord('A'), ord('Z')+1), 1):
    lower = upper + 32
    if i == 26:
        print(f"{chr(upper)} ({upper:02X}) -> {chr(lower)} ({lower:02X})", end='.\n')
    elif i % 6 == 0:
        print(f"{chr(upper)} ({upper:02X}) -> {chr(lower)} ({lower:02X})", end=',\n')
    else:
        print(f"{chr(upper)} ({upper:02X}) -> {chr(lower)} ({lower:02X})", end=', ')

letters = {f"{chr(i)} ({i:02X})": f"{chr(i+32)} ({i+32:02X})" for i in range(ord('A'), ord('Z')+1)}

l = len(letters)
for i, (k, v) in enumerate(letters.items(),start=1):
    if i == l: 
        end_char = ".\n"
    elif i % 6 == 0:
        end_char = ",\n"
    else:
        end_char = ", "

    print(f"{k} -> {v}",end=end_char)




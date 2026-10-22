def calculateElapsedTime(seconds):
    if seconds < 0:
        return 'Invalid Input!'
    
    hours = 0

    while seconds >= 3600:
        hours += 1
        seconds -= 3600

    minutes = 0

    while seconds >= 60:
        minutes += 1
        seconds -= 60

    elapsedTime = []
    elapsedTime.append(str(hours).zfill(2) + "H")
    elapsedTime.append(str(minutes).zfill(2) + "M")
    elapsedTime.append(str(seconds).zfill(2) + "S")

    return ':'.join(elapsedTime)


t1 = 3600
t2 = 3665
t3 = 0
t4 = 12345
t5 = 86399
t6 = -120

print(f"{t1} seconds is {calculateElapsedTime(t1)}")
print(f"{t2} seconds is {calculateElapsedTime(t2)}")
print(f"{t3} seconds is {calculateElapsedTime(t3)}")
print(f"{t4} seconds is {calculateElapsedTime(t4)}")
print(f"{t5} seconds is {calculateElapsedTime(t5)}")
print(f"{t6} seconds is {calculateElapsedTime(t6)}")


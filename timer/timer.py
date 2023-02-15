import time

hours = 0
minutes = 0
seconds = 0
while True:
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0
        if minutes > 59:
            hours += 1
            minutes = 0
            seconds = 0
            if hours > 23:
                hours = 0
                minutes = 0
                seconds = 0
                break
    time.sleep(1.0)
    print(f'{hours}:{minutes}:{seconds}')

def countdown(i):
    print(i)
    if i > 0:
        countdown(i-1)
    else:
        return 0

countdown(1)

for n in range(1,31):
    fb = ''
    if n % 3 == 0:
        fb += 'Fizz'
    if n % 5 == 0:
        fb += 'Buzz'
    if not fb:
        fb += str(n)
    print fb
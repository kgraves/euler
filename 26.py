def reciprocal_cycles(n):
  length = 0
  number = 2

  for denom in reversed(range(2, n+1)):
    if length >= denom:
      break

    remainders = [0] * denom
    numer = 1
    position = 0

    while remainders[numer] == 0 and not numer == 0:
      remainders[numer] = position
      numer *= 10
      numer %= denom
      position += 1

    if position - remainders[numer] > length:
      length = position - remainders[numer]
      number = denom

  print 'number %d -- length %d' % (number, length)

if __name__ == '__main__':
    reciprocal_cycles(1000)

def printpyramid(levels):
  result = ''

  for i in range(levels):
    level = ''
    level += ' ' * (levels - i - 1)
    level += '*' * (2 * i + 1)

    result += level + '\n'

  return result

print (printpyramid(5))

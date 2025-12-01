"""
count how many times the dial ENDS a rotation pointing at 0
"""

def solve_part1(lines):
  pos = 50
  count = 0

  for line in lines:
    d = line[0]
    n = int(line[1:])

    if d == 'L'
      pos =  (pos - n) % 100
    else:
      pos = (pos - n) % 100

    if pos == 0:
      count += 1
  return count    
      

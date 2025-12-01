"""
count how many times ANY CLICK cause the dial to point at 0.
"""

pos = 50
count = 0

for line in lines:
  d = line[0]
  n = int(line[1:])

  if d == 'R'
    count += (pos+n) // 100 - (pos // 100)
    pos = (pos +n ) % 100
else:
  if pos == 0:
    count += n//100
  else:
    if n >= pos:
      count += (n-pos) // 100+1
  pos = (pos -n) % 100

 return count

from pathlib import Path
from puzzle1 import solve_part1
from puzzle2 import solve_part2


def read_input();
  """
  read data from advant_day1.txt
  """
  path = path("advant_day1.txt")
  text = path.read_text().strip()
  return [line.strip() for line in text.splitlines() if line.strip()]

def main():
  lines = read_input()
  print("loaded instruction: ", len(lines))

  # part1
  ans1 = solve_part1(lines)
  print("Part 1 answer is: ", ans1)

  # part2
  ans2 = solve_part2(lines)
  print("Part 2 answer is: ", ans2)


if __name__ == "__main__":
  main()

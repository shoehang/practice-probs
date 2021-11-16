import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
'''
1,4,5,2,8

2,4,1,8,5
1,4,2,8,5
1,4,5,8,2
seems like any arary works so long as same num of elements and same occ of elements
'''

def are_they_equal(array_a, array_b):
  # Write your code here
  d = {}
  
  for num in array_a:
    if num in d:
      d[num] += 1
    else:
      d[num] = 1

  for num in array_b:
    if num in d:
      if d[num] == 0:
        return False
      else:
        d[num] -= 1
    else:
      return False
  return True

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
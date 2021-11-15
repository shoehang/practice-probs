import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def numberOfWays(arr, k):
  # Write your code here
  dct = {}
  arr.sort()
  output = 0

  for num in arr:
    if num in dct:
      dct[num] += 1
    else:
      dct[num] = 1

  left, right = 0, len(arr) - 1

  while left < right:
    weightL = weightR = 1
    
    if k / 2 == arr[left] and k / 2 == arr[right]:
      output += dct[arr[left]] * (dct[arr[left]] - 1) / 2
      break
    
    if dct[arr[left]] > 1:
      weightL += dct[arr[left]] - 1
      left += dct[arr[left]] - 1
    if dct[arr[right]] > 1:
      weightR += dct[arr[right]] - 1
      right -= dct[arr[right]] - 1
      
    if arr[left] + arr[right] == k:
      output += weightL * weightR
      left += 1
      right -= 1

    elif arr[left] + arr[right] < k:
      left += 1

    else:
      right -= 1

  return output
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  print('finished')

  # Add your own test cases here
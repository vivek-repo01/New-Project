def sum_list(numbers):

  total = 0
  for num in numbers:
    total = total + num
  return total

# Example usage
numbers = [1, 2, 3, 4, 5]

result = sum_list(numbers)
print(result)

#total = total + num: Inside the loop, this line adds the current value 
#of num to the current value of total, and then assigns the result back 
#to total. This is equivalent to total += num.

#After the loop finishes, return total is used to return the final value 
#of total, which is the sum of all numbers in the list.
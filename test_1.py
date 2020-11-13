
"""
The program is trying to determine which payment option is better and has a higher pay.
The first option is 100 dollars per day for 10 days. The second option is 1 dollar a day
with it being doubled on each consecutive day for 10 days. There will be two functions to calculate the pay rate.
function1 will calculate the amount for the first option, function2 will calculate the amount for the second option.

function1 will output 100 dollars * 10 days.
function2 will loop for 10 times, with each time, it will double the amount and then add the amount to the total.

if both the amounts are equal, we output to the user "Option 1 and Option 2 pays the same"
if option1 is better, we output to the user "Option 1 is better"
if option2 is better, we output to the user "Option 2 is better"
"""


"""
# option1
  return 100 * 10

# option2
  amount = 1
  list1 = []
  loop 10 times
    add amount to list1
    amount *= 2
  sum = sum of all items in loop
  return sum

# main
  var1 = option1
  var2 = option2

  if var1 = var2
    "Option 1 and Option 2 pays the same"
  if var1 < var2
    "Option 2 is better"
  if var1 > var2
    "Option 1 is better"

main
"""
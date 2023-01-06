# is_binary_equal will return true if there are an equal amount of 1's to 0's, and false if there is an unequal amount
def is_binary_equal(binary):
  return binary.count('1')  == binary.count('0')

# tests 
print(is_binary_equal('100101') # true 
print(is_binary_equal('1010101') # false 
print(is_binary_equal('010101') # true 
print(is_binary_equal('110101') # false

# is_binary_equal 
# @param - takes a binary number  
# @returns - 
# True if there are an equal amount of ones to zeros
# False and the ones and zeros count if there is an unequal amount
def is_binary_equal(binary):
  
  # handle nonstring input error
  if type(binary) != str: 
    print('Error: Binary must be in string format')
    return
  
  ones_count = binary.count('1')
  zeros_count = binary.count('0') 
  
  if ones_count == zeros_count:
    return True
  else: 
    return false, one_count, zero_count

# tests 
print(is_binary_equal('100101')) # true 
print(is_binary_equal('1010101')) # (4, 3) 
print(is_binary_equal('010101')) # true 
print(is_binary_equal('110101')) # (4, 2)
print(is_binary_equal(010101)) # Error

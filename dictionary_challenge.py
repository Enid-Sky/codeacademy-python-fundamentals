# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  return sum(my_dictionary.values())

# Test function calls:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6



#  This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
    count = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            count += my_dictionary[key]
    return count

# Test function calls:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6



# The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key] += 10
    return my_dictionary

  

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


#  This function should return a list of all values in the dictionary that are also keys.

# Write your values_that_are_keys function here:
# input: dictionary
# return a list of values
# create an empty list
# loop over dictionary values
# if value in dictionary
# append value to list
# return list
# * Remember to check if value is IN dictionary keys.

def values_that_are_keys(my_dictionary):
    list_values = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            list_values.append(value)
    return list_values


# flip it and check for keys in values
# def values_that_are_keys(my_dictionary):
#   list_keys = []
#   for key in my_dictionary.keys():
#     if key in my_dictionary.values():
#       list_keys.append(key)
#   return list_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
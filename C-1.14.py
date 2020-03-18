# Exercise C-1.14 page 52

def odd_product(nums):
  for a in range(len(nums)):
    for b in range(len(nums)):
      if  a != b:
        product = nums[a] * nums[b]
        if product & 1:
          return True
          return False
          
first = [4, 8, 5, 7, 6, 10, 12, 15, 16, 18, 23]
second = [3, 6, 9, 7, 8, 11 , 18, 15, 16, 19]
print(first, odd_product(first));
print(second, odd_product(second));
odd_first = list(filter(lambda i: (i % 2 !=0),first))
odd_second = list(filter(lambda i: (i % 2 !=0),second))
print("Numbers in the 1st sequence whose product is an odd number: ", odd_first)
print("Numbers in the 2nd sequence whose product is an odd number: ", odd_second)
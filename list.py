#list
marks = [80,90,75,85]
print(marks[0])
print(marks[1])
print(marks[3])

#list append
nums = [1,2,3,4,5,6]
nums.append(90) # adds the element at the end of the list elements
print(nums)

#remove the elements from a list
marks = [80,90,75]
marks.remove(90) # remove the particular element that we need
print(marks)

#insert method
numbers = [80,90,78,67]

numbers.insert(0,12) # it inserts the value that the position that where we need
print(numbers)

#extend method
a = [1,2,3]
b =[4,5,6]
a.extend(b) # it combines the given two variables lists
print(a)

nums = [1,2,3]
nums.clear() #clears all the elements in the elements
print(nums)

#index method
nums = [1,2,3,4]
n = nums.index(4) # it specifies the index of the element in the list
print(n)
#count method
a = [10,20,20,30,20]
print(a.count(20)) #it counts the no of times the number 20 is repeated

#sort method
numbers = [10,40,30,20,50,70]
numbers.sort() # it sorts the values in a ascending order
print(numbers)
#reverse sort method
numbers = [10,20,40,70,60,40]
numbers.sort(reverse=True) #it sorts the value in the descending order
print(numbers)

# reverse method
nums = [10,30,20,40]
nums.reverse() # it simply reverse the list without any particular order
print(nums)
#copy method
a = [1,2,3]
b = a.copy()  # it copies the first variable to the another variable

print(a)

# slicing
nums = [10,20,30,40,50]
print(nums[1:4]) #print starts at 1 and stop when 4 comes

print(nums[:3]) #print starts from 0 and stops when 3 comes

print( nums[2:])# print starts from 3 and continues upto the last

print(nums[::-3]) # start from 50 means end and jump through 3 numbers

print(nums[::-1])#starts from the end jumps by 1

print(nums[::-2])#starts from the end jumps by 2 to the end

print(nums[-2::])#starts from -2 and continues to the end without any jumping here

print(nums[-3::])#starts from -3 and continues to the end without any jumping here















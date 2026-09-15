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
nums = [10,20,30,40,50,60,70,80]
print(nums[1:4]) #print starts at 1 and stop when 4 comes

print(nums[:3]) #print starts from 0 and stops when 3 comes

print( nums[2:])# print starts from 3 and continues upto the last

print(nums[::-3]) # start from 50 means end and jump through 3 numbers

print(nums[::-1])#starts from the end jumps by 1

print(nums[::-2])#starts from the end jumps by 2 to the end

print(nums[-2::])#starts from -2 and continues to the end without any jumping here

print(nums[-3::])#starts from -3 and continues to the end without any jumping here

print(nums[1:7:2]) #simply print(nums[start:stop:step])


#tuples in python
# Tuple is a collection of multiple values that is ordered and cannot be changed after creation
student= ("Vihan",90,"python")
print(student[0])

#access values in a tuple
student = ("Vihan",21,85.5)

print(student[0])
print(student[1])
print(student[2])

# #immutable nature of tuples
# studen=("Madhan",21,85.5)

# student[1]=22
# #This gives an error because we cannot modify a tuple


#tuples are immutable,meaning they cannot be changed after they created.they are defined 
numbers=(10,20,20,30,20)

print(numbers.count(20))

#tuple in index method
numbers = (10,20,30,40)

print(numbers.index(30))

#various methods
numbers = (10,20,30,40,50,60)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#set in python

#set is a colletion of unique values that is unordered and mutable
numbers = {10,20,30,40,20,30,40}
print(numbers)

#why to use set ?

#sstudent has participated in cricket game in two years and want to know how many games he participated in the four years
student = {"cricket","football","cricket","volleyball"}
print(student)

#add values to a set

subjects = {"python","java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects = {"python","java"}
subjects.remove("python")

print(subjects)

#Dictionaries in python
#Dictionarues is a collection of key values pairs that is unordered and mutable
student = {
            "name":"vihan",
            "age": 33 ,
            "course":"python"



}
print(student["name"])
print(student["age"])
print(student["course"])





student = {"name":"vihan",
            "age": 33 ,
            "course":"python"



}

print(student.keys())
#keys() returns all the keys in the dictionary
print(student.values())
#values() returns all the values in the dictionary
print(student.items()) 
#items() returns all the key-value pairs in the dictionary
print(student.get("name"))
# get() returns the value for the specified key
student.update({"age": 22})
# update() update the value of the specified key
student.pop("age")
#pop is just nithing but remove a item
student.popitem()
#popitem()removes the last titem in the inserted key-value pairs
student.setdefault("hobbies","play games")
#setdefault is used to add the element to the dictionary 
print(student)















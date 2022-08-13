strList = ["StrA", "StrB", "StrC", "StrD", "StrE", "StrF"]
typelessList = ["StrA", 1, True]

print(strList[1])
print(typelessList[2])
print(typelessList[0:])
print(strList[3:5])

numbers = [4, 8, 15, 16, 23, 42]
letters = ["A", "B", "C", "D", "E", "F"]
print(strList)
print(strList)
strList.extend(numbers)
letters.append("A")
print(letters.count("A"))

numbers.append(99)
print(numbers)
numbers.insert(0, 101)
print(numbers)
numbers.remove(15)
print(numbers)
numbers.pop(1)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_copy = numbers.copy()
print(numbers_copy)
numbers_copy.clear()
print(numbers_copy)

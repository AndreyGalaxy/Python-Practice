List = [1,1,2,3,5,8,13,21,34,55,89]
Number = int(input("Input a number: "))

List2 = [element for element in List if element < Number]

print (List2)
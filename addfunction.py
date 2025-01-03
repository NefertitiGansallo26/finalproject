def mathFunction():
    no1 = int(input("Enter first number: "))  # getno1
    no2 = int(input("Enter second number: "))  # getno2
    return addNumbers(no1, no2)

def addNumbers(no1, no2):
    result = no1+no2
    print(result)
    return result


mathFunction()

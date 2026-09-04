class Calculator:
    def multiply(self,a,b, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply(10,11))            
print(calc.multiply(10,11))           

# Using multiple arguments
print(calc.multiply(2,2,2,2,2,2,1,4,4))       
print(calc.multiply(2, 2, 2))


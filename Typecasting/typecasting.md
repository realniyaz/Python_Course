# Typecasting in Python

The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.

## Types of Typecasting: 

### Explicit Typecastnig
The conversion of one data type into another data type, done via programmeris known as explicit type conversion.
It can be achieved with the help of functions such as int(), float(), hex(), oct(), str(), etc .

```
s = "20"
num = 7

sum1 = int(s) + num #explicit typecastimg
print(f"the sum of two numbers is {sum1}")
```

### Implicit Typecasting
Some of the data types have higher-order, and some have lower-order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher order data type. According to the level, one data type is converted into other by the Python interpreter automatically. This is called, implicit typecasting.

```
i = 8.09
j = 10

sum2 = i + j #implicit typecasting
print(sum2)
```

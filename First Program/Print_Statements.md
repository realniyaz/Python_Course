## FIRST PROGRAM
### Using Print Command
The print command is used to display the output of the program as when we start programming and learn about it we tend to understand that the program would ultimately result in some output. In `Python` we use `Print` statements to print the output or display the outputs on the console.

### Program Descripiton 
```
print("Hello, World")

#Print statements using variables
name = "Niyaz"
age = 21

print(name, age)
print("Name:", name, "Age:", age)

#Print statements using f-string concepts
Name = "Alex"
Age = 18

print(f"My name is {name} and I am {age} years old")
print(f"My name is {Name} and I am {Age} years old")
```

#### Using variables 
Using any kind of variables, we store our data in a memor location called the variables and it can be printed using those variables 
```
Syntax : var_name = object
print(var_name)
```

#### Using f-sting
These are the formated strings which were used to embed the varibales in a common way to print on the console, this improves efficiency and concise the code.
```
Syntax: var_name = object
print(f"we are using {var_name}")
```

#### Use of end and sep 
`#end:` used to add objects at the end of the displayed values
```
print("Hi","Hello", "Ola", end="Niyaz\n") # We saw Niyaz added at the last of the displayed result
```
`#sep:` used to seperate the multiple objects in the print statement
```
print(14 , 6, 2004, sep="-")
```

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
"""

my_age = 21
your_age = int(input("Enter your age: "))
year = 2024 - your_age
if(my_age>your_age):
  print("My age is greater than you")
  difference : my_age - your_age
  if(difference == 1):
    print(year)
  else:
    print("year difference > 1")
else:
  print("your age is greater than my age")

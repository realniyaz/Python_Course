marks_list = list(map(int, input("Enter your marks separated by spaces: ").split()))
total_marks = sum(marks_list)
marks_percent = (total_marks / 500) * 100  # 5 subjects each of 100 marks

if 90 <= marks_percent <= 100:
    print("Grade : A")
elif 70 <= marks_percent < 90:
    print("Grade : B")
elif 60 <= marks_percent < 70:
    print("Grade : C")
elif 50 <= marks_percent < 60:
    print("Grade : D")
else:
    print("Grade : F")

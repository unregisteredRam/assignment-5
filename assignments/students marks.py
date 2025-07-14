class21={'Alice':85,'tom':88,'sam':92,'Alex':98,'jeff':89}
students_name=input('Enter the student`s name:')
if students_name in class21:
    print(f"{students_name}`s marks:{class21[students_name]}")
else:
    print('student not found.')

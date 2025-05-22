# Input age
age = int(input("What is your age: "))
# input if a Copperfield student YES/No
is_student_input = input("Are you a student of Copperfield College? (yes/no): ")
# Put input into lowercase and compare
is_student = is_student_input.lower() == "yes"
#  If Copperfield College Student
if is_student:
    if age >= 15:
        print("You are in middle school or above")
    else:
        print("Have a nice day Copperfield Student")
# If not a Copperfield Student
else:
    print("Have a nice day")
    
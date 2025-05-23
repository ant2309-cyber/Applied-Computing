#Enter how many students in the class
int(input("Enter the total number of students in your class: "))
#Enter the students name
input("What is the name of student 1: ")
input("What is the name of student 2: ")
input("What is the name of student 3: ")
#Ask for the number of periods that occured
total_periods = int(input("Enter the total number of periods that were held: "))
#if the student was absent of present
present_count = 0
absent_count = 0
for i in range(1, total_periods + 1):
    status = input(f"was the student present or absent in period {1}? (p/a): ").strip().lower()
    if status == 'p':
        present_count += 1
    elif status == 'a':
        absent_count += 1
    else:
        print("No No do it right")
        i -= 1
#THIS IS NOT FINISHED I WILL DO MORE AT HOME
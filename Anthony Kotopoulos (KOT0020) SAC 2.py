#ask how many students in the class
amount_students = int(input('Enter the total amount of students in the class (1-3): '))
student_names = []

#enter the students' names
for i in range(1, amount_students + 1):
    name = input(f'What is the name of student {i}? ').strip().title()
    student_names.append(name)

#ask for the number of periods that occurred
while True:
    total_periods = int(input("Enter the total number of periods that were held that day (1-5): "))
    if 1 <= total_periods <= 5:
        break
    print("Please enter a number between 1 and 5.")

#store attendance
attendance_data = {}

#ask what period each student attended
for name in student_names:
    print(f"\nEntering attendance for {name}:")
    period_attendance = []
    for i in range(1, total_periods + 1):
        while True:
            status = input(f"  Was the student present or absent in period {i}? (p/a): ").strip().lower()
            if status in ['p', 'a']:
                period_attendance.append(status)
                break
            else:
                print("  Invalid input. Please enter 'p' for present or 'a' for absent.")
    attendance_data[name] = period_attendance

#calculate percentages
print("\n--- Attendance Summary ---")
for name, records in attendance_data.items():
    present_count = records.count('p')
#calculation
    percentage = (present_count / total_periods) * 100
    print(f"\nStudent: {name}")
    print(f"  Total Periods Present: {present_count}/{total_periods}")
    print(f"  Attendance Percentage: {percentage:.2f}%")
#if attendeance is below 75% issue a warning
    if percentage < 75:
        print("  WARNING: ATTENDANCE BELLOW 75%!")

#save attendnce to data file
with open("attendance_records.txt", "w") as file:
    for name, records in attendance_data.items():
        record_str = ', '.join([s.upper() for s in records])
        file.write(f"{name}: {record_str}\n")

print("Data saved to file")

hours_worked = float(input("hours"))
pay_rate = float(input("rate"))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_rate = pay_rate*1.5

    total = (hours_worked * pay_rate) + (overtime_hours * overtime_rate)

    print(f"Total to be paid: ${total}")
else:
    total = hours_worked * pay_rate
    print(f"Total to be paid: ${total}")
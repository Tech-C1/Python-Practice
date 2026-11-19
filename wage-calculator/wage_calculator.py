hours = float(input("how many hours have you worked?"))
hourly_rate = float(input("what is your hourly pay rate?"))
overtime_rate = hourly_rate * 1.25

if hours < 0 or hourly_rate < 0:
    print("Hours and hourly rate cannot be negative.")
elif hours <= 40.00:
    gross_pay = hours * hourly_rate
else:
    extra_hours = hours - 40
    overtime_pay = extra_hours * overtime_rate
    gross_pay = (40 * hourly_rate) + overtime_pay



if hours >= 0 and hourly_rate >= 0:
    print(f"Gross Pay: £{gross_pay:.2f}")
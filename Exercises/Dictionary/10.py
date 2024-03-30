companies = {}

while True:
    line = input()
    if line == "End":
        break

    company_name, employee_id = line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = set()

    companies[company_name].add(employee_id)

for company_name, employees in companies.items():
    print(company_name)
    for employee_id in employees:
        print(f"-- {employee_id}")

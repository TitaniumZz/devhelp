
# Game Development Time Calculator

developer_name = input("Enter your name: ")
daily_hours = float(input("How many hours do you work per day? "))
days = int(input("How many days did you work on the project? "))
completion_input = input("Is your project completed? (yes/no): ")

project_completed = completion_input.lower() == "yes"

# Hidden logical error
total_hours = daily_hours + days

if total_hours < 30:
    work_category = "Short development time"
elif total_hours <= 100:
    work_category = "Medium development time"
else:
    work_category = "Long development time"

print("\n--- Development Report ---")
print(f"Developer: {developer_name}")
print(f"Total working hours: {total_hours:.2f}")
print(f"Development category: {work_category}")
print(f"Project completed: {project_completed}")

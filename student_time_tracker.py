
print("STUDENT TIME LEAK DETECTOR")
print("--------------------------")

activities = []

while True:
    activity = input("Enter activity (or done): ")

    if activity.lower() == "done":
        break

    minutes = int(input("Enter minutes: "))

    category = input(
        "Enter category (productive/non-productive): "
    ).lower()

    activities.append({
        "name": activity,
        "minutes": minutes,
        "category": category
    })

# Calculate total time
total_time = 0
productive_time = 0
non_productive_time = 0

for item in activities:
    total_time += item["minutes"]

    if item["category"] == "productive":
        productive_time += item["minutes"]
    elif item["category"] == "non-productive":
        non_productive_time += item["minutes"]

# Create daily report
report = "\n--- DAILY ACTIVITY REPORT ---\n"

for item in activities:
    report += (
        f'{item["name"]} - {item["minutes"]} minutes'
        f' - {item["category"]}\n'
    )

report += "\n--- TIME SUMMARY ---\n"
report += f"Total time: {total_time} minutes\n"
report += f"Productive time: {productive_time} minutes\n"
report += f"Non-productive time: {non_productive_time} minutes\n"

# Find biggest time leak
non_productive_activities = []

for item in activities:
    if item["category"] == "non-productive":
        non_productive_activities.append(item)

if non_productive_activities:
    biggest_leak = max(
        non_productive_activities,
        key=lambda item: item["minutes"]
    )

    report += "\n--- BIGGEST TIME LEAK ---\n"
    report += f"Activity: {biggest_leak['name']}\n"
    report += f"Time: {biggest_leak['minutes']} minutes\n"

    print("\nBiggest time leak:", biggest_leak["name"])
    print("Time:", biggest_leak["minutes"], "minutes")
else:
    print("\nNo non-productive activities recorded!")

# Display and save report
print(report)

with open("daily_report.txt", "w") as file:
    file.write(report)

print("Report saved successfully!")
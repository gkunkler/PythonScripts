from icalendar import Calendar
import os

# Replace 'your_calendar.ics' with the path to your .ics file
file_path = 'period4.ics'

# Load the calendar file
with open(file_path, 'r', encoding='utf-8') as f:
    calendar_data = f.read()

# Parse the calendar data
calendar = Calendar.from_ical(calendar_data)

# Create a new Calendar instance for filtered events
filtered_calendar = Calendar()

# Loop through each event in the original calendar
for component in calendar.walk():
    # Check if the component is an event and contains "IE2405" in the summary

    matchesTitle = False
    for word in {"SF1861"}:
        if word in component.get("SUMMARY", ""):
            matchesTitle = True
            break

    if component.name == "VEVENT" and matchesTitle:
        # Add the event to the new calendar
        filtered_calendar.add_component(component)

# Define the path for the new filtered calendar file
filtered_file_path = 'filtered_SF1861_events.ics'

# Write the filtered events to a new .ics file
with open(filtered_file_path, 'wb') as f:
    f.write(filtered_calendar.to_ical())

print(f"Filtered events saved to {filtered_file_path}")
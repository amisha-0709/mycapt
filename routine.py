import matplotlib.pyplot as plt

# Initialize empty lists to store productivity levels and times of day
productivity_levels = []
times_of_day = []

# Continuously prompt user to input productivity level and time of day
while True:
    # Prompt user to input productivity level
    productivity_input = input("Enter your productivity level (1-5): ")
    # If the user enters 'done', stop recording
    if productivity_input == "done":
        break
    # Convert productivity input to integer and append to list
    productivity_levels.append(int(productivity_input))
    # Prompt user to input time of day
    time_input = input("Enter the time of day (in hours): ")
    # Convert time input to integer and append to list
    times_of_day.append(int(time_input))

# Create a bar graph of productivity levels by time of day
plt.bar(times_of_day, productivity_levels)
plt.xlabel("Time of day (hours)")
plt.ylabel("Productivity level (1-5)")
plt.show()
'''terminal will look like this--
Enter your productivity level (1-5): 3
Enter the time of day (in hours): 8
Enter your productivity level (1-5): 2
Enter the time of day (in hours): 9
Enter your productivity level (1-5): 4
Enter the time of day (in hours): 11
Enter your productivity level (1-5): 1
Enter the time of day (in hours): 12
Enter your productivity level (1-5): 0
Enter the time of day (in hours): 1
Enter your productivity level (1-5): 2
Enter the time of day (in hours): 2
Enter your productivity level (1-5): 4
Enter the time of day (in hours): 4
Enter your productivity level (1-5): 5
Enter the time of day (in hours): 5
Enter your productivity level (1-5): 1
Enter the time of day (in hours): 6
Enter your productivity level (1-5): 4
Enter the time of day (in hours): 7
Enter your productivity level (1-5): 2
Enter the time of day (in hours): 8
Enter your productivity level (1-5): 1
Enter the time of day (in hours): 9
Enter your productivity level (1-5): done'''

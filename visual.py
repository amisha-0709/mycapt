import matplotlib.pyplot as plt

# Define the marks in the cycle tests
cycle_tests = [110, 98, 114, 71]

# Define the total marks for each cycle test
total_marks = [150, 150, 150, 150]

# Calculate the percentage marks for each cycle test
percentages = [round(marks / total * 100) for marks, total in zip(cycle_tests, total_marks)]

# Define the labels for the x-axis
x_labels = ['Cycle Test 1', 'Cycle Test 2', 'Cycle Test 3', 'Cycle Test 4']

# Set the title and labels for the plot
plt.title('Cycle Test Marks')
plt.xlabel('Cycle Tests')
plt.ylabel('Marks')

# Create the bar plot
plt.bar(x_labels, percentages)

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Sample monthly rainfall data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [50, 40, 60, 30, 70, 80, 90, 85, 75, 65, 55, 45]  # Replace with your actual rainfall data

plt.figure(figsize=(8, 6))
plt.scatter(months, rainfall, color='blue')

plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()

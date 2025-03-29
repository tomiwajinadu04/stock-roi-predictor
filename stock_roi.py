import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def calculate_roi():
    try:
        # Get user inputs
        principal_str = principal_entry.get()
        rate_str = rate_entry.get()
        years_str = years_entry.get()
        
        # Check if any field is empty
        if not principal_str or not rate_str or not years_str:
            result_label.config(text="Please fill in all fields.")
            return
        
        # Convert to correct data types and validate
        principal = float(principal_str)  # Principal investment
        rate = float(rate_str) / 100  # Convert to decimal for percentage
        years = int(years_str)  # Investment duration in years

        # Validate inputs
        if principal <= 0:
            result_label.config(text="Principal investment must be a positive number.")
            return
        if rate <= 0:
            result_label.config(text="Growth rate must be a positive number.")
            return
        if years <= 0:
            result_label.config(text="Investment duration must be a positive number.")
            return

        # Calculate projected ROI
        future_values = [principal * ((1 + rate) ** i) for i in range(1, years + 1)]

        # Display the result
        result_label.config(text=f"Projected ROI in {years} years: ${future_values[-1]:.2f}")

        # Plot the graph
        plt.figure(figsize=(6, 4))
        plt.plot(range(1, years + 1), future_values, marker='o', linestyle='-')
        plt.xlabel('Years')
        plt.ylabel('Projected Value ($)')
        plt.title('Stock ROI Projection')
        plt.grid()
        plt.show()

    except ValueError:
        result_label.config(text="Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Stock ROI Predictor")
root.geometry("400x300")

tk.Label(root, text="Principal Investment ($):").pack()
tk.Label(root, text="Enter the amount you want to invest (e.g., 1000 for $1,000)").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Annual Growth Rate (%):").pack()
tk.Label(root, text="Enter the expected annual growth rate (e.g., 8 for 8% growth)").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Investment Duration (Years):").pack()
tk.Label(root, text="Enter the number of years you plan to invest for (e.g., 5)").pack()
years_entry = tk.Entry(root)
years_entry.pack()

calculate_button = tk.Button(root, text="Calculate ROI", command=calculate_roi)
calculate_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()

import tkinter as tk
from tkinter import ttk

# ---------------- CONVERSION FUNCTIONS ---------------- #

def convert():
    value = float(entry.get())
    choice = combo.get()

    result = ""

    # LENGTH
    if choice == "Meters to Kilometers":
        result = value / 1000
    elif choice == "Kilometers to Meters":
        result = value * 1000
    elif choice == "Meters to Centimeters":
        result = value * 100
    elif choice == "Centimeters to Meters":
        result = value / 100
    elif choice == "Miles to Kilometers":
        result = value * 1.60934

    # WEIGHT
    elif choice == "Kilograms to Grams":
        result = value * 1000
    elif choice == "Grams to Kilograms":
        result = value / 1000
    elif choice == "Pounds to Kilograms":
        result = value * 0.453592
    elif choice == "Kilograms to Pounds":
        result = value / 0.453592

    # TEMPERATURE
    elif choice == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
    elif choice == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
    elif choice == "Celsius to Kelvin":
        result = value + 273.15
    elif choice == "Kelvin to Celsius":
        result = value - 273.15

    # SPEED
    elif choice == "Km/h to m/s":
        result = value / 3.6
    elif choice == "m/s to Km/h":
        result = value * 3.6

    # AREA
    elif choice == "Square meters to Square km":
        result = value / 1_000_000
    elif choice == "Square km to Square meters":
        result = value * 1_000_000
    elif choice == "Square feet to Square meters":
        result = value * 0.092903
    elif choice == "Square meters to Square feet":
        result = value / 0.092903

    # VOLUME
    elif choice == "Liters to Milliliters":
        result = value * 1000
    elif choice == "Milliliters to Liters":
        result = value / 1000
    elif choice == "Cubic meters to Liters":
        result = value * 1000
    elif choice == "Liters to Cubic meters":
        result = value / 1000

    # TIME
    elif choice == "Hours to Minutes":
        result = value * 60
    elif choice == "Minutes to Seconds":
        result = value * 60
    elif choice == "Days to Hours":
        result = value * 24
    elif choice == "Seconds to Minutes":
        result = value / 60

    else:
        result = "Select conversion"

    output_label.config(text=f"Result: {result}")


# ---------------- UI SETUP ---------------- #

root = tk.Tk()
root.title("Unit Converter (25 Conversions)")
root.geometry("400x300")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# 25 conversions list
conversions = [
    "Meters to Kilometers",
    "Kilometers to Meters",
    "Meters to Centimeters",
    "Centimeters to Meters",
    "Miles to Kilometers",

    "Kilograms to Grams",
    "Grams to Kilograms",
    "Pounds to Kilograms",
    "Kilograms to Pounds",

    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius",

    "Km/h to m/s",
    "m/s to Km/h",

    "Square meters to Square km",
    "Square km to Square meters",
    "Square feet to Square meters",
    "Square meters to Square feet",

    "Liters to Milliliters",
    "Milliliters to Liters",
    "Cubic meters to Liters",
    "Liters to Cubic meters",

    "Hours to Minutes",
    "Minutes to Seconds",
    "Days to Hours",
    "Seconds to Minutes"
]

combo = ttk.Combobox(root, values=conversions, font=("Arial", 10))
combo.pack(pady=10)
combo.set("Select Conversion")

btn = tk.Button(root, text="Convert", command=convert)
btn.pack(pady=10)

output_label = tk.Label(root, text="Result:", font=("Arial", 14))
output_label.pack(pady=10)

root.mainloop()
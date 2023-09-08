import tkinter as tk

def calculate_total():
    item_price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    total = item_price * quantity
    total_label.config(text=f"Total: Rp {total:,.2f}")

# Create the main window
window = tk.Tk()
window.title("Cashier Program")

# Create and place the entry labels and fields
price_label = tk.Label(window, text="Harga:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

quantity_label = tk.Label(window, text="Kuantitas:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Create and place the calculate button
calculate_button = tk.Button(window, text="Hitung Total", command=calculate_total)
calculate_button.pack()

# Create and place the total label
total_label = tk.Label(window, text="Total: Rp 0.00")
total_label.pack()

# Start the main loop
window.mainloop()

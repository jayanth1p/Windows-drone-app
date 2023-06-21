import tkinter as tk

def show_selected_axes():
    selected_axes = []
    if x_gyro_var.get():
        selected_axes.append("Gyro X-axis")
    if y_gyro_var.get():
        selected_axes.append("Gyro Y-axis")
    if z_gyro_var.get():
        selected_axes.append("Gyro Z-axis")
    if x_accl_var.get():
        selected_axes.append("Accelerometer X-axis")
    if y_accl_var.get():
        selected_axes.append("Accelerometer Y-axis")
    if z_accl_var.get():
        selected_axes.append("Accelerometer Z-axis")
    print("Selected Axes:", selected_axes)



# Gyro Frame
def gyro(name):
    gyro_frame = tk.Frame(name, bg="blue", padx=10, pady=10)
    gyro_frame.pack(side="left",)

    gyro_label = tk.Label(gyro_frame, text="GYRO:", bg="blue", fg="white", font=("Arial", 12, "bold"))
    gyro_label.pack()

    x_gyro_var = tk.BooleanVar()
    y_gyro_var = tk.BooleanVar()
    z_gyro_var = tk.BooleanVar()

    x_gyro_checkbox = tk.Checkbutton(gyro_frame, text="X-axis", variable=x_gyro_var)
    y_gyro_checkbox = tk.Checkbutton(gyro_frame, text="Y-axis", variable=y_gyro_var)
    z_gyro_checkbox = tk.Checkbutton(gyro_frame, text="Z-axis", variable=z_gyro_var)

    x_gyro_checkbox.pack()
    y_gyro_checkbox.pack()
    z_gyro_checkbox.pack()

    # Accelerometer Frame
def acc(name):
    accl_frame = tk.Frame(name, bg="navy blue", padx=10, pady=10)
    accl_frame.pack(padx=10)

    accl_label = tk.Label(accl_frame, text="ACCEL:", bg="navy blue", fg="white", font=("Arial", 12, "bold"))
    accl_label.pack()

    x_accl_var = tk.BooleanVar()
    y_accl_var = tk.BooleanVar()
    z_accl_var = tk.BooleanVar()

    x_accl_checkbox = tk.Checkbutton(accl_frame, text="X-axis", variable=x_accl_var)
    y_accl_checkbox = tk.Checkbutton(accl_frame, text="Y-axis", variable=y_accl_var)
    z_accl_checkbox = tk.Checkbutton(accl_frame, text="Z-axis", variable=z_accl_var)

    x_accl_checkbox.pack()
    y_accl_checkbox.pack()
    z_accl_checkbox.pack()
    
 

if __name__=="__main__":
    
    root = tk.Tk()
    root.title("TRON TECH LABS")
    gyro(root)
    acc(root)
    root.mainloop()   
    pass


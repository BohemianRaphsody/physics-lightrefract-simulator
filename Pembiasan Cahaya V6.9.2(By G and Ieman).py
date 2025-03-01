import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Arc
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to update the plot based on slider values
def update_plot(angle_incidence, refractive_index1, refractive_index2):
    angle_incidence_rad = np.radians(angle_incidence)
    sin_angle_refraction = (refractive_index1 / refractive_index2) * np.sin(angle_incidence_rad)
    angle_refraction_rad = np.arcsin(sin_angle_refraction)
    angle_refraction = np.degrees(angle_refraction_rad)

    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    # Normal line (garis normal)
    ax.plot([0, 0], [-5, 5], linestyle='--', color='green', label="Garisan Normal")

    # Incident ray
    ax.plot([0, -4 * np.cos(angle_incidence_rad)], [0, 4 * np.sin(angle_incidence_rad)], label="Sudut Tuju(Incident Ray)", color="blue")

    # Refracted ray
    ax.plot([0, 4 * np.cos(angle_refraction_rad)], [0, -4 * np.sin(angle_refraction_rad)], label="Sudut Biasan(Refraction Ray)", color="red")

    # Add arcs to show angles connected to the normal line
    arc1 = Arc((0, 0), 2, 2, angle=90, theta1=0, theta2=90-angle_incidence, edgecolor='blue')  # Blue arc starts from 0 degrees and increases
    arc2 = Arc((0, 0), 2, 2, angle=-90, theta1=360, theta2=90-angle_refraction, edgecolor='red')  # Red arc starts from -90 degrees and reduces by the refracted angle
    ax.add_patch(arc1)
    ax.add_patch(arc2)

    # Annotate angles
    ax.text(-2 * np.cos(np.radians(angle_incidence/2)), 2 * np.sin(np.radians(angle_incidence/2)), f"{angle_incidence:.2f}°", color="blue", fontsize=12, ha='center')
    ax.text(2 * np.cos(np.radians(angle_refraction/2)), -2 * np.sin(np.radians(angle_refraction/2)), f"{angle_refraction:.2f}°", color="red", fontsize=12, ha='center')

    ax.legend()

# Function to update sliders and plot
def on_slider_change(val):
    if hot_reload_var.get():
        angle_incidence = angle_incidence_slider.get()
        refractive_index1 = refractive_index1_slider.get()
        refractive_index2 = refractive_index2_slider.get()

        angle_incidence_entry.delete(0, ctk.END)
        angle_incidence_entry.insert(0, str(angle_incidence))
        
        refractive_index1_entry.delete(0, ctk.END)
        refractive_index1_entry.insert(0, str(refractive_index1))
        
        refractive_index2_entry.delete(0, ctk.END)
        refractive_index2_entry.insert(0, str(refractive_index2))

        update_plot(angle_incidence, refractive_index1, refractive_index2)
        canvas.draw_idle()

# Function to simulate on button press
def on_simulate_button_press():
    try:
        angle_incidence = float(angle_incidence_entry.get())
        refractive_index1 = float(refractive_index1_entry.get())
        refractive_index2 = float(refractive_index2_entry.get())

        angle_incidence_slider.set(angle_incidence)
        refractive_index1_slider.set(refractive_index1)
        refractive_index2_slider.set(refractive_index2)
        
        update_plot(angle_incidence, refractive_index1, refractive_index2)
        canvas.draw_idle()
    except ValueError:
        print("Please enter valid numerical values.")

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode_var.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

# Create the main window
root = ctk.CTk()
root.title("Pembiaasan Cahaya V6.9.2(By G and Ieman)")

# Create plot figure
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

# Create control frame
control_frame = ctk.CTkFrame(root)
control_frame.pack(side=ctk.BOTTOM, fill=ctk.BOTH)

# Create sliders and entry boxes
angle_incidence_frame = ctk.CTkFrame(control_frame)
angle_incidence_frame.pack(fill=ctk.X)
angle_incidence_slider = ctk.CTkSlider(angle_incidence_frame, from_=0, to=90, command=on_slider_change)
angle_incidence_slider.set(30)
angle_incidence_slider.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
angle_incidence_entry = ctk.CTkEntry(angle_incidence_frame, width=50)
angle_incidence_entry.pack(side=ctk.RIGHT, padx=10)
angle_incidence_label = ctk.CTkLabel(control_frame, text="Sudut Tuju(Angle Of Incidence)")
angle_incidence_label.pack()

refractive_index1_frame = ctk.CTkFrame(control_frame)
refractive_index1_frame.pack(fill=ctk.X)
refractive_index1_slider = ctk.CTkSlider(refractive_index1_frame, from_=1, to=2, command=on_slider_change)
refractive_index1_slider.set(1.00)
refractive_index1_slider.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
refractive_index1_entry = ctk.CTkEntry(refractive_index1_frame, width=50)
refractive_index1_entry.pack(side=ctk.RIGHT, padx=10)
refractive_index1_label = ctk.CTkLabel(control_frame, text="Indeks Biasan(Refractive Index)1")
refractive_index1_label.pack()

refractive_index2_frame = ctk.CTkFrame(control_frame)
refractive_index2_frame.pack(fill=ctk.X)
refractive_index2_slider = ctk.CTkSlider(refractive_index2_frame, from_=1, to=2, command=on_slider_change)
refractive_index2_slider.set(1.33)
refractive_index2_slider.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
refractive_index2_entry = ctk.CTkEntry(refractive_index2_frame, width=50)
refractive_index2_entry.pack(side=ctk.RIGHT, padx=10)
refractive_index2_label = ctk.CTkLabel(control_frame, text="Indeks Biasan(Refractive Index)2")
refractive_index2_label.pack()

# Add dark mode toggle button
dark_mode_var = ctk.BooleanVar()
dark_mode_toggle = ctk.CTkCheckBox(control_frame, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
dark_mode_toggle.pack()

# Add hot reload toggle button
hot_reload_var = ctk.BooleanVar(value=True)
hot_reload_toggle = ctk.CTkCheckBox(control_frame, text="Hot Reload", variable=hot_reload_var, command=lambda: simulate_button.pack_forget() if hot_reload_var.get() else simulate_button.pack(fill=ctk.X))
hot_reload_toggle.pack()

# Add simulate button
simulate_button = ctk.CTkButton(control_frame, text="Simulate", command=on_simulate_button_press)
simulate_button.pack()

# Initialize plot
update_plot(30, 1.00, 1.33)

# Animation function to continuously update the plot
def animate(i):
    on_slider_change(None)

ani = FuncAnimation(fig, animate, interval=100)
plt.show(block=False)

# Start the Tkinter main loop
root.mainloop()

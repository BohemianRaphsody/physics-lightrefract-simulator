# Light Refraction Simulator School Project(Created February 24)

This Project is a lite version of the original(<150 lines). In its raw form is 1700 lines long and runs upto 12% CPU capacity. This Version Minimizes total CPU usage by 10000% and only runs at the max of 0.001% CPU. 


Light Refraction Simulator School Project created by **BohemianRaphsody** Also Known As G. The program is designed to simulate light refraction using a dual language interface (Malay-English).

## Features

- **Dual Language Interface**: Malay and English are displayed simultaneously (no included translation; both languages are shown at one time). Customize to your liking.
- **Hot Reload**: Automatically updates the plot when slider values are changed.
- **Dark Mode**: Toggle dark mode for a more comfortable viewing experience.

## Installation

1. Ensure you have Python installed on your computer.
2. Install the required libraries using the following command:
    ```bash
    pip install numpy matplotlib customtkinter
    ```

## Usage

1. Run the `main.py` file:
    ```bash
    python main.py
    ```
2. Use the sliders or entry boxes to input the angle of incidence and the refractive indices.
3. The plot will update automatically if the Hot Reload feature is enabled. Otherwise, press the Simulate button to update the plot.
4. Toggle dark mode using the checkbox provided.

## Code Overview

- **`update_plot` Function**: Updates the plot based on the slider values.
- **`on_slider_change` Function**: Updates the plot and sliders dynamically.
- **`on_simulate_button_press` Function**: Simulates the refraction based on input values.
- **`toggle_dark_mode` Function**: Toggles between light and dark modes.
- **Tkinter GUI Setup**: Sets up the main window and adds all the necessary widgets (sliders, entry boxes, labels, buttons, and checkboxes).

## Verification

This project is verified by GitHub.

## Acknowledgments

Creator: BohemianRaphsody(IM:Lower Division: peak rating of 2118)

This Project Was created By BohemianRaphsody as a school project and only uploaded here for external data research. Please inform for any bugs to ammend as fast as Possible


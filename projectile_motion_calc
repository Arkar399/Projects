from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

planets = [["Earth", 9.81], ["Moon", 1.62], ["Mars", 3.72], ["Jupiter", 24.79]]

def set_grav():
    scale1.set(planets[x.get()][1])

def graph(val):
    ax.clear()

    g = scale1.get()
    u = scale2.get()
    theta_degrees = scale3.get()
    theta = np.radians(theta_degrees)

    if g != 0:
        range = u**2 * np.sin(2*theta) / g
        hp = u**2 * (np.sin(theta))**2 / (2*g)
        t = (2 * u * np.sin(theta)) / g

        x = np.linspace(0, range, 50)
        y = x * np.tan(theta) - (g * x**2) / (2 * u**2 * (np.cos(theta))**2)
    else:
        x = np.linspace(0, 1000, 50) #!!!!!
        y = x

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_xlabel("Distance (m)", font="Arial")
    ax.set_ylabel("Height (m)", font="Arial")
    ax.grid(True, alpha=0.2)

    ax.plot(x, y)

    text_var.set(f"Max Height: {round(hp, 2)}m | Range: {round(range, 2)}m | Air time: {round(t, 2)}s")

    canvas.draw()

# initialize Tkinter
root = tk.Tk()
root.title("Tkinter x Matplotlib")

fig, ax = plt.subplots(figsize=(8, 5))
# ax = fig.add_subplot()

ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_xlabel("Distance (m)", font="Arial")
ax.set_ylabel("Height (m)", font="Arial")
ax.grid(True, alpha=0.2)

# Tkinter application
frame = tk.Frame(root)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True) #to make plot fill windows ig

# for toolbar
toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="w", fill=tk.X)

frame.pack()

text_var = tk.StringVar()
label = tk.Label(frame, textvariable=text_var, font=("Consolas", 18))
label.pack(anchor="w", pady=10)

scale1 = tk.Scale(frame, from_=0, to=30,
              length=400, font=("Consolas", 12), orient="horizontal", command=graph,
              showvalue=1, resolution=0.01,
              troughcolor="gray", fg ="white", bg="black", label="Gravity (N/kg)")

scale1.pack(anchor="w")

scale2 = tk.Scale(frame, from_=0, to=100,
              length=400, font=("Consolas", 12), orient="horizontal", command=graph,
              showvalue=1, resolution=0.01,
              troughcolor="gray", fg ="white", bg="black", label="Initial Velocity (m/s)")

scale2.pack(anchor="w")

scale3 = tk.Scale(frame, from_=0, to=90,
              length=400, font=("Consolas", 12), orient="horizontal", command=graph,
              showvalue=1, resolution=0.01,
              troughcolor="gray", fg ="white", bg="black", label="Angle (degrees)")

scale3.pack(anchor="w")

x = tk.IntVar()
for i in range(len(planets)):
    radio_button = tk.Radiobutton(frame, variable=x, value=i, text=planets[i][0], padx=15, pady=10,
                                  font=("Consolas", 15), command=set_grav, indicatoron=0)

    radio_button.pack(side="left")

root.mainloop()

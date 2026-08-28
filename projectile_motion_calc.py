from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

planets = [["Earth", 9.81], ["Moon", 1.62], ["Mars", 3.72], ["Jupiter", 24.79]]

def submit_with_enter(event):
    text = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    scale1.set(float(text[0]))
    scale2.set(float(text[1]))
    scale3.set(float(text[2]))
    scale4.set(float(text[3]))

def set_grav():
    scale1.set(planets[x.get()][1])

def graph(val):
    ax.clear()

    g = scale1.get()
    u = scale2.get()
    theta_degrees = scale3.get()
    y0 = scale4.get()
    theta = np.radians(theta_degrees)

    if g != 0:
        t = (u * np.sin(theta) + np.sqrt((u * np.sin(theta))**2 + (2 * y0 * g))) / g
        range = u * np.cos(theta) * t
        hp = u**2 * (np.sin(theta))**2 / (2*g) + y0
        hp_x = (u**2 * np.sin(2*theta) / g) / 2

        x = np.linspace(0, range, 50)
        y = y0 + (x * np.tan(theta) - (g * x**2) / (2 * u**2 * (np.cos(theta))**2))

    ax.scatter(hp_x, hp, color="red", s=0.03*range, label=f"Highest Point ({round(hp_x)}, {round(hp)})")
    ax.scatter(range, 0, color="green", s=0.03*range, label=f"Furthest Point ({round(range)}, 0)")
    ax.axhline(y0, color="black", linewidth=1, linestyle="dashed", alpha=0.4)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_xlabel("Distance (m)", font="Arial", size=12)
    ax.set_ylabel("Height (m)", font="Arial", size=12)
    ax.grid(True, alpha=0.2)

    ax.legend()
    ax.plot(x, y)

    # rounding to 3 sf
    hp = round(hp, 2)
    if len(str(hp)) > 4:
        hp = round(hp, 1)

    range = round(range, 2)
    if len(str(range)) > 4:
        range = round(range, 1)

    t = round(t, 2)
    if len(str(t)) > 4:
        t = round(t, 1)

    # text_var.set(f"Max Height: {hp}m | Range: {range}m | Air time: {t}s")

    ax.set_title((f"Max Height: {hp}m    |    Range: {range}m    |    Air time: {t}s"))

    canvas.draw()

# initialize Tkinter
root = tk.Tk()
root.title("Tkinter x Matplotlib")

fig, ax = plt.subplots(figsize=(9, 5))

ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_xlabel("Distance (m)", font="Arial", size=12)
ax.set_ylabel("Height (m)", font="Arial", size=12)
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

# text_var = tk.StringVar()
# label = tk.Label(frame, textvariable=text_var, font=("Consolas", 18))
# label.pack(anchor="w", pady=10)

scale1 = tk.Scale(frame, from_=0, to=30,
              length=400, font=("Consolas", 12), orient="horizontal", command=graph,
              showvalue=1, resolution=0.01,
              troughcolor="gray", fg ="white", bg="black", label="Gravity (N/kg)")
scale1.set(planets[0][1])

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

scale4 = tk.Scale(frame, from_=0, to=1000,
              length=400, font=("Consolas", 12), orient="horizontal", command=graph,
              showvalue=1, resolution=0.01,
              troughcolor="gray", fg ="white", bg="black", label="Starting Height (m)")

scale4.pack(anchor="w")

x = tk.IntVar()
for i in range(len(planets)):
    radio_button = tk.Radiobutton(frame, variable=x, value=i, text=planets[i][0], padx=15, pady=10,
                                  font=("Consolas", 15), command=set_grav, indicatoron=0)

    radio_button.pack(side="left")

entry1 = tk.Entry(frame, font=("Consolas", 12), width=20)
entry1.insert(0, "0")
entry1.pack(anchor="ne", pady=2)
entry1.bind("<Return>", submit_with_enter)

entry2 = tk.Entry(frame, font=("Consolas", 12), width=20)
entry2.insert(0, "0")
entry2.pack(anchor="ne", pady=2)
entry2.bind("<Return>", submit_with_enter)

entry3 = tk.Entry(frame, font=("Consolas", 12), width=20)
entry3.insert(0, "0")
entry3.pack(anchor="ne", pady=2)
entry3.bind("<Return>", submit_with_enter)

entry4 = tk.Entry(frame, font=("Consolas", 12), width=20)
entry4.insert(0, "0")
entry4.pack(anchor="ne", pady=2)
entry4.bind("<Return>", submit_with_enter)

root.mainloop()

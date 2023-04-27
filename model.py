# Import Tkinter
import matplotlib
matplotlib.use('TkAgg')

# Import modules
import matplotlib.animation as anim
import imageio
import os
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry.get_distance as ge
import tkinter as tk

# Import time
import time

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

# Set the pseudo-random seed for reproducibility
import random
rn = random.random()
print(rn)
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Include the agents list and add an attribute for storing the shares:
def __init__(self, agents, i, environment, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    agents : List
        A list of Agent instances.
    i : Integer
        To be unique to each instance.
    environment : List
        A reference to a shared environment
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.

    Returns
    -------
    None.

    """
    self.agents = agents
    self.i = i
    self.environment = environment
    tnc = int(n_cols / 3)
    self.x = random.randint(tnc - 1, (2 * tnc) - 1)
    tnr = int(n_rows / 3)
    self.y = random.randint(tnr - 1, (2 * tnr) - 1)
    self.store = 0
    self.store_shares = 0

# Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 3

n_iterations = 100

# Initialise agents
agents = []
for i in range(n_iterations):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Move agents
for i in range(n_iterations):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)
    
# Append to the list agents
agents.append([agents[0][0],agents[0][1]])

# Initialise variable x0
agents[0][0] = random.randint(0, 99)
print("agents[0][0]", agents[0][0])

# Initialise variable y0
agents[0][1] = random.randint(0, 99)
print("agents[0][1]", agents[0][1])
agents.append([agents[0][0], agents[0][1]])

# Set the pseudo-random seed for reproducibility
import random
rn = random.random()
print(rn)
random.seed(1)

# Initialise variable x1
x1 = 1
print("x1", x1)

# Initialise variable y1
y1 = 1
print("y1", y1)

# Change x1 and y1 randomly
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
x0 = 0
print("x0", x0)
y0 = 0
print("y0", y0)
x1 = 3
print("x1", x1)
y1 = 4
print("y1", y1)

import matplotlib.pyplot as plt
import operator

# Animate
# Initialise fig and carry_on
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False

# GUI
root = tk.Tk()
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_0 = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=menu_0)
menu_0.add_command(label="Run model", command=lambda: run(canvas))
menu_0.add_command(label="Write data", command=lambda: output())
menu_0.add_command(label="Exit", command=lambda: exiting())
menu_0.entryconfig("Write data", state="disabled")
# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)
tk.mainloop()

def output():
    # Write data
    print("write data")
    io.write_data('../../data/output/out.txt', environment)
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)

# Plot agants code
def plot():
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
global ite
filename = '../../data/output/images/image' + str(ite) + '.png'
plt.savefig(filename)
images.append(imageio.imread(filename))
plt.show()


# Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))


# Set time variable
start = time.perf_counter()

# calculate and report a time interval
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Apply movement constraints.
if agents[i][0] < x_min:
    agents[i][0] = x_min
if agents[i][1] < y_min:
    agents[i][1] = y_min
if agents[i][0] > x_max:
    agents[i][0] = x_max
if agents[i][1] > y_max:
    agents[i][1] = y_max
    
# Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 1
    images = []
    
# Main simulation loop
def update(frames):
    # Model loop
    #for ite in range(1, n_iterations + 1):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))
    
# Define gen_function function
def gen_function():
    global ite
    global carry_on
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Set the Write data menu to normal.
        menu_0.entryconfig("Write data", state="normal")
        data_written = True
        
# Magic command - plot directed to pop-up window
%matplotlib qt

    # Stopping condition
    global carry_on
    # Random
    if random.random() < 0.1:
        #if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    plot()
    
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))
    
# Plot environment
filename = '../../data/output/images/image' + str(ite) + '.png'
#filename = '../../data/output/images/image' + str(ite) + '.gif'
plt.savefig(filename)
plt.show()
plt.close()
images.append(imageio.imread(filename))

# Turn images into animated GIF
imageio.mimsave('../../data/output/out.gif', images, fps=3)

# initialise 'x_max' 
x_max = n_cols - 1
    
# initialise 'y_max' 
y_max = n_rows - 1

# Flip the y-axis
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)

# Initialise Agents
def __init__(self, i, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    i : Integer
        To be unique to each instance.
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.
    Returns
    -------
    None.
    """
    self.i = i
    tnc = int(n_cols / 3)
    self.x = random.randint(tnc - 1, (2 * tnc) - 1)
    tnr = int(n_rows / 3)
    self.y = random.randint(tnr - 1, (2 * tnr) - 1)


# Define Agents
def __init__(self, i, environment, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    i : Integer
    To be unique to each instance.
    environment : List
    A reference to a shared environment
    n_rows : Integer
    The number of rows in environment.
    n_cols : Integer
    The number of columns in environment.

    Returns
    -------
    None.

    """
self.i = i
self.environment = environment
tnc = int(n_cols / 3)
self.x = random.randint(tnc - 1, (2 * tnc) - 1)
tnr = int(n_rows / 3)
self.y = random.randint(tnr - 1, (2 * tnr) - 1)
self.store = 0

# Agent class
def eat(self):
    if self.environment[self.y][self.x] >= 10:
        self.environment[self.y][self.x] -= 10
        self.store += 10
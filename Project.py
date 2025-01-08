import tkinter as tk
import random
import threading
import time

pause_flag = False
running = False
stop_flag = False


######### De aici in jos sunt algoritmii, pe rand, de sortare care pot fi selectati din meniu #########
def bubble_sort(data, draw_data, delay):
    global pause_flag, running, stop_flag
    running = True
    stop_flag = False

    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if stop_flag:
                running = False
                return
            while pause_flag:
                time.sleep(0.1)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw_data(data, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
            time.sleep(delay)

    draw_data(data, ['green' for _ in range(len(data))]) ######### Pentru colorarea barelor.
    running = False


def insertion_sort(data, draw_data, delay):
    global pause_flag, running, stop_flag
    running = True
    stop_flag = False

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            if stop_flag:
                running = False
                return
            while pause_flag:
                time.sleep(0.1)
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ['red' if x == j or x == i else 'blue' for x in range(len(data))])
            time.sleep(delay)
        data[j + 1] = key

    draw_data(data, ['green' for _ in range(len(data))])
    running = False


def selection_sort(data, draw_data, delay):
    global pause_flag, running, stop_flag
    running = True
    stop_flag = False

    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if stop_flag:
                running = False
                return
            while pause_flag:
                time.sleep(0.1)
            if data[j] < data[min_idx]:
                min_idx = j
            draw_data(data, ['red' if x == j or x == min_idx else 'blue' for x in range(len(data))])
            time.sleep(delay) # Pentru asigurarea functionarii corecte a programului , pentru ca altfel nu ar merge foarte bine, dat fiind faptul ca fara asta nu s-ar mai actualiza corect barele.
        data[i], data[min_idx] = data[min_idx], data[i]

    draw_data(data, ['green' for _ in range(len(data))])
    running = False


# Asta e functia pentru afisarea animatiei
def draw_data(data, colors):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 800
    bar_width = canvas_width / len(data)
    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - value
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i], outline="")


def generate_data():
    global data, running, pause_flag, stop_flag
    running = False
    pause_flag = False
    stop_flag = False
    data = [random.randint(10, 400) for _ in range(size_var.get())]
    draw_data(data, ['blue' for _ in range(len(data))])

def start_sorting():
    global running, pause_flag, stop_flag
    if running:
        return
    running = True
    pause_flag = False
    stop_flag = False
    sorting_algorithm = algorithm_menu.get()
    sorting_thread = threading.Thread(target=lambda: {
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort
    }[sorting_algorithm](data, draw_data, speed_var.get()), daemon=True)
    sorting_thread.start()

def pause_sorting():
    global pause_flag
    pause_flag = not pause_flag

def stop_sorting():
    global stop_flag, running, pause_flag
    stop_flag = True
    pause_flag = False
    running = False
    time.sleep(0.1)
    generate_data()

def reset_settings():
    global speed_var, size_var, running, pause_flag, stop_flag
    stop_flag = True
    running = False
    pause_flag = False
    time.sleep(0.1) # Altfel incepe sa flicareasca prea rau
    speed_var.set(0.1)
    size_var.set(50)
    generate_data()


# Prima fereastra
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 700)
root.config(bg="orange")

# Variables
data = []
speed_var = tk.DoubleVar(value=0.1)
size_var = tk.IntVar(value=50)

# De aci-n jos sunt elementele programului/meniului cum vreti sa-i ziceti
ui_frame = tk.Frame(root, width=900, height=300, bg="lightgray")
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = tk.Canvas(root, width=800, height=400, bg="gray")
canvas.grid(row=1, column=0, padx=10, pady=5)

algorithm_menu = tk.StringVar(value='Bubble Sort')
tk.Label(ui_frame, text="Algoritm", bg="lightgray").grid(row=0, column=0)
algorithm_dropdown = tk.OptionMenu(ui_frame, algorithm_menu, 'Sortarea cu Bule (Bubble Sort) ', 'Sortarea prin insertie (Insertion Sort)', 'Sortarea prin selectie (Selection Sort)')
algorithm_dropdown.grid(row=0, column=1)

speed_scale = tk.Scale(ui_frame, from_=0.01, to=10.0, resolution=0.01, orient='horizontal', variable=speed_var,
                       label='Speed')
speed_scale.grid(row=0, column=2)

size_scale = tk.Scale(ui_frame, from_=5, to=1000, resolution=1, orient='horizontal', variable=size_var, label='Size')
size_scale.grid(row=0, column=3)

generate_button = tk.Button(ui_frame, text="Generate", command=generate_data, bg="green")
generate_button.grid(row=1, column=0)
start_button = tk.Button(ui_frame, text="Start", command=start_sorting, bg="blue")
start_button.grid(row=1, column=1)
pause_button = tk.Button(ui_frame, text="Pause/Resume", command=pause_sorting, bg="yellow")
pause_button.grid(row=1, column=2)
stop_button = tk.Button(ui_frame, text="Stop", command=stop_sorting, bg="orange")
stop_button.grid(row=1, column=3)
reset_button = tk.Button(ui_frame, text="Reset", command=reset_settings, bg="purple")
reset_button.grid(row=1, column=4)
exit_button = tk.Button(ui_frame, text="Exit", command=root.quit, bg="red")
exit_button.grid(row=1, column=5)


generate_data()
root.mainloop()
# Generam si incepem programul
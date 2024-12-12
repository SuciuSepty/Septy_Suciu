import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def selection_sort_visual(data, bar_rects, ax):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            for rect, val in zip(bar_rects, data):
                rect.set_color('#00ffff')

            bar_rects[min_idx].set_color('#ffe400')
            bar_rects[j].set_color('#ffe400')

            if data[j] < data[min_idx]:
                min_idx = j

            yield data

        data[i], data[min_idx] = data[min_idx], data[i]
        yield data

def update(frame, data, bar_rects):
    for rect, val in zip(bar_rects, frame):
        rect.set_height(val)

def start_visualization():
    data = [random.randint(1, 1000) for _ in range(15)]
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    fig.patch.set_facecolor('#d1c1ff')
    ax.set_title("Vizualizare rudimentară pentru Sortare prin Selecție")
    bar_rects = ax.bar(range(len(data)), data, color='#00ffff')
    ax.set_facecolor("#ff0080")

    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 100)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=selection_sort_visual(data, bar_rects, ax),
        fargs=(data, bar_rects),
        repeat=False,
        interval=500
    )

    plt.show()

if __name__ == "__main__":
    start_visualization()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort_visual(data, bar_rects, ax):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            for rect, val in zip(bar_rects, data):
                rect.set_color('#00ffff')  # Aici am initializat cu ce culoare sa inceapa
            bar_rects[i - 1].set_color('#ffe400')
            bar_rects[i].set_color('#ffe400')

            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                swapped = True

            yield data

        n -= 1


def update(frame, data, bar_rects):
    for rect, val in zip(bar_rects, frame):
        rect.set_height(val)


def start_visualization():
    data = [random.randint(1, 1000) for _ in range(15)]
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    fig.patch.set_facecolor('#d1c1ff')
    ax.set_title("Vizualizare sortarii")
    bar_rects = ax.bar(range(len(data)), data, color='#00ffff')
    ax.set_facecolor("#ff0080")

    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 100) # Asta e pus aici nu pt c-am vrut eu , ci ca sa arate bine (sa nu fie inghesuit)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=bubble_sort_visual(data, bar_rects, ax),
        fargs=(data, bar_rects),
        repeat=False,
        interval=500
    )

    plt.show()

if __name__ == "__main__":
    start_visualization()

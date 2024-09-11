import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def visualize_quicksort(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='center')

    def update_plot(arr):
        for bar, height in zip(bars, arr):
            bar.set_height(height)
        plt.draw()
        plt.pause(0.2)  

    def quicksort_visualize(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        update_plot(left + middle + right)
      
        quicksort_visualize(left)
        quicksort_visualize(right)
        
        return left + middle + right

    quicksort_visualize(arr)
    plt.title('Quicksort Visualization')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

if __name__ == "__main__":
    data = np.random.randint(0, 100, size=20)
    visualize_quicksort(data.tolist())

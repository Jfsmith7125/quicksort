# Quicksort Visualization with Python

This repository contains a Python implementation of the **Quicksort algorithm** with a live visualization using `matplotlib`. This project aims to demonstrate how Quicksort works by visually sorting an array of random integers, making the process easy to understand.

## Features

- **Quicksort algorithm**: A divide-and-conquer sorting algorithm that recursively sorts elements around a pivot.
- **Visualization**: The algorithm is visualized in real-time using `matplotlib` bar charts, showing the changes in array order as it is sorted.
  
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/quicksort-visualization.git
   cd quicksort-visualization
   ```

2. **Install required libraries:**
   You will need `matplotlib` and `numpy`. Install them with:
   ```bash
   pip install matplotlib numpy
   ```

## Usage

To run the visualization:

```bash
python quicksort_visualization.py
```

This will generate a random array of 20 integers and show the sorting process step by step.

## How It Works

- The array is split into three parts: elements less than the pivot, equal to the pivot, and greater than the pivot.
- The algorithm recursively sorts the left and right subarrays.
- As the sorting occurs, the `matplotlib` bar chart is updated to reflect the current state of the array.

## Example Output

![](screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



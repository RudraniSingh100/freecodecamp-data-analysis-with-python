# Mean-Variance-Standard Deviation Calculator

This project is part of the **freeCodeCamp Data Analysis with Python Certification**.

## Overview

The program accepts a list of **9 numbers**, converts it into a **3 × 3 NumPy matrix**, and computes descriptive statistics for:

- Columns
- Rows
- Entire matrix

## Statistics Calculated

- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

## Technologies Used

- Python 3
- NumPy

## Project Structure

```
mean-variance-standard-deviation-calculator/
│── mean_var_std.py
│── main.py
│── test_module.py
│── README.md
```

## Example

```python
from mean_var_std import calculate

result = calculate([0,1,2,3,4,5,6,7,8])

print(result)
```

## Output

```python
{
'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
'max': [[6,7,8],[2,5,8],8],
'min': [[0,1,2],[0,3,6],0],
'sum': [[9,12,15],[3,12,21],36]
}
```

## How to Run

Install NumPy:

```bash
pip install numpy
```

Run the project:

```bash
python main.py
```

Run the tests:

```bash
python test_module.py
```

## Author

**Rudrani**

Completed as part of the freeCodeCamp Data Analysis with Python certification.

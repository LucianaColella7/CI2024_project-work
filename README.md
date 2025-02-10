# Computational Intelligence Project

This project implements symbolic regression, a type of regression analysis that searches for mathematical expressions that best fit a given dataset.
For detailed information about the project see the Report.pdf file.
    
## Project Structure

- `data/`: Contains the datasets used for testing.
- `results/`: Directory to store the results obtained
- `src/`: Contains the source code and notebooks for the project
  - `sym_reg.ipynb`: Jupyter notebook implementing the symbolic regression algorithm.
- `s328092.py`: Script that shows the best mathematical expressions found
- `Report.pdf`: Report about the implementation details


## Results
In the following, the outcomes found for each problem can be observed:
| Problem | X            | y           | Variables                        | Best Fitness              |
|----------|--------------|-------------|----------------------------------|---------------------------|
| P1       | (1, 500)     | (500,)      | ['x0']                           | 0.0                       |
| P2       | (3, 5000)    | (5000,)     | ['x0', 'x1', 'x2']              | 2.9255618201714156e+13     |
| P3       | (3, 5000)    | (5000,)     | ['x0', 'x1', 'x2']              | 1858.2448027781834        |
| P4       | (2, 5000)    | (5000,)     | ['x0', 'x1']                    | 14.074100713713625        |
| P5       | (2, 5000)    | (5000,)     | ['x0', 'x1']                    | 5.572810232617333e-18      |
| P6       | (2, 5000)    | (5000,)     | ['x0', 'x1']                    | 2.5346321229997786        |
| P7       | (2, 5000)    | (5000,)     | ['x0', 'x1']                    | 357.52091727544365        |
| P8       | (6, 50000)   | (50000,)    | ['x0', 'x1', 'x2', 'x3', 'x4', 'x5'] | 1.6107278993818918e+07     |



## Author's note
All the implementations of this project have been develop by me, giving my personal understanding and approach to the task.
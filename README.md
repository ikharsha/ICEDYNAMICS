# ICEDynamics Prediction
A Numerical Study on optimum prediction algorithm for performance of internal combustion engine using various Correlation algorithms.



This repository contains code for various regression algorithms applied to the "ICEDYNAMICS" project. The goal of this project is to predict target variables based on input features using different regression techniques. The regression algorithms used in this project include Linear Regression, Support Vector Regression (SVR), Bayesian Ridge Regression, and Lasso Regression.

## Getting Started

These instructions will help you set up the project on your local machine and run the correlation algorithms.

### Prerequisites

- Python (>=3.6)
- Jupyter Notebook or any Python IDE

### Installing

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ICEDYNAMICS.git
```

2. Navigate to the project directory:

```bash
cd ICEDYNAMICS
```

3. Install the required Python packages:

```bash
pip install pandas scikit-learn
```

3. Run the python Script

```bash
python correation_algorithms.py
```

### Usage

1. Place your training data in a CSV file named `Train_data.csv` within the project directory.

2. Open a Jupyter Notebook or your preferred Python IDE.

3. Open and run the `correlation_algorithms.py ` notebook. This notebook contains code to apply different regression algorithms on the dataset and generate algebraic equations for the target variables._

### Algorithms

- Linear Regression: Uses the `LinearRegression` class from scikit-learn to perform linear regression.
- SVR: Utilizes the `SVR` class from scikit-learn with a linear kernel for support vector regression.
- Bayesian Ridge Regression: Implements the Bayesian Ridge Regression algorithm using the `BayesianRidge` class.
- Lasso Regression: Applies Lasso Regression using the `Lasso` class.

## Results

The algebraic equations generated by each regression algorithm for the target variables are displayed in the notebook's output.

## Contributing

Contributions are welcome! If you have suggestions or find issues with the code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [scikit-learn](https://scikit-learn.org/): Machine learning library used for regression algorithms.
- [Pandas](https://pandas.pydata.org/): Data manipulation library used for handling the dataset.



# all of the imports needed for linear regression math
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# needed for plotting
import matplotlib.pyplot as plt

# needed for numpy arrays
import numpy as np

# needed to calculate the mean of a list
from statistics import mean

def generate_coefficients():
    # creates a uniform list of coeffecients from -0.5 to 0.5
    return np.random.uniform(-0.5, 0.5, 5)

def generate_data(m, coefs):
    # creates m evenly distributed x values between -5 and 5
    x_values = np.linspace(start = -5, stop = 5, num = m).reshape(-1, 1)
    y_values = np.array([])
    
    # creates y values based on the x values and the formula given
    y_values = coefs[0] + (coefs[1] * x_values) + (coefs[2] * (x_values ** 2)) + (coefs[3] * (x_values ** 3)) + (coefs[4] * (x_values ** 4)) + np.random.randn()

    return x_values, y_values

def fit_curve(X, y, degree):
    # creates polynomial features to create the linear regression model
    poly_features = PolynomialFeatures(degree, include_bias = False)
    X_poly = poly_features.fit_transform(X)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    
    return lin_reg

def plot_curve(degree, model):
    # have to recreate poly_features
    poly_features = PolynomialFeatures(degree, include_bias = False)
    
    # get x values again
    X = np.linspace(start = -5, stop = 5, num = 100).reshape(-1, 1)
    X_poly = poly_features.fit_transform(X)

    # get y values from these x values and the linear regression model
    Y = model.predict(X_poly)

    # plot it
    plt.plot(X, Y)

def plot_data(X, y):
    # copy and pasted from Peter
    plt.ylim((y.min() - 0.1 * (y.max() - y.min()),
    y.max() + 0.1 * (y.max() - y.min())))
    plt.scatter(X, y)

def experiment_1(m):
    # copy and pasted from Peter
    coeffs = generate_coefficients()
    X, y = generate_data(m, coeffs)
    plot_data(X, y)
    for d in [1, 2, 20]:
        model = fit_curve(X, y, d)
        plot_curve(d, model)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def mse(X, y, degree, model):
    # recreate poly_features and X_poly to predict the Y value for this x value
    poly_features = PolynomialFeatures(degree, include_bias=False)
    X_poly = poly_features.fit_transform(X)

    Y = model.predict(X_poly)

    # calculate MSE from tested Y and approximate Y
    return mean_squared_error(y, Y)

def experiment_2(m):
    # copy and pasted from Peter
    mses = {i : [] for i in range(1, 31)}
    for i in range(100):
        coeffs = generate_coefficients()
        X_train, y_train = generate_data(m, coeffs)
        X_test, y_test = generate_data(100, coeffs)
        for d in range(1, 31):
            model = fit_curve(X_train, y_train, d)
            mses[d] += [mse(X_test, y_test, d, model)] 
    averages = [mean(mses[d]) for d in mses]
    plt.ylim(0, 500)
    plt.plot(range(1, 31), averages)
    plt.xlabel('Degree')
    plt.ylabel('Average MSE (100 runs)')
    plt.show()


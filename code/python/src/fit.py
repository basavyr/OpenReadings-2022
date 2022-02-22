from scipy.optimzie import curve_fit


def data_fit(model_function, x_data, y_data, p0, parameter_bounds):
    """
    - finds the best parameter such that the model function describes the data (experimental)
    - p0 -> initial guess for the params
    - parameter_bounds -> set fixed bounds for each parameter, such that the fitting algorithm uses only those limits
    """

    return 1

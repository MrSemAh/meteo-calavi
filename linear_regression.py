from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


def linear_regression(dataset, x_columns, y_column="next_day_temperature_max"):
    dataset = dataset.dropna()
    X = dataset[x_columns]
    y = dataset[y_column]
    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    return predictions, mean_absolute_error(y, predictions)

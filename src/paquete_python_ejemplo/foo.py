def foo(bar: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """
    print(bar)

    return bar

def preprocess_data(data: str) -> str:
    data=data.strip()
    return data.lower()

def train_random_forest(X, y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


if __name__ == "__main__":  # pragma: no cover
    foo("Hello world")

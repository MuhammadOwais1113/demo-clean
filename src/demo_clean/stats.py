import statistics


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return float(statistics.fmean(values))


def normalize(values: list[float]) -> list[float]:
    if not values:
        raise ValueError("values must not be empty")
    low, high = min(values), max(values)
    if low == high:
        return [0.0 for _ in values]
    return [(v - low) / (high - low) for v in values]

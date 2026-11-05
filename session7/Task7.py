def calculate_risk_score(data_points, sensitivity):

    """
    Calculate the risk score.

    Parameters
    ----------
    data_points : array-like
        List or tuple containing numerical data points.

    sensitivity : float
        Sensitivity multiplier used to calculate risk.

    Returns
    -------
    float
        Calculated risk score.
    """

    total = sum(data_points)

    average = total / len(data_points)

    risk_score = average * sensitivity

    return risk_score


print("\n--- Task 7: Risk Score ---")

data = [10, 20, 30, 40]

risk = calculate_risk_score(data, 1.5)

print("Data Points:", data)
print("Sensitivity:", 1.5)
print("Risk Score:", risk)
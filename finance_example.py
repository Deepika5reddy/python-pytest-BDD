import pandas as pd
import numpy as np
from scipy import stats


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Chicago", "San Francisco"]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])


# Expected tax values (from spec or CSV)
expected = np.array([100.0, 200.0, 300.0])

# Actual values returned by an API (with small rounding differences)
actual = np.array([100.00001, 199.99999, 300.0001])

# Use assert_allclose to validate within a tolerance
np.testing.assert_allclose(actual, expected, rtol=1e-4)

print("All values are close enough – test passed ✅")

# Sample activity scores: current vs. last month
current_scores = [89, 90, 92, 88, 87, 91, 90]
last_month_scores = [88, 89, 90, 87, 88, 89, 90]

# Perform a t-test to compare both samples
t_stat, p_value = stats.ttest_ind(current_scores, last_month_scores)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Typically, if p-value > 0.05, the data sets are not significantly different
if p_value > 0.05:
    print("✅ The datasets are statistically similar.")
else:
    print("❌ The datasets are significantly different.")

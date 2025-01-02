import pandas as pd
import numpy as np

# Membuat dummy dataset
np.random.seed(42)
data = pd.DataFrame({
    'CustomerID': range(1, 501),
    'Age': np.random.randint(18, 65, 500),
    'Annual Income (k$)': np.random.randint(15, 150, 500),
    'Spending Score (1-100)': np.random.randint(1, 100, 500)
})

# Simpan dataset ke file CSV
data.to_csv('dummy_dataset.csv', index=False)



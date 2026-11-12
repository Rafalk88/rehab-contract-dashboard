import numpy as np
import pandas as pd
import config

rng = np.random.default_rng(config.SEED)
n = config.PATIENTS_NUMBER

patients = pd.DataFrame({
    "id": range(1, n + 1),
    "age_group": rng.choice(["child", "adult"], size=n, p=[config.CHILDREN_PERCENTAGE, 1 - config.CHILDREN_PERCENTAGE]),
    "sex": rng.choice(["M", "F"], size=n),
})

patients.to_csv("data/patients.csv", index=False)
print(f"Generated {n} patients and saved to data/patients.csv")
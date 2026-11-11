import numpy as np
import pandas as pd
import config

rng = np.random.default_rng(config.SEED)
n = config.LICZBA_PACJENTOW

patients = pd.DataFrame({
    "id": range(1, n + 1),
    "grupa_wiekowa": rng.choice(["dziecko", "dorosły"], size=n, p=[config.KIDS_PERCENTAGE, 1 - config.KIDS_PERCENTAGE]),
    "plec": rng.choice(["M", "K"], size=n),
})

patients.to_csv("data/patients.csv", index=False)
print(f"Generated {n} patients and saved to data/patients.csv")
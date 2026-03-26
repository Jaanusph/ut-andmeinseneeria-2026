import pandas as pd
import numpy as np

# 1. Koostame testandmed (simuleerime ERP süsteemi vigast sisendit)
data = {
    'masina_id': ['  M1  ', 'M2', '  M1', 'M3 '],
    'tsükli_aeg': ['12.5', '14.2', 'viga', '11.8'],
    'mõõdetud_väärtus': [100, np.nan, 105, 98]
}

df = pd.DataFrame(data).copy()

# 2. Robustne puhastus (Eemaldame tühikud)
df['masina_id'] = df['masina_id'].str.strip()

# 3. Turvaline tüübikontroll
df['tsükli_aeg'] = pd.to_numeric(df['tsükli_aeg'], errors='coerce')

# 4. Imputeeri puuduvad väärtused keskmisega (Protsessiinseneri loogika)
avg_cycle = df['tsükli_aeg'].mean()
df['tsükli_aeg'] = df['tsükli_aeg'].fillna(avg_cycle)

print("--- Andmetöötluse kontroll ---")
print(df)
print("\n--- Süsteemi info ---")
df.info()
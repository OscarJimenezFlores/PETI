import pandas as pd

df = pd.read_csv("MP04_articulacion.csv")

total = len(df)

print("=== CALIDAD DE LA ARTICULACIÓN PEI-PGD ===")
print(f"Total de objetivos del PGD analizados: {total}")

for columna in [
    "¿Declara articulación con el PEI?",
    "¿La articulación es verificable en el texto?",
    "¿Tiene indicador?",
    "¿Tiene línea base?",
    "¿Tiene meta anual?"
]:
    cantidad = (df[columna].astype(str).str.strip().str.lower() == "sí").sum()
    porcentaje = (cantidad / total) * 100
    print(f"{columna}: {cantidad}/{total} ({porcentaje:.1f}%)")
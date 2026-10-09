import pandas as pd

# Cria exemplo bagunçado
dados = {"Nome": ["Ana", "João", None, "Marta", "Ana"], "Valor": [100, None, 200, 300, 100]}
df = pd.DataFrame(dados)

print("ANTES:")
print(df)

# Limpa tudo: vazios + duplicados
tabela_limpa = df.dropna().drop_duplicates()

print("\nDEPOIS - Limpa e organizada:")
print(tabela_limpa)
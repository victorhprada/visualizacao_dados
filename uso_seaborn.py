import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # ['scatter', 'hist', 'hex', 'kde', 'reg', 'resid']
# plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de slários')
plt.xlabel('Salário')
# plt.show()

# Gráfico de Pairplt - Dispersão e Histograma
plt.figure(figsize=(10, 6))
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
# plt.show()

# Gráfico de Regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
# plt.show()

# Gráfico countplot com hue
plt.figure(figsize=(10, 6))
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nivel de Educação')
plt.show()
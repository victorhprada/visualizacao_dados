import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Documentação para tipos de gráfiocs .plot() https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70') # plot para visualizar valores, value_counts para contar a frequência de cada valor único
plt.title('Divisão de Escolariedade - 1')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0) # Rotação do eixo x em graus
# plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65') # Faz a mesma coisa que -> df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
# plt.show()

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
# plt.show()

# Gráfico de Dispersão
plt.figure(figsize=(10, 6))
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

# Criar gráfico de pizza
# plt.figure(figsize=(8, 8))
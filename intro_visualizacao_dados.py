import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
#plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10,6)) # Tamanho da imagem
plt.hist(df['salario'], bins=100, color='green', alpha=0.8) # bins define o númeo de intervalos no histograma, alpha define a opacidade das barras do histograma
plt.title('Histograma - Distribuição de Salário')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000)) # o eixo x vai de 0 (zero) até o máximo com intervalos de 2000
plt.ylabel('Frquência')
plt.grid(True)
# plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10,6))
plt.subplot(2, 2, 1) # 2 Linha, 2 Colunas, 1 (Primeiro) Gráfico

# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario']) # Scatter faz a correlação de salário e salário
plt.title('Dispersão - Salário e Salário') 
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1, 2, 2) # 1 Linha, 2 Colunas, 2 (Segundo) Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], colorizer='#5883a8', alpha=0.6, s=30) # Scatter faz a correlação de salário e anos_experiencia
plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')
# plt.show()

# Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr() # Correlação entre salário e anos de experiencia
plt.subplot(2, 2, 3) # 1 Linha, 2 Coluna, 3 (terceiro) Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.show()
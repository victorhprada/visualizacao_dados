import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')

print(df.head().to_string())

# Análise de desempenho do produto

# Tratamento de dados
print(df.dtypes)
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce') # Transformar a coluna em númerico
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].fillna(0) # Substituir NaN por 0 (zero)
# df['Marca'] = df['Marca'].astype('category').cat.codes # Converte marcas para códigos
marca_mapping = dict(enumerate(df['Marca'].astype('category').cat.categories)) # Criar o mapeamento de código para nome, corrigindo o que foi feito na linha de cima


# Melhores produtos
best_product = df.sort_values(by='Nota', ascending=False)
print(best_product[['Título', 'Nota', 'N_Avaliações']].head())

best_10_product = best_product.head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=best_10_product, x='Nota', y='Título', palette='viridis') # Visualização em barra
plt.title('Top 10 produtos com as melhores notas')
plt.xlabel('Nota')
plt.ylabel('Título')
# plt.show()

# # Notas x Número de avaliações dos 100 produtos mais vendidos
top_sell = df.nlargest(100, 'Qtd_Vendidos')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=top_sell, 
                x='N_Avaliações',
                y='Nota',
                palette='cool',
                size='Qtd_Vendidos', # Tamanho do ponto baseado na qtd de venda
                sizes=(20, 200)
                )
plt.title('Notas x Número de Avaliações dos 100 produtos mais vendidos')
plt.xlabel('Número de Avaliações')
plt.ylabel('Notas')
plt.tight_layout()
plt.show()

# Piores 10 produtos
worse_product = df.sort_values(by='Nota', ascending=True)

worse_10_product = worse_product.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(
    data=worse_10_product,
    x='Nota',
    y='Título',
    color='#FF5733'
)
plt.title('Top 10 produtos com as piores notas')
plt.xlabel('Nota')
plt.ylabel('Título')
plt.show()

# Os 10 produtos com maior desconto
descont_product = df.sort_values(by='Desconto', ascending=False)
descont_10_product = descont_product.head(10)


plt.figure(figsize=(12, 6))
sns.barplot(
    data=descont_10_product,
    x='Desconto',
    y='Título',
    color='#4682b4'
    )
plt.title('Top 10 produtos com maior desconto')
plt.xlabel('Desconto (%)')
plt.ylabel('Título')
plt.show()

sns.scatterplot(
    data=descont_10_product,
    x='Desconto',
    y='Qtd_Vendidos',
    size='Preço',
    palette='green',
    sizes=(50, 200)
)
plt.title('Impacto do desconto nas vendas')
plt.xlabel('Desconto (%)')
plt.ylabel('Quantidade de vendas')
plt.show()

# Apresentar as 10 marcas com maior frequência de vendas
top_10_marks = df['Marca'].value_counts().head(10)


x = top_10_marks.index
y = top_10_marks.values

print(f"\n Começa X: {x}")
print(f"\n Começa Y: {y}")
plt.figure(figsize=(10, 6))
plt.pie(
    y,
    labels=x,
    autopct='%.1f%%',
    startangle=90
)
plt.title('Distribuição de Marca')
plt.show()

# Frequência cruzada para apresentar a frequência de produtos combinando Marca e Genêro
cross_df = pd.crosstab(df['Marca'], df['Gênero']).head(5)

sns.heatmap(
    cross_df,
    annot=True,
    cmap='coolwarm',
    fmt='d'
)

plt.title('Frequência cruzada entre marca e gênero')
plt.xlabel('Gênero')
plt.ylabel('Marca')
plt.show()
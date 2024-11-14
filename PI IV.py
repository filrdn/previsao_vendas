import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Passo 1: Carregar os dados
df = pd.read_excel("C:\\Users\\filrd\\Downloads\\Livro caixa 23-24.xlsx")

# Passo 2: Verificar os tipos de dados e valores ausentes
print("\nTipos de dados das colunas:")
print(df.dtypes)

# Verificar se existem valores ausentes
print("\nValores ausentes nas colunas:")
print(df.isnull().sum())

# Passo 3: Limpeza e Pré-processamento
# Remover vírgulas e converter para float a coluna 'Pago'
if 'Pago' in df.columns:
    df['Pago'] = df['Pago'].replace({',': '.'}, regex=True).astype(float)
else:
    print("Coluna 'Pago' não encontrada!")

# Converter a coluna 'Data' para um formato numérico (exemplo: número de dias desde a data mínima)
if 'Data' in df.columns:
    df['Data'] = pd.to_datetime(df['Data'], format='%d-%m-%Y', errors='coerce')
    df['Dias Desde Referencia'] = (df['Data'] - df['Data'].min()).dt.days
else:
    print("Coluna 'Data' não encontrada!")

# Codificar a coluna 'Notas' (marca) usando a codificação one-hot
if 'Notas' in df.columns:
    df = pd.get_dummies(df, columns=['Notas'], drop_first=True)
else:
    print("Coluna 'Notas' não encontrada!")

# Remover linhas com valores ausentes em 'Recebido' ou 'Pago'
df = df.dropna(subset=['Recebido', 'Pago'])

# Remover a coluna 'Contas' pois ela contém texto e não pode ser usada diretamente no modelo
df = df.drop(columns=['Contas'], errors='ignore')

# Verificar novamente os dados após a limpeza
print("\nPrimeiras linhas após a limpeza:")
print(df.head())

# Passo 4: Seleção de Recursos (Features) e Variável-Alvo
if 'Recebido' in df.columns:
    X = df.drop(columns=['Recebido', 'Data'], errors='ignore')  # Remover 'Recebido' e 'Data' de X
    y = df['Recebido']
else:
    print("Coluna 'Recebido' não encontrada!")

# Verificar se todas as colunas em X são numéricas
print("\nTipos de dados das colunas em X após a remoção de 'Data':")
print(X.dtypes)

# Passo 5: Dividir os Dados em Conjuntos de Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nConjunto de treino e teste criado com sucesso.")

# Passo 6: Treinar o Modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModelo treinado com sucesso.")

# Passo 7: Fazer Previsões
predictions = model.predict(X_test)
print("\nPrimeiras previsões:")
print(predictions[:5])

# Passo 8: Avaliar o Modelo
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions, squared=False)

print("\nAvaliação do modelo:")
print(f"MAE (Erro Médio Absoluto): {mae}")
print(f"MSE (Erro Médio Quadrado): {mse}")
print(f"RMSE (Raiz do Erro Médio Quadrado): {rmse}")

# Passo 9: Exportar Resultados
result_df = pd.DataFrame({'Real': y_test, 'Previsto': predictions})
result_df.to_excel("resultados_previsao_vendas.xlsx", index=False)
print("\nResultados exportados para 'resultados_previsao_vendas.xlsx'")

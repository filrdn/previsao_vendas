Previsão de Vendas
Este projeto realiza a previsão de vendas com base em dados históricos, utilizando um modelo de aprendizado de máquina para estimar os valores de vendas futuras. O código foi desenvolvido em Python e utiliza bibliotecas como Pandas, Scikit-Learn e Matplotlib para manipulação de dados, treinamento de modelos e visualização dos resultados.

Tecnologias Usadas
Python 3.x
Pandas
Scikit-Learn
Matplotlib
OpenPyXL (para exportar os resultados)
Requisitos
Antes de rodar o código, é necessário instalar algumas dependências. Para isso, você pode utilizar um ambiente virtual, o que facilita o gerenciamento de pacotes e evita conflitos com outras versões de pacotes no seu sistema.

Passo 1: Instalando o Python
Se você ainda não tem o Python instalado, pode baixá-lo e instalá-lo a partir do site oficial:

Python.org

Verifique se a instalação foi bem-sucedida com o comando:

bash
Copy code
python --version
Passo 2: Criando e Ativando um Ambiente Virtual
Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. Abra o terminal ou Git Bash e siga os passos:

Criar o ambiente virtual:

bash
Copy code
python -m venv venv
Ativar o ambiente virtual:

No Windows (Git Bash):
bash
Copy code
source venv/Scripts/activate
No macOS/Linux:
bash
Copy code
source venv/bin/activate
Passo 3: Instalando as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o pip:

bash
Copy code
pip install -r requirements.txt
Se você não tiver o arquivo requirements.txt, pode instalar as bibliotecas manualmente:

bash
Copy code
pip install pandas scikit-learn matplotlib openpyxl
Passo 4: Rodando o Código
Com as dependências instaladas, o próximo passo é rodar o código. Se você já tem os arquivos necessários (como a planilha de dados), basta executar o script Python:

bash
Copy code
python "PI IV.py"
Esse comando vai executar o modelo, fazer as previsões e salvar os resultados na planilha resultados_previsao_vendas.xlsx.

Estrutura do Projeto
A estrutura do projeto é a seguinte:

bash
Copy code
previsao_vendas/
├── PI IV.py                   # Código principal
├── dados/                      # Pasta para armazenar os dados de entrada (caso tenha)
├── resultados_previsao_vendas.xlsx  # Planilha com os resultados gerados
└── requirements.txt            # Dependências do projeto (caso você queira incluir)
Explicação do Código
Carregamento e Limpeza dos Dados: O código começa carregando os dados de vendas históricos e realiza a limpeza, tratando valores ausentes e transformando dados categóricos.

Divisão dos Dados: O conjunto de dados é dividido em dois conjuntos: treino e teste. O modelo será treinado no conjunto de treino e avaliado no conjunto de teste.

Criação do Modelo: Utilizamos o modelo de regressão linear do Scikit-learn para prever os valores de vendas.

Avaliação do Modelo: O modelo é avaliado usando métricas como MAE (Erro Médio Absoluto), MSE (Erro Médio Quadrado) e RMSE (Raiz do Erro Médio Quadrado).

Exportação dos Resultados: O resultado das previsões é exportado para a planilha resultados_previsao_vendas.xlsx.

Resultados Esperados
Após executar o código, a planilha resultados_previsao_vendas.xlsx será gerada com as previsões de vendas. As métricas de avaliação do modelo também serão exibidas no terminal.

Exemplo de saída no terminal:

arduino
Copy code
MAE (Erro Médio Absoluto): 113.95
MSE (Erro Médio Quadrado): 21343.76
RMSE (Raiz do Erro Médio Quadrado): 146.10

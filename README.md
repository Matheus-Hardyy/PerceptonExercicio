Perceptron Exercício
Autores: Matheus Hardy e Vinícius Henryky

Descrição do Projeto
Implementação do algoritmo Perceptron para classificar se um aluno passou ou não com base em duas características:

Estudou (Não=0, Sim=1)

Fez o trabalho (Não=0, Sim=1)

Algoritmo do Perceptron
O perceptron segue as seguintes etapas:

Inicialização: Pesos iniciais são definidos

Para cada época:

Para cada exemplo de treinamento (x, y):

Calcular predição: ŷ = f(w·x + b)

Se ŷ ≠ y:

Atualizar pesos: w = w + α(y - ŷ)x

Atualizar bias: b = b + α(y - ŷ)

Configuração do Exercício
Problema: Classificação de alunos (passou/não passou)

Base de dados:

Aluno	Estudou	Fez trabalho	Passou
Joãozinho	0	0	0
Huguinho	0	1	0
Zezinho	1	0	1
Luizinho	1	1	1
Parâmetros:

Pesos iniciais: [0.0, 0.0]

Bias inicial: 0.0

Taxa de aprendizagem (α): 0.1

Número de épocas: 2

Estrutura do Projeto
text
perceptron-exercicio/
│
├── perceptron.py          # Implementação do algoritmo
├── exercicio_aula.py      # Teste com o exercício da aula
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
Como Executar
bash
# Instalar dependências (se houver)
pip install -r requirements.txt

# Executar o exemplo da aula
python exercicio_aula.py
Resultados
O algoritmo foi testado com 2 épocas completas e convergiu para uma solução que classifica corretamente todos os exemplos da base de dados.

Estado Final
Pesos finais: [0.2, 0.0]

Bias final: -0.1

Acurácia: 100%

Tecnologias Utilizadas
Python 3.x

NumPy

Licença
Este projeto é para fins educacionais.



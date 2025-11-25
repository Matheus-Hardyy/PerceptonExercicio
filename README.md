# PerceptonExercicio
Matheus Hardyy e VinÃ­cius Henrykyy

# ImplementaÃ§Ã£o do Perceptron

## DescriÃ§Ã£o
ImplementaÃ§Ã£o do algoritmo Perceptron para classificar se um aluno passou ou nÃ£o com base em duas caracterÃ­sticas:

Estudou (NÃ£o=0, Sim=1)

Fez o trabalho (NÃ£o=0, Sim=1)

## Algoritmo
O perceptron segue as seguintes etapas:

1. **InicializaÃ§Ã£o**: Pesos iniciais sÃ£o definidos
2. **Para cada Ã©poca**:
   - Para cada exemplo de treinamento (x, y):
      - Calcular prediÃ§Ã£o: Å· = f(wÂ·x + b)
         - Se Å· â‰  y:
              - Atualizar pesos: w = w + Î±(y - Å·)x
                   - Atualizar bias: b = b + Î±(y - Å·)

                   ## Teste com ExercÃ­cio PrÃ¡tico da Aula

                   ### ConfiguraÃ§Ã£o
                   - **Problema**: Porta lÃ³gica AND
                   - **Dados de treinamento**:
                     
                     Aluno	Estudou	Fez trabalho	Passou
                     JoÃ£ozinho	NÃ£o (0)	NÃ£o (0)	NÃ£o (0)
                     Huguinho	NÃ£o (0)	Sim (1)	NÃ£o (0)
                     Zezinho	Sim (1)	NÃ£o (0)	Sim (1)
                     Luizinho	Sim (1)	Sim (1)	Sim (1)
                           - **ParÃ¢metros**:
                             Pesos iniciais: [0.0, 0.0]

                             Bias inicial: 0.0

                             Taxa de aprendizagem (Î±): 0.1

                             NÃºmero de iteraÃ§Ãµes: 2 Ã©pocas completas

                                 ### Resultados do Treinamento

=== TREINAMENTO DO PERCEPTRON ===
Base de dados:
Estudou | Trabalho | Passou
   0    |    0     |    0
      0    |    1     |    0
         1    |    0     |    1
            1    |    1     |    1

            Pesos iniciais: [0. 0.], Bias: 0.0
            Taxa de aprendizagem: 0.1
            ============================================================

            --- Ã‰POCA 1 ---

            Exemplo 1: x=[0 0], y=0, Å·=1
            Erro: -1
            Î”pesos = Î± * erro * x = 0.1 * -1 * [0 0]
            Pesos anterior: [0. 0.]
            Pesos atualizado: [0. 0.]
            Bias anterior: 0.0
            Bias atualizado: -0.1

            Exemplo 2: x=[0 1], y=0, Å·=1
            Erro: -1
            Î”pesos = Î± * erro * x = 0.1 * -1 * [0 1]
            Pesos anterior: [0. 0.]
            Pesos atualizado: [ 0.  -0.1]
            Bias anterior: -0.1
            Bias atualizado: -0.2

            Exemplo 3: x=[1 0], y=1, Å·=0
            Erro: 1
            Î”pesos = Î± * erro * x = 0.1 * 1 * [1 0]
            Pesos anterior: [ 0.  -0.1]
            Pesos atualizado: [ 0.1 -0.1]
            Bias anterior: -0.2
            Bias atualizado: -0.1

            Exemplo 4: x=[1 1], y=1, Å·=0
            Erro: 1
            Î”pesos = Î± * erro * x = 0.1 * 1 * [1 1]
            Pesos anterior: [ 0.1 -0.1]
            Pesos atualizado: [0.2 0. ]
            Bias anterior: -0.1
            Bias atualizado: 0.0

            --- Ã‰POCA 2 ---

            Exemplo 1: x=[0 0], y=0, Å·=1
            Erro: -1
            Î”pesos = Î± * erro * x = 0.1 * -1 * [0 0]
            Pesos anterior: [0.2 0. ]
            Pesos atualizado: [0.2 0. ]
            Bias anterior: 0.0
            Bias atualizado: -0.1

            Exemplo 2: x=[0 1], y=0, Å·=0 âœ“ (sem atualizaÃ§Ã£o)

            Exemplo 3: x=[1 0], y=1, Å·=1 âœ“ (sem atualizaÃ§Ã£o)

            Exemplo 4: x=[1 1], y=1, Å·=1 âœ“ (sem atualizaÃ§Ã£o)

            ================================================================================
            RELATÃ“RIO COMPLETO DO TREINAMENTO
            ================================================================================

            Estado 0: Estado inicial
            Pesos: [0. 0.], Bias: 0.0

            Estado 1: Ã‰poca 1, Exemplo 1
            Entrada: [0 0], y_real: 0, y_pred: 1
            Erro: -1
            Pesos anterior: [0. 0.]
            Pesos atualizado: [0. 0.]
            Bias anterior: 0.0
            Bias atualizado: -0.1

            Estado 2: Ã‰poca 1, Exemplo 2
            Entrada: [0 1], y_real: 0, y_pred: 1
            Erro: -1
            Pesos anterior: [0. 0.]
            Pesos atualizado: [ 0.  -0.1]
            Bias anterior: -0.1
            Bias atualizado: -0.2

            Estado 3: Ã‰poca 1, Exemplo 3
            Entrada: [1 0], y_real: 1, y_pred: 0
            Erro: 1
            Pesos anterior: [ 0.  -0.1]
            Pesos atualizado: [ 0.1 -0.1]
            Bias anterior: -0.2
            Bias atualizado: -0.1

            Estado 4: Ã‰poca 1, Exemplo 4
            Entrada: [1 1], y_real: 1, y_pred: 0
            Erro: 1
            Pesos anterior: [ 0.1 -0.1]
            Pesos atualizado: [0.2 0. ]
            Bias anterior: -0.1
            Bias atualizado: 0.0

            Estado 5: Ã‰poca 2, Exemplo 1
            Entrada: [0 0], y_real: 0, y_pred: 1
            Erro: -1
            Pesos anterior: [0.2 0. ]
            Pesos atualizado: [0.2 0. ]
            Bias anterior: 0.0
            Bias atualizado: -0.1

            ==================================================
            TESTE FINAL
            ==================================================
            JoÃ£ozinho  | Estudou: 0 | Trabalho: 0 | Passou: 0 | Predito: 0 âœ“
            Huguinho   | Estudou: 0 | Trabalho: 1 | Passou: 0 | Predito: 0 âœ“
            Zezinho    | Estudou: 1 | Trabalho: 0 | Passou: 1 | Predito: 1 âœ“
            Luizinho   | Estudou: 1 | Trabalho: 1 | Passou: 1 | Predito: 1 âœ“

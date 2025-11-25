import numpy as np

class Perceptron:
    def __init__(self, taxa_aprendizagem=0.1, max_epocas=2):
        self.taxa_aprendizagem = taxa_aprendizagem
        self.max_epocas = max_epocas
        self.pesos = None
        self.bias = None
        self.historico = []
        
    def funcao_ativacao(self, x):
        return 1 if x >= 0 else 0
    
    def prever(self, x):
        soma_ponderada = np.dot(x, self.pesos) + self.bias
        return self.funcao_ativacao(soma_ponderada)
    
    def treinar(self, X, y):
        n_exemplos, n_caracteristicas = X.shape
        
        # Inicializa pesos e bias conforme exercício (todos 0)
        self.pesos = np.zeros(n_caracteristicas)
        self.bias = 0.0
        
        print("=== TREINAMENTO DO PERCEPTRON ===")
        print("Base de dados:")
        print("Estudou | Trabalho | Passou")
        for i in range(len(X)):
            print(f"   {X[i][0]}    |    {X[i][1]}     |    {y[i]}")
        print(f"\nPesos iniciais: {self.pesos}, Bias: {self.bias}")
        print(f"Taxa de aprendizagem: {self.taxa_aprendizagem}")
        print("=" * 60)
        
        # Codificação: Não=0, Sim=1
        self.historico.append({
            'epoca': 0,
            'pesos': self.pesos.copy(),
            'bias': self.bias,
            'descricao': 'Estado inicial'
        })
        
        for epoca in range(self.max_epocas):
            print(f"\n--- ÉPOCA {epoca + 1} ---")
            erro_epoca = False
            
            for i in range(n_exemplos):
                # Predição atual
                predicao = self.prever(X[i])
                erro = y[i] - predicao
                
                if erro != 0:
                    erro_epoca = True
                    
                    # Salva estado antes da atualização
                    estado_anterior = {
                        'pesos': self.pesos.copy(),
                        'bias': self.bias
                    }
                    
                    # Atualiza pesos e bias
                    self.pesos += self.taxa_aprendizagem * erro * X[i]
                    self.bias += self.taxa_aprendizagem * erro
                    
                    # Mostra detalhes da atualização
                    print(f"\nExemplo {i+1}:")
                    print(f"Entrada: x={X[i]}, y_real={y[i]}, y_pred={predicao}")
                    print(f"Erro: {erro}")
                    print(f"Δpesos = α * erro * x = {self.taxa_aprendizagem} * {erro} * {X[i]}")
                    print(f"Pesos anterior: {estado_anterior['pesos']}")
                    print(f"Pesos atualizado: {self.pesos}")
                    print(f"Bias anterior: {estado_anterior['bias']:.1f}")
                    print(f"Bias atualizado: {self.bias:.1f}")
                    
                    # Salva no histórico
                    self.historico.append({
                        'epoca': epoca + 1,
                        'exemplo': i + 1,
                        'pesos_antes': estado_anterior['pesos'],
                        'bias_antes': estado_anterior['bias'],
                        'pesos_depois': self.pesos.copy(),
                        'bias_depois': self.bias,
                        'entrada': X[i],
                        'y_real': y[i],
                        'y_pred': predicao,
                        'erro': erro
                    })
                else:
                    print(f"\nExemplo {i+1}: x={X[i]}, y={y[i]}, ŷ={predicao} ✓ (sem atualização)")
            
            if not erro_epoca:
                print(f"\nConvergência alcançada na época {epoca + 1}!")
                break
    
    def mostrar_relatorio(self):
        print("\n" + "="*80)
        print("RELATÓRIO COMPLETO DO TREINAMENTO")
        print("="*80)
        
        for i, registro in enumerate(self.historico):
            if i == 0:
                print(f"\nEstado {i}: {registro['descricao']}")
                print(f"Pesos: {registro['pesos']}, Bias: {registro['bias']:.1f}")
            else:
                print(f"\nEstado {i}: Época {registro['epoca']}, Exemplo {registro['exemplo']}")
                print(f"Entrada: {registro['entrada']}, y_real: {registro['y_real']}, y_pred: {registro['y_pred']}")
                print(f"Erro: {registro['erro']}")
                print(f"Pesos anterior: {registro['pesos_antes']}")
                print(f"Pesos atualizado: {registro['pesos_depois']}")
                print(f"Bias anterior: {registro['bias_antes']:.1f}")
                print(f"Bias atualizado: {registro['bias_depois']:.1f}")

def exercicio_perceptron():
    """
    Resolução do exercício proposto
    """
    # Codificação dos dados: Não=0, Sim=1
    # Características: [Estudou, Fez trabalho]
    X = np.array([
        [0, 0],  # Joãozinho
        [0, 1],  # Huguinho  
        [1, 0],  # Zezinho
        [1, 1]   # Luizinho
    ])
    
    # Labels: Passou (Não=0, Sim=1)
    y = np.array([0, 0, 1, 1])
    
    # Cria e treina o perceptron conforme exercício
    perceptron = Perceptron(taxa_aprendizagem=0.1, max_epocas=2)
    perceptron.treinar(X, y)
    perceptron.mostrar_relatorio()
    
    # Teste final
    print("\n" + "="*50)
    print("TESTE FINAL")
    print("="*50)
    nomes = ["Joãozinho", "Huguinho", "Zezinho", "Luizinho"]
    for i in range(len(X)):
        predicao = perceptron.prever(X[i])
        status = "✓" if predicao == y[i] else "✗"
        print(f"{nomes[i]:10} | Estudou: {X[i][0]} | Trabalho: {X[i][1]} | Passou: {y[i]} | Predito: {predicao} {status}")

# Executa o exercício
if __name__ == "__main__":
    exercicio_perceptron()

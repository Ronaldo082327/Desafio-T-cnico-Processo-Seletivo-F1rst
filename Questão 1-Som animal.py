class Animal:
    def som(self):
        raise NotImplementedError("Subclass deve implementar este método")

class Gato(Animal):
    def som(self):
        return "Miau"

class Cachorro(Animal):
    def som(self):
        return "Auau"

class Historico:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Historico, cls).__new__(cls)
            cls._instance.execucoes = []
        return cls._instance

    def adicionar_execucao(self, input, output):
        self.execucoes.append((input, output))

    def obter_historico(self):
        return self.execucoes

def main():
    historico = Historico()
    
    while True:
        entrada = input("Input: ")
        
        if entrada == "1":
            animal = Gato()
            som = animal.som()
            historico.adicionar_execucao("1", som)
            print("Output:", som)
        elif entrada == "2":
            animal = Cachorro()
            som = animal.som()
            historico.adicionar_execucao("2", som)
            print("Output:", som)
        elif entrada.lower() == "historico":
            execucoes = historico.obter_historico()
            for execucao in execucoes:
                print(execucao[0], execucao[1])
        else:
            print("Input inválido. Tente novamente.")

if __name__ == "__main__":
    main()



    
    #Explicação do Código

Classes usadas “Animal, Gato e Cachorro”:
A classe base “Animal” está definindo um método som que é implementado nas subclasses “Gato e Cachorro”. Cada subclasse de “Animal” implementa o seu próprio som.

Classe Singleton Historico:

Implementei o padrão Singleton na classe “Historico” para garantir que apenas uma instância do histórico seja criada e gerenciada no decorrer do processo.
Utilizei o  método “adicionar_execucao” para  adicionar uma execução ao histórico, e o método “obter_historico” para retornar todas as execuções armazenadas.

Função main:

Usei essa função para  executar um loop infinito que recebe inputs do usuário.
Dependendo do input, cria uma instância de “Gato ou Cachorro” obtendo o som e depois adiciona ao histórico e imprime o output.
Se o input for "historico", imprime todas as execuções armazenadas no histórico, conforme pedido no projeto.


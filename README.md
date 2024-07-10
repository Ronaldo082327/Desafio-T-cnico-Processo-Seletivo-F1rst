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

import sqlite3
import sys
import time as t
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class GerenciadorProdutos:
    def __init__(self):
        self.conn = sqlite3.connect('produtos.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS produtos
                            (Nome TEXT, Preco REAL, Quantidade INTEGER)''')
        self.conn.commit()

    def add_produto(self, nome, preco, quantidade):
        self.c.execute("INSERT INTO produtos VALUES (?, ?, ?)", (nome, preco, quantidade))
        self.conn.commit()
        print("Adicionando Produto...")
         for i in range(2):
            print(".")
            t.sleep(0.5)
        print("Produto adicionado com sucesso.")

    def remover_produto(self, nome):
        self.c.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
        self.conn.commit()
        print("Removendo Produto...")
        for i in range(2):
            print(".")
            t.sleep(0.5)
        print("Produto removido com sucesso.")

    def visualizar_tabela(self):
        self.c.execute("SELECT * FROM produtos")
        rows = self.c.fetchall()
        if len(rows) == 0:
            print("Nenhum produto encontrado.")
        else:
            for row in rows:

                print("-----------------------")
                print("Nome: ", row[0])
                print("Preço: ", row[1])
                print("Quantidade: ", row[2])
                print("-----------------------")

    def plot_grafico(self):
        self.c.execute("SELECT nome, quantidade FROM produtos")
        query = self.c.fetchall()
        df = pd.DataFrame(query, columns=['Nome', 'Quantidade'])
        plt.figure(figsize=(20, 10))
        
        sns.barplot(data=df, x='Nome', y='Quantidade',palette='dark')
        plt.xlabel('Nome do Produto')
        plt.ylabel('Quantidade')
        plt.title('Quantidade de Produtos')
        plt.xticks(rotation=80)
        plt.show(block=True)
        

                
    def contar_produtos(self):
        print('Contando...')
        for i in range(2):
            print(".")
            t.sleep(0.5)
        self.c.execute("SELECT COUNT(*) FROM produtos")
        quant = self.c.fetchone()[0]
        print('Quantidade total de produtos:', quant)

    def fechar_conexao(self):
        self.conn.close()


class InterfaceUsuario:
    def __init__(self):
        self.gerenciador_produtos = GerenciadorProdutos()

    def add_produto(self):

        try:
            print("Adicionar Produto:")
            nome = input("Insira o Nome: ")
            preco = float(input("Insira o Preço: "))
            quantidade = int(input("Insira a Quantidade: "))

            self.gerenciador_produtos.add_produto(nome, preco, quantidade)
        except:
            print('Valor invalido, por favor tente novamente.')

    def remover_produto(self):
        print("Remover Produto")
        nome = input("Insira o Nome: ")
        
        self.gerenciador_produtos.remover_produto(nome)

    def interromper_programa(self):
        print("Encerrando o Programa...")
        for i in range(3):
            print(".")
            t.sleep(0.5)
        print("Programa Encerrado com Sucesso.")
        self.fechar_conexao()
        sys.exit()

    def fechar_conexao(self):
        self.gerenciador_produtos.fechar_conexao()

    def visualizar_tabela(self):
        self.gerenciador_produtos.visualizar_tabela()
       
    def contar_produtos(self):
        self.gerenciador_produtos.contar_produtos()
    
    def plot_grafico(self):
        print('Gerando grafico...')
        for i in range(3):
            print(".")
            t.sleep(0.5)
        print('Aperte a tecla Q para sair.\n')

        print('Aperte a tecla F para ver em tela cheia.')

        self.gerenciador_produtos.plot_grafico()


if __name__ == "__main__":
    interface = InterfaceUsuario()

    while True:
        print("=====================================================")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Visualizar Tabela de Produtos")
        print('4. Total de Produtos')
        print('5. Plotar Grafico')
        print("0. Encerrar Programa")
        print("\n")
        opcao = input("Escolha uma opção: ")
        print("=====================================================")
        

        if opcao == "1":
            interface.add_produto()
        elif opcao == "2":
            interface.remover_produto()
        elif opcao == "3":
            interface.visualizar_tabela()
        elif opcao == "0":
            interface.interromper_programa()
        elif opcao == '4':
            interface.contar_produtos()
        elif opcao == '5':
            interface.plot_grafico()
        else:
            print('Comando Invalido. Tente novamente.')
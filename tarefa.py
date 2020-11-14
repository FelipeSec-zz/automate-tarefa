# Instalar docxtpl com 'pip install docxtpl'
from docxtpl import DocxTemplate

from tabulate import tabulate
from datetime import date

<<<<<<< HEAD
#Pega a informação da data de hoje, e guarda na variável 'hoje'
hoje = date.today()
=======
today = date.today()

data  = today.strftime("%d/%m/%Y")

print(" " "\n")

print(tabulate([['Matemática', 1], ['Química', 2], ['Biologia', 3], ['Português', 4], ['Cultura Religiosa', 5], ['Filosofia', 6], ['Física', 7], ['Artes', 8], ['Literatura', 9], ['Geografia', 10], ['História', 11], ['Inglês', 12], ['Sociologia', 13],  ], headers=['Matéria', 'Num'], tablefmt='orgtbl'))

prof = int(input("Qual o professor? "))

nome = input("Nome do arquivo: ")
>>>>>>> 512cb7a71fc2811767d78396f83f5014b8ed81ee

# Formata a data, para dd/mm/AAAA 
data  = hoje.strftime("%d/%m/%Y")

def doc(n):
    # Acessa o modelo template para tarefas em geral, e guarda na variável tmp
    tmp = DocxTemplate("template.docx")
    # Todos os tipos de edições no .docx que podem ser feitas utilizando essa função
    context = {

        1:{"prof":"Walter Maluf Júnior","date":data,"mat":"MATEMÁTICA"},
        2:{"prof":"Rowlian Luciano Dantas","date":data,"mat":"QUÍMICA"},
        3:{"prof":"Paulo César Franco","date":data,"mat":"BIOLOGIA"},
        4:{"prof":"Ana Maria","date":data,"mat":"PORTUGUÊS"},
        5:{"prof":"Leandro Carlos Santos Rosa","date":data,"mat":"CULTURA RELIGIOSA"},
        6:{"prof":"Leandro Carlos Santos Rosa","date":data,"mat":"FILOSOFIA"},
        7:{"prof":"Thiago Carrara de Lima","date":data,"mat":"FÍSICA"},
        8:{"prof":"Gustavo Borges de Sousa","date":data,"mat":"ARTES"},
        9:{"prof":"Gustavo Borges de Sousa","date":data,"mat":"LITERATURA"},
        10:{"prof":"Fabiana Vieira da Silva","date":data,"mat":"GEOGRAFIA"},
        11:{"prof":"Edgar Luiz Carvalho Macedo de Noronha","date":data,"mat":"HISTÓRIA"},
        12:{"prof":"Ana Flávia Sabino Vilela","date":data,"mat":"INGLÊS"},
        13:{"prof":"Adriano Donizete Rodrigues da Silva","date":data,"mat":"SOCIOLOGIA"}        
    }
    # Escreve as alterações baseado no número da matéria escolhida
    tmp.render(context[n])
    # Salva o novo arquivo com o nome escolhido
    tmp.save("%s.docx" % (nome,))


def red(p):
    # Acessa o modelo template para a redação, e guarda na variável temp
    temp = DocxTemplate("template1.docx")
    # Só há uma modificação que pode ser feita com essa função, a de data e inserção do tema
    context = {
        14:{"date":data,"tema":theme}
    }

    temp.render(context[p])
    # Salva o novo arquivo, especificando o tema "redação_'tema'.docx"
    temp.save("redação_" + "%s.docx" % (theme,))

print(" " "\n")

# Produz uma tabela relacionando as matérias com seus respectivos números
print(tabulate([
['Matemática', 1], 
['Química', 2], 
['Biologia', 3], 
['Português', 4], 
['Cultura Religiosa', 5],
['Filosofia', 6],
['Física', 7], 
['Artes', 8], 
['Literatura', 9], 
['Geografia', 10], 
['História', 11], 
['Inglês', 12], 
['Sociologia', 13], 
['Redação', 14]  
], headers=['Matéria', 'Num'], tablefmt='orgtbl'))

print("\n")

# Captura o número da matéria, e transforma para um número inteiro, necessário para a compilação do docxtpl
prof = int(input("Qual a matéria? "))

# Se o número da matéria for 14, iniciará a função de redação
if prof == 14:
    theme = input("Qual o tema? ")
    red(prof)
# Porém, se essa estiver no intervalo [1,14) , será utilizada a função para tarefas.
elif prof == range(1,14):
    nome = input("Nome do arquivo: ")
    doc(prof)
else:
    pass
from docxtpl import DocxTemplate
from tabulate import tabulate
from datetime import date

today = date.today()

data  = today.strftime("%d/%m/%Y")

print(" " "\n")

print(tabulate([['Matemática', 1], ['Química', 2], ['Biologia', 3], ['Português', 4], ['Cultura Religiosa', 5], ['Filosofia', 6], ['Física', 7], ['Artes', 8], ['Literatura', 9], ['Geografia', 10], ['História', 11], ['Inglês', 12], ['Sociologia', 13],  ], headers=['Matéria', 'Num'], tablefmt='orgtbl'))

prof = int(input("Qual o professor? "))

print("\n")

nome = input("Nome do arquivo: ")


def doc(n):
    tmp = DocxTemplate("template.docx")
    context = {

        1:{"prof":"Maluf","date":data,"mat":"MATEMÁTICA"},
        2:{"prof":"Rowlian","date":data,"mat":"QUÍMICA"},
        3:{"prof":"PC","date":data,"mat":"BIOLOGIA"},
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
    tmp.render(context[n])
    tmp.save("%s.docx" % (nome,))

doc(prof)


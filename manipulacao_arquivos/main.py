'''arquivo = open("texto.txt","r")
print(arquivo.read())'''
'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
#print(arquivo.seek(0))'''
'''print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''
'''print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read(8))'''
'''print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)'''

'''arquivo = open("novo.txt","w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt","w")
arquivo.write("banana")
arquivo.write("uva")
arquivo.write("mamao")
arquivo.close()'''

'''precos = [20,100,500,600]
with open("precos_roupas.txt","w") as arquivo:
 for preco in precos:
     arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''precos =  [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''
'''precos = [100000]
with open("precos_roupas", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''

disciplinas = ["Rad \n", "intordução a C \n", "Programação 1 \n"]
'''with open("disciplinas.txt", "w") as file:
    file.write("Relação de disciplinas \n")
    file.writelines(disciplinas)

with open("disciplinas.txt", "r") as file:
    print(file.read())'''

'''with open("texto.txt","r") as arquivo:
    print("Representação original da linha")
    #for linha in arquivo:
        #print(repr(linha))

with open("texto.txt", "r") as arquivo:
    print("Conteudo da linha")
    for linha in arquivo:
        linha_ = linha.strip()
        print(repr(linha_))'''

'''minha_lista = ["Arroz", "feijao","Carne"]
lista_ = '.'.join(minha_lista)
with open("texto_.txt","w") as arquivo:
 arquivo.write(lista_)'''

'''try:
     with open("arquivo_teste.txt","r") as arquivo:
         print(arquivo.read())
except FileNotFoundError:
    print("Arquivo inexistente")'''

'''import os 
try:
    os.remove("teste.txt")
    print("Arquivo foi removido")
except FileNotFoundError as erro:
    print("arquivo ")
    print("descrição", erro)'''

try:
    f = open("novo2.txt","r")
    f.write("Hello")
except IOError as erro:
    print("O erro foi", erro)



 





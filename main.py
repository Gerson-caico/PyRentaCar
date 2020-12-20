#Locadora de veículos RentaCar
from datetime import datetime
from tkinter import *


class Veiculos(object):
  def __init__(self, marca="", modelo="", ano=0, valor=0):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    self.codigo = ""
    self.status = "DISPONÍVEL"

class Clientes(object):
  def __init__(self, cod='', nome="", email="", tel=""):
    self.codigo = ""
    self.nome = nome
    self.email = email
    self.tel = tel

Codigos = []
Marca = []
Modelo = []
Ano = []
Valor = []
Status = []
Ialuguel = []
Faluguel = []
Cliente = []
Prazo = []
objetos = []
opcao=0
now = datetime.now()
Dia = now.day
Mes = now.month
Anos = int(now.year)

def salvar_veiculos(objetos):
  objetos=[]
  with open("veiculos.csv", "w") as arquivo:
    for veiculo in objetos:
      arquivo.writelines("{}#{}#{}#{}\n".format(Marca['marca'], Modelo['modelo'], Ano['ano'], Codigos["codigo"]))
      arquivo.close()
  return objetos

def carregar_veiculos(): 
    with open("veiculos.csv", "r") as arquivo:
      for linha in arquivo.readlines():
          coluna = linha.strip().split("#")
          veiculo = {
                'marca': coluna[0],
                'modelo': coluna[1],
                'ano': coluna[2],
                'codigo': coluna[3]
          }
          objetos.extend(veiculo)
      arquivo.close()
    return objetos

def salvar_clientes(Cliente):
  Cliente=[] 
  with open("clientes.csv", "w") as arquivo:
    for cliente in Cliente:
      arquivo.writelines("{}#{}#{}\n".format(Cliente['nome'], Cliente['email'], Cliente['tel']))
  arquivo.close()

def carregar_clientes(): 
    Cliente = []

    with open("clientes.csv", "r") as arquivo:
      for linha in arquivo.readlines():
          coluna = linha.strip().split("#")
          cliente = {
                'email': coluna[1],
                'nome': coluna[0],
                'cod': coluna[3],
                'tel': coluna[2],
          }
          Cliente.extend(cliente)
    arquivo.close()
    return Cliente

janela = Tk()
janela.geometry("800x800")
janela.configure(bg='lightblue')

def funcao(n):
  global opcao
  opcao=0+int(n)
  return opcao

def sair():
  janela.quit()

label_1 = Label(janela, text="Bem-vindo à Locadora PyRentaCar", font="Arial 25")
label_1.place(x=150, y=250)

img=PhotoImage(file="carro.png")
label_2 = Label(janela, image=img)
label_2.place(x=250, y=350)

m = Menubutton(janela, text="Menu de opções",font="Arial 25", background="white", foreground='red')
m.menu = Menu(m)
m["menu"] = m.menu
m.place(x=260, y=50)

m.menu.add_command(label="Adicionar veículo", font='Arial 22', command=lambda:[funcao(1), sair()])

m.menu.add_command(label="Consultar veículo",font='Arial 22', command=lambda:[funcao(2), sair()])

m.menu.add_command(label="Alugar/Reservar veículo", font='Arial 22', command=lambda:[funcao(3), sair()])

m.menu.add_command(label="Devolver/Liberar veículo", font='Arial 22', command=lambda:[funcao(4), sair()])

m.menu.add_command(label="Excluir veículo",font='Arial 22', command=lambda:[funcao(5), sair()])

m.menu.add_command(label="Avançar para a data atual", font='Arial 22', command=lambda: [funcao(6), sair()])

m.menu.add_separator()
m.menu.add_command(label="Sair do sistema", font='Arial 22', command=lambda:[funcao(7), sair()])

janela.mainloop()


while opcao != 7:
  print("========= LOCADORA 'PYRENTACAR' =========")
  print("--------- DATA: {} \ {} \ {} ----------\n".format(Dia, Mes, Anos))
  
  print('')

  if opcao == 1:#Adicionando veículo
        print("============= CADASTRO DE VEÍCULOS =============\n")
        print("-----------------------------------")
        a = input("MARCA: ")
        b = input("MODELO: ")
        c = input("ANO: ")
        d = int(input("VALOR DA DIÁRIA DO VEÍCULO: "))
        print("-----------------------------------\n")
        Marca.append(a)
        Modelo.append(b)
        Ano.append(c)
        Valor.append(d)
        e = len(Modelo)
        Codigos.append("00" + str(e))
        obj = Veiculos()
        obj.codigo = e
        obj.valor = float(d)
        obj.ano = int(c)
        obj.modelo = b
        obj.marca = a
        objetos.append(obj)
        Status.append(obj.status)
        Ialuguel.append(str(Dia) + str(Mes) + str(Anos))
        Faluguel.append("")
        Cliente.append("")
        Prazo.append(0)
        salvar_veiculos(objetos)
        carregar_veiculos()
        print("================================================\n")
        janela.mainloop()
          
  if opcao == 2:#Consultando veículo
    print("")
    print("======== CONSULTAR VEÍCULOS =========\n")
    NumerodeCarros = len(Codigos)
    c = 0
    print("-----------------------------------")
    while c < NumerodeCarros:
      print("{}--{}--{}".format(Codigos[c], Modelo[c], Status[c]))
      c = c + 1
    print("-----------------------------------")
    print("\nDigite 1 para ver mais detalhes ")
    print("Digite 2 para voltar a tela Inicial ")
    aux = int(input("Digite a operação desejada: "))
    print("")
    if aux == 1:
        print("============== INFORMAÇÕES DETALHADAS ================\n")
        print("------------------------------------------------------\n")
        c = 0
        while c < NumerodeCarros:
          print("{} - {} {} {} - Valor: R${},00 {}".format(Codigos[c], Marca[c], Modelo[c], Ano[c], Valor[c], Status[c]))
          c = c + 1
          print(
              "------------------------------------------------------\n")
          print("======================================================\n")
          
    if aux == 2:
      print("")
      janela.mainloop()

  if opcao == 3: #Alugando/Reservando veículo
    print("===== ALUGAR/RESERVAR VEÍCULO ======")
    print("Digite 1 para ALUGAR o veículo.")
    print("Digite 2 para RESERVAR o veículo.")
    op = int(input("Digite a operação desejada: "))
    print("")
    if op == 1:
      obj2 = Clientes()
      obj2.nome = input("Nome do Cliente: ")
      obj2.email = input("E-mail do Cliente: ")
      obj2.tel = input("Telefone do Cliente: ")
      prazo = int(input("Prazo de locação: "))
      salvar_clientes(obj2)
      carregar_clientes()
      if prazo > 30:
        print("Prazo muito grande.")
        prazo = int(input("Digite um prazo de locação menor: "))
      cd = input("Código do veículo: ")
      if str(Status[int(cd) - 1]) == "DISPONÍVEL":
        Prazo[int(cd) - 1] = prazo
        Status[int(cd) - 1] = "ALUGADO"
        Cliente[int(cd) - 1] = obj2.nome
        Ialuguel[int(cd) - 1] = str(str(Dia) + str(Mes) + str(Anos))
        d = Dia + prazo
        m = Mes
        a = Anos
        if d > 30:
          d = d - 30
          m = m + 1
          if m > 12:
            m = m - 12
            a = a + 1
            Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
      elif str(Status[int(cd) - 1]) == "ALUGADO":
        print("esse veículo não pode ser alugado")
        cd = input("Código de um outro veículo: ")
        if str(Status[int(cd) - 1]) == "DISPONÍVEL":
          Status[int(cd) - 1] = "ALUGADO"
          Cliente[int(cd) - 1] = obj2.nome
          Ialuguel[int(cd) - 1] = str(str(Dia) + str(Mes) + str(Anos))
          d = Dia + prazo
          m = Mes
          a = Anos
          if d > 30:
            d = d - 30
            m = m + 1
            if m > 12:
              m = m - 12
              a = a + 1
              Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
      if str(Status[int(cd) - 1]) == "RESERVADO":
        print("há sobreposição de datas e deve ser escolhido outro carro ou outra data")
      janela.mainloop()
    elif op == 2:
      obj2.nome = input("Nome do Cliente: ")
      prazo = int(input("Prazo de locação: "))
      if prazo > 30 - Dia:
        print("Prazo muito grande.")
        prazo = int(input("Digite um prazo de locação menor: "))
        cd = int(input("Código do veículo:"))
        if str(Status[int(cd) - 1]) == "DISPONÍVEL":
          Prazo[int(cd) - 1] = prazo
          Status[int(cd) - 1] = "RESERVADO"
          Cliente[int(cd) - 1] = obj2.nome
          ini = (input("Data do inicio do aluguel sem '/' ex: 12012017 : "))
          d = int(ini[0] + ini[1])
          m = int(ini[2] + ini[3])
          a = int(ini[4] + ini[5] + ini[6] + ini[7])
          d = d + prazo
          if d > 30:
            d = d - 30
            m = m + 1
            if m > 12:
              m = m - 12
              a = a + 1
              Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
              print("\n====================================\n")
      janela.mainloop()
    
  if opcao == 4: #Devolvendo veículo
    print("========= DEVOLVER/LIBERAR VEÍCULO =========")
    print("\n-----------------------------------")
    a = len(Codigos)
    b = 0
    while b < a:
      if Status[b] != "DISPONÍVEL":
        print(str(Codigos[b]) + "--" + str(Modelo[b]) + "--" + str(Status[b]))
        print("-----------------------------------")
        b = b + 1
      print("\nDigite 1 para Devolver Veículo")
      print("Digite 2 para Liberar Veículo")
      res = int(input("Digite a operação desejada:   "))
      print("")
      if res == 1:
        print("----------------------------------------")
        cod = int(input("Digite o Código do veículo: "))
        print("\nCliente: ", Cliente[cod - 1])
        val = int(Ialuguel[cod - 1]) // 1000000
        d = val
        m = (int(Ialuguel[cod - 1]) - d * 1000000) // 10000
        a = (int(Ialuguel[cod - 1]) - d * 1000000) % 10000
        if a == Anos:
          if m > Mes:
            print("Total a pagar: R$ ",(((30 - d) + Dia) * float(Valor[cod - 1])))
            Status[cod - 1] = "DISPONÍVEL"
          elif m == Mes:
            if Dia == d:
              print("Total a pagar: R$ ", (float(Valor[cod - 1])))
              Status[cod - 1] = "DISPONÍVEL"
            elif Dia > d:
              print("Total a pagar: R$ ",((Dia - d) * float(Valor[cod - 1])))
              Status[cod - 1] = "DISPONÍVEL"
            elif d > Dia:
              Status[cod - 1] = "DISPONÍVEL"
          elif a < Anos:
            print("Total a pagar: R$ ",((Dia + (30 - d)) * float(Valor[cod - 1])))
            Status[cod - 1] = "DISPONÍVEL"
          elif a > Anos:
            Status[cod - 1] = "DISPONÍVEL"
        print("----------------------------------------\n")
        print("================================================\n")
        janela.mainloop()
        
        if res == 2:
          cod = int(input("Digite o Código do veículo: "))
          print("Cliente: ", Cliente[cod - 1])
          val = int(Ialuguel[cod - 1]) // 1000000
          d = val
          m = (int(Ialuguel[cod - 1]) - d * 1000000) // 10000
          a = (int(Ialuguel[cod - 1]) - d * 1000000) % 10000
          if a > Anos:
                Status[cod - 1] = "DISPONÍVEL"
          elif a < Anos:
            val = Dia + (30 - d)
            print("Total a pagar: R$ ", (val * float(Valor[cod - 1])))
            Status[cod - 1] = "DISPONÍVEL"
          elif a == Anos:
            if m == Mes:
              if d == Dia:
                print("Total a pagar: R$ ", (float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
              elif d > Dia:
                Status[cod - 1] = "DISPONÍVEL"
              else:
                val = Dia - d
                print("Total a pagar: R$ ",
                (val * float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
                janela.mainloop()
    
  if opcao == 5: #exclUindo veículo
    print("========== EXCLUIR VEÍCULOS ===========\n")
    vei = int(input("Digite o Código do veículo: "))
    if Status[vei - 1] == "DISPONÍVEL":
      del Codigos[vei - 1]
      del Marca[vei - 1]
      del Modelo[vei - 1]
      del Ano[vei - 1]
      del Valor[vei - 1]
      del Status[vei - 1]
      del Ialuguel[vei - 1]
      del Faluguel[vei - 1]
      del Cliente[vei - 1]
      del objetos[vei - 1]
      ve = len(Status)
      y = 1
      x = 0
      while x < ve:
        Codigos[x] = "00" + str(y)
        x = x + 1
        janela.mainloop()
      
  if opcao == 6: #Avançando para a data atual 
      Dia = Dia + 1
      if Dia > 30:
        Dia = Dia - 30
        Mes = Mes + 1
        if Mes > 12:
          Mes = Mes - 12
          Anos = Anos + 1
      cod = len(Status)
      while cod > 0:
        d = (int(Ialuguel[cod - 1])) // 1000000
        m = (int(Ialuguel[cod - 1]) - d * 1000000) // 10000
        a = (int(Ialuguel[cod - 1]) - d * 1000000) % 10000
        if Status[cod - 1] == "DISPONÍVEL":
          print()
        elif a == Anos:
          if m > Mes:
            if ((30 - d) + Dia) > Prazo[cod - 1]:
              Status[cod - 1] = "ATRASADO"
        elif m == Mes:
          if Dia == d:
            Status[cod - 1] = "ALUGADO"
        elif Dia > d:
          if (Dia - d) > Prazo[cod - 1]:
            Status[cod - 1] = "ATRASADO"
        elif a < Anos:
          if (Dia + (30 - d)) > Prazo[cod - 1]:
            Status[cod - 1] = "ATRASADO"
            cod = cod - 1
        print("")
        print("========= PASSOU-SE UM DIA =======\n\n")
        janela.mainloop()
       
  if opcao == 7: #Saindo do sistema
    print()
    print('#' * 52)
    print('# Obrigado por utilizar a LOCADORA "PYRENTACAR"!!  #')
    print('#      Aluno GERSON - Matr: 20200019420 - BSI   #')
    print('#' * 52)
    janela.mainloop()



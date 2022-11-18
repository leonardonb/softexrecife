def calculadora(n1,n2,operacoes):
   if operacoes==1:
       return n1+n2
   if operacoes==2:
       return n1-n2
   if operacoes==3:
       return n1*n2
   if operacoes==4:
       return n1/n2

execute=True
while execute:
   print("Operações Matemáticas:")
   print("\n")
   print("1.Soma")
   print("2.Subtração")
   print("3.Multiplicação")
   print("4.Divisão")
   print("0.Sair")

   operacoes=int(input("Qual operação você quer realizar?"))
   print("\n")
   if operacoes >=1 and operacoes <=4:
       n1=float(input("Digite o primeiro número: "))
       n2=float(input("Digite o segundo número: "))

       solucao=calculadora(n1,n2,operacoes)
       print("O resultado da sua operação é:", solucao)
       print("\n")

   elif operacoes==0:
       print("Volte sempre que for preciso!")
       print("\n")
       execute=False

   else:
       print("Opção inválida")
       print("\n")

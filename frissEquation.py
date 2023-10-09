## Programa para teste da equação de Friss

#Considerações: (1) Não há perdas por reflexão (casamento perfeito);
#               (2) As polarizações das antenas são iguais
#               (3) Antenas perfeitamente alinhadas
import math

#Constantes:
c = 300000000    #3*10^8 m/s velocidade da luz no vácuo
f = 500000000    #100MHz frequência dummy pra exemplos
lbda = c/f
Gt = 1           #dB
Gr = 1           #dB
Pt = 10          #dBm
d = 10           #distancia entre as antenas em metros

#Calculo da potência recebida dados os ganhos das antenas
#(transmissora e receptora) e a potência transmitida (tudo em Db)
L0 = 20*math.log10((4*math.pi*d)/lbda)
Pr = Gt + Gr - L0 + Pt
print('fim da equação de Friss')
print('A potência recebida pela receptora é:', round(Pr,3), 'dBm')

#Cálculo da distância dados os parâmetros do link entre as antenas,
#supondo que podemos medir a potência recebida
L0 = Pt - Pr + Gt + Gr
d = (lbda/(4*math.pi))*(10**((1/20)*(L0)))                  #20*math.log10((4*math.pi*d)/lbda) = L0
                                                            #math.log10((4*math.pi*d)/lbda) = (1/20)*(L0)
                                                            #(4*math.pi*d)/lbda = 10**((1/20)*(L0))
                                                            #d/lbda = (1/(4*math.pi))*(10**((1/20)*(L0)))
def calculaPotencia():
    Gt = float(input("Digite o valor do ganho da Antena transmissora: "))
    Gr = float(input("Digite o valor do ganho da Antena receptora: "))
    Pt = float(input("Digite o valor da potência de transmissão em dBm: "))
    d =  float(input("Digite o valor da distância entre as antenas (em metros): "))
    f =  float(input("Digite a frequência de comunicação (em Hz): "))
    lbda = c/f
    L0 = 20*math.log10((4*math.pi*d)/lbda)
    Pr = Gt + Gr - L0 + Pt
    print("A potência recebida pela antena receptora é: ", Pr, "dBm")

def calculaDistancia():
    Gt = float(input("Digite o valor do ganho da Antena transmissora: "))
    Gr = float(input("Digite o valor do ganho da Antena receptora: "))
    Pt = float(input("Digite o valor da potência de transmissão em dBm: "))
    Pr =  float(input("Digite o valor esperado ou medido da potência recebida: "))
    f =  float(input("Digite a frequência de comunicação (em Hz): "))
    lbda = c/f
    L0 = Pt - Pr + Gt + Gr
    d = (lbda/(4*math.pi))*(10**((1/20)*(L0)))
    print('A distância calculada foi', d)

modo = 100
while modo != 0:
    modo = int(input("Digite 1 caso queira calcular a potência recebida, 2 caso queira calcular a distância esperada e 0 para fechar o programa: "))
    match modo:
        case 1:
            calculaPotencia()
        case 2:
            calculaDistancia()
        case 0:
            print("Fechando programa")

"""
O if, elif e else são estruturas condicionais em Python usadas para tomar
decisões no código.

O if verifica a primeira condição. Se ela for True, o bloco de código dentro
dele será executado.

O elif significa "senão se". Ele é usado para testar uma nova condição caso
o if anterior seja False. Podemos usar vários elif no mesmo bloco.

O else é usado como alternativa final. Ele será executado quando nenhuma das
condições anteriores for verdadeira.

A indentação, ou seja, o espaço antes do código, é muito importante em Python,
pois ela define quais comandos pertencem ao if, elif ou else.

"""

nota = float(input('Digite a nota '))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Inicializa a variável soma com zero para acumular as notas
soma = 0
# Usa um laço for para repetir 9 vezes (para 9 notas)
for i in range(9):
    # Solicita ao usuário que digite a nota e converte para float
    n = float(input(f"Digite a {i+1}ª nota: "))
    # Adiciona a nota digitada à soma total
    soma += n
# Calcula a média dividindo a soma total pelo número de notas (9)
media = soma / 9
# Exibe a média das notas
print(f"A média das notas é: {media}")

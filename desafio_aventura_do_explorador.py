# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input("Quantos passos deseja que nosso aventureiro dê?  "))

# //TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
if quantidade_passos<=0:
  print("Nenhum passo dado na floresta.")
# // Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
else:
# // Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
  for p in range(1, quantidade_passos + 1):
    if p == 1:
      print(f"Explorador: {p} passo")
    else:
      print(f"Explorador: {p} passos")

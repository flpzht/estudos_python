from datetime import datetime, timedelta

# entrada do horário inicial
horario_str = input("Digite o horário inicial (HH:MM:SS): ")
horario = datetime.strptime(horario_str, "%H:%M:%S")

while True:
    print("\nDigite os valores para somar ou 'sair' para encerrar.")
    
    minutos_str = input("Quantos minutos deseja somar? (ou 'sair'): ")
    if minutos_str.lower() == "sair":
        break

    segundos_str = input("Quantos segundos deseja somar? (ou 'sair'): ")
    if segundos_str.lower() == "sair":
        break

    try:
        minutos = int(minutos_str)
        segundos = int(segundos_str)
        soma = timedelta(minutes=minutos, seconds=segundos)
        horario += soma
        print("⏱️ Novo horário:", horario.strftime("%H:%M:%S"))
    except ValueError:
        print("⚠️ Entrada inválida! Certifique-se de digitar números válidos.")

print("\n✅ Processo finalizado. Horário final:", horario.strftime("%H:%M:%S")) 

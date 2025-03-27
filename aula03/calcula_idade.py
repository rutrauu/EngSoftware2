from datetime import datetime

data_nasc = input("Digite sua data de nascimento: (dd/mm/yyyy")
nascimento = datetime.strptime(data_nasc, "%d/%m/%y")
hoje = datetime.today()
idade = hoje.year - nascimento.year


print(f"Voce têm {idade} anos.")
from dao.medicacaoDAO import MedicacaoDAO
from entidades.medicacao import Medicacao

def nova_medicacao(codigo_paciente):
	codigo = 0
	nome = input("Nome da medicacao: ")
	dosagem = input("Dose prescrita: ")
	print("""\
Insira os horarios de administracao diaria HH:MM,
para encerrar digite algo invalido:\n""")
	i = 1
	horarios = []
	while True:
		try:
			h = input(f"{i}\t").strip()
			if h == "":
				continue
			h = h.split(":")
			h = datetime.time(int(h[0]), int(h[1]))
		except:
			break
		else:
			horarios.append(h)
			i += 1
	horarios.sort(key=lambda t: t.hour*60+t.minute)
	lembrar = input("Deseja configurar alarmes para esses horarios? [s/n]")
	if lembrar == "s":
		lembrar = True
	elif lembrar == "n":
		lembrar = False
	else:
		print("Nao entendi, entao suponho que nao deseja")
		lembrar = False	
	return Medicacao(codigo, codigo_paciente, nome, dosagem, horarios, lembrar)

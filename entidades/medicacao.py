class Medicacao:

    def __init__(self, codigo, codigo_paciente, nome, dosagem, horarios, lembrar):
        self.codigo = codigo
        self.codigo_paciente = codigo_paciente
        self.nome = nome
        self.dosagem = dosagem
        self.horarios = horarios
        self.lembrar = lembrar

    def set_horarios(self, novo):
        if isinstance(novo, list):
            self.horarios = novo
class RegistroNutricional:

    def __init__(self, codigo, codigo_paciente, dia, mes, ano, proteinas, gorduras, carboidratos):
        self.codigo = codigo
        self.codigo_paciente = codigo_paciente
        # trocar 3 ints por 1 datetime
        self.dia = dia
        self.mes = mes
        self.ano = ano
        # formula para evitar discrepancia
        self.calorias = 4*(proteinas+carboidratos)+9*(gorduras)
        self.proteinas = proteinas
        self.gorduras = gorduras
        self.carboidratos = carboidratos

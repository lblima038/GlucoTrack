from crud.crud_paciente import buscar_pacientes
from crud.crud_usuario import buscar_usuarios

usuarios = buscar_usuarios()
pacientes = buscar_pacientes()

for usuario in usuarios:
    print(usuario)
    
for paciente in pacientes:
    print(paciente)

def signo_zodiacal(dia: int, mes: int):
    if mes == 12 and dia >= 22 and dia <= 31 or mes == 1 and dia >= 1 and dia <= 20:
        signo = 'Capricornio'
    elif mes == 1 and dia >= 21 and dia <= 31 or mes == 2 and dia >= 1 and dia <= 19:
        signo = 'Acuario'
    elif mes == 2 and dia >= 20 and dia <= 28 or mes == 3 and dia >= 1 and dia <= 20:
        signo = 'Piscis'
    elif mes == 3 and dia >= 21 and dia <= 31 or mes == 4 and dia >= 1 and dia <= 20:
        signo = 'Aries'
    elif mes == 4 and dia >= 21 and dia <= 30 or mes == 5 and dia >= 1 and dia <= 20:
        signo = 'Tauro'
    elif mes == 5 and dia >= 21 and dia <= 31 or mes == 6 and dia >= 1 and dia <= 21:
        signo = 'Géminis'
    elif mes == 6 and dia >= 22 and dia <= 30 or mes == 7 and dia >= 1 and dia <= 22:
        signo = 'Cáncer'
    elif mes == 7 and dia >= 23 and dia <= 31 or mes == 8 and dia >= 1 and dia <= 23:
        signo = 'Leo'
    elif mes == 8 and dia >= 24 and dia <= 31 or mes == 9 and dia >= 1 and dia <= 22:
        signo = 'Virgo'
    elif mes == 9 and dia >= 23 and dia <= 30 or mes == 10 and dia >= 1 and dia <= 22:
        signo = 'Libra'
    elif mes == 10 and dia >= 23 and dia <= 31 or mes == 11 and dia >= 1 and dia <= 22:
        signo = 'Escorpio'
    elif mes == 11 and dia >= 23 and dia <= 30 or mes == 12 and dia >= 1 and dia <= 21:
        signo = 'Sagitario'
    else:
        signo = 'Inválido'

    return signo

dia_ = int(input('Escriba su día de nacimiento: '))
mes_ = int(input('Escriba su mes de nacimiento (con numeros): '))
print('\nSigno zodiacal: ', signo_zodiacal(dia_, mes_))
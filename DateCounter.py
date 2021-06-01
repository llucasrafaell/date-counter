from datetime import timedelta, datetime #IMPORTANDO APENAS O NECESSÁRIO
import time
print()
print('QUANTO TEMPO FALTA PARA O ANIVERSÁRIO DO LUCAS?')
print('aceito presentes \o/')

try:
    while True:
        date_now = datetime.today()
        date_now_timestamp = int(date_now.timestamp())
        birthdaydate = datetime(year=date_now.year, month=6, day=25, hour=0, minute=0, second=0) #DEFININDO A DATA DO ANIVERSÁRIO
        birthdaytimestamp = int(birthdaydate.timestamp())
        remaining_time_seconds = birthdaytimestamp - date_now_timestamp
        remaining_time = timedelta(seconds=remaining_time_seconds)

        #DIAS, SEGUNDOS, MINUTOS E HORAS RESTANTES
        remainingDays = remaining_time.days
        remaining_seconds = remaining_time.seconds
        remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
        remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)

        if remainingDays:
            if remainingDays > 1:
                remainingDays = '{} dias'.format(remainingDays)
            else:
                remainingDays = '{} dia'.format(remainingDays)
        else:
            remainingDays = ''

        if remaining_hours:
            if remaining_hours > 1:
                remaining_hours = ', {} horas'.format(remaining_hours)
            else:
                remaining_hours = ', {} hora'.format(remaining_hours)
        else:
            remaining_hours = ''

        if remaining_minutes:
            if remaining_minutes > 1:
                remaining_minutes = ', {} minutos'.format(remaining_minutes)
            else:
                remaining_minutes = ', {} minuto'.format(remaining_minutes)
        else:
            remaining_minutes = ''

        if remaining_seconds:
            if remaining_seconds > 1:
                remaining_seconds = ', {} segundos'.format(remaining_seconds)
            else:
                remaining_seconds = ', {} segundo'.format(remaining_seconds)
        else:
            remaining_seconds = ''

        spaces = '                                    '

        print('\rTempo restante: {}{}{}{}{}'.format(remainingDays,
                                                    remaining_hours,
                                                    remaining_minutes,
                                                    remaining_seconds,
                                                    spaces), end='')

        time.sleep(1)


except KeyboardInterrupt:

    exit()
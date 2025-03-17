from crontab import CronTab
from idna.idnadata import scripts
import os

def crear_tarea(min, hora, dia, mes, evento):

    cron = CronTab(user=True)

    scripts_path = os.path.join(os.getcwd(), "recordatorio.sh")


    #crear una nueva tarea
    job = cron.new(command=f'{scripts_path} {evento}')

    #Especificar fecha y hora
    job.minute.on(min)
    job.hour.on(hora)
    job.day.on(dia)
    job.month.on(mes)

    #guardar cambios
    cron.write()
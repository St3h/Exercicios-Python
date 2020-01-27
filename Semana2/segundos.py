seconds = int(input("Por favor, entre com o número de segundos que deseja converter:"))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = ((seconds % 86400) % 3600) // 60
secondsCalculated = ((seconds % 86400) % 3600) % 60
print(days, "dias,", hours, "horas,", minutes, "minutos e", secondsCalculated, "segundos.")
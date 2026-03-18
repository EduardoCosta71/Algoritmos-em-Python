from datetime import datetime, timedelta

agora = datetime.now()
print("Data e hora atual: ", agora)

formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada: ", formatada)

futuro = agora + timedelta(days=7)
print("Daqui a 7 dias sera:", futuro.strftime("%d/%m/%Y"))

data_prova = datetime(2026, 6, 2)
diferença = data_prova - agora
print('faltam', diferença.days, 'dias para prova')

print("Bom dia: ", agora.hour<12)
print("Boa tarde: ", agora.hour>=12 and agora.hour<8)
print("Boa noite: ", agora.hour<18 and agora.hour>23.59)
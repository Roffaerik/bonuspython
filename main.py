import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC88ee3bd591fd25d46aa67614b84d9485"
# Your Auth Token from twilio.com/console
auth_token  = "8a3c565772c7a2203a7f321c2f4a35b3"

client = Client(account_sid, auth_token)

# pandas
# openpyxl
# twilio

# passo a passo de solução

# abrir os 6 arquivos em excel
lista_meses = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabelas_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabelas_vendas['Vendas'] > 55000).any():
        vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5573991153694",
            from_="+12176651792",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)



# Para cada arquivo:

# verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# se for maior que 55.00 -> Enviar um sms com o Nome , o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada


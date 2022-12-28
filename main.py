import pandas as pd
import os
from twilio.rest import Client


# basicamente irei criar um programa que simula a bonificação do funcionário que
# ao vender 55.000, irei receber um SMS informando qual funcionário será bonificado
#o SMS conterá o nome do ganhador e o mês referente
#-------------------------------------------------------------------------------------------------
#código para ler um arquivo excel : 
#tabela_vendas = pd.read_excel('janeiro.xlsx')
#print (tabela_vendas)
#--------------------------------------------------------------------
#para fazer com que o código leia não só um mês, mas sim vários, tem que por esse código
#tabela_vendas = pd.read_excel(f'{variavel}.xlsx')
#---------------------------------------------------------------------------------------
#para eu fazer a condição pra ele me mostrar que em um dos meses vendeu mais de 55000, eu uso o código:
#if (tabela_vendas['coluna que eu quero que ele veja'] > 55000).any():
#        print('deu certo, vendeu mais que 55000')
#tradução, Se a tabela_vendas (coluna de vendas) for maior que 55000 em algum mês, diga "deu certo, vendeu mais que 55000"
#--------------------------------------------------------------------------------------------
#para eu botar pro código dizer em qual mês vendeu mais que 55000, basta usar o mesmo código que usei no 'for', que é:
# (f'{variavel} o que eu quero escrever na resposta do código) / obs: posso botar quantas váriaveis eu quiser.
#---------------------------------------------------------------------------------------
#para localizar alguma linha da tabela, se usa .loc  / e para no final ele retornar valor/nome específico que eu quero, se usa .value(0) no final.



lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vencedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        total_vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, alguém vendeu mais que 55000. Vendedor: {vencedor},  total de vendas: {total_vendas}')
        
        account_sid = 'id do perfil site twilo'
        auth_token = 'token secreto do perfil site twilo'
        client = Client(account_sid, auth_token)
        
        message = client.messages \
            .create(
                 body=f'No mês de {mes}, alguém vendeu mais que 55000. Vendedor: {vencedor},  total de vendas: {total_vendas}',
                 from_='Número Conta do site Twilo',
                 to='número pessoal'
                 )

        print(message.sid)


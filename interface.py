import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [

            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Escolha o Provedor de Email?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0,orientation='h', size=(15,20),key='Slider')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,20))]
        ]

        self.janela = sg.Window('Usuários').layout(layout)
        

    def Iniciar(self):

        while True:
            
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            egmail = self.values['gmail']
            eoutlook = self.values['outlook']
            aceitaCartao = self.values['aceitaCartao']
            naoAceitaCartao = self.values['naoAceitaCartao']
            script_slider = self.values['Slider']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'Gmail: {egmail}')
            print(f'Outlook: {eoutlook}')
            print(f'Aceita Cartão: {aceitaCartao}')
            print(f'Não Aceita Cartão: {naoAceitaCartao}')
            print(f'Script: {script_slider}')
            

tela = TelaPython()
tela.Iniciar()

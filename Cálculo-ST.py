import PySimpleGUI as sg


layout = [[sg.Text('Insira o valor do Preço Bruto:', size=(25,0)), sg.Input('R$', readonly=True, size=(3, 0)), sg.Input(key='-Bruto', size=(10, 0))],
          [sg.Text('Insira o valor do ICMS do Produto:', size=(25,0)), sg.Combo(['4%', '12%', '18%'], key='-ICMS1', readonly=True)],
          [sg.Text('Insira o valor do ICMS Interno:', size=(25,0)), sg.Combo(['18%'], key='-ICMS2', readonly=True)],
          [sg.Text('Insira o valor do MVA:', size=(25, 0)), sg.Input(key='-MVA', size=(6, 0)), sg.Input('%', size=(2, 0), readonly=True)],
          [sg.Text('Insira o valor do IPI:', size=(25, 0)), sg.Input(key='-IPI', size=(6, 0)), sg.Input('%', size=(2, 0), readonly=True)],
          [sg.Submit('Avançar'), sg.Cancel('Cancelar')]

]

window = sg.Window('Cálculo de ST (ver. 1.0)', layout)

event, values = window.read()
window.close()

Bruto = float(values['-Bruto'])
ICMS1 = (values['-ICMS1'])
if ICMS1 == '4%':
    ICMS1 = float(0.04)
if ICMS1 == '12%':
    ICMS1 = float(0.12)
if ICMS1 == '18%':
    ICMS1 = float(0.18)
ICMS2 = (values['-ICMS2'])
if ICMS2 == '18%':
    ICMS2 = float(0.18)
IPI = float((values['-IPI']))
IPI = float(IPI/100)
MVA = float((values['-MVA']))
MVA = float(MVA/100)

ValorICMS = float(Bruto * ICMS1)
ValorIPI = float(Bruto * IPI)
BaseCalculoST = float(Bruto + ValorIPI)

BaseCalculoIVA = float(BaseCalculoST * (1 + MVA))
ICMSInterno = float(BaseCalculoIVA * ICMS2)
ICMSDestacado = float(ValorICMS)
ValorST = float(ICMSInterno - ICMSDestacado)
ValorNota = float(BaseCalculoST + ValorST)

PercentualST = float(((ValorNota / BaseCalculoST) - 1) * 100)

ICMS1Porcentagem = float(ICMS1 * 100)
ICMS2Porcentagem = float(ICMS2 * 100)
MVAPorcentagem = float(MVA * 100)
IPIPorcentagem = float(IPI * 100)

sg.popup(f'------------------DADOS INSERIDOS------------------\n\n'
         f'Preço Bruto: R$ {Bruto}\n'
         f'ICMS do Produto: {ICMS1Porcentagem}%\n'
         f'ICMS Interno SP: {ICMS2Porcentagem}%\n'
         f'MVA: {MVAPorcentagem}%\n'
         f'IPI: {IPIPorcentagem}%\n\n'
         f'----------------RESULTADO DA OPERAÇÃO----------------\n\n'
         f'Valor ICMS: R$ {ValorICMS:.2f}\n'
         f'Valor IPI: R$ {ValorIPI:.2f}\n'
         f'Base Cálculo ST: R$ {BaseCalculoST:.2f}\n'
         f'Base Cálculo + IVA: R$ {BaseCalculoIVA:.2f}\n'
         f'\n'
         f'ICMS Fonte (Interno): R$ {ICMSInterno:.2f}\n'
         f'ICMS Destacado: R$ {ICMSDestacado:.2f}\n'
         f'Valor do ST: R$ {ValorST:.2f}\n'
         f'Valor Nota Fiscal: R$ {ValorNota:.2f}\n'
         f'\n'
         f'Percentual ST: {PercentualST:.2f}%\n', title='Operação concluída!')

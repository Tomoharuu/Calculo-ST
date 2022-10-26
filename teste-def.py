import PySimpleGUI as sg

layout = [[sg.Text('Insira o valor do Preço Bruto:', size=(25, 0)), sg.Input('R$', readonly=True, size=(3, 0)),
           sg.Input(key='-Bruto', size=(10, 0))],
          [sg.Text('Insira o valor do ICMS do Produto:', size=(25, 0)),
           sg.Combo(['4%', '12%', '13,3%', '18%', '25%'], key='-ICMS1', readonly=True)],
          [sg.Text('Insira o valor do ICMS Interno:', size=(25, 0)),
           sg.Combo(['4%', '12%', '13,3%', '18%', '25%'], key='-ICMS2', readonly=True)],
          [sg.Text('Insira o valor do MVA:', size=(25, 0)), sg.Input(key='-MVA', size=(6, 0)),
           sg.Input('%', size=(2, 0), readonly=True)],
          [sg.Text('Insira o valor do IPI:', size=(25, 0)), sg.Input(key='-IPI', size=(6, 0)),
           sg.Input('%', size=(2, 0), readonly=True)],
          [sg.Submit('Avançar'), sg.Cancel('Cancelar')]

          ]

window = sg.Window('Cálculo de ST (ver. 2.0.1)', layout)


def resultado_operacoes():
    resultado_layout = [[sg.Text(f'Preço Bruto: R$ {Bruto:.2f}')],
                        [sg.Button('Retornar'), sg.Button('Fechar')]

                        ]

    resultado_operacoes = sg.Window('Resultado', resultado_layout)

    while True:
        event, values = resultado_operacoes.read()
        if event == 'Retornar' or event == sg.WINDOW_CLOSED:
            break

    resultado_operacoes.close()


while True:
    event, values = window.read()
    if event == 'Avançar':
        Bruto = float(values['-Bruto'].replace(',', '.'))
        ICMS1 = (values['-ICMS1'])
        if ICMS1 == '4%':
            ICMS1 = float(0.04)
        if ICMS1 == '12%':
            ICMS1 = float(0.12)
        if ICMS1 == '13,3%':
            ICMS1 = float(0.133)
        if ICMS1 == '18%':
            ICMS1 = float(0.18)
        if ICMS1 == '25%':
            ICMS1 = float(0.25)
        ICMS2 = (values['-ICMS2'])
        if ICMS2 == '4%':
            ICMS2 = float(0.04)
        if ICMS2 == '12%':
            ICMS2 = float(0.12)
        if ICMS2 == '13,3%':
            ICMS2 = float(0.133)
        if ICMS2 == '18%':
            ICMS2 = float(0.18)
        if ICMS2 == '25%':
            ICMS2 = float(0.25)

        IPI = float(values['-IPI'].replace(',', '.'))
        IPI = float(IPI / 100)
        MVA = float(values['-MVA'].replace(',', '.'))
        MVA = float(MVA / 100)

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

        resultado_operacoes()
        window.close()

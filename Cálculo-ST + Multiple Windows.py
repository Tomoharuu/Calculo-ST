import PySimpleGUI as sg

layout1 = [[sg.Text('Insira o valor do Preço Bruto:', size=(25, 0)), sg.Input('R$', readonly=True, size=(3, 0)),
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


def janela2():
    layout2 = [[sg.Text("------------------------DADOS INSERIDOS------------------------", justification="right")],
               [sg.Text(f"Preço Bruto: R$ {Bruto:.2f}")],
               [sg.Text(f"ICMS do Produto: {ICMS1Porcentagem:.2f}%")],
               [sg.Text(f"ICMS Interno SP: {ICMS2Porcentagem:.2f}%")],
               [sg.Text(f"MVA: {MVAPorcentagem:.2f}%")],
               [sg.Text(f"IPI: {IPIPorcentagem:.2f}%\n")],
               [sg.Text("----------------RESULTADO DA OPERAÇÃO----------------")],
               [sg.Text(f"Valor ICMS: R$ {ValorICMS:.2f}")],
               [sg.Text(f"Valor IPI: R$ {ValorIPI:.2f}")],
               [sg.Text(f"Base Cálculo ST: R$ {BaseCalculoST:.2f}")],
               [sg.Text(f"Base Cálculo + IVA: R$ {BaseCalculoIVA:.2f}")],
               [sg.Text(f"ICMS Fonte (Interno): R$ {ICMSInterno:.2f}")],
               [sg.Text(f"ICMS Destacado: R$ {ICMSDestacado:.2f}")],
               [sg.Text(f"Valor do ST: R$ {ValorST:.2f}")],
               [sg.Text(f"Valor Nota Fiscal: R$ {ValorNota:.2f}\n")],
               [sg.Text(f"Percentual ST: {PercentualST:.2f}%")],
               [sg.Text("")],

               [sg.Button('Retornar', size=(100, 0))]

               ]

    janela2 = sg.Window('Operação Concluída!', layout2, size=(350, 520))

    while True:
        event, values = janela2.read()
        if event in (sg.WIN_CLOSED, "Retornar"):
            break

    janela2.close()


janela1 = sg.Window('Cálculo de ST (versão 2.0)', layout1)

while True:
    event, values = janela1.read()
    if event in (None, "Cancelar"):
        break
    if event == "Avançar":
        if values['-Bruto'] == "":
            sg.popup("Favor inserir um valor válido de Preço Bruto!", title="Erro!", line_width=50)
        if values['-Bruto'] == "":
            sg.popup("Favor inserir um valor válido de MVA!", title="Erro!", line_width=50)
        else:
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
            if values["-IPI"] == "":
                IPI = float(0)
            else:
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

            janela2()

janela1.close()

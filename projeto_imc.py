import flet as ft

def main(page: ft.Page):
    page.title = "Projeto IMC"
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window.width = 900
    page.window.height = 600
    
    fundo= ft.Image(src=r"giphy (1).gif", width=900, height=600, fit="cover",opacity=0.3)

    # Título
    titulo = ft.Text("Calculadora de IMC", size=50, weight="bold")
  
    # Campos de entrada
    nome = ft.TextField(label="Nome", width=300)
    peso = ft.TextField(label="Peso (kg)", width=300)
    altura = ft.TextField(label="Altura (m)", width=300)

    def calcular_imc(e):
        try:
            nome_valor = nome.value
            peso_valor = float(peso.value)
            altura_valor = float(altura.value)
            imc = peso_valor / (altura_valor * altura_valor)

            if imc <= 18.5:
                resultado = f"{nome_valor} está abaixo do peso"
            elif imc > 18.5 and imc <= 24.9:
                resultado = f"{nome_valor} está com o peso normal"
            elif imc > 24.9 and imc <= 29.9:
                resultado = f"{nome_valor} está com sobrepeso"
            elif imc > 29.9 and imc <= 34.9:
                resultado = f"{nome_valor} está com obesidade grau 1"
            elif imc > 34.9 and imc <= 39.9:
                resultado = f"{nome_valor} está com obesidade grau 2"
            else:
                resultado = f"{nome_valor} está com obesidade grau 3"

            page.open(ft.SnackBar(ft.Text(resultado),bgcolor="green"))
            page.update()
            with open("pessoa.txt", "a") as beraldo:
                beraldo.write(nome_valor + " | " + str(imc) + "\n")
        except Exception as ex:
            page.open(ft.SnackBar(ft.Text(resultado),bgcolor="red"))
            page.update()
    # Botão de ação
    botao = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc,width=300, height= 50)   


    # Adicionando elementos à página
    page.add(
        titulo,
        nome,
        peso,
        altura,
        botao,
        fundo
    )
    page.update()
ft.app(target=main)
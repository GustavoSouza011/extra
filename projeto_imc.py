import flet as ft

def main(page: ft.Page):
    page.title = "Projeto IMC"
    page.theme_mode = "dark"
    page.window.width = 380
    page.window.height = 480
    page.window_resizable = False
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Fundo como imagem expansível
    fundo = ft.Image(src="giphy (1).gif", expand=True, fit=ft.ImageFit.COVER)

    # Título
    titulo = ft.Text("Calculadora de IMC", size=30, weight="bold")

    # Campos de entrada
    nome = ft.TextField(label="Nome", width=300)
    peso = ft.TextField(label="Peso (kg)", width=300)
    altura = ft.TextField(label="Altura (m)", width=300,hint_text=(" utilize ponto ao invez de virgula"))
    def calcular_imc(e):
        try:
            nome_valor = nome.value
            peso_valor = float(peso.value)
            altura_valor = float(altura.value)
            imc = peso_valor / (altura_valor ** 2)

            if imc <= 18.5:
                resultado = f"{nome_valor} está abaixo do peso"
            elif imc <= 24.9:
                resultado = f"{nome_valor} está com o peso normal"
            elif imc <= 29.9:
                resultado = f"{nome_valor} está com sobrepeso"
            elif imc <= 34.9:
                resultado = f"{nome_valor} está com obesidade grau 1"
            elif imc <= 39.9:
                resultado = f"{nome_valor} está com obesidade grau 2"
            else:
                resultado = f"{nome_valor} está com obesidade grau 3"

            page.open(ft.SnackBar(ft.Text(resultado), bgcolor="green"))
            page.update()

            with open("pessoa.txt", "a") as beraldo:
                beraldo.write(f"{nome_valor} | {imc:.2f}\n")
        except:
            page.open(ft.SnackBar(ft.Text("Erro ao calcular. Verifique os dados!"), bgcolor="red"))
            page.update()

    botao = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc, width=300, height=50)

    # Conteúdo central empilhado sobre o fundo
    conteudo = ft.Column(
        controls=[titulo, nome, peso, altura, botao],
        alignment="center",
        horizontal_alignment="center"
    )

    # Empilha o fundo + conteúdo
    page.add(
        ft.Stack([
            fundo,
            conteudo
        ])
    )

ft.app(target=main)

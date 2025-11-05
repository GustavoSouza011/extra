import flet as ft


class InputField(ft.UserControl):
    def __init__(self, width, height, hint_text, icon,password=False,):
        super().__init__()
        self.body = ft.Container(
            content=ft.Row(
                [
                    ft.TextField(
                        color='white',
                        hint_text=hint_text,
                        border=InputBorder.NONE,
                        hint_style=ft.TextStyle(
                            color='white',
                        ),
                        width=width,
                        height=height/5*4,
                        bgcolor= 'transparent',
                        text_style=TextStyle(
                            size=18,
                            weight='w400',
                            password=password,
                            
                        )
                        expand=True,
                    ), ft.Icon(
                        icon,
                        color='white',)
                    
                ]
            ),
            width=width 
            alignment=alignment.center,
            border=ft.border.all(1, '#44f4f4f4'),
            border_radius=18,
            bgcolor='transparent',
            padding=8,
        )
    def build(self):
        return self.body   

def main(page: ft.Page):
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window.height = 500
    page.window.max_height = 500
    page.window.min_height = 500
    page.window.width = 600
    page.window.max_width = 600
    page.window.min_width = 600
    page.window.title_bar_hidden = True
    
    # Definindo a imagem de fundo
    image = ft.Image(
        src="essentials/michi luna.jfif",
        height=500,
        width=600,
        fit=ft.ImageFit.COVER
    )
    
    # Container com blur
    blur_container = ft.Container(
        content=ft.Container(
            content=ft.Column([
                ft.Text(
                    'Login',
                    color='white',
                    weight='w400',
                    size=20,
                    text_align='CENTER' 
                ),
                InputField(
                    width=300,
                    height=50,
                    hint_text='Username',
                    icon=ft.Icons.PERSON_ROUNDED

                    ),
                InputField(
                    width=300,
                    height=50,
                    hint_text='Password',
                    icon=ft.Icons.LOCK_ROUNDED,
                    password=True
                    
                    )

            ],alignment=MainAxisAlignment.CENTER),
            width=250,
            height=250,
            border_radius=20,
            # Aplicando o efeito de blur
            blur=ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
            border=ft.border.all(1, '#44f4f4f4'),
            alignment=ft.alignment.center,
        )
    )

    # Layout principal com a imagem de fundo e o blur centralizado
    body = ft.Container(
        content=ft.Stack(
            [
                image,  
                blur_container, 
            ],
            alignment=ft.alignment.center  # Alinhando tudo ao centro na Stack
        ),
    )
    
    page.add(body)

ft.app(target=main)

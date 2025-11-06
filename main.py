import flet as ft
import pygame
import random
import threading
import time

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Lista de músicas
playlist = [
    "take a 4 min Lofi Coffee Break - aesthetic R&B music for calming (FREE).mp3",
    "Bob Marley & The Wailers - Three Little Birds (Official Music Video).mp3",
    "01 Abertura Sonhei Trilha Sonora do Gueto.mp3",
    "Jesus Chorou.mp3"
]

def play_music():
    """Função que toca músicas em loop infinito aleatório."""
    ultima_musica = None
    while True:
        musica = random.choice([m for m in playlist if m != ultima_musica])
        ultima_musica = musica
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()
        print(f"Tocando: {musica}")
        while pygame.mixer.music.get_busy():
            time.sleep(1)

# Inicia o player em uma thread separada
music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

# Função para criar campos de input
def InputField(width, height, hint_text, icon, password=False):
    return ft.Container(
        content=ft.Row(
            [
                ft.TextField(
                    color='white',
                    hint_text=hint_text,
                    border=ft.InputBorder.NONE,
                    hint_style=ft.TextStyle(color='white'),
                    width=width,
                    height=height / 5 * 4,
                    bgcolor='transparent',
                    text_style=ft.TextStyle(size=20, weight='w400'),
                    password=password,
                    expand=True,
                ),
                ft.Icon(icon, color='white')
            ]
        ),
        width=width,
        alignment=ft.alignment.center,
        border=ft.border.all(1, '#44f4f4f4'),
        border_radius=18,
        bgcolor='transparent',
        padding=8,
    )

# Função principal da interface
def main(page: ft.Page):
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window.height = 500
    page.window.width = 600
    page.window.title_bar_hidden = True

    # Imagem de fundo
    image = ft.Image(
        src="download.gif",
        height=500,
        width=600,
        fit=ft.ImageFit.COVER
    )

    # Texto de login centralizado
    login_text = ft.Text(
        'Login',
        font_family='Vladimir Script',
        weight='w400',
        size=35,
        color='white',
        text_align='center'
    )

    # Container com blur e campos de login
    blur_container = ft.Container(
        content=ft.Column(
            [
                login_text,
                InputField(300, 50, 'Username', ft.Icons.PERSON_ROUNDED),
                InputField(300, 50, 'Password', ft.Icons.LOCK_ROUNDED, password=True),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Entrar",
                        on_click=lambda e: print("Botão 'Entrar' clicado!"),
                        bgcolor='transparent',
                        color='white',
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=18),
                            padding=ft.padding.symmetric(horizontal=40, vertical=12),
                            text_style=ft.TextStyle(size=18, weight='w400'),
                            side=ft.border.all(1, '#44f4f4f4')
                        )
                    ),
                    width=300,
                    alignment=ft.alignment.center
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=320,
        height=350,
        border_radius=20,
        bgcolor="rgba(0, 0, 0, 0.6)",
        border=ft.border.all(1, '#44f4f4f4'),
        alignment=ft.alignment.center,
        blur=ft.Blur(3, 5, ft.BlurTileMode.MIRROR),
    )

    # Layout principal
    body = ft.Container(
        content=ft.Stack(
            [
                image,
                blur_container
            ],
            alignment=ft.alignment.center
        ),
        width=600,
        height=500,
        alignment=ft.alignment.center
    )

    page.add(body)

# Executa o app Flet
ft.app(target=main)


ft.app(target=main)


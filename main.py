import flet as ft


body = ft.Container(
    content=ft.Stack(
        [
            ft.Image(
                src="assets/michi luna.jfif",
                height=500,
                width=800,
                fit=ft.ImageFit.COVER
            ),
            ft.Container(
                content=ft.Container(
                    width=400,
                    height=400,
                    
                    margin=ft.margin.only(top=120),
                    border_radius=18,
                    blur=ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
                    # border=ft.border.all(1, '#44f4f4f4'),
                ),alignment=ft.alignment.center
            )
        ]
    )
)

def main(page: ft.Page):
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window.height = 600
    page.window.max_height = 600
    page.window.min_height = 600
    page.window.width = 700
    page.window.max_width = 700
    page.window.min_width = 700
    page.window.title_bar_hidden = True
    page.window.center()
    page.add(body)

ft.app(target=main)
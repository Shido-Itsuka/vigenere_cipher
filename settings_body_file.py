# interface
import flet as ft
from flet_core import Container
from flet_core.control import Control


def settings_page(page: ft.Page) -> Container:
    settings_body = Container(
        expand=True,
        alignment=ft.alignment.center,
        # all settings
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            controls=[
                ft.Divider(10, color=ft.colors.TRANSPARENT),
                # row for container with activation menu
                ft.Row(
                    [
                        ft.Text('Тут могут быть настройки')
                    ],
                    alignment=ft.alignment.center,
                    spacing=20
                )
            ]
        )
    )

    return settings_body

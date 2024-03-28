import flet as ft
from flet_core import Container
from flet_core.control import Control


def info_page(page: ft.Page) -> Container:
    settings_body = Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.alignment.center,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text('О программе', weight=ft.FontWeight.BOLD),
                    ]
                )
            ]
        )
    )

    return settings_body

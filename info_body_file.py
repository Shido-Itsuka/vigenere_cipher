import flet as ft
from flet_core import Container
from flet_core.control import Control


def info_page(page: ft.Page) -> Container:
    settings_body = Container(
        # expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            'Лозунговый шифр | Vigenere cipher',
                            style=ft.TextThemeStyle.TITLE_SMALL,
                            size=22
                        ),
                        ft.Text(
                            'Версия | Version 0.9.0',
                            style=ft.TextThemeStyle.BODY_MEDIUM,
                            size=18
                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    'Ссылка на GitHub | GitHub link',
                                    style=ft.TextStyle(
                                        color=ft.colors.BLUE,
                                        size=18
                                    ),
                                    url='https://github.com/Shido-Itsuka/vigenere_cipher'
                                )
                            ]
                        ),
                        ft.Divider(
                            thickness=2,
                            height=25,
                            # color=ft.colors.TRANSPARENT,
                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Copyright © 2024 | ',
                                    style=ft.TextStyle(
                                        size=16
                                    )
                                ),
                                ft.TextSpan(
                                    text='Shido-Itsuka',
                                    style=ft.TextStyle(
                                        color=ft.colors.BLUE,
                                        size=16
                                    ),
                                    url='https://github.com/Shido-Itsuka'
                                ),
                                ft.TextSpan(
                                    text=' | All rights reserved.',
                                    style=ft.TextStyle(
                                        size=16
                                    )
                                )
                            ],
                            style=ft.TextThemeStyle.LABEL_LARGE
                        )
                    ]
                )
            ]
        )
    )

    return settings_body

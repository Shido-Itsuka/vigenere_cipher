import flet as ft
from flet_core import Container
from flet_core.control import Control
from networkx import radius
from networkx.algorithms.bipartite import color


def info_page(page: ft.Page) -> Container:
    code_info = """    В поле "Текст для шифрования" вводится текст, который необходимо зашифровать. Также, можно нажать на кнопку "Вставить" для вставки текста из буфера обмена.
    В поле для ввода ключа вводится ключ, который необходимо использовать при шифровании, но также можно нажать на кнопку "Генерировать" для генерации случайного ключа.
    После ввода текста и ключа будет разблокирована кнопка "Шифровать". Для шифрования текста следует нажать на нее.
    В поле "Зашифрованный текст" появится зашифрованный текст. Для копирования зашифрованного текста нажмите на кнопку "Копировать".
    После нажатия на кнопку "Очистить" все поля будут очищены."""
    decode_info = """    В поле "Текст для дешифрования" вводится текст, который необходимо зашифровать. Также, можно нажать на кнопку "Вставить" для вставки текста из буфера обмена.
    В поле для ввода ключа вводится ключ, который необходимо использовать при дешифровании, но также можно нажать на кнопку "Генерировать" для генерации случайного ключа.
    После ввода текста и ключа будет разблокирована кнопка "Дешифровать". Для дешифрования текста следует нажать на нее.
    В поле "Расшифрованный текст" появится расшифрованный текст. Для копирования расшифрованного текста нажмите на кнопку "Копировать".
    После нажатия на кнопку "Очистить" все поля будут очищены."""
    settings_info = """    В данный момент настроек приложения нет. Вы можете нажать на кнопку "Настройки" для перехода к настройкам приложения."""
    info_info = """    В этом разделе находится информация о приложении и разработчике, а также справка по использованию приложения."""
    settings_body = Container(
        # expand=True,
        alignment=ft.alignment.top_center,
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
                            size=22,
                            selectable=True
                        ),
                        ft.Text(
                            'Версия | Version 0.9.0',
                            style=ft.TextThemeStyle.BODY_MEDIUM,
                            size=18,
                            selectable=True
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
                            ],
                            selectable=True
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
                            style=ft.TextThemeStyle.LABEL_LARGE,
                            selectable=True
                        ),
                        ft.Divider(
                            thickness=2,
                            height=10,
                            color=ft.colors.TRANSPARENT,
                        ),
                        ft.ExpansionTile(
                            title=ft.Text("Справка"),
                            # subtitle=ft.Text("Leading expansion arrow icon"),
                            affinity=ft.TileAffinity.LEADING,
                            maintain_state=True,
                            # shape=ft.RoundedRectangleBorder(radius=0),
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                'Шифрование',
                                                style=ft.TextThemeStyle.TITLE_SMALL,
                                                size=20,
                                                selectable=True
                                            ),
                                            ft.Text(
                                                'Кодирование текста с использованием'
                                                ' лозунгового шифра (шифра Виженера).',
                                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                                size=18,
                                                selectable=True,
                                                italic=True
                                            ),
                                            ft.Text(
                                                value=code_info,
                                                size=16,
                                                selectable=True
                                            ),
                                            ft.Divider(
                                                height=25,
                                                thickness=2
                                            ),
                                            ft.Text(
                                                'Дешифрование',
                                                style=ft.TextThemeStyle.TITLE_SMALL,
                                                size=20,
                                                selectable=True
                                            ),
                                            ft.Text(
                                                'Декодирование текста с использованием'
                                                ' лозунгового шифра (шифра Виженера).',
                                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                                size=18,
                                                selectable=True,
                                                italic=True
                                            ),
                                            ft.Text(
                                                value=decode_info,
                                                size=16,
                                                selectable=True
                                            ),
                                            ft.Divider(
                                                height=25,
                                                thickness=2
                                            ),
                                            ft.Text(
                                                'Настройки',
                                                style=ft.TextThemeStyle.TITLE_SMALL,
                                                size=20,
                                                selectable=True
                                            ),
                                            ft.Text(
                                                'Настройки приложения.',
                                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                                size=18,
                                                selectable=True,
                                                italic=True
                                            ),
                                            ft.Text(
                                                value=settings_info,
                                                size=16,
                                                selectable=True
                                            ),
                                            ft.Divider(
                                                height=25,
                                                thickness=2
                                            ),
                                            ft.Text(
                                                'О программе',
                                                style=ft.TextThemeStyle.TITLE_SMALL,
                                                size=20,
                                                selectable=True
                                            ),
                                            ft.Text(
                                                'Информация о программе.',
                                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                                size=18,
                                                selectable=True,
                                                italic=True
                                            ),
                                            ft.Text(
                                                value=info_info,
                                                size=16,
                                                selectable=True
                                            ),
                                            ft.Divider(
                                                height=25,
                                                thickness=2,
                                                color=ft.colors.TRANSPARENT
                                            ),
                                        ],
                                        spacing=10
                                    ),
                                    padding=0,
                                )
                            ],
                        ),

                    ],
                )
            ],
            scroll=ft.ScrollMode.HIDDEN
        )
    )

    return settings_body

import flet as ft
from flet_core.control import Control
import module
import re
import random as rd


def main(page: ft.Page) -> None:
    page.title = 'Vigner Cipher'
    page.window_focused = True
    page.theme_mode.SYSTEM = True

    page.window_maximizable = False
    page.window_minimizable = True
    page.window_resizable = False

    page.window_height = 600
    page.window_width = 900
    page.padding = 0
    page.window_center()

    page.theme = ft.Theme(
        color_scheme_seed='#5a84ff'
    )

    def on_change_rail(e):
        match e.control.selected_index:
            case 0:
                main_body.content = code_body
            case 1:
                main_body.content = decode_body
            case 2:
                main_body.content = settings_body
            case 3:
                main_body.content = info_body
        page.update()

    def on_change_text_input(e):
        if text_input.value == '':
            key_input.disabled = True
            key_input.value = ''
            text_input.data = None
            key_input.max_length = None
            key_input.update()
            text_input.error_text = None
            text_input.update()
        else:
            if re.fullmatch(r'[а-яА-ЯёЁ]+', text_input.value):
                text_input.data = 'RU'
                key_input.suffix_text = 'RU'
                key_input.disabled = False
                key_input.max_length = 33
                key_input.update()
                text_input.error_text = None
            elif re.fullmatch(r'[a-zA-Z]+', text_input.value):
                text_input.data = 'EN'
                key_input.suffix_text = 'EN'
                key_input.disabled = False
                key_input.max_length = 26
                key_input.update()
                text_input.error_text = None
            else:
                text_input.error_text = 'Только русский или английский текст'
                text_input.data = '??'
                key_input.disabled = True

        page.update()

    def on_click_paste(e):
        text_input.value = page.get_clipboard()
        text_input.update()
        text_input.on_change(e)

    def on_click_generate_key(e):
        if text_input.data == 'RU':
            letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            length = rd.randint(4, len(letters)-4)
            out = ''.join(rd.sample(letters, length))
            key_input.value = out
            key_input.update()

        elif text_input.data == 'EN':
            letters = 'abcdefghigklmnopqrstuvwxyz'
            length = rd.randint(4, len(letters) - 4)
            out = ''.join(rd.sample(letters, length))
            key_input.value = out
            key_input.update()
        elif text_input.data == '??':
            print('Undefined')
        else:
            pass

    def on_click_copy(e):
        pass

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,
        bgcolor=ft.colors.TRANSPARENT,
        min_width=100,
        min_extended_width=200,
        group_alignment=0,
        on_change=on_change_rail,
        indicator_color=ft.colors.TRANSPARENT,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.ENHANCED_ENCRYPTION_OUTLINED,
                    color=ft.colors.WHITE54
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.ENHANCED_ENCRYPTION,
                    color=ft.colors.WHITE
                ),
                label='Шифрование',
                padding=20
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.NO_ENCRYPTION_OUTLINED,
                    color=ft.colors.WHITE54
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.NO_ENCRYPTION,
                    color=ft.colors.WHITE
                ),
                label='Дешифрование',
                padding=20
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.SETTINGS_OUTLINED,
                    color=ft.colors.WHITE54
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.SETTINGS,
                    color=ft.colors.WHITE
                ),
                label='Настройки',
                padding=20
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    name=ft.icons.HELP_OUTLINE,
                    color=ft.colors.WHITE54
                ),
                selected_icon_content=ft.Icon(
                    name=ft.icons.HELP,
                    color=ft.colors.WHITE
                ),
                label='О программе',
                padding=20
            )
        ],
    )

    code_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.alignment.center,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.PASTE,
                            tooltip='Вставить',
                            icon_color=ft.colors.ON_BACKGROUND,
                            on_click=on_click_paste
                        ),

                        text_input := ft.TextField(
                            max_lines=5,
                            multiline=True,
                            width=355,
                            border_color=ft.colors.OUTLINE,
                            focused_border_color=ft.colors.ON_SURFACE_VARIANT,
                            label='Текст для шифрования',
                            hint_text='Введите текст для шифрования',
                            input_filter=ft.InputFilter(allow=True, regex_string=r"[a-zA-Zа-яА-ЯёЁ]",
                                                        replacement_string=""),
                            on_change=on_change_text_input
                        )
                    ]
                ),

                ft.Row(
                    spacing=20,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CASINO_OUTLINED,
                            tooltip='Генерировать',
                            on_click=on_click_generate_key
                        ),
                        key_input := ft.TextField(
                            width=355,
                            border_color=ft.colors.OUTLINE,
                            focused_border_color=ft.colors.ON_SURFACE_VARIANT,
                            max_lines=2,
                            label='Ключ',
                            hint_text='Введите ключ',
                            capitalization=ft.TextCapitalization.CHARACTERS,
                            suffix_text='',
                            disabled=True,
                            input_filter=ft.InputFilter(allow=True,
                                                        regex_string=r"[a-zA-Z]",
                                                        replacement_string="")
                        ),
                        ft.VerticalDivider(
                            visible=True,
                            width=40
                        ),
                        ft.OutlinedButton(
                            text='Шифровать',
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                            scale=1.2
                        )
                    ]
                ),

                ft.Row(
                    spacing=20,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.COPY,
                            tooltip='Копировать'
                        ),

                        ft.TextField(
                            read_only=True,
                            max_lines=5,
                            multiline=True,
                            width=355,
                            border_color=ft.colors.OUTLINE,
                            focused_border_color=ft.colors.ON_SURFACE_VARIANT,
                            label='Зашифрованный текст'

                        )
                    ]
                )
            ]
        )
    )
    decode_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Text('Дешифрование')
    )

    settings_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Text('Настройки')
    )

    info_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Text('О программе')
    )

    main_body = ft.Container(
        padding=10,
        margin=ft.margin.only(left=20),
        expand=True,
        content=code_body
    )

    main_container = ft.Stack(
        expand=True,
        controls=[
            ft.Image(src='assets/bg_low.png',
                     width=page.window_width,
                     height=page.window_height,
                     fit=ft.ImageFit.COVER,
                     ),
            ft.Container(
                padding=0,
                content=ft.Row(
                    spacing=0,
                    controls=[
                        rail,
                        ft.VerticalDivider(width=1),
                        main_body
                    ],
                    expand=True
                ),
                expand=True
            )
        ]
    )

    page.add(
        main_container
    )

    page.update()


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    ft.app(target=main,
           assets_dir='assets'
           )

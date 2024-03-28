import flet as ft
from flet_core import Container
from flet_core.control import Control
import re
import random as rd
import module


def decode_page(page: ft.Page) -> Container:
    def on_change_text_input(e: Control):
        text_output.value = ''
        text_output.disabled = True
        text_output.update()
        if text_input.value == '':
            key_input.disabled = True
            key_input.value = ''
            text_input.data = None
            key_input.max_length = None
            key_input.update()
            text_input.error_text = None
            text_input.update()
            decode_button.disabled = True
            decode_button.update()
        else:
            if re.fullmatch(r'[а-яА-ЯёЁ\n ]+', text_input.value):
                text_input.data = 'RU'
                key_input.suffix_text = 'RU'
                key_input.disabled = False
                key_input.max_length = 33
                key_input.input_filter.regex_string = r"[а-яА-ЯёЁ\n]"
                key_input.update()
                text_input.error_text = None
            elif re.fullmatch(r"[a-zA-Z\n ]+", text_input.value):
                text_input.data = 'EN'
                key_input.suffix_text = 'EN'
                key_input.disabled = False
                key_input.max_length = 26
                key_input.input_filter.regex_string = r"[a-zA-Z\n]"
                key_input.update()
                text_input.error_text = None
            else:
                text_input.error_text = 'Только русский или английский текст'
                text_input.data = '??'
                key_input.disabled = True
                decode_button.disabled = True
                decode_button.update()
        page.update()

    def on_click_paste(e: Control):
        text_input.value = page.get_clipboard()
        text_input.update()
        text_input.on_change(e)

    def on_click_generate_key(e: Control):
        if text_input.data == 'RU':
            letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            length = rd.randint(4, len(letters) - 4)
            out = (''.join(rd.sample(letters, length))).upper()
            key_input.value = out
            key_input.update()

        elif text_input.data == 'EN':
            letters = 'abcdefghigklmnopqrstuvwxyz'
            length = rd.randint(4, len(letters) - 4)
            out = (''.join(rd.sample(letters, length))).upper()
            key_input.value = out
            key_input.update()
        elif text_input.data == '??':
            print('Undefined')
        else:
            pass
        on_change_key_input(e)

    def on_change_key_input(e: Control):
        if key_input.value != '':
            decode_button.disabled = False
            decode_button.update()
        else:
            decode_button.disabled = True
            decode_button.update()
        text_output.value = ''
        text_output.disabled = True
        text_output.update()

    def on_click_decode(e: Control):
        out = module.vigenere_decipher(
            ciphertext=text_input.value,
            key=key_input.value,
        )
        text_output.disabled = False
        text_output.value = out
        text_output.update()

    def on_click_copy(e: Control):
        if not text_output.disabled:
            page.set_clipboard(text_output.value)

    decode_body = ft.Container(
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
                            label='Текст для дешифрования',
                            hint_text='Введите текст для дешифрования',
                            input_filter=ft.InputFilter(allow=True, regex_string=r"[a-zA-Zа-яА-ЯёЁ\n ]",
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
                                                        replacement_string=""),
                            on_change=on_change_key_input
                        ),
                        ft.VerticalDivider(
                            visible=True,
                            width=40
                        ),
                        decode_button := ft.OutlinedButton(
                            text='Дешифровать',
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                            scale=1.2,
                            on_click=on_click_decode,
                            disabled=True
                        )
                    ]
                ),

                ft.Row(
                    spacing=20,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.COPY,
                            tooltip='Копировать',
                            on_click=on_click_copy
                        ),

                        text_output := ft.TextField(
                            read_only=True,
                            max_lines=5,
                            multiline=True,
                            width=355,
                            border_color=ft.colors.OUTLINE,
                            focused_border_color=ft.colors.ON_SURFACE_VARIANT,
                            label='Расшифрованный текст',
                            disabled=True,
                        )
                    ]
                )
            ]
        )
    )

    return decode_body

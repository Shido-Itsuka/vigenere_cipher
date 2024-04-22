import flet as ft
from flet_core import Container
from flet_core.control import Control
import keygen


def settings_page(page: ft.Page) -> Container:

    def anim_act_menu(status: bool):
        if status is True:
            act_menu.shadow = ft.BoxShadow(
                spread_radius=15,
                blur_radius=15,
                color=ft.colors.GREEN_500,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER
            )
            page.update()
            print('Anim status true')
        elif status is False:
            act_menu.bgcolor = ft.colors.RED_500
            page.update()

    def submit_license(e):
        k = keygen.KeyInput(license_input.value)
        if k.main() is True:
            page.snack_bar = ft.SnackBar(
                ft.Text('Активация прошла успешно!')
            )
            page.snack_bar.open = True
            anim_act_menu(True)
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text('Неверный лицензионный ключ!')
            )
            page.snack_bar.open = True
            anim_act_menu(False)
        page.update()

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
                    controls=[
                        # activation menu
                        act_menu := ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        'Активация',
                                        size=20
                                    ),
                                    license_input := ft.TextField(
                                        label='Лицензионный ключ',
                                        hint_text='Введите код для активации программы',
                                        max_length=23
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.OutlinedButton(
                                                text='Активировать',
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.BLUE
                                                    },
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                ),
                                                on_click=submit_license

                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    )
                                ],
                                spacing=20
                            ),
                            blur=ft.Blur(
                                10,
                                12,
                                ft.BlurTileMode.MIRROR
                            ),
                            border=ft.border.all(1, ft.colors.WHITE24),
                            border_radius=ft.border_radius.all(10),
                            width=400,
                            padding=15,
                            animate=ft.animation.Animation(
                                curve=ft.AnimationCurve.EASE_IN_OUT_CIRC,
                                duration=1
                            )
                        )
                    ],
                    alignment=ft.alignment.center
                )
            ]
        )
    )

    return settings_body

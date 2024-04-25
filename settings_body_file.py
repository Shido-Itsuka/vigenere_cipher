import flet as ft
from flet_core import Container
from flet_core.control import Control
import keygen


def settings_page(page: ft.Page) -> Container:

    def anim_act_menu(status: bool):
        # if status is True:
        #     act_menu.shadow = ft.BoxShadow(
        #         spread_radius=15,
        #         blur_radius=15,
        #         color=ft.colors.GREEN_500,
        #         offset=ft.Offset(0, 0),
        #         blur_style=ft.ShadowBlurStyle.OUTER
        #     )
        #     print('Anim status true')
        # elif status is False:
        #     act_menu.bgcolor = ft.colors.with_opacity(0.25, ft.colors.RED_500)
        #
        page.update()

    def submit_license(e):
        k = keygen.KeyInput(license_input.value)
        if k.main() is True:
            page.snack_bar = ft.SnackBar(
                ft.Text('Активация прошла успешно!'),
                dismiss_direction=ft.DismissDirection.DOWN,
            )
            page.snack_bar.open = True
            anim_act_menu(True)
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text('Неверный лицензионный ключ!'),
                dismiss_direction=ft.DismissDirection.DOWN,
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
                                duration=200
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                'Активировано',
                                                size=20
                                            ),
                                            ft.Icon(
                                                ft.icons.CHECK_CIRCLE_OUTLINE,
                                                color=ft.colors.GREEN_500
                                            )
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                'Тип лицензии:',
                                                size=16
                                            ),
                                            ft.Text(
                                                'Полноценная',
                                                size=16
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.START
                                    ),
                                    ft.Divider(
                                        20,
                                        2
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            '30:00',
                                            size=40
                                        ),
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        expand=True
                                    )
                                ],
                                expand=True,
                                spacing=15,
                                alignment=ft.MainAxisAlignment.START
                            ),
                            blur=ft.Blur(
                                10,
                                12,
                                ft.BlurTileMode.MIRROR
                            ),
                            border=ft.border.all(1, ft.colors.WHITE24),
                            border_radius=ft.border_radius.all(10),
                            padding=15,
                            expand=True,
                            height=229
                        ),
                        ft.VerticalDivider(0, color=ft.colors.TRANSPARENT),
                    ],
                    alignment=ft.alignment.center,
                    spacing=20
                )
            ]
        )
    )

    return settings_body


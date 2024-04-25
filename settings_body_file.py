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
            act_status.value = 'Активировано'
            act_status_icon.selected = True
            license_type.value = k.type
            license_type_row.visible = True
            timer_container.visible = False
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
                                        max_length=23,
                                        border_color=ft.colors.WHITE24,
                                        focused_border_color=ft.colors.ON_SURFACE_VARIANT,
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
                            height=230,
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
                                            act_status := ft.Text(
                                                'Не активировано',
                                                # size=20,
                                                theme_style=ft.TextThemeStyle.TITLE_LARGE,
                                            ),
                                            act_status_icon := ft.IconButton(
                                                icon=ft.icons.WARNING_AMBER_ROUNDED,
                                                icon_color=ft.colors.YELLOW_800,
                                                selected_icon=ft.icons.CHECK_CIRCLE_OUTLINE_ROUNDED,
                                                selected_icon_color=ft.colors.GREEN_500,
                                                disabled=True
                                            )
                                        ],
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.START
                                    ),
                                    license_type_row := ft.Row(
                                        controls=[
                                            ft.Text(
                                                'Тип лицензии:',
                                                size=15,
                                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                                weight=ft.FontWeight.W_500
                                            ),
                                            license_type := ft.Text(
                                                '',
                                                size=15,
                                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,

                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        visible=False
                                    ),
                                    ft.Divider(
                                        20,
                                        2
                                    ),
                                    timer_container := ft.Container(
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
                            height=230
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

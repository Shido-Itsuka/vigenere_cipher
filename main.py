import flet as ft
from flet_core.control import Control

import decode_body_file
import code_body_file
import settings_body_file
import info_body_file


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

    # needs to be rewritten or deleted from here

    code_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=code_body_file.code_page(page)
    )

    decode_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=decode_body_file.decode_page(page)
    )

    settings_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=settings_body_file.settings_page(page)
    )

    info_body = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=info_body_file.info_page(page)
    )

    main_body = ft.Container(
        padding=10,
        margin=ft.margin.only(left=20),
        expand=True,
        content=code_body
    )

    # to here

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

    # logging.basicConfig(level=logging.DEBUG)

    ft.app(target=main,
           assets_dir='assets'
           )

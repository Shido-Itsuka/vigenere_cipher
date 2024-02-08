import flet as ft
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.title = 'Vigner Cipher'
    page.window_focused = True
    page.theme_mode.SYSTEM = True

    page.window_maximizable = False
    page.window_minimizable = False
    page.window_resizable = False

    page.window_height = 600
    page.window_width = 800
    page.window_center()

    page.theme = ft.Theme(
        color_scheme_seed='#5a84ff'
    )

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=0,

        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.ENHANCED_ENCRYPTION_OUTLINED,
                selected_icon=ft.icons.ENHANCED_ENCRYPTION,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.NO_ENCRYPTION_OUTLINED,
                selected_icon=ft.icons.NO_ENCRYPTION,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP
            )
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index)
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [
                        ft.Text('DUDUDU!'),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                )
            ],
            expand=True
        )
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets',

           )

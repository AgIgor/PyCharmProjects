import flet as ft
import time


def main(page: ft.Page):
    page.title = "Meu app"
    page.window_width = 800
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(value="5", text_align=ft.TextAlign.CENTER, width=50)

    def theme(e):
        e.control.selected = not e.control.selected
        e.control.update()

        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    def decrement(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def increment(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    slct = False

    def counter_start(e):
        e.control.selected = not e.control.selected
        if e.control.selected:
            for i in range(int(txt_number.value)):
                slct = True
                txt_number.value = str(int(txt_number.value) - 1)
                page.update()
                time.sleep(1)
                if not e.control.selected:
                    break
        else:
            slct = False
            page.update()

    page.add(
        ft.Container(
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.DARK_MODE,
                        on_click=theme,
                        selected_icon=ft.icons.LIGHT_MODE,
                        selected=False,
                    ),
                    ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=increment),
                    ft.IconButton(ft.icons.TIMER, on_click=counter_start,
                                  selected=False,
                                  # style=ft.ButtonStyle(color={"selected":ft.colors.GREEN, "":ft.colors.GREY}),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

# flet run main.py -d

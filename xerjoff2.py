import flet as ft

def main(page: ft.Page):
    page.title = "erbapura"

    title_label = ft.Text(value="Title Label")
    number_label = ft.Text(value="Number Label")

    img = ft.Image(src="erbapura.png")

    def add1(e):
        prenumb = int(number.value)
        prenumb += 1
        number.value = str(prenumb)
        page.update()

    def minus1(e):
        prenumb = int(number.value)
        prenumb -= 1
        number.value = str(prenumb)
        page.update()

    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    gamename = ft.Text(value="Treats for imghildo")
    number = ft.Text(value="0")

    plusb = ft.ElevatedButton(text="+", on_click=add1)
    minusb = ft.ElevatedButton(text="-", on_click=minus1)

    rowButtons = ft.Row(controls=[minusb, plusb], alignment=ft.MainAxisAlignment.CENTER)

    cologne_img = ft.Image(src="erbapura.png")

    page.add(gamename, title_label, number_label, number, rowButtons, cologne_img)

ft.app(target=main)

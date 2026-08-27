import flet as ft


def main(page: ft.Page):
    page.title = "Simple Linear Regression"
    test_run = ft.Text("Hello", size=50)
    page.add(test_run)


if __name__ == "__main__":
    ft.run(main)

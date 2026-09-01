import flet as ft

import ols


def main(page: ft.Page):
    page.title = "Simple Linear Regression"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10.01]
    lm = ols.LinearModel()
    if lm.pValue(y, x)[2] > 0.005:
        pval_cond = "Fail to Reject $H_{{0}}$"
    else:
        pval_cond = "Reject $H_{{0}}$"

    variable_container = ft.Column(
        width=ft.Window.width,
        height=ft.Window.height,
        spacing=10,
        controls=[
            ft.Markdown(
                value=(f"$\\mathbf{{x}} = {x}^{{\\textsf{{T}}}}$"),
                width=ft.Window.width,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\mathbf{{y}} = {y}^{{\\textsf{{T}}}}$"),
                width=ft.Window.width,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\hat{{y}} = {round(lm.estimateIntercept(y, x), 4)} + {round(lm.estimateSlope(y, x), 4)}x$\n\n"
                    f"$\\text{{p-value}} = {round(lm.pValue(y, x)[2], 4)} \\implies \\text{{{pval_cond}}}$\n\n"
                    f"$\\hat{{\\sigma}} = {round(lm.regressionStandardError(y, x), 4)}$\n\n"
                    f"$\\mathrm{{R}}^{2} = {round(lm.coefficientOfDetermination(y, x), 40):2.2%}$".replace(
                        "%", "\\%"
                    )
                ),
                width=ft.Window.width,
                selectable=True,
            ),
        ],
    )
    page.add(
        variable_container,
    )


if __name__ == "__main__":
    ft.run(main)

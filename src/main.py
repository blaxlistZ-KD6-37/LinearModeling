import flet as ft

import ols


def main(page: ft.Page):
    page.title = "Simple Linear Regression"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    x = [1.2, 1.27, 1.35, 1.36, 1.16, 1.16, 1.22, 1.23, 1.27, 1.42]
    y = [1.2, 1.4, 1.5, 1.6, 1.6, 1.7, 1.7, 1.7, 1.8, 1.8]
    lm = ols.LinearModel()
    variable_container = ft.Column(
        width=ft.Window.width,
        height=ft.Window.height,
        spacing=10,
        controls=[
            ft.Markdown(
                value=(f"$\\mathbf{{x}} = {x}^{{\\textsf{{T}}}}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\mathbf{{y}} = {y}^{{\\textsf{{T}}}}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\beta_{{0}} = {lm.estimateIntercept(y, x)}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\beta_{{1}} = {lm.estimateSlope(y, x)}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\hat{{\\sigma}} = {lm.regressionStandardError(y, x)}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\mathrm{{SE}}\\left(\\beta_{0}~|~X\\right) = {(se := lm.estimateStandardError(y, x))[0]}$\n"
                    f"$\\mathrm{{SE}}\\left(\\beta_{{1}}~|~X\\right) = {se[1]}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$t\\text{{-value}}_{{\\beta_{0}}} = {(t_val := lm.tValue(y, x))[0]}$\n"
                    f"$t\\text{{-value}}_{{\\beta_{1}}} = {t_val[1]}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$p\\text{{-value}}_{{\\beta_{0}}} = {(p_val := lm.pValue(y, x))[0]}$\n"
                    f"$p\\text{{-value}}_{{\\beta_{1}}} = {p_val[1]}\n$"
                    f"$p\\text{{-value}}_{{\\text{{model}}}} = {p_val[2]}\n$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\mathrm{{R}}^{{2}} = {lm.coefficientOfDetermination(y, x)}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\mathrm{{R}}_{{\\text{{adj}}}}^{{2}} = {lm.adjustedCoefficientofDetermination(y, x)}$"
                ),
                width=260,
                selectable=True,
            ),
        ],
    )
    page.add(
        variable_container,
    )


if __name__ == "__main__":
    ft.run(main)

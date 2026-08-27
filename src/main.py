import flet as ft

import ols


def main(page: ft.Page):
    page.title = "Simple Linear Regression"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ls = ols.RegressionStatistics()
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
                value=(
                    f"$\\bar{{x}} = {ls.sampleMean(x)}$, $\\bar{{y}} = {ls.sampleMean(y)}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\texttt{{SXX}} = {ls.sumOfSquares(x)}$, $\\texttt{{SYY}} = {ls.sumOfSquares(y)}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\sigma_{{\\mathbf{{x}}}} = {ls.sampleStandardDeviation(x)}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(
                    f"$\\sigma_{{\\mathbf{{y}}}} = {ls.sampleStandardDeviation(y)}$"
                ),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$\\texttt{{SXY}} = {ls.sumOfCrossProducts(x, y)}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$s_{{\\mathbf{{xy}}}} = {ls.sampleCovariance(x, y)}$"),
                width=260,
                selectable=True,
            ),
            ft.Markdown(
                value=(f"$r_{{\\mathbf{{xy}}}} = {ls.sampleCorrelation(x, y)}$"),
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

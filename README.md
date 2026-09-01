# Simple Linear Regression Visualizer

## Running on uv

Running the source app:

```bash
uv run flet run --<options>
```

1. `web` --- To run on the web.
2. `android` --- To run on the flet app.

## Upcoming Features

### 1. Regression Statistics

These shall include the following:

1. Sample Mean

```math
\bar{u} = \dfrac{1}{n}\displaystyle\sum_{i = 1}^{n}u_{i}
```

2. Sum of Squares:

```math
\texttt{SS}_{\mathbf{u}} = \displaystyle\sum_{i = 1}^{n}(u_{i} - \bar{u})^{2}
```

3. Sample Variance:

```math
s_{\mathbf{u}}^{2} = \dfrac{\texttt{SS}_{\mathbf{u}}}{n - 1}
```

4. Sample Standard Deviation:

```math
s_{\mathbf{u}} = \sqrt{\dfrac{\texttt{SS}_{\mathbf{u}}}{n - 1}}
```

5. Sum of Cross Products:

```math
\texttt{SS}_{\mathbf{uv}} = \displaystyle\sum_{i = 1}^{n}(u_{i}-\bar{u})(v_{i} - \bar{v})
```

6. Sample Covariance:

```math
\textrm{Cov}(\mathbf{u},\mathbf{v}) = \dfrac{\texttt{SS}_{\mathbf{uv}}}{n-1}
```

7. Sample Correlation:

```math
\textrm{Cor}(\mathbf{u},\mathbf{v}) = \dfrac{\textrm{Cov}(\mathbf{u},\mathbf{v})}{s_{\mathbf{u}}\cdot s_{\mathbf{v}}}
```

### 2. Fitted Value and Estimators

These shall include:

1. Fitted Model:

```math
\hat{y} = \hat{\beta}_{0} + \hat{\beta_{1}}x
```

2. Intercept Estimate:

```math
\hat{\beta}_{0} = \bar{y} - \hat{\beta}_{1}\bar{x}
```

3. Slope Estimate:

```math
\hat{\beta_{1}} = \dfrac{\texttt{S}_{\mathbf{xy}}}{\texttt{SS}_{\mathbf{x}}}
```

4. Residual Sum of Squares:

```math
\texttt{SS}_{\mathbf{r}} = \texttt{SS}_{\mathbf{y}} - \hat{\beta}_{1}^{2}\texttt{SS}_{\mathbf{x}}
```

5. Regression Sum of Squares:

```math
\texttt{SS}_{\text{reg}} = \texttt{SS}_{\mathbf{y}} - \texttt{SS}_{\mathbf{r}}
```

6. Standard Error of Regression:

```math
\hat{\sigma} = \sqrt{\dfrac{\texttt{SS}_{\mathbf{r}}}{n-2}}
```

7. Variance Estimates:

```math
\widehat{\mathrm{Var}}\left(\pmb{\hat{\beta}}~\big|~X\right) = \dfrac{\hat{\sigma}^{2}}{\texttt{SS}_{\mathbf{x}}}\begin{bmatrix}\frac{\mathtt{SS}_{\mathbf{x}} + n\bar{x}^{2}}{n} \\ 1 \end{bmatrix}
```

8. Standard Error:

```math
\mathrm{SE}\left(\pmb{\hat{\beta}}~\big|~X\right) = \sqrt{\widehat{\mathrm{Var}}\left(\pmb{\hat{\beta}}~\big|~X\right)}
```

9. T-values:

```math
\mathbf{t}_{\text{value}} = \dfrac{\pmb{\hat{\beta}}}{\mathrm{SE}\left(\pmb{\hat{\beta}}~\big|~X\right)}
```

10. F-statistic:

```math
F_{\text{stat}} = \dfrac{\texttt{SS}_{\text{reg}}}{\hat{\sigma}^{2}}
```

11. P-values (2-tailed):

```math
\mathbf{p}_{\text{value}} = 2\left[1 - t_{\nu}\left(t_{\text{value}}^{\left(\hat{\beta}_{k}\right)}, n - 2\right)\right],~k = 0,1\qquad\text{(For t-statistic)}
```

```math
\text{p-value} = 1 - F(F_{\text{stat}}, 1, n - 2)\qquad\qquad\qquad\text{(For F-statistic)}
```

12. Coefficient of Determination:

```math
\mathrm{R}^{2} = 1 -  \dfrac{\texttt{SS}_{\mathbf{r}}}{\texttt{SS}_{\mathbf{y}}}
```

```math
\mathrm{R}_{\text{adj}}^{2} = 1 - \dfrac{\texttt{SS}_{\mathbf{r}}}{\texttt{SS}_{\mathbf{y}}}\left(\dfrac{n-1}{n-2}\right)
```

### 3. Plot Visualizations

### 4. Derivations

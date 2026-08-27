# Simple Linear Regression Visualizer

## Running on uv

Runing the source app:

```bash
uv run flet run --<options>
```
1. `web` - To run on the web.
2. `android` - To run on the flet app.

## Upcoming Features

### 1. Regression Statistics
These shall include the following:
$$
\begin{align}
\tag{mean} \bar{u} &= \dfrac{1}{n}\displaystyle\sum_{i = 1}^{n}u_{i} \\
\tag{ss} \texttt{SS}_{\mathbf{u}} &= \displaystyle\sum_{i = 1}^{n}(u_{i} - \bar{u})^{2} \\
\tag{var} s_{\mathbf{u}}^{2} &= \dfrac{\texttt{SS}_{\mathbf{u}}}{n - 1} \\
\tag{stdev} s_{\mathbf{u}} &= \sqrt{\dfrac{\texttt{SS}_{\mathbf{u}}}{n - 1}} \\
\tag{cross-prod} \texttt{SS}_{\mathbf{uv}} &= \displaystyle\sum_{i = 1}^{n}(u_{i}-\bar{u})(v_{i} - \bar{v}) \\
\tag{covar} \operatorname{Cov}(\mathbf{u},\mathbf{v}) &= \dfrac{\texttt{SS}_{\mathbf{uv}}}{n-1} \\
\tag{corr} \operatorname{Cor}(\mathbf{u},\mathbf{v}) &= \dfrac{\operatorname{Cov}(\mathbf{u},\mathbf{v})}{s_{\mathbf{u}}\cdot s_{\mathbf{v}}}
\end{align}
$$

### 2. Fitted Value and Estimators
These shall include:
$$
\begin{align}
\tag{linear model}\hat{y} &= \hat{\beta}_{0} + \beta_{1}x \\
\tag{intercept coef.} \hat{\beta}_{0} &= \bar{y} - \hat{\beta}_{1}\bar{x} \\
\tag{slope est.} \hat{\beta_{1}} &= \dfrac{\texttt{SXY}}{\texttt{SXX}}
\end{align}
$$

### 3. Plot Visualizations

### 4. Derivations
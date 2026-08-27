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
$$\bar{u} = \dfrac{1}{n}\displaystyle\sum_{i = 1}^{n}u_{i}$$

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

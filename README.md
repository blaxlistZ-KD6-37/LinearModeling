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
\hat{y} = \hat{\beta}_{0} + \beta_{1}x
```

2. Intercept Estimate: 
```math
\hat{\beta}_{0} = \bar{y} - \hat{\beta}_{1}\bar{x}
```

3. Slope Estimate: 
```math
\hat{\beta_{1}} = \dfrac{\texttt{SXY}}{\texttt{SXX}}
```

### 3. Plot Visualizations

### 4. Derivations

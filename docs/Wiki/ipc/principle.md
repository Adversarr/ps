# Principle of IPC

## Contact Model

Admissible set of Trajectories：一条Piecewise-Linear的 路径，在这条路径上不发生任何的 「相交」 (Intersection Free)

$$
  \boldsymbol{x}\in\mathcal{A} \implies \forall t, \boldsymbol{x}(t) d(x_1, x_2) > 0
$$

> Note: Can we achieve $= 0$ ?

显然：迭代法确定迭代方向后，可以搜索得到一个延长的路径。

### 能量定义

$$
b(d, \hat{d}) = \begin{cases}
  - (d - \hat{d})^2 \ln (d / \hat{d})\\
  0
\end{cases}
$$

### Variational Friction

最大耗散原理。

缺点：实现精确的静摩擦需要更多的迭代步。





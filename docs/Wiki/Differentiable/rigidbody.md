# Rigid body dynamics and Differentiable simulation

在这里不涉及很多和 Dynamics 相关的内容，总的来说是 6DoF 及其导数。

因为DoF数量少，前向仿真可以采用 Dual Method 来直接求其导数。

关于碰撞，主要是两类方法：

1. Penalty method：惩罚力方法
2. LCP：直接将接触力建模到约束问题中 -> Explicit Integration

See:

1. [ADD](../../Papers/_articles/TOG/20-ADD.md).
2. [DiffPD](../../Papers/_articles/TOG/21-DiffPD.md)


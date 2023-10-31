---
title: "Elasto Monolith: A Monolithic Optimization-based Liquid Solver for Contact-Aware Elastic-Solid Coupling"
tags: 
  - Collision
  - FSI
  - FVM
date: 2022-11-20
paperAuthor: #TODO
paperYear: 2020
paperSource: SIGGRAPH ASIA
---

实现了初步的FVM流体-可变形体的强流固耦合。

<!-- more -->

# ElastoMonolith: A Monolithic Optimization-based Liquid Solver for Contact-Aware Elastic-Solid Coupling


## Elasto Monolith Overview

使用基于优化的时间积分器，来实现流固动力学计算及其耦合。

1. 流体动力学：使用APIC，网格上全隐式的求解
2. 变形体动力学：Position-level Optimization
3. 刚体动力学：Velocity-level Friction contact handling(ref: Siggraph 2022 course)

```
Algorithm EM:
1. map fluid velocity (P->G)
2. add Explicit External Force
3. solve the system
4. advect particles and update rigid body positions.
```

该最小化问题集成了：

1. 粘性、无粘性液体 + Incompressibility
2. 刚体、弹性体 + Friction

消除了可见的错误：

1. 体积流失
2. 穿透
3. 流固耦合上的能量损失

$$
\mathbf{u}, \mathbf{x}_e \mathbf{v}_r = \arg\min_{d\in \mathcal{D}, h \in \mathcal{H}} E(u, x, r)
$$

其中，$E$由三部分组成：

$$
E = E_{f} + E_{e} + E_{r}
$$

分别是流体项、弹性体项、刚体项

> 相当的朴实无华...

### Rigid body Simulation

Contact handling of rigid bodies => Energy Minimization.

Object for rigid bodies can be written as the kinematic energy-norm of difference between before and after.

$$
E_r(v_r) = \frac{1}{2} \| v_r - v_{r}^{*} \|_{\alpha M_r}
$$

其中：$v_r^*$ 和 $v_r$ 是 before 和 after 的刚体速度，$M_r$ 为质量矩阵

$$
v_r = v_{r}^{*} + \Delta t (\alpha M_r)^{-1} (F_{r s} s + F_{r p} p + \alpha J_r^Tc)
$$

---
paperSource: SIGGRAPH
paperAuthor: "Mickeal Verschoor, Andrei C. Jalba"
paperYear: 2019
doi: "10.1145/3209887"
title: "Efficient and Accurate Collision Response for Elastically Deformable Models"
date: 2023-11-13
tags: 
  - Collision
---

本文提出了一种高效准确的弹性可变形模型碰撞响应方法，通过直接解决混合线性互补问题（MLCP）来处理碰撞问题，避免了构建线性互补问题（LCP）矩阵的过程，使用共轭残差（CR）求解器作为碰撞响应系统的核心，通过动态更新活动约束集合，可以高效地解决带有不等式约束的MLCP问题，并提出了一个简单而有效的预处理器以加快收敛速度，实验结果表明该方法比现有方法更快且能准确处理摩擦。

<!-- more -->

## Basic Information:

- Title: Efficient and Accurate Collision Response for Elastically Deformable Models (高效准确的弹性可变形模型碰撞响应)
- Authors: Mickeal Verschoor, Andrei C. Jalba
- Affiliation: Mickeal Verschoor - Eindhoven University of Technology and Universidad Rey Juan Carlos (荷兰埃因霍温科技大学和西班牙胡安卡洛斯大学), Andrei C. Jalba - Eindhoven University of Technology (荷兰埃因霍温科技大学)
- Keywords: Collision response, conjugate residual (碰撞响应, 共轭残差)
- URLs: [Paper](https://doi.org/10.1145/3209887), [GitHub: None]

## 论文简要 :

- 本文提出了一种高效准确的弹性可变形模型碰撞响应方法，通过直接解决混合线性互补问题（MLCP）来处理碰撞问题，避免了构建线性互补问题（LCP）矩阵的过程，使用共轭残差（CR）求解器作为碰撞响应系统的核心，通过动态更新活动约束集合，可以高效地解决带有不等式约束的MLCP问题，并提出了一个简单而有效的预处理器以加快收敛速度，实验结果表明该方法比现有方法更快且能准确处理摩擦。

## 背景信息:

- 论文背景: 在计算机图形学中，模拟可变形模型之间以及与环境的碰撞仍然是一个具有挑战性的任务。
- 过去方案: 传统方法通常通过构建和解决线性互补问题（LCP）来获得碰撞响应力，但这需要求解广义质量矩阵的逆，而对于可变形体问题来说，这通常很难获得。因此，研究人员通常寻求逼近或解决一系列耦合问题。
- 论文的Motivation: 本文旨在通过直接解决混合线性互补问题（MLCP）来处理碰撞问题，避免了构建LCP矩阵的过程，并提出了一种高效的共轭残差（CR）求解器作为碰撞响应系统的核心。通过动态更新活动约束集合，可以高效地解决带有不等式约束的MLCP问题，并提出了一个简单而有效的预处理器以加快收敛速度。该方法能够处理大变形和大接触力，实现稳定堆叠（几乎）刚体对象，并准确近似库仑摩擦锥。实验结果表明，该方法比现有方法更快且能准确处理摩擦。

## 方法:

- a. 理论背景:
  - 本文介绍了在计算机图形学应用中广泛使用的基于物理的模型。作者提出了一种直接解决混合线性互补问题（MLCP）的方法，用于碰撞响应，而无需构建LCP矩阵。他们使用共轭残差（CR）求解器作为碰撞响应系统的主要方法，并提出了一种预处理器以加快收敛速度。该方法能够准确处理摩擦，并且比现有方法更快，同时保持相同的准确性。
- b. 技术路线:
  - 作者提出了一种用于弹性可变形模型的高效准确的碰撞响应方法。他们使用有限元方法（FEM）离散化运动方程，并使用约束响应（CR）方法求解得到的方程组。CR方法将不等式约束视为可以改变状态的等式约束，允许在求解器迭代过程中取消和重新激活约束。当约束误差低于指定的容差时，该方法收敛。作者还引入了非穿透约束，以防止可变形物体之间的碰撞。这些约束使用一阶近似将其转化为速度约束。碰撞响应使用Lagrange乘子建模，并将接触力包含在模型的运动方程中。由此产生的问题是一个混合线性互补问题（MLCP），使用CR方法求解。CR方法将MLCP转化为线性互补问题（LCP），并使用Krylov子空间方法求解。该方法还通过引入摩擦约束并在求解器迭代过程中更新它们来处理摩擦。

## 结果:

- a. 详细的实验设置:
  - 作者进行了一系列实验来验证他们的方法。他们使用了包含许多内部元素的复杂对象进行实验。他们随机放置了120只兔子，并以0.001秒的时间步长进行模拟。所有模拟中摩擦系数均设为0.5。
- b. 详细的实验结果:
  - 作者提供了关于碰撞检测、接触解决、整个接触问题求解的平均时间和中位数时间的表格。完整的预处理器占用了总时间的约15％，构建时间可以忽略不计。与ICA方法相比，基于CR的方法平均加速了4
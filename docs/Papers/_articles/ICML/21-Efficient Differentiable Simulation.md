---
paperSource: ICML
paperAuthor: "Yi-Ling Qiao, Junbang Liang, Vladlen Koltun, Ming C. Lin"
paperYear: 2021
doi: 
title: "Efﬁcient Differentiable Simulation of Articulated Bodies"
date: 2023-11-04
tags: 
  - Differentiable Simulation
  - Rigid-body Dynamics
---

本文提出了一种高效可微分的关节体模拟方法，通过使用空间代数和**伴随方法**推导出前向动力学的梯度，实现了对关节体动力学的深度学习框架集成和基于梯度的神经网络优化。

<!-- more -->

# Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: Efﬁcient Differentiable Simulation of Articulated Bodies (高效可微分的关节体模拟)
- Authors: Yi-Ling Qiao, Junbang Liang, Vladlen Koltun, Ming C. Lin
- Affiliation: University of Maryland, College Park (马里兰大学学院公园分校)
- Keywords: differentiable simulation, articulated bodies, deep learning, gradient-based optimization, reinforcement learning
- URLs: [Paper](https://arxiv.org/abs/2109.07719v1), [GitHub](https://github.com/YilingQiao/diffarticulated)

## 论文简要 :

- 本文提出了一种高效可微分的关节体模拟方法，通过使用空间代数和伴随方法推导出前向动力学的梯度，实现了对关节体动力学的深度学习框架集成和基于梯度的神经网络优化。通过仅保存初始状态，我们的方法将内存需求降低了两个数量级，并在控制和逆问题的应用中加速了收敛速度超过一个数量级。

## 背景信息:

- 论文背景: Differentiable physics（可微分物理）使得学习和优化使用基于梯度的方法成为可能，但在涉及关节体的物理系统中，目前的方法存在计算和内存消耗过大的问题。
- 过去方案: 过去的方法使用自动微分工具，但当模拟步骤较多时，这些工具会消耗过多的内存。此外，关节体模拟的动力学算法是高度串行的，与在网格和粒子上的并行计算不同，因此很难实现相同的加速。
- 论文的Motivation: 本文的动机是设计一种高效可微分的关节体模拟方法，以提高计算和内存效率，从而支持与关节体在物理环境中交互的可微分系统的快速基于梯度的优化。

## 方法:

- a. 理论背景:
  - 本文提出了一种高效的可微分关节体模拟方法，旨在将关节体动力学集成到深度学习框架中，并实现对操作于关节体上的神经网络的基于梯度的优化。该方法使用空间代数和伴随方法推导出前向动力学的梯度。与自动微分工具相比，该方法的速度提高了一个数量级，并且内存需求减少了两个数量级。作者还引入了一种检查点策略，进一步减少内存消耗。该方法应用于各种应用，包括强化学习、控制和逆问题，并在这些场景中加速了收敛。
- b. 技术路线:
  - 作者提出了一种高效的可微分关节体模拟方法。他们将伴随方法应用于关节动力学，从而显著减少了内存消耗，并实现了对长时间经验的稳定模拟。与以前的方法不同，作者在减少坐标中操作，并为关节体算法和空间代数运算符推导出伴随，确保了具有关节力矩、限制、科里奥利力和链接之间内部力的物理有效模拟。该方法还利用神经逼近来使用神经网络近似物理模拟。然而，作者指出，虽然神经网络在自然上是可微分的，但它们不受制于底层物理动力学，这可能导致模拟保真度在训练分布之外的情况下降低。

## 结果:

- a. 详细的实验设置:
  - 作者开发了一种关节体的可微分模拟方法。
  - 他们将其方法与其他自动微分工具（如CppAD、Ceres、PyTorch、autodiff和JAX）进行了比较。
  - 分析了不同方法的内存消耗，发现他们的方法是最节省内存的。
  - 他们的方法在模拟时间和梯度计算方面比其他方法更快。
  - 他们进一步展示了他们的方法在与强化学习的集成中的效率，比如在n-link pendulum和MuJoCo Ant等任务中，他们的方法实现了更快的收敛。
- b. 详细的实验结果:
  - 表4报告了不同链接数的摆的最大回报统计数据。MBPO的性能下降，而我们的方法没有。

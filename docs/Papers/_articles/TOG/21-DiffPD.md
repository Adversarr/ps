---
paperAuthor: "TAO DU, KUI WU, PINGCHUAN MA, SEBASTIEN WAH, ANDREW SPIELBERG, DANIELA RUS, and WOJCIECH MATUSIK, MIT CSAIL"
paperSource: TOG
paperYear: 2021
title: "DiffPD: Differentiable Projective Dynamics"
date: 2023-10-31
doi: "https://doi.org/10.1145/3490168"
tags:
  - Differentiable Simulation
  - Projective Dynamics
---

可微分的 Projective Dynamics 模拟框架，提升了可微仿真 Backward 的效率。核心思想是，用于 Forward 过程的求解器同样适用于逆向导数的求解。

<!-- more -->

# DiffPD： Differentiable Projective Dynamics

- 本总结源自于 LLM 的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: DiffPD: Differentiable Projective Dynamics (DiffPD: 可微分的投影动力学)
- Authors: Tao Du, Kui Wu, Pingchuan Ma, Sebastien Wah, Andrew Spielberg, Daniela Rus, Wojciech Matusik
- Affiliation: MIT CSAIL (麻省理工学院计算机科学与人工智能实验室)
- Keywords: differentiable simulation, projective dynamics, soft-body dynamics, contact handling (可微分仿真, 投影动力学, 软体动力学, 接触处理)
- URLs: [Paper](https://doi.org/10.1145/3490168), [GitHub: None]

## 论文简要 :

- 本文提出了一种新颖的、快速可微分的软体学习和控制应用模拟器 DiffPD。通过基于投影动力学（PD）的隐式时间积分，DiffPD 在前向 PD 模拟中利用预分解的 Cholesky 分解加速反向传播，支持两种类型的接触处理，并在多个应用中展示了其高效性能。

## 背景信息:

- 论文背景: 近年来，可微分物理学的兴起引发了可微分模拟器的出现，并在具有模拟优化循环的逆问题中取得了成功。然而，由于软体动力学中自由度的增加，可微分软体模拟器的研究仍处于初级阶段。
- 过去方案: 过去的研究主要分为两类：一类是基于显式时间积分方案的模拟器，需要较小的时间步长以避免梯度计算中的数值不稳定性；另一类是基于隐式时间积分的模拟器，通常通过使用伴随方法和求解昂贵的线性化动力学来计算梯度。
- 论文的 Motivation: 本文的动机是开发一种可微分的软体模拟器，以解决软体动力学中自由度增加的挑战。与基于神经网络的方法不同，本文的方法基于物理学原理，直接对软体动力学的控制方程进行求导，同时通过借鉴投影动力学的思想，提出了一种高效的隐式时间积分方案，并支持接触处理。

## 方法:

- a. 理论背景:
  - 本文介绍了可微分模拟器的概念及其在逆问题、运动规划、控制器设计和优化中的应用。它强调了可微分模拟器在为物理系统提供额外指导和促进各种下游应用的定量研究方面的潜力。
- b. 技术路线:
  - 本文提出了 DiffPD，一种基于有限元方法（FEM）和隐式时间步进方案的高效可微分软体模拟器。DiffPD 利用 PD 中的非线性分解概念加速正向模拟和反向传播。它支持使用基于惩罚的接触和摩擦力或基于互补性的非穿透接触和静摩擦力进行可微分接触处理。DiffPD 在各种 3D 应用中进行了评估，并与显式和隐式可微分 FEM 模拟进行了比较。

## 结果:

- a. 详细的实验设置:
  - 本文未提及具体的实验设置。
- b. 详细的实验结果:
  - 本文未提及具体的实验结果。

---
paperSource: ICRA
paperAuthor: "Yuanming Hu, Jiancheng Liu, Andrew Spielberg, Joshua B. Tenenbaum, William T. Freeman, Jiajun Wu, Daniela Rus, Wojciech Matusik"
paperYear: 2019
doi: "10.48550/arXiv.1810.01054"
title: "ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics"
date: 2023-11-05
tags: 
  - Differentiable Simulation
  - MPM
---

本文提出了一种用于软体机器人的实时可微分物理模拟器ChainQueen，基于Moving Least Squares Material Point Method (MLS-MPM)，能够高精度地进行前向模拟和反向梯度计算，并成功应用于软体机器人的控制任务。

<!-- more -->

# Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics (ChainQueen：一种用于软体机器人的实时可微分物理模拟器)
- Authors: Yuanming Hu, Jiancheng Liu, Andrew Spielberg, Joshua B. Tenenbaum, William T. Freeman, Jiajun Wu, Daniela Rus, Wojciech Matusik
- Affiliation: Massachusetts Institute of Technology (麻省理工学院)
- Keywords: physical simulator, soft robotics, differentiable simulation, deformable objects, MLS-MPM
- URLs: [Paper](https://arxiv.org/abs/1810.01054), [GitHub Code](https://github.com/yuanming-hu/chainqueen)

## 论文简要 :

- 本文提出了一种用于软体机器人的实时可微分物理模拟器ChainQueen，基于Moving Least Squares Material Point Method (MLS-MPM)，能够高精度地进行前向模拟和反向梯度计算，并成功应用于软体机器人的控制任务。

## 背景信息:

- 论文背景: 物理模拟器在机器人规划和控制算法中起着重要作用，而可微分的物理模拟器能够通过梯度优化算法进行反向问题的求解，提高控制效率和精度。
- 过去方案: 目前已经有了许多针对刚体的可微分物理模拟器的研究，但对于软体物体的模拟仍存在挑战，包括模拟速度慢、接触检测和解决困难、梯度计算复杂等问题。
- 论文的Motivation: 鉴于软体机器人的特殊性，本文提出了一种基于MLS-MPM的实时可微分物理模拟器ChainQueen，能够高效地模拟软体物体的运动，并实现了对整个模拟过程的梯度计算，从而在软体机器人的控制和系统识别等方面具有广泛的应用前景。

## 方法:

- a. 理论背景:
  - 本文提出了一种名为ChainQueen的可微分物理模拟器，用于模拟可变形物体。
  - ChainQueen基于Moving Least Squares Material Point Method (MLS-MPM)，可以模拟具有接触的可变形物体。
  - 该模拟器完全可微分，并且可以高效地计算状态和模型参数的梯度。
  - 它可以用于基于优化的闭环控制器设计、轨迹优化和机器人几何、材料和控制的共同设计。
- b. 技术路线:
  - 该模拟器ChainQueen基于MLS-MPM方法构建。
  - 它被设计用于模拟软体机器人的弹性材料。
  - ChainQueen完全可微分，并且比当前最先进的模拟器快4-9倍。
  - 数值和实验验证表明，ChainQueen在正向模拟和反向梯度计算方面具有高精度。

## 结果:

- a. 详细的实验设置:
  - 使用ChainQueen模拟器进行了一系列实验，包括物理参数推断、软体机器人控制和机器人臂结构设计的共同设计。
  - 在物理参数推断任务中，使用模拟器推断了两个碰撞弹性球的相对密度。
  - 在控制任务中，优化了基于回归的软体机器人控制器，发现了稳定的步态。
  - 在共同设计任务中，模拟器实现了对软体机器人结构设计参数的优化，例如多连杆机器人臂的刚度分布。
- b. 详细的实验结果:
  - ChainQueen在基于梯度的优化任务中展示了其有效性。
  - 在物理参数推断任务中，模拟器成功推断了碰撞球的相对密度。
  - 在控制任务中，与最先进的强化学习算法相比，优化后的软体机器人控制器表现出更好的性能。
  - 在共同设计任务中，优化后的机器人臂设计在实现目标目标时比固定设计具有更低的驱动成本。
  - 实验结果突出了ChainQueen在各种软体机器人应用中的高效性和准确性。


---
paperSource: IEEE-RA-L
paperAuthor: "Simon Le Cleac’h, Mac Schwager, Zachary Manchester, Vikas Sindhwani, Pete Florence, Sumeet Singh"
paperYear: 2023
doi:
title: "Single-Level Differentiable Contact Simulation"
date: 2023-11-05
tags:
  - Differentiable Simulation
  - Contact Modeling
---

本文提出了一种单层可微分刚体接触动力学的表达方式，用于表示由**凸多面体**组成的物体和机器人。通过将**接触仿真和碰撞检测结合为一个统一的单层优化问题**，解决了传统物理引擎和最新的优化方法在现实接触仿真场景中的问题。通过在机器人操作任务中的应用，证明了该方法的可行性和优越性能。

<!-- more -->

# Note:

- 本总结源自于 LLM 的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: Single-Level Differentiable Contact Simulation (单层可微分接触仿真)
- Authors: Simon Le Cleac’h, Mac Schwager, Zachary Manchester, Vikas Sindhwani, Pete Florence, Sumeet Singh
- Affiliation: Simon Le Cleac’h is affiliated with Stanford University, Mac Schwager is affiliated with Stanford University, Zachary Manchester is affiliated with Carnegie Mellon University, Vikas Sindhwani, Pete Florence, and Sumeet Singh are affiliated with Google Research.
- Keywords: Simulation and animation, contact modeling, differentiable contact simulation, dexterous manipulation.
- URLs: [Paper](https://ieeexplore.ieee.org/document/9630007), [GitHub](https://github.com/simon-lc/Silico.jl)

## 论文简要 :

- 本文提出了一种单层可微分刚体接触动力学的表达方式，用于表示由凸多面体组成的物体和机器人。通过将接触仿真和碰撞检测结合为一个统一的单层优化问题，解决了传统物理引擎和最新的优化方法在现实接触仿真场景中的问题。通过在机器人操作任务中的应用，证明了该方法的可行性和优越性能。

## 背景信息:

- 论文背景: 物理引擎在机器人操作和运动任务的规划和控制中起着越来越重要的作用。然而，传统的物理引擎和最新的优化方法在接触仿真方面存在一些问题，如非可微分的碰撞检测和接触位置的不确定性。
- 过去方案: 传统的物理引擎依赖于非可微分的碰撞检测算法，而最新的优化方法则将碰撞检测和接触仿真分离为两个层次的优化问题。然而，这些方法在现实接触仿真场景中不可靠，因为将碰撞检测问题隔离开来会导致接触位置的不唯一性。
- 论文的 Motivation: 为了解决传统物理引擎和最新优化方法在接触仿真中的问题，本文提出了一种单层可微分接触仿真的新方法，通过将接触仿真和碰撞检测结合为一个统一的优化问题，解决了接触位置不唯一性的问题，并提供了更可靠和计算复杂度更低的仿真方法。通过在机器人操作任务中的应用，证明了该方法的有效性和优越性能。

## 方法:

- a. 理论背景:
  - 本文介绍了一种可微分的刚体接触动力学的表达方式，适用于由凸多面体组成的物体和机器人。它强调了传统物理引擎和最近的基于优化的方法在模拟真实接触场景方面的局限性。所提出的方法将接触模拟和碰撞检测结合为一个统一的单层优化问题，提高了模拟的鲁棒性并降低了计算复杂性。本文还讨论了物理引擎在机器人操作和运动控制中的重要性。
- b. 技术路线:
  - 本文首先介绍了一种用于模拟刚性物体之间非弹性接触的变分积分方案。通过将约束的最小作用量原理与最大耗散原理相结合，将可行性问题形式化。在每个积分步骤中求解该问题，以找到下一个时间步长的配置。该方案可以处理多个接触的情况。接触模拟需要三个映射：有符号距离函数（SDF）用于测量物体与环境之间的距离，接触点指示接触力矩被施加的位置，接触法线定义了施加冲击力的方向。该方案还包括动力学、非穿透、摩擦锥和最大耗散的约束。

# 结果:

- a. 详细的实验设置:
  - 本文使用凸束和面对面接触作为模拟场景，评估了单层方案的能力。凸形状可以通过联合操作组合成复杂的非凸形状。凸多面体的 Minkowski 和用于形成复杂的凸形状。面对面接触发生在两个物体彼此接触时。这种情况在机器人场景中很常见，例如将物体放在平地上、堆叠块以形成塔和进行钉孔插入。
- b. 详细的实验结果:
  - 本文将单层方案与双层方案在模拟精度和可靠性方面进行了比较。与双层方案相比，单层方法显示出改进的模拟鲁棒性和减少的地面穿透。模拟器的可微性被利用来解决通过接触的优化问题。单层方案的能力在一组常见的机器人场景中得到了证明，包括抓取、堆叠和钉孔插入。模拟结果在视频中呈现，并附带了 3D 中的其他实验。

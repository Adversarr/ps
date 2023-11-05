---
paperAuthor: "MORITZ GEILINGER∗ and DAVID HAHN∗, ETH Zürich
  JONAS ZEHNDER, Université de Montréal
  MORITZ BÄCHER, Disney Research
  BERNHARD THOMASZEWSKI, ETH Zürich and Université de Montréal STELIAN COROS, ETH Zürich"
paperSource: TOG
paperYear: 2020
title: "ADD: Analytically Differentiable Dynamics for Multi-Body Systems with Frictional Contact"
date: 2023-11-04
doi: "10.1145/3414685.3417766"
tags:
  - Differentiable Simulation
  - Rigid-body Dynamics
  - Frictional Contact
---

本文提出了一种可解析可微分的动力学求解器，能够在统一框架下处理**刚性和可变形物体的摩擦接触问题**。通过对法向和切向接触力进行原则性的平滑处理，我们的方法克服了摩擦接触的非光滑特性所带来的主要困难。

<!-- more -->

# Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: ADD: Analytically Differentiable Dynamics for Multi-Body Systems with Frictional Contact (ADD: 可解析可微分的多体系统摩擦接触动力学)
- Authors: Geilinger, M., Hahn, D., Zender, J., Bächer, M., Thomaszewski, B., Coros, S.
- Affiliation: Geilinger, M. - ETH Zürich (瑞士苏黎世联邦理工学院)
- Keywords: differentiable dynamics, frictional contact, multi-body systems, simulation, parameter estimation, motion planning, self-supervised learning
- URLs: [Paper](https://arxiv.org/abs/2007.00987v1), [GitHub: None]

## 论文简要 :

- 本文提出了一种可解析可微分的动力学求解器，能够在统一框架下处理刚性和可变形物体的摩擦接触问题。通过对法向和切向接触力进行原则性的平滑处理，我们的方法克服了摩擦接触的非光滑特性所带来的主要困难。我们将这种新的接触模型与完全隐式的时间积分相结合，得到了一个稳健高效的可解析可微分的动力学求解器。通过伴随灵敏度分析，我们的方法使得能够在模拟精度和目标函数平滑性之间进行自适应权衡的梯度优化成为可能。我们在一系列模拟示例中对我们的方法进行了详细分析，涉及刚体、粘弹性材料和耦合多体系统。我们还展示了我们的可微分模拟器在可变形物体参数估计、机器人操作的运动规划、柔性步行机器人的轨迹优化以及高效的自监督学习控制策略等应用领域的潜力。

## 背景信息:

- 论文背景: 仿真工具在工程和机器人学的各种应用中至关重要，可以在第一个原型制造之前测试设计的性能。然而，基于正向仿真的虚拟验证通常局限于试错方法，用户需要费力地找到适当的控制或设计参数。反向仿真工具承诺一种更直接和强大的方法，因为它们可以预测和利用参数变化对设计性能的影响方式。与正向仿真不同，这种反向方法依赖于计算仿真运行的导数能力。
- 过去方案: 近年来，可微分仿真在视觉、图形和机器人领域越来越受关注，例如在流体动画、软体动力学和光传输等领域。然而，由于碰撞和摩擦接触引起的强非线性和准不连续性是现实世界交互的特征，这对可微分仿真提出了重大挑战。
- 论文的Motivation: 本文旨在克服非光滑问题设置的困难，提出了一种可解析可微分的模拟器，将完全隐式的时间步进与法向和切向接触力的原则性平滑处理相结合。我们的模拟模型通过伴随灵敏度分析能够计算仿真结果的导数，从而实现了精确性和目标函数平滑性之间的易于调整的权衡。我们展示了该模型在可变形物体参数估计、机器人操作的运动规划、柔性步行机器人的轨迹优化以及高效的自监督学习控制策略等应用领域的潜力。

## 方法:

- a. 理论背景:
  - 本文介绍了在工程和机器人应用中模拟工具的重要性。作者强调了正向模拟的局限性以及反向模拟的潜力，后者具有更直接和强大的方法。他们强调了计算模拟运行的导数对于反向模拟工具的必要性。
- b. 技术路线:
  - 本文提出了一种处理刚体和可变形体的摩擦接触的解析可微动力学求解器。该方法基于正向和伴随模拟的组合，并使用软约束形式处理摩擦接触，从而实现了模拟模型的简单微分。该方法使用隐式时间积分结合惩罚力模型，准确地处理了摩擦接触的正常和切向分量。

## 结果:

- a. 详细的实验设置:

  - 本文没有明确提及实验设置。它主要关注开发一种解析可微动力学方法，并没有提供具体的实验设置或条件。

- b. 详细的实验结果:

   

  - 本文没有提供数值实验结果。它主要关注开发一种解析可微动力学方法，并没有提供具体的实验数据或性能评估。

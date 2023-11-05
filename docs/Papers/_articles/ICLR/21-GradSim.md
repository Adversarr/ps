---
paperSource: ICLR
paperAuthor: ""
paperYear: 2021
doi:
title: "∇Sim: Differentiable simulation for system identification and visuomotor control"
date: 2023-11-05
tags:
  - Differentiabl Simulation
  - System Identification
---

本文提出了一种名为 ∇Sim 的可微分仿真框架，通过结合可微分多物理仿真和可微分渲染，**从图像序列中直接估计物体的物理属性**，解决了系统识别问题和视觉运动控制问题。

<!-- more -->

# Note:

- 本总结源自于 LLM 的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: DIFFERENTIABLE SIMULATION FOR SYSTEM IDENTIFICATION AND VISUOMOTOR CONTROL (可微分仿真用于系统识别和视觉运动控制)
- Authors: Krishna Murthy Jatavallabhula, Miles Macklin, Florian Golemo, Vikram Voleti, Linda Petrini, Martin Weiss, Breandan Considine, Jérôme Parent-Lévesque, Kevin Xie, Kenny Erleben, Liam Paull, Florian Shkurti, Derek Nowrouzezahrai, Sanja Fidler
- Affiliation: Montreal Robotics and Embodied AI Lab, NVIDIA, Mila, Université de Montréal, McGill, University of Toronto, Vector Institute, University of Copenhagen
- Keywords: system identification, visuomotor control, differentiable simulation, differentiable rendering, physical properties estimation
- URLs: [Paper], [GitHub](https://gradsim.github.io/)

## 论文简要 :

- 本文提出了一种名为 ∇Sim 的可微分仿真框架，通过结合可微分多物理仿真和可微分渲染，从图像序列中直接估计物体的物理属性，解决了系统识别问题和视觉运动控制问题。

## 背景信息:

- 论文背景: 准确地从图像序列中预测物体的动力学和物理特性是计算机视觉领域长期以来的挑战。现有的解决方案需要精确的三维标签，但收集这些标签非常耗时，对于可变形固体或布料等许多系统来说几乎不可行。
- 过去方案: 过去的解决方案主要分为黑盒、灰盒和白盒方法。黑盒方法通过学习嵌入状态或观测的方式来建模动力系统的状态，但由于变分因素的纠缠或无监督学习的模糊性，缺乏可解释性。灰盒方法利用对系统动力学的部分知识来提高性能。白盒方法通过使用显式动力学模型来引入先验知识，减少可学习参数的空间，提高系统的可解释性。
- 论文的 Motivation: 然而，所有这些方法都需要精确的三维标签，而这些标签的收集非常耗时，对于可变形固体或布料等许多系统来说几乎不可行。本文旨在通过结合可微分多物理仿真和可微分渲染，消除白盒动力学方法对三维监督的依赖，从而实现仅使用图像空间监督进行学习。这样的方法可以从视频像素到生成它们的物理属性进行反向传播，并在视觉运动控制任务中实现学习，而无需依赖精确的三维标签。

## 方法:

- a. 理论背景:
  - 本文介绍了 ∇Sim，这是一个结合可微分多物理仿真和可微分渲染的框架，用于从视频序列中直接估计物体的物理属性。∇Sim 通过建模场景动力学和图像形成，实现了从视频像素到底层物理属性的反向传播。该方法旨在在不依赖于 3D 监督的情况下，展示 ∇Sim 在系统识别和视觉运动控制任务中的有效性。
- b. 技术路线:
  - ∇Sim 是一个统一的可微分仿真引擎，结合了物理估计和渲染。仿真被表示为一个函数 Sim(p, t) = I，其中 p 表示仿真状态和参数，t 表示仿真时间，I 是生成的图像。通过在图像空间上优化损失函数，使用基于梯度的优化方法，目标是从视频中估计物理参数。∇Sim 由一个可微分的物理引擎和一个可微分的渲染器组成。

## 结果:

- a. 详细的实验设置:
  - 作者进行了一系列实验，评估了 ∇Sim 在从视频中识别物理参数和视觉运动控制方面的效果。他们测试了 ∇Sim 在从视频观察中识别质量、摩擦力和弹性等物理属性的准确性。他们还将 ∇Sim 的性能与需要 3D 监督的可微分物理引擎进行了比较。实验涉及具有特定物理力和约束的环境，并通过对模拟器进行反向传播来恢复最佳物理参数。
- b. 详细的实验结果:
  - 实验结果表明，∇Sim 能够准确地从视频观察中识别物理参数。结果表明，在性能方面，∇Sim 与仅可微分物理引擎相比具有竞争力或更好的表现。∇Sim 的损失景观被发现是平滑的。实验还表明，∇Sim 可以在不需要 3D 监督的情况下用于视觉运动控制任务。在系统级别上，∇Sim 对建模假设的敏感性被认为是中等的。

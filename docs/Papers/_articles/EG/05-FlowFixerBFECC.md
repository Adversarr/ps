---
paperSource: EuroGraphics
paperAuthor: "ByungMoon Kim, Yingjie Liu, Ignacio Llamas, Jarek Rossignac"
paperYear: 2005
doi: 
title: "FlowFixer: Using BFECC for Fluid Simulation"
date: 2023-11-11
tags: 
  - Fluid
  - FVM
  - Advection
---

# Basic Information:

- Title: FlowFixer: Using BFECC for Fluid Simulation (流体模拟中的FlowFixer: 使用BFECC方法)
- Authors: ByungMoon Kim, Yingjie Liu, Ignacio Llamas, Jarek Rossignac
- Affiliation: Georgia Institute of Technology (佐治亚理工学院)
- Keywords: BFECC, fluid simulation, advection, level set method, velocity, smoke density, image advection (BFECC, 流体模拟, 平流, 水平集方法, 速度, 烟密度, 图像平流)
- URLs: [ResearchGate](https://www.researchgate.net/publication/221314833), [GitHub: None]

# 论文简要 :

- 本文介绍了一种名为BFECC的方法，用于减少流体模拟中的耗散和扩散问题，并应用于速度、烟密度和图像平流等多种平流步骤。该方法在空间和时间上提供了二阶精度，并通过与变密度投影相结合，实现了逼真的两相流体动画效果。

# 背景信息:

- 论文背景: 流体模拟涉及多个计算步骤，包括扩散、平流和压力投影。本文主要探讨流体模拟中的四种平流形式：速度、烟密度、图像和水平集平流。
- 过去方案: 过去的方法中，一阶半拉格朗日方法在计算简单性方面具有优势，但存在较大的数值扩散和耗散问题。因此，需要更高阶的方法来解决这些问题。
- 论文的Motivation: 本文提出了BFECC方法，通过将其添加到一阶半拉格朗日方法中，可以提高其空间和时间精度，减少速度阻尼和烟密度稀释，并在多种平流步骤中展示了其优势。

# 方法:

- a. 理论背景:
  - BFECC方案可用于改善流体模拟。在使用BFECC进行水平集平流时，需要进行重新分配以保持水平集函数作为有符号距离函数。这可以通过求解重新分配方程来实现，该方程涉及重新分配的速度向量。重新分配方程可以使用一阶上风或半拉格朗日样式积分来求解。然而，将重新分配的积分公式与BFECC结合使用可能会导致从二阶精确的BFECC计算得到的良好水平集值的退化。为了解决这个问题，提出了一种简单的重新分配方法，该方法在接口附近关闭重新分配以保持良好的水平集值。这种简单的重新分配方法对于保持体积至关重要，并且易于实现。它只需要在满足某些条件的网格点处进行重新分配，例如当网格点不靠近界面或斜率足够高时。
- b. 技术路线:
  - 使用BFECC方案进行水平集平流。
  - 解决重新分配方程，其中包括重新分配的速度向量。
  - 使用一阶上风或半拉格朗日样式积分来求解重新分配方程。
  - 将重新分配的积分公式与BFECC结合使用。

# 结果:

- a. 详细的实验设置:
  - 实验中使用BFECC方案进行水平集平流。
  - 解决重新分配方程，其中包括重新分配的速度向量。
  - 使用一阶上风或半拉格朗日样式积分来求解重新分配方程。
  - 在接口附近关闭重新分配以保持良好的水平集值。
- b. 详细的实验结果:
  - 实验结果表明，使用BFECC方案进行水平集平流时，通过关闭接口附近的重新分配，可以保持良好的水平集值。
  - 这种简单的重新分配方法对于保持体积至关重要，并且易于实现。
  - 实验结果还表明，在满足某些条件的网格点处进行重新分配，例如当网格点不靠近界面或斜率足够高时，可以有效地实现重新分配。

# Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
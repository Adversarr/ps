---
title: "Differentiable Optimal Control for Retargeting Motions onto Legged Robots"
date: 2023-11-01
tags:
  - Differentiable Simulation
  - Control
paperAuthor: Ruben Grandia, Farbod Farshidian, Espen Knoop, Christian Schumacher, Marco Hutter, Moritz Bächer
paperYear: 2023
paperSource: SIGGRAPH
---

本文提出了一种可微分最优控制（DOC）框架，用于将动物或动画的丰富动作重新定位到四足机器人上，通过优化参数来最小化重新定位误差，并展示了在不同比例和质量分布的机器人上的重新定位结果。

<!-- more -->

## Basic Information:

- Title: Differentiable Optimal Control for Retargeting Motions onto Legged Robots (可微分最优控制用于将动作重新定位到四足机器人上)
- Authors: Ruben Grandia, Farbod Farshidian, Espen Knoop, Christian Schumacher, Marco Hutter, Moritz Bächer
- Affiliation: Ruben Grandia - Disney Research, Switzerland (瑞士迪士尼研究所)
- Keywords: differentiable optimal control, motion retargeting, model-predictive control (可微分最优控制，动作重新定位，模型预测控制)
- URLs: [Paper](https://doi.org/10.1145/3592454), [GitHub: None]

## 论文简要 :
- 本文提出了一种可微分最优控制（DOC）框架，用于将动物或动画的丰富动作重新定位到四足机器人上，通过优化参数来最小化重新定位误差，并展示了在不同比例和质量分布的机器人上的重新定位结果。


## 背景信息:

- 论文背景: 四足机器人设计用于执行高度动态的运动，但是将表达性动作重新定位到这些复杂系统上仍然具有挑战性。
- 过去方案: 过去的方法要求机器人具有相似的比例、完全驱动或使用与机器人相同自由度的动画。
- 论文的Motivation: 为了解决这些问题，本文提出了一种不受比例、自由度和质量分布差异影响的重新定位技术，通过可微分最优控制框架实现动作的优化和重新定位。

## 方法:

- a. 理论背景:
  - 本文介绍了一种不同iable Optimal Control (DOC)框架，用于将丰富的动作从动物或动画转移到四足机器人上。该框架通过优化参数来最小化重定向误差，从而实现了对不同比例和自由度的机器人的动作重定向。
- b. 技术路线:
  - 作者使用Differentiable Optimal Control (DOC)框架，将动作捕捉或动画数据转移到具有不同比例和质量分布的四足机器人上。
  - 作者使用Model-Predictive Control (MPC)公式，将DOC应用于机器人上，以实现动作的重定向。
  - 作者通过在线MPC，展示了重定向的动作在物理上是可行的，并且机器人保留了对意外干扰的反应能力。

## 结果:

- a. 详细的实验设置:
  - 作者使用物理机器人进行实验，并使用Model-Predictive Control (MPC)跟踪重定向的动作。
- b. 详细的实验结果:
  - 作者展示了一组具有不同比例和质量分布的机器人的重定向结果。
  - 重定向的动作在意外干扰之前和之后都能自然地紧跟目标动作。
  - 该系统展示了处理具有非周期性脚步模式的动态运动的能力。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
---
paperSource: arxiv
paperAuthor: "Stanford University"
paperYear: 2022
doi: 
title: "Rethinking Optimization with Differentiable Simulation from a Global Perspective "
date: 2023-11-06
tags: 
  - Differentiable Simulation
---

本研究从全局视角重新思考了可微分仿真优化，针对接触丰富的场景提出了一种结合贝叶斯优化和半局部搜索的方法，通过有效利用梯度并在具有噪声梯度的区域保持鲁棒性，取得了优于其他基于梯度和无梯度的方法的结果。

<!-- more -->

# Basic Information:

- Title: Rethinking Optimization with Differentiable Simulation from a Global Perspective (从全局视角重新思考可微分仿真优化)
- Authors: Rika Antonova, Jingyun Yang, Krishna Murthy Jatavallabhula, Jeannette Bohg
- Affiliation: Stanford University (斯坦福大学)
- Keywords: Differentiable simulation, Global optimization, Deformable objects
- URLs: [Paper](https://arxiv.org/abs/2207.00167v1), [GitHub: None]

# 论文简要 :

- 本研究从全局视角重新思考了可微分仿真优化，针对接触丰富的场景提出了一种结合贝叶斯优化和半局部搜索的方法，通过有效利用梯度并在具有噪声梯度的区域保持鲁棒性，取得了优于其他基于梯度和无梯度的方法的结果。

# 背景信息:

- 论文背景: 物理仿真在机器人学习中起着重要作用，但现有的可微分仿真方法主要解决了大部分动力学平滑的系统，而在接触丰富的场景中很难期望单一下降达到全局最优解。
- 过去方案: 之前的研究主要集中在刚体动力学和一些特定形状、关节、接触等方面的可微分仿真，而对于可变形物体、布料、流体等领域的可微分仿真的研究相对较少。
- 论文的Motivation: 随着越来越多的研究致力于开发和使用可微分仿真引擎，有必要对这些系统的局限性进行深入分析。本研究旨在探究可变形物体仿真中的梯度质量，并提出一种全局搜索方法，以在粗糙的优化景观中取得进展。

# 方法:

- a. 理论背景:
  - 本文介绍了物理模拟在机器人学习中的重要性，以及可微分物理引擎在快速基于梯度的策略优化和系统识别中的应用。现有的可微分模拟方法主要集中在具有平滑动力学的场景中，并讨论了在具有可变形物体的接触丰富场景中分析这些系统的局限性的必要性。本研究的目标是了解可微分模拟器中梯度的质量，并提出一种将全局搜索与半局部搜索相结合的方法，以应对崎岖的优化景观所带来的挑战。
- b. 技术路线:
  - 本文提出的全局搜索方法将贝叶斯优化（BO）与半局部策略相结合。BO用于通过建模不确定性并选择最有希望的候选点进行全局探索。每个候选点被视为半局部搜索的起点。为了解决具有噪声梯度的情况，提出了一种混合下降策略，将无梯度搜索与基于梯度的下降相结合。收集一小部分局部样本，并基于CMA-ES计算采样分布。使用梯度下降演化分布均值，并使用更新后的均值采样下一代种群。该方法旨在在保持噪声梯度区域的鲁棒性的同时有效利用梯度。

# 结果:

- a. 详细的实验设置:
  - 作者使用了几个可微分模拟框架来实现各种场景，包括Nimble、Warp、DiffTaichi和PlasticineLab。这些框架支持不同类型的模拟，如基于网格、基于粒子的模拟，以及包括刚体、可变形和流体物体在内的多个模型。实验中使用的环境在表1中进行了总结，其中包括对研究创建的特定场景和支持的模型的详细信息。
- b. 详细的实验结果:
  - 在不同环境中进行的实验表明，BO-Leap在刚体物体场景（1-Link Cartpole和3-Link Cartpole）中优于无梯度基线（Rand和C
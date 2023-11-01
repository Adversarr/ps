---
title: "DiffFR: Differentiable SPH-based Fluid-Rigid Coupling for Rigid Body Control"
paperSource: "siggraph asia"
paperYear: 2023
date: 2023-10-31
author: Adversarr
doi: "10.1145/3618318"
tag:
  - SPH
  - Differential Simulation
---

本文使用SPH模型，实现了流固的弱双向耦合。解决了模拟过程中的导数数值稳定性、高维度输入下的计算效率问题。

<!-- more -->

# LLM Summary

本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
## Basic Information:

- Title: DiffFR: Differentiable SPH-based Fluid-Rigid Coupling for Rigid Body Control (DiffFR: 可微分的基于SPH的流体-刚体耦合用于刚体控制)
- Authors: Zhehao Li, Qingyu Xu, Xiaohan Ye, Bo Ren, Ligang Liu
- Affiliation: Zhehao Li - University of Science and Technology of China, China (中国科学技术大学); Qingyu Xu - University of Science and Technology of China, China (中国科学技术大学); Xiaohan Ye, Bo Ren - TMCC, College of Computer Science, Nankai University, China (南开大学计算机科学学院); Ligang Liu - University of Science and Technology of China, China (中国科学技术大学)
- Keywords: Differentiable Simulation, Physics-based Simulation, Fluid-Rigid Coupling
- URLs: [Paper](https://doi.org/10.1145/3618318), [GitHub: None]

## 论文简要 :

- 本文提出了一种基于SPH的可微分流体-刚体耦合模拟器，用于解决刚体控制问题，通过优化初始速度使刚体在与流体相互作用后达到预定目标。

## 背景信息:

- 论文背景: 可微分的物理模拟在逆向设计问题中显示出其有效性，但对于流体-刚体耦合的逆向设计问题，仍然存在两个主要挑战：流体-固体相互作用中普遍存在的不连续接触以及由于流体动力学的大自由度而导致的梯度计算的高计算成本。
- 过去方案: 过去的研究主要集中在单向流体-刚体耦合或对流体模型进行强假设的情况下，或者需要大量训练数据来学习流体动力学的情况下，无法直接应用于流体-刚体耦合的逆向设计问题。
- 论文的Motivation: 鉴于流体-刚体耦合在日常生活中的广泛应用，如水瓶翻转使其在旋转后正立着落，或在湖面上跳石头以实现多次弹跳，本文旨在提供一种可微分的流体-刚体耦合模拟器，用于解决刚体控制任务中的逆向设计问题。本文通过提出一种基于SPH的流体-刚体耦合模拟器，解决了梯度爆炸和高计算成本的问题，并在各种具有多样化流体-刚体相互作用的刚体控制任务中展示了方法的有效性、可扩展性和可拓展性。

## 方法:

- a. 理论背景:
  - 本文介绍了可微分物理模拟的概念及其在逆向设计问题中的应用。重点强调了在液体-刚体耦合中需要可微分模拟器的需求。该模拟器的开发面临的挑战包括流体-固体相互作用中的不连续接触和梯度计算的高计算成本。本文提出了一种新颖的基于SPH的可微分流体-刚体耦合模拟器来解决这些挑战。
- b. 技术路线:
  - 本文提出了一种基于SPH的可微分流体-刚体耦合模拟器，用于刚体控制任务的逆向设计。该模拟器使用粒子来统一表示流体和固体。然而，前向模拟粒子系统的微分计算遇到了梯度爆炸的问题。为了解决这个问题，本文提出了一种可行的梯度计算方案，通过减小问题规模并仅考虑梯度计算中固体周围的流体，实现了局部梯度计算方案。这种局部梯度计算方案可以高效地计算流体-刚体耦合的梯度，而不会产生高计算成本。

## 结果:

- a. 详细的实验设置:
  - 本文未提供详细的实验设置。
- b. 详细的实验结果:
  - 本文未提供详细的实验结果。

---
title: Fast and Versatile Fluid-Solid Coupling for Turbulent Flow Simulation
paperAuthor:  Chaoyang Lyu, Wei Li,Mathieu Desbrun, Xiaopei Liu
paperYear: 2021
paperSource: TOG
tags:
  - LBM
  - FSI
date: 2023-10-24
---

本文提升了格子玻尔兹曼方法的流固耦合准确性。本文基于原本的Bounce-Back方法，提出了修正力项来解决因为流固边界不对齐而引入的计算误差。

<!-- more -->

讨论班：2023-10-28

摘要：格子玻尔兹曼方法（LBM）是一类较新的流体仿真算法。尽管其在工业界已经有所应用，而在图形学领域仅有近年的几篇文章有所涉及。本次汇报将主要介绍 LBM 的基本原理和方法、分析其优缺点、并简要介绍21年TOG文章的工作。该文章基于原先的Bounce-back方法，提升了 LBM 在流固耦合上的计算精度。

See more:

- [LBM](../../../Wiki/FluidSimulation/LBM/index.md)
- [LBBook](../../../Wiki/FluidSimulation/LBM/books/LBM%20Principles%20and%20practice.md#boltzmann-eqn-and-collision-operator)
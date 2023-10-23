---
paperSource: SIGGRAPH
paperAuthor:
  - LEI LAN, The University of Utah, USA
  - MINCHEN LI, UCLA, USA
  - CHENFANFU JIANG, UCLA, USA
  - HUAMIN WANG, Style3D Research, China
  - YIN YANG, The University of Utah & Style3D Research, USA
paperYear: 2023
title: Second-order Stencil Descent for Interior-point Hyperelasticity
date: 2023-10-22
tags:
  - IPC
  - GPU
  - Hyperelasticity
---

本文基于GPU实现了基于IPC内点法的有限元超弹性模拟算法，旨在利用GPU加速和内点法，来提高同时处理碰撞和接触约束的有限元法模拟算法的效率。文章提出的算法利用在局部利用Hessian进行迭代求解，全局使用并行计算，确保目标函数能够快速收敛，并使用互补着色和混合扫描方案来充分利用GPU计算能力。此外，文章还提出了一种专门的预热过程，用于改善迭代初值并提高算法的收敛速度和稳定性。
<!-- more -->
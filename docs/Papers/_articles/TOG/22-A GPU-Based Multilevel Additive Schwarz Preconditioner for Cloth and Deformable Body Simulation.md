---
paperSource: TOG
paperAuthor: "BOTAO WU, ZHENDONG WANG, HUAMIN WANG"
paperYear: 2022
doi: "10.1145/3528223.3530085"
title: "A GPU-Based Multilevel Additive Schwarz Preconditioner for Cloth and Deformable Body Simulation"
date: 2023-11-13
tags: 
  - GPU
  - Acceleration
---

本文提出了一种基于GPU的多层级加性Schwarz预处理器，用于布料和可变形体模拟，通过优化预处理器的设计和实现，实现了更快速和有效的模拟效果。

<!-- more -->
## Basic Information:

- Title: A GPU-Based Multilevel Additive Schwarz Preconditioner for Cloth and Deformable Body Simulation (基于GPU的多层级加性Schwarz预处理器在布料和可变形体模拟中的应用)
- Authors: BOTAO WU, ZHENDONG WANG, HUAMIN WANG
- Affiliation: Style3D Research, China (中国Style3D研究机构)
- Keywords: GPU-based preconditioner, multilevel additive Schwarz, cloth simulation, deformable body simulation (基于GPU的预处理器，多层级加性Schwarz，布料模拟，可变形体模拟)
- URLs: [Paper](https://doi.org/10.1145/3528223.3530085), [GitHub: None]

## 论文简要 :

- 本文提出了一种基于GPU的多层级加性Schwarz预处理器，用于布料和可变形体模拟，通过优化预处理器的设计和实现，实现了更快速和有效的模拟效果。

## 背景信息:

- 论文背景: 布料和可变形体模拟问题可以归结为大规模非线性优化问题，如何快速解决这些问题一直是数学家和科学家们面临的主要挑战。
- 过去方案: 过去的研究者们已经开展了广泛的研究，并开发了各种优化方法，但是对于更高质量的实时模拟，现有方法不足以解决相关的大规模、病态问题。
- 论文的Motivation: 鉴于在各种图形应用中实现实时模拟的迫切需求，更快速的求解器比以往任何时候都更加紧迫。多层级和域分解方法近年来越来越受欢迎，因为它们在解决大规模、病态问题方面非常有效。在这些方法中，多层级加性Schwarz（MAS）预处理与（非线性）迭代方法结合起来，不仅因为它采用了这两个概念，而且因为它简单易用。MAS预处理器自然地避免了其他域分解方法中涉及的域不连续性问题，并且不依赖于层次化粗化和传播算子。与其他预处理器（如多重网格）相比，MAS预处理器具有明显的可并行性：不同级别的所有域可以并行运行，而不是以任何循环顺序。这使得MAS预处理器成为GPU加速的理想选择。因此，本文旨在开发一种能够充分利用GPU计算能力的MAS预处理器，以实现更快速的布料和可变形体模拟效果。

## 方法:

- a. 理论背景:
  - 过去几年中，布料和可变形物体动力学模拟领域一直受到积极研究。早期的技术使用显式时间积分，但存在数值不稳定性问题。随后，研究人员探索了基于牛顿迭代的隐式时间积分方法。还开发了用于快速模拟的优化技术。多重网格方法和预处理器已经得到研究，但在计算机图形学中的使用有限。多层级加性Schwarz预处理器在解决多重网格方法的局限性方面显示出潜力。还探索了其他域分解方法，如平衡域分解和有限元撕裂和互连（FETI）。
- b. 技术路线:
  - 研究人员提出了一种用于布料和可变形物体模拟的多层级加性Schwarz（MAS）预处理器。预处理器分为三个阶段：多层级域构建、子矩阵逆预计算和预处理。算法流程包括按照Morton码对节点进行排序、域划分和构建粗化系统矩阵。预处理器具有高度可并行化的特点，并可应用于各种模拟器。

## 结果:

- a. 详细的实验设置:
  - 布料模拟器处理非结构化三角网格，使用平面弹性的共旋线性模型和弯曲弹性的二次模型。可变形物体模拟器处理四面体网格，并支持多种弹性模型，包括投影动力学、共旋有限元模型和超弹性模型。碰撞检测使用空间哈希，摩擦处理使用基于冲量和粘附的方法。
- b. 详细的实验结果:
  - 将MAS预处理器与PCG求解器和AmgX求解器进行比较。评估了预处理器的收敛速度和收敛速度。与Jacobi和AS预处理器相比，MAS预处理器显示出改进的收敛性能。MAS预处理器的GPU实现表现出更快的性能。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
---
paperSource: CMAME
paperAuthor: "Xuan Li, Yu Fang, Minchen Li, Chenfanfu Jiang"
paperYear: 2021
doi: 
title: "BFEMP: Interpenetration-Free MPM-FEM Coupling with Barrier Contact"
date: 2023-11-18
tags: 
  - MPM
  - IPC
---

本文提出了BFEMP方法，通过使用变分时间步长公式和基于障碍能的粒子-网格摩擦接触，实现了无缝耦合的材料点法（MPM）和有限元法（FEM）。该方法采用修正的线搜索牛顿法，严格防止材料点穿透FEM域，确保收敛性和可行性，无论时间步长大小或网格分辨率如何。该耦合方案还可用于在FEM域中所有节点位移都由Dirichlet边界条件指定时，施加可分离的摩擦运动边界。通过实验证明了该方法的鲁棒性和准确性。

<!-- more -->

## Basic Information:

- Title: BFEMP: Interpenetration-Free MPM-FEM Coupling with Barrier Contact (BFEMP: 无穿透的MPM-FEM耦合与障碍接触)
- Authors: Xuan Li, Yu Fang, Minchen Li, Chenfanfu Jiang
- Affiliation: Department of Mathematics, University of California, Los Angeles, United States (美国加州大学洛杉矶分校数学系)
- Keywords: Material Point Method, MPM-FEM Coupling, Implicit Integration, Barrier Method, Frictional Contact
- URLs: [Paper](https://arxiv.org/abs/2108.03349v2), [GitHub: None]

## 论文简要 :

- 本文提出了BFEMP方法，通过使用变分时间步长公式和基于障碍能的粒子-网格摩擦接触，实现了无缝耦合的材料点法（MPM）和有限元法（FEM）。该方法采用修正的线搜索牛顿法，严格防止材料点穿透FEM域，确保收敛性和可行性，无论时间步长大小或网格分辨率如何。该耦合方案还可用于在FEM域中所有节点位移都由Dirichlet边界条件指定时，施加可分离的摩擦运动边界。通过实验证明了该方法的鲁棒性和准确性。

## 背景信息:

- 论文背景: 本文介绍了材料点法（MPM）和有限元法（FEM）的耦合问题。MPM通过使用拉格朗日粒子来表示连续材料，并使用欧拉背景网格离散化控制方程，适用于高速、大变形和拓扑变化等问题。然而，由于稳定性、准确性、边界条件强制和数值断裂等方面的挑战，MPM在某些情况下不如FEM。因此，将MPM与FEM耦合成为许多多材料模拟任务或涉及强烈异质变形的问题中的理想选择。
- 过去方案: 过去的MPM-FEM耦合方法主要是基于网格的方法，如将FEM顶点作为MPM粒子嵌入MPM网格或将FEM壳体公式嵌入MPM网格。这些方法在处理材料相互作用时存在一些问题，如网格间距和边界处理的限制。
- 论文的Motivation: 本文的动机是解决隐式时间积分下MPM-FEM耦合的摩擦接触问题。由于非线性和非光滑的不等式约束，隐式耦合方案中的摩擦接触问题具有挑战性。作者提出了一种基于障碍能的变分摩擦接触公式，通过在隐式积分过程中保持MPM粒子与FEM网格之间的严格正距离，同时求解FEM网格节点位移和MPM网格节点位移的最优解。该方法不需要调整刚度参数，并且能够保证严格的非穿透条件。

## 方法:

- a. 理论背景:
  - 本文提出了一种新的方法，称为BFEMP，用于将材料点法（MPM）与有限元法（FEM）耦合，采用变分时间步长公式。通过基于障碍能的粒子-网格摩擦接触实现耦合。耦合系统的完全隐式时间积分被构造为一个带有障碍增强的无约束非线性优化问题。采用修改的线搜索牛顿法，防止材料点穿透FEM域，确保收敛性和可行性，无论时间步长大小或网格分辨率如何。所提出的耦合方案还允许在FEM域中的所有节点位移都被规定为Dirichlet边界条件时，对MPM施加可分离的摩擦运动边界。所提出的方法中的接触处理仅需要简单的几何查询，并且可以处理用codimension-1单形表示的任意FEM网格边界。通过实验和分析证明了所提出方法的鲁棒性和准确性。
- b. 技术路线:
  - 通过施加非穿透约束来建模有限元法（FEM）和材料点法（MPM）域之间的耦合。将变分MPM-FEM耦合问题描述为在等式约束下最小化某个方程。可行域可以表示为严格的不等式约束。使用障碍方法来强制施加接触压力。FEM域使用线性单形元素离散化，而MPM域使用材料点和具有二次B样条核的欧拉背景网格进行离散化。推导出时间积分更新规则，并解决最小化问题以获得更新的位置。使用接触势模型对FEM和MPM方案之间的接触进行建模。

## 结果:

- a. 详细的实验设置:
  - 本文的实验设置部分未提供具体信息。
- b. 详细的实验结果:
  - 本文的实验结果部分未提供具体信息。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
---
paperSource: SIGGRAPH
paperAuthor: ""
paperYear: 2023
doi: 
title: ""
date: 2023-11-13
tags: 
  - Rigid Body
  - IPC
---

本文提出了一种名为仿射体动力学（ABD）的框架，用于高效、稳定且无交叉地模拟接近刚性的物体。通过利用基于障碍函数的摩擦接触建模，ABD降低了刚体建模中的碰撞和接触处理成本，同时获得高质量的无交叉轨迹。通过在具有挑战性的应力测试基准中模拟复杂的齿轮系统，ABD在所有现有的刚体模拟算法中表现出色，实现了稳定的仿真。ABD还能够在处理大位移（旋转）接触的情况下使用大时间步长，具有出色的性能表现。

<!-- more -->

## Basic Information:

- Title: Affine Body Dynamics: Fast, Stable and Intersection-free Simulation of Stiff Materials (刚性材料的仿射体动力学：快速、稳定和无交叉仿真)
- Authors: Lei Lan, Danny M. Kaufman, Minchen Li, Chenfanfu Jiang, Yin Yang
- Affiliation: Lei Lan - Clemson University & University of Utah, USA (美国克莱姆森大学和犹他大学); Danny M. Kaufman - Adobe Research, USA (美国Adobe研究所); Minchen Li - University of California, Los Angeles & TimeStep Inc., USA (美国加州大学洛杉矶分校和TimeStep公司); Chenfanfu Jiang - University of California, Los Angeles & TimeStep Inc., USA (美国加州大学洛杉矶分校和TimeStep公司); Yin Yang - Clemson University, University of Utah & TimeStep Inc., USA (美国克莱姆森大学、犹他大学和TimeStep公司)
- Keywords: Affine body dynamics, Stiff materials, Simulation, Rigid body modeling, Intersection-free (仿射体动力学，刚性材料，仿真，刚体建模，无交叉)
- URLs: Paper - [ACM Digital Library](https://doi.org/10.1145/3528223.3530064), GitHub code - None (论文 - ACM数字图书馆，GitHub代码 - 无)

## 论文简要 :

- 本文提出了一种名为仿射体动力学（ABD）的框架，用于高效、稳定且无交叉地模拟接近刚性的物体。通过利用基于障碍函数的摩擦接触建模，ABD降低了刚体建模中的碰撞和接触处理成本，同时获得高质量的无交叉轨迹。通过在具有挑战性的应力测试基准中模拟复杂的齿轮系统，ABD在所有现有的刚体模拟算法中表现出色，实现了稳定的仿真。ABD还能够在处理大位移（旋转）接触的情况下使用大时间步长，具有出色的性能表现。

## 背景信息:

- 论文背景: 在各个领域中，模拟刚性材料在应用中的行为是一项基本任务，尤其是在涉及到变形不显著或可以安全忽略的情况下。刚体建模一直是一种关键工具，目前是最常用的模拟策略，用于建模刚性固体。然而，刚体方法仍然存在一些已知的挑战和权衡，包括交叉、不稳定性、不准确性和/或随着接触问题复杂性增加的性能下降。
- 过去方案: 过去的刚体方法主要集中在高效的速度（扭矩）级解决方案上，但是这些方法往往会产生不希望的位置误差，如交叉和不稳定性。最近，Ferguson等人提出了一种用于刚体的位置级障碍方法，称为刚性-IPC方法，它通过将增量潜在接触（IPC）模型应用于刚体模型，实现了具有摩擦接触的刚性固体的稳健无交叉仿真。然而，刚性-IPC方法在曲线连续碰撞检测（CCD）中的性能开销仍然很大，特别是在每个仿真步骤中频繁调用CCD时。这限制了刚性-IPC的效率和适用性。
- 论文的Motivation: 鉴于刚体模型的关键优势不是刚性假设，而是紧凑的表示，本文从不同的角度解决了刚体问题。作者构建了一种名为仿射体动力学（ABD）的模型，通过直接加强刚性来获得接近刚性的轨迹，并增加了类似IPC的障碍。ABD保留了IPC模型的所有保证，包括解的收敛性、无交叉保证和准确的摩擦接触。然而，ABD的离散步骤现在是分段线性的，类似于有限元方法（FEM）情况，这使我们能够利用高效的线性CCD例程。同时，ABD保持紧凑，每个物体使用12个自由度（DOFs），比刚体多一点，

## 方法:

- a. 理论背景:
  - 本文讨论了使用刚体建模模拟刚性材料的方法。刚体方法常用，但存在交叉、不稳定和性能慢等局限性。作者提出了一种名为Affine Body Dynamics (ABD)的新框架，改进了刚体动力学的模拟。ABD放松了刚性运动的约束，并用分段线性轨迹替代了分段线性化。这种方法结合了紧凑坐标和高效约束评估的优点。ABD在性能和模拟质量方面优于现有方法，并成功解决了其他方法无法解决的具有挑战性的模拟问题。
- b. 技术路线:
  - 本文中描述的方法涉及使用摩擦模型来捕捉接触对中的摩擦粘滞和滑动行为。该模型利用摩擦系数和几何对之间的相对滑动速度的平滑范数。作者证明了该模型提供了与可控精度的非光滑Coulomb摩擦模型的平滑近似。该方法还涉及在每个时间步骤中构建接触耦合系统的全局碰撞点，并使用线搜索过滤的牛顿方法对其进行最小化。此外，该方法还包括使用Affine CCD (Continuous Collision Detection)和通过i-AABB (Intersection-AABB)进行接触剔除，以确保非交叉并高效评估接触对。作者还提出了一种考虑系统中接触耦合的接触感知Hessian构建方法。

## 结果:

- a. 详细的实验设置:
  - 本文的实现平台是一台配备Intel i9 11900K CPU、64GB内存和Nvidia 3090 GPU的台式电脑。
  - 数值方法使用C++在CPU上实现，使用Eigen库进行线性代数计算，使用Intel TBB进行并行化。
  - 基准测试主要与刚性-IPC和Bullet进行比较，它们分别代表基线和最先进的刚体模拟器。
- b. 详细的实验结果:
  - 在模拟金属球与一堆木块碰撞的实验中，ABD比刚性-IPC快124倍。
  - 在模拟小型链网的实验中，ABD比刚性-IPC快34倍。
  - 在模拟具有复杂碰撞和接触的大型链网的实验中，ABD比刚性-IPC快1200倍。
  - 在模拟初始由摩擦平衡的10层卡片堆的实验中，ABD比刚性-IPC快103倍。
  - 在涉及动态摩擦/接触的螺纹示例的模拟中，ABD比刚性-IPC快30倍。
  - 在以静态摩擦为主的拱形示例的模拟中，ABD比刚性-IPC快77倍。
  - 在使用CUDA在大型链网模拟中，ABD相对于刚性-IPC实现了总体加速比达到10000倍。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
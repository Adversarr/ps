---
paperSource: EUROGRAPHICS
paperAuthor: "Min Hyung Kee, Kiwon Um, HyunMo Kang, JungHyun Han"
paperYear: 2023
doi: 
title: "An Optimization-based SPH Solver for Simulation of Hyperelastic Solids"
date: 2023-11-18
tags: 
  - SPH
  - Hyperelasticity
---


本文提出了一种基于优化的SPH求解器，用于模拟超弹性固体。通过将隐式积分方案转化为优化问题，并使用通用的拟牛顿方法进行求解，实现了对不同类型的超弹性材料（如Neo-Hookean和St. Venant-Kirchoff模型）的模拟。实验结果表明，该方法在SPH框架中能够稳定高效地模拟复杂材料，并简化了不同材料之间的耦合和碰撞处理。

<!-- more -->

提出了一种使用光滑粒子流体力学 (SPH) 模拟超弹性固体的新方法。该方法将最先进的弹性SPH固体方法扩展到包括不同类型的超弹性材料。将SPH弹性实体的隐式积分方案重新表述为优化问题，并使用通用准牛顿方法求解。使用有限内存 BFGS (L-BFGS) 算法来有效地解决 SPH 框架中的优化问题。本发明的方法演示了在SPH框架下对复杂材料进行稳定、高效的模拟。由于对固体和流体的统一表示，它简化了不同材料之间的耦合和操作碰撞。

## Basic Information:

- Title: An Optimization-based SPH Solver for Simulation of Hyperelastic Solids (基于优化的SPH求解器用于超弹性固体模拟)
- Authors: Min Hyung Kee, Kiwon Um, HyunMo Kang, JungHyun Han
- Affiliation: Korea University, Korea (韩国高丽大学)
- Keywords: hyperelastic solids, Smoothed Particle Hydrodynamics (SPH), optimization, simulation (超弹性固体，平滑粒子流体动力学，优化，模拟)
- URLs: [Paper](https://diglib.eg.org/) , [GitHub: None]

## 论文简要 :

- 本文提出了一种基于优化的SPH求解器，用于模拟超弹性固体。通过将隐式积分方案转化为优化问题，并使用通用的拟牛顿方法进行求解，实现了对不同类型的超弹性材料（如Neo-Hookean和St. Venant-Kirchoff模型）的模拟。实验结果表明，该方法在SPH框架中能够稳定高效地模拟复杂材料，并简化了不同材料之间的耦合和碰撞处理。

## 背景信息:

- 论文背景: 弹性固体的模拟一直是计算机图形学中的研究热点。然而，当模拟涉及到不同类型的材料和不同离散化方法时，通常需要复杂的耦合机制来稳定求解不同材料之间的相互作用。
- 过去方案: 为了解决不同模拟方法之间的耦合问题，研究人员提出了基于粒子的统一框架，如基于位置的动力学（PBD）和平滑粒子流体动力学（SPH）。这些统一框架不仅简化了耦合机制，还便于处理相变和碰撞。
- 论文的Motivation: 然而，现有的SPH弹性固体模拟方法在处理大变形时往往存在不稳定性问题。本文旨在提出一种新的SPH弹性固体模拟方法，通过优化求解的方式支持更复杂的超弹性模型，并解决现有方法的不稳定性问题。通过将隐式积分方案转化为优化问题，并使用L-BFGS算法进行求解，实现了对超弹性模型的稳定模拟。

## 方法:

- a. 理论背景:
  - 本文提出了一种新的方法，用于使用平滑粒子流体动力学（SPH）模拟超弹性固体。该方法将最先进的弹性SPH固体方法扩展到包括不同类型的超弹性材料，如Neo-Hookean和St. Venant-Kirchoff模型。该方法将SPH弹性固体的隐式积分方案重新构造为一个优化问题，并使用通用的拟牛顿方法来解决。采用有限内存BFGS（L-BFGS）算法来高效地解决SPH框架中的优化问题。该方法在SPH框架中展示了复杂材料的稳定和高效的模拟。
- b. 技术路线:
  - 本文提出的方法是一种基于优化的平滑粒子流体动力学（SPH）求解器，用于模拟超弹性固体。通过Bonet和Lok提出的一种鲁棒方法来评估变形梯度。使用变形梯度和弹性能量密度函数定义超弹性能量。为了解决零能量模式的问题，引入了隐式惩罚力。将优化问题形式化为最小化目标函数的系统下一个状态的问题。采用L-BFGS算法来解决优化问题。基于超弹性能量的常数近似确定Hessian矩阵的初始近似。使用无散SPH求解器实现固体-流体耦合和碰撞处理。

## 结果:

- a. 详细的实验设置:
  - 本文使用基于OpenMP的并行化的AMD Ryzen 7 5800X 3.8 GHz处理器进行了实验。使用了各种超弹性材料进行了测试，包括旋转、Neo-Hookean和St. Venant-Kirchoff模型，以及多个超弹性固体之间的相互作用和与流体的双向耦合。实验使用了开源的基于SPH的模拟框架SPlisHSPlasH和线性代数库Eigen。
- b. 详细的实验结果:
  - 本文进行了两个实验，名为“Swinging cloth”和“Stretching cube”，以展示基于优化的求解器的稳定性和鲁棒性。两个实验都使用了旋转材料。与一种名为操作分裂求解器（OSS）的最先进的基于SPH的弹性求解器相比，结果进行了比较。在“Swinging cloth”实验中，模拟了一个附着在固定点上的弹性布料受到重力作用的情况。OSS求解器在具有大变形区域中出现了振荡伪影。增加OSS中的零能量控制参数会导致不希望的刚性运动。相比之下，基于优化的求解器成功地模拟了大变形，没有振荡伪影或人为刚度。在“Stretching cube”实验中，测试了一个几乎不可压缩的弹性长方体固体的变形。基于优化的求解器只需两次迭代和较大的时间步长即可产生稳定的模拟。相比之下，OSS需要更小的时间步长才能实现稳定，所需时间大约是基于优化的求解器的五倍。其他实验还包括“Twisting beam”实验，模拟了两端扭曲的弹性梁，以及“Colliding bunnies”实验，测试了SPH框架处理复杂超弹性材料之间碰撞的能力。此外，还进行了“Melting duck”实验，模拟了一个可变形的鸭子掉落到热板上的情况。基于优化的求解器通过根据粒子温度减小弹性力大小有效地处理了熔化效应。最后，还成功地将基于优化的求解器应用于超弹性固体与流体的耦合。将多个超弹性固体投放到一个盒子中，并从两个喷嘴中向盒子中喷射流体。求解器与DFSPH流体求解器共同工作，准确地模拟了固体和流体之间的相互作用和双向耦合。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
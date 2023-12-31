---
paperSource: TOG
paperAuthor: "David Hahn, Pol Banzet, James M. Bern, Stelian Coros"
paperYear: 2019
doi: 10.1145/3355089.3356548
title: "Real2Sim: Visco-elastic parameter estimation from dynamic motion"
date: 2023-11-04
tags: 
  - Differentiable Simulation
---

*从动态运动中估计粘弹性参数*

本文提出了一种从真实世界的软物体的动态运动中优化粘弹性材料参数的方法，**通过直接敏感性分析或伴随状态方法计算材料参数的梯度**，并优化材料参数以使模拟运动尽可能接近真实观测。通过这种方式，**我们可以直接构建一个能够捕捉感兴趣样本的粘弹性行为的有用模拟模型**。我们在各种示例中展示了我们方法的有效性，包括数值粗化、自定义目标函数以及由泡沫或3D打印格子结构制成的真实柔性弹性物体，包括软体机器人的演示应用。

<!-- more -->

## Basic Information:

- Title: Real2Sim: Visco-elastic parameter estimation from dynamic motion (Real2Sim：从动态运动中估计粘弹性参数)
- Authors: David Hahn, Pol Banzet, James M. Bern, Stelian Coros
- Affiliation: ETH Zürich (ETH苏黎世联邦理工学院)
- Keywords: Deformable Models, Motion Capture, Optimization, Physically-based Simulation, Robotics
- URLs: [Paper](https://doi.org/10.1145/3355089.3356548), [GitHub: None]

## 论文简要 :

- 本文提出了一种从真实世界的软物体的动态运动中优化粘弹性材料参数的方法，通过直接敏感性分析或伴随状态方法计算材料参数的梯度，并优化材料参数以使模拟运动尽可能接近真实观测。通过这种方式，我们可以直接构建一个能够捕捉感兴趣样本的粘弹性行为的有用模拟模型。我们在各种示例中展示了我们方法的有效性，包括数值粗化、自定义目标函数以及由泡沫或3D打印格子结构制成的真实柔性弹性物体，包括软体机器人的演示应用。

## 背景信息:

- 论文背景: 创建准确捕捉真实物体变形行为的快速模拟模型并不容易。即使物理材料参数已知（例如通过专门的测量工具），由于各种其他问题，这些参数可能无法直接转化为实际模拟，这些问题包括所选择的数值方法的局限性、需要高分辨率离散化以获得准确解以及非线性材料的测试和模拟变形范围之间的不匹配。许多软材料还由于制造过程中的不一致性而在相同基础材料制成的多个物体之间表现出粘弹性参数的大幅变化。
- 过去方案: 传统方法是首先使用标准测试测量材料的小样本，然后构建足够分辨率的模拟模型以重现测量数据，最后将该模型应用于实际感兴趣的物体。然而，这些步骤中的每一步都需要高精度才能获得令人满意的结果。此外，许多材料测试设备（如流变仪）只能测量线性变形范围，即材料的小应变行为。如何将这些测量推广到非线性范围对于许多材料来说并不完全清楚。总的来说，即使可以以这种方式构建准确的模拟模型，由于数值误差和伪影，它可能无法用于快速、低分辨率的模拟，需要额外的修正，如数值粗化，才能达到实际有用的模拟。
- 论文的Motivation: 鉴于这些挑战，我们的目标是回答以下问题：我们如何找到一个模拟模型，它能够（a）捕捉感兴趣的变形行为，（b）适用于非线性和可能非均匀的材料，（c）在实际分辨率下使用？

## 方法:

- a. 理论背景:
  - 本文提出了一种优化有限元模拟中粘弹性材料参数的方法，以最佳逼近真实软物体的动态运动。目标是找到一个适合实际分辨率的模拟模型，能够捕捉非线性和可能非均匀材料的变形行为。传统的测量材料参数和构建模拟模型的方法在快速、低分辨率模拟中可能由于数值误差和伪影而无法使用。所提出的方法直接将粘弹性有限元模拟与真实运动数据拟合，从而得到适用于相对粗糙的网格和感兴趣的变形和运动范围的模拟模型。这项工作在软体机器人控制和软物体操纵方面具有应用价值。
- b. 技术路线:
  - 本文首先描述了一种弹性动力学有限元方法（FEM），然后使用直接敏感性分析和伴随状态方法推导了目标函数的梯度。得到的方程允许计算目标函数的梯度。作者还讨论了使用二阶向后差分公式（BDF2）进行时间离散化，并解释了为什么选择了这种方法。
  - 实验方法涉及使用商业光学运动捕捉系统和10个OptiTrack Prime 13相机。使用小型半球形反射标记物跟踪软标本的变形，使用带有运动捕捉标记物的刚性夹具跟踪夹具的运动，并将其映射到模拟中的Dirichlet边界条件。运动捕捉数据和模拟共享一个公共坐标系。目标函数基于运动捕捉标记物的跟踪轨迹与模拟中的“虚拟标记物”之间的距离来制定。计算每个标记物的均方根误差以评估模拟的准确性。测试标本和软体机器人的材料采用了柔性聚氨酯泡沫，具体是Smooth-On公司的FlexFoam-iT III和V。泡沫的混合和成型，其材料参数根据环境温度和混合比等因素而变化。快速参数估计对于确定每个标本的特定参数至关重
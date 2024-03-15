---
paperSource: SIGGRAPH
paperAuthor: ""
paperYear: 2020
doi: 
title: "IQ-MPM: An Interface Quadrature Material Point Method for Non-sticky Strongly Two-Way Coupled Nonlinear Solids and Fluids"
date: 2023-12-21
tags: 
  - Fluids
  - MPM
  - FSI
---

# Basic Information:

- Title: IQ-MPM: An Interface Quadrature Material Point Method for Non-sticky Strongly Two-Way Coupled Nonlinear Solids and Fluids (IQ-MPM: 一种界面积分材料点法，用于非粘弹性固体和流体的强耦合双向耦合)
- Authors: Yu Fang, Ziyin Qu, Minchen Li, Xinxin Zhang, Yixin Zhu, Mridul Aanjaneya, and Chenfanfu Jiang
- Affiliation: University of Pennsylvania (宾夕法尼亚大学)
- Keywords: Fluids, numerical methods, MPM, Fluid-structure interaction
- URLs: [Paper](https://doi.org/10.1145/3386569.3392438), [GitHub: None](https://github.com/)

# 论文简要 :

- 本研究提出了一种新颖的方案，用于模拟非粘弹性固体和不可压缩流体之间的双向耦合相互作用，通过界面积分材料点法（IQ-MPM），成功解决了传统MPM在处理多材料界面时的粘滞问题。

# 背景信息:

- 论文背景: 现代应用中需要快速的固体-流体耦合方法，以模拟丰富的物理相互作用，如虚拟手术、数字制造和软体机器人等。
- 过去方案: 传统的分离方案在稳定性方面存在问题，需要较小的时间步长；而单体方案则需要外部迭代以解决非线性问题，计算成本较高。
- 论文的Motivation: 鉴于现有方法的局限性，研究人员提出了一种新颖的界面积分材料点法，旨在解决传统MPM在处理多材料界面时的粘滞问题，从而实现更稳定和高效的固体-流体耦合模拟。

# 方法:

- a. 理论背景:
  - 本文提出了一种名为IQ-MPM的新颖方案，用于模拟非线性弹性固体和不可压缩流体之间的双向耦合相互作用。该方法的关键是通过弱形式处理强耦合的非线性弹性体和不可压缩流体的幽灵矩阵算子分裂方案。该方案允许在CFL极限下处理大时间步长的稳定和高效，并且即使对于高度非线性的弹性固体，也使用单一的整体求解来处理耦合压力场。该方案采用材料点法（MPM）设计，保持了与混合拉格朗日-欧拉流体求解器的离散一致性。该方案还采用界面积分（IQ）离散化来支持自由滑移边界条件，在固体-流体界面处支持不连续的切向速度。IQ-MPM框架完全基于粒子，避免了中间水平集或显式网格表示所带来的复杂性。该方案的有效性通过各种具有挑战性的流体-弹性体相互作用模拟得到验证。
- b. 技术路线:
  - 该方法称为界面积分材料点法（IQ-MPM），是一种整体的双向耦合方法，将材料点法（MPM）用于非线性可压弹性和不可压自由表面流体。该方法确保了具有不连续切向速度的自由滑移界面，避免了多材料相互作用中常见的数值粘滞性伪影。
  - 该方法包括几个步骤。首先，将固体连续体视为超弹性固体组件和类似空气的无质量幽灵矩阵连续体的组合。将固体与流体的相互作用重新构造为矩阵与流体之间的仅压力相互作用。
  - 接下来，假设无粘性的不可压缩流体域。使用不可压缩性假设和滑移边界的压力来求解流体方程。
  - 为了解决完全耦合的系统，该方法采用算子分裂。使用完全非线性的牛顿求解来推进固体速度，忽略矩阵和流体。然后，固体速度替换完全线性耦合方程中的原始速度。
  - 该方法还包括对系统
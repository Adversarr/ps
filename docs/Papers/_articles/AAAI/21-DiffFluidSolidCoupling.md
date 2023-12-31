---
paperSource: AAAI
paperAuthor: "Tetsuya Takahashi, Junbang Liang, Yi-Ling Qiao, Ming C. Lin"
paperYear: 2021
doi: 
title: "Differentiable Fluids with Solid Coupling for Learning and Control "
date: 2023-11-06
tags: 
  - Differentiable Simulaation
  - FSI
---

本文提出了一种高效的可微分流体模拟器，可以与深度神经网络集成，作为学习动力学和解决控制问题的一部分。通过使用变分原理，该模拟器能够处理流体与刚体物体的**单向耦合**，并在流体-固体界面上自然地施加必要的边界条件。通过应用伴随方法，该模拟器能够高效地计算多个时间步长的流体模拟的梯度，并在解决涉及单向耦合固体的逆问题和控制问题时表现出比先前的梯度计算、无导数优化和无模型强化学习技术至少高一个数量级的性能。

<!-- more -->

# Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.

## Basic Information:

- Title: Differentiable Fluids with Solid Coupling for Learning and Control (可学习和控制的可微分流体与固体耦合)
- Authors: Tetsuya Takahashi, Junbang Liang, Yi-Ling Qiao, Ming C. Lin
- Affiliation: Adobe, University of Maryland at College Park (第一作者隶属于Adobe)
- Keywords: differentiable fluids, solid coupling, learning, control
- URLs: [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/16547), [GitHub: None]

## 论文简要 :

- 本文提出了一种高效的可微分流体模拟器，可以与深度神经网络集成，作为学习动力学和解决控制问题的一部分。通过使用变分原理，该模拟器能够处理流体与刚体物体的**单向耦合**，并在流体-固体界面上自然地施加必要的边界条件。通过应用伴随方法，该模拟器能够高效地计算多个时间步长的流体模拟的梯度，并在解决涉及单向耦合固体的逆问题和控制问题时表现出比先前的梯度计算、无导数优化和无模型强化学习技术至少高一个数量级的性能。

## 背景信息:

- 论文背景: 可微分物理学是一种强大而有效的方法，用于解决控制和逆问题。不同于传统的物理模拟方法，可微分物理学的不同之处在于其能够计算具有用户定义目标函数的梯度，从而可以使用基于梯度的优化器来高效地解决问题。
- 过去方案: 过去的研究已经提出了许多可微分物理学的方法，包括刚体、可变形物体、薄壳和布料等不同类型的物体。然而，针对流体材料的可微分方法因其不同的流体模拟方法而有所不同，通常由于空间离散化技术的差异。
- 论文的Motivation: 由于流体系统的自由度较多且计算成本较高，利用梯度信息来高效地最小化目标函数是必不可少的。然而，现有的可微分流体模拟方法在处理涉及固体相互作用的流体行为时仍存在一些挑战，因此需要开发一种新的方法来解决这些问题。

## 方法:

- a. 理论背景:
  - 本文介绍了一种可与深度神经网络集成的可微分流体模拟器，用于学习动力学和解决控制问题。该模拟器使用变分原理处理流体与刚体物体的单向耦合，并在流体-固体界面处强制施加必要的边界条件。采用伴随方法有效地计算多个时间步长的流体模拟的梯度，用户可以定义目标函数。该方法在梯度计算、无导数优化和无模型强化学习技术方面优于以往的方法。
- b. 技术路线:
  - 本文提出的可微分流体模拟器作为深度神经网络中的一部分进行集成，实现端到端的学习和梯度反向传播。该模拟器通过强制流体不可压缩性和在流体-固体界面处应用自由滑移边界条件来处理单向耦合的固体。伴随方法应用于动力系统的整个模拟步骤，实现高效可扩展的梯度计算。模拟器基于高级流体模拟操作的自动微分计算梯度，避免了低级原始操作的昂贵反向模式自动微分。

## 结果:

- a. 详细的实验设置:
  - 本文未提及实验设置。
- b. 详细的实验结果:
  - 本文进行了多个实验比较：
    - 对比试验：作者将基于伴随方法的方法与使用中心有限差分法（FD）进行了比较。结果表明，作者的方法比FD快得多，平均相对误差小于1.0%。作者的方法的计算成本与控制输入的数量基本无关，而FD的计算成本与控制自由度的数量呈线性增长。作者得出结论，他们的方法在实际应用中具有优势。
    - 与体素化方法的比较：作者将他们的方法与McNamara等人（2004）的体素化方法进行了比较。结果表明，作者的方法实现了亚网格精度，而体素化方法实现了体素分辨率。在反向传递中忽略体积分数会对梯度的准确性产生负面影响。考虑体积分数的梯度的相对误差为1.8%，而不考虑体积分数的相对误差为6.4%。
    - 与PhiFlow的比较：作者将他们的方法与PhiFlow（Holl, Thuerey和Koltun 2020）进行了比较。结果表明，作者的方法在梯度计算性能方面比PhiFlow快1-2个数量级。
    - 与低级自动微分的比较：作者将他们的高级自动微分（AD）与使用PyTorch 1.5中的C++ AD实现的低级AD进行了比较。结果表明，作者的高级AD比低级AD快得多。
    - 空间-时间优化：作者展示了他们的可微分模拟器在流体控制的空间-时间优化中的效率。他们将他们的方法与无导数优化器CMA-ES进行了比较。他们的方法快速收敛并生成所需的速度场，而CMA-ES无法收敛并生成与所需速度场相距甚远的速度场。
    - 学习和控制：作者将他们的模拟器与神经网络集成，用于学习和控制。他们在一个控制场景中展示了他们的方法的有效性，其中一个刚性盒子被控制以生成所需的速度。他们使用训练好的神经网络在每个模拟步骤生成控制输入，并实现了所需的速度。
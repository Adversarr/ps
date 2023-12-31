---
paperSource: Arxiv
paperAuthor: "Yufei Wang, Zhou Xian, Feng Chen, Tsun-Hsuan Wang, Yian Wang, Katerina Fragkiadaki, Zackory Erickson, David Held, Chuang Gan"
paperYear: 2023
doi: "abs/2311.01455v1"
title: "ROBOGEN: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation"
date: 2023-11-11
tags: 
  - Robot
  - LLM
---

本文提出了RoboGen，一种通过生成模拟实现自动学习多样化机器人技能的生成式机器人代理。RoboGen利用了基础模型和生成模型的最新进展，通过生成模拟自动产生多样化的任务、场景和训练监督，从而在最小的人工监督下扩展机器人技能学习。我们的方法为机器人代理配备了自主提出-生成-学习循环：代理首先提出有趣的任务和技能进行开发，然后通过合适的空间配置将相关对象和资源填充到模拟环境中生成相应的模拟环境。然后，代理将提出的高级任务分解为子任务，选择最佳的学习方法（强化学习、运动规划或轨迹优化），生成所需的训练监督，然后学习策略以获得提出的技能。我们的工作旨在提取大规模模型中嵌入的广泛而多样化的知识，并将其转移到机器人领域。我们的完全生成式流水线可以重复查询，产生与各种任务和环境相关的无限技能演示流。

这篇文章的创新之处在于通过最小化人类监督来扩大机器人技能学习的规模。文章提出了一种自主引导的提出-生成-学习循环方法，使机器人代理能够自主提出有趣的任务和技能，并通过生成相应的仿真环境来学习这些技能。该方法将高级任务分解为子任务，并选择最优的学习方法（强化学习、运动规划或轨迹优化），生成所需的训练监督，并学习获取所提出的技能。这项工作试图提取大规模模型中嵌入的广泛而多样化的知识，并将其转移到机器人领域。通过不断查询，我们的完全生成式流水线可以产生与各种任务和环境相关联的无限技能演示。

<!-- more -->

## Basic Information:

- Title: ROBOGEN: TOWARDS UNLEASHING INFINITE DATA FOR AUTOMATED ROBOT LEARNING VIA GENERATIVE SIMULATION (ROBOGEN：通过生成模拟实现无限数据的自动化机器人学习)
- Authors: Yufei Wang, Zhou Xian, Feng Chen, Tsun-Hsuan Wang, Yian Wang, Katerina Fragkiadaki, Zackory Erickson, David Held, Chuang Gan
- Affiliation: CMU, Tsinghua IIIS, MIT CSAIL, UMass Amherst, MIT-IBM AI Lab (CMU, 清华大学信息科学与技术学院, MIT CSAIL, UMass Amherst, MIT-IBM AI Lab)
- Keywords: generative simulation, robotic skill learning, automated learning, diverse tasks, simulation environments (生成模拟, 机器人技能学习, 自动化学习, 多样化任务, 模拟环境)
- URLs: [Paper](https://arxiv.org/abs/2311.01455v1), [GitHub](https://robogen-ai.github.io/)

## 论文简要 :

- 本文提出了RoboGen，一种通过生成模拟实现自动学习多样化机器人技能的生成式机器人代理。RoboGen利用了基础模型和生成模型的最新进展，通过生成模拟自动产生多样化的任务、场景和训练监督，从而在最小的人工监督下扩展机器人技能学习。我们的方法为机器人代理配备了自主提出-生成-学习循环：代理首先提出有趣的任务和技能进行开发，然后通过合适的空间配置将相关对象和资源填充到模拟环境中生成相应的模拟环境。然后，代理将提出的高级任务分解为子任务，选择最佳的学习方法（强化学习、运动规划或轨迹优化），生成所需的训练监督，然后学习策略以获得提出的技能。我们的工作旨在提取大规模模型中嵌入的广泛而多样化的知识，并将其转移到机器人领域。我们的完全生成式流水线可以重复查询，产生与各种任务和环境相关的无限技能演示流。

## 背景信息:

- 论文背景: 本研究的动机是机器人学习领域中一个长期存在且具有挑战性的目标：赋予机器人多样化的技能，使其能够在各种非工厂环境中操作并执行广泛的任务。近年来，在教授机器人各种复杂技能方面取得了令人瞩目的进展：从可变形物体和流体操作到动态和灵巧技能，如物体投掷、手中重新定位、踢足球甚至机器人跑酷。然而，这些技能仍然是孤立的，具有相对较短的时间范围，并且需要人工设计的任务描述和训练监督。由于实际数据收集的昂贵和繁琐性质，许多这些技能是在具有适当领域随机化的模拟中进行训练，然后部署到实际环境中。
- 过去方案: 过去的研究中，模拟环境已成为多样化机器人技能学习的重要推动力。与在现实世界中进行探索和数据收集相比，模拟环境中的技能学习具有几个优势：1）模拟环境提供对特权低级状态和无限探索机会；2）模拟支持大规模并行计算，可以更快地收集数据，而无需依赖大量投资于机器人硬件和人力资源；3）在模拟中进行探索可以使机器人开发闭环策略和错误恢复能力，而现实世界的演示通常只提供专家轨

## 方法:

- a. 理论背景:
  - 本文介绍了RoboGen，一种通过生成式模拟学习多样化机器人技能的生成式机器人代理。目标是使机器人能够在各种非工厂环境中操作并执行广泛的任务。作者强调了当前机器人技能的局限性，这些技能是分隔的，具有短期视野，并且需要人工设计的任务描述和训练监督。作者提出了一种生成式方案，利用生成模型自动生成任务、场景和训练监督，从而在最小的人工监督下扩大机器人技能学习的规模。所提出的方法涉及自主引导的提出-生成-学习循环，代理提出任务和技能，生成模拟环境，将任务分解为子任务，选择最佳学习方法，生成训练监督，并学习获取所提出的技能。本文旨在从大规模模型中提取广泛的知识，并将其转化为机器人领域，提供与各种任务和环境相关的无尽技能演示。
- b. 技术路线:
  - RoboGen是一个自动化流水线，利用基础模型（如LLMs）为机器人技能学习生成任务、场景和训练监督。流水线包括几个阶段：任务提出、场景生成、训练监督生成和技能学习。
  - 在任务提出阶段，系统为机器人生成高级任务。它从特定的机器人类型和随机抽样的对象开始初始化系统。这些信息被用作LLM的输入，以提出任务。采样过程确保任务的多样性，因为不同的机器人-对象组合可以导致各种任务。另一个选项是基于示例的初始化，其中使用提供的机器人和示例任务作为任务提出的提示。
  - 在场景生成阶段，根据提出的任务生成模拟场景。场景组件和配置是根据任务描述条件生成的。此外，获取相关资产的查询以增加场景的复杂性和多样性。这些查询用于检索或生成场景所需的对象资产。
- 
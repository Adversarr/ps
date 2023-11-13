---
paperSource: EUROGRAPHICS
paperAuthor: "X. L. Wang, M. Tang, D. Manocha, R. F. Tong"
paperYear: 2018
doi: "10.1111/cgf13499"
title: "Efﬁcient BVH-based Collision Detection Scheme with Ordering and Restructuring"
date: 2023-11-13
tags: 
  - BVH
  - Accelerate
---

本文提出了一种基于BVH的高效碰撞检测方案，通过排序和重构BVH和BVTT前端，解决了大变形和GPU缓存效率低下的问题，实现了高效的碰撞查询，并在具有空时相干性的模拟中表现出色。

<!-- more -->

## Basic Information:

- Title: Efﬁcient BVH-based Collision Detection Scheme with Ordering and Restructuring (基于BVH的高效碰撞检测方案：排序和重构)
- Authors: X. L. Wang, M. Tang, D. Manocha, R. F. Tong
- Affiliation: Zhejiang University, China (浙江大学)
- Keywords: collision detection, BVH, ordering, restructuring
- URLs: [Paper](https://diglib.eg.org/handle/10.1111/cgf13499) , [GitHub: None]

## 论文简要 :

- 本文提出了一种基于BVH的高效碰撞检测方案，通过排序和重构BVH和BVTT前端，解决了大变形和GPU缓存效率低下的问题，实现了高效的碰撞查询，并在具有空时相干性的模拟中表现出色。

## 背景信息:

- 论文背景: 碰撞检测在基于物理的计算机模拟中通常是性能瓶颈。本文主要关注广相碰撞检测，其中广相步骤通过使用边界体积（BV）来排除不可能发生碰撞的物体，生成潜在碰撞集合。
- 过去方案: 过去的广相碰撞检测方法主要采用空间细分和对象分割两种主要方法。空间细分算法将空间划分为单元格，而对象分割方法则使用边界体积层次结构（BVH）作为主要选择。然而，这些方法在处理大变形和GPU缓存效率低下时存在一些问题。
- 论文的Motivation: 鉴于过去方法的局限性，本文旨在通过排序和重构BVH和BVTT前端来提高碰撞检测的效率。通过分析BVTT前端和BVH质量的动态状态，本文提出了一种基于直方图排序和辅助结构BVTT前端日志的技术，有效处理物体间和物体内的碰撞，并在具有空时相干性的模拟中表现出色。

## 方法:

- a. 理论背景:
  - 本文介绍了基于物理的计算机模拟中碰撞检测的问题及其在触觉、机器人和制造等领域的重要性。碰撞检测包括基于边界体积的广相位步骤和检查精确交叉的狭相位步骤。本文的重点是广相位碰撞检测。
- b. 技术路线:
  - 本文提出的方法旨在提高基于边界体积层次结构（BVH）的碰撞检测中的缓存命中率和内存带宽利用率。它通过优化BVH节点和BVTT前端的布局来减少缓存未命中和内存延迟。该方法包括以下步骤：
    1. 友好的缓存BVH布局计算：使用遍历的内部节点的左边界作为参考，为外部节点创建段。每个段内的内部节点位置按严格升序排列，以匹配深度优先顺序。
    2. 友好的缓存和较少分歧的BVTT前端：根据每个前端节点的第二个组件，将BVTT前端分为外部和内部前端。这种分类有助于提高带宽效率和减少分支分歧。前端节点进一步按深度优先顺序布局，以更好地利用缓存。

## 结果:

- a. 详细的实验设置:
  - 本文未提及实验设置。
- b. 详细的实验结果:
  - 本文未提及实验结果。

## Note:

- 本总结源自于LLM的总结，请注意数据判别. Power by ChatPaper. End.
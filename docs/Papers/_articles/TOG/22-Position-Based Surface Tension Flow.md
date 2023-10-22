---
paperSource: TOG
paperAuthor:
  - JINGRUI XING∗, SIST & KLMP (MOE), Peking University, China
  - LIANGWANG RUAN∗, SCS & KLMP (MOE), Peking University, China BIN WANG†, Beijing Institute for General Artificial Intelligence, China BO ZHU, Dartmouth College, United States of America
  - BAOQUAN CHEN†, SIST & KLMP (MOE), Peking University, China
paperYear: 2022
title: Position-Based Surface Tension Flow
date: 2023-10-22
---

本文提出了在PBD框架下流体表面张力的计算方法，为PBD框架下的流体模拟提供了更真实的表面张力和与固体的接触，能够支持薄膜、液滴等复杂界面。其关键是动态地对流体表面进行局部网格划分。该算法通过局部网格划分，得到每个表面粒子周围的局部几何体，并基于该几何体，计算表面张力约束，整合入PBD框架中。相较于其他方法，该算法具有较高的计算效率较高和鲁棒性。

<!-- more -->
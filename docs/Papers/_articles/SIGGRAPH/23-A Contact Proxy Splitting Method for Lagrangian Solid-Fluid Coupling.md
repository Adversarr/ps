---
title: A Contact Proxy Splitting Method for Lagrangian Solid-Fluid Coupling
paperAuthor: TIANYI XIE, MINCHEN LI, YIN YANG, and CHENFANFU JIANG
paperSource: SIGGRAPH
paperYear: 2023
date: 2023-10-22
---

本文提出了一种用于FEM可变形体与SPH流体之间的强流固耦合算法。首先，本文将SPH流体的运动、不可压条件等求解转化为能量函数优化问题。其次，本文将流固耦合问题转化为流体粒子与固体网格之间的碰撞问题，通过引入了IPC模型，在运动求解的同时处理了碰撞与耦合，并提出了强流固耦合对应的能量函数优化问题。最后，本文针对提出的优化问题使用了交替迭代方法，借助Contact Proxy实现了快速且稳定的求解。

<!-- more -->


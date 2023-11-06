---
---

# Backward methods

## Auto Diff

语言层面的自动微分计算。

Explicit method.

- 计算图（PyTorch）
- Tape（Tensorflow、Taichi）

Papers:

1. GradSim (∇Sim: DIFFERENTIABLE SIMULATION FOR SYSTEM IDENTIFICATION AND VISUOMOTOR CONTROL)
2. A Differentiable Physics Engine for Deep Learning in Robotics
3. Taichi
4. ChainQueen: Cuda


## Dual Diff

和前向仿真同时计算，使用 Taylor 展开

1. DiffFR

## Adjoint Method

通常基于 Implicit method

1.  DiffPD, DiffCloth
2.  DiffXPBD
3.  ADD
4.  Differentiable Fluids with Solid Coupling for Learning and Control
5.  Efﬁcient Differentiable Simulation of Articulated Bodies(2021 icml)
6.  Fluid Control Using the Adjoint Method (2004)
7.  Keyframe Control of Complex Particle Systems Using the Adjoint Method

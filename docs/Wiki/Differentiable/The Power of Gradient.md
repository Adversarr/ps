---
title: The power of gradient in Inverse Dynamics Problems
author: Du Tao
---

<!-- more -->

动力系统中求解反问题

## Introduction

状态量：$s$ 描述整个系统。

随着时间变化：$\dot s$

PDE 就是一个动力系统。

$$ F(s, \quad \dot s, \ddot s, ...) = 0 $$

$s$ 仅仅是输入的一部分，还有很多参数：
1. 内部参数：物体属性
2. 外部参数：外力

### Concrete Example

mass-spring system

- 状态：$x(t)$
- 参数：质量、弹簧系数
- 模型：胡克定律+牛顿第二定律

### Two problem

Forward problem: Given model and parameter, compute the state sequence
- Parameterization: Describe the param and variable
- Modeling: Equation
- Evaluation: Solve the equation

Inverse dynamics problem: Given the state of a dynamic system, infer its model and parameters.
- 将Forward Problem的三步骤反过来

### The gradient methodology

Three part: 
1. Parameterization
2. Modeling
3. Evaluation

## Parameterization

Find the optimal shape and control of soft robotic fishes to achieve extermal performance.

- Desired Performance
- Known Dynamic Model
- ? Parameteriaztion

问题：
1. 有限元方法自由度高
2. 形态多样

需要一种简单高效的参数化方式

计算量！

Wasserstein Gradients

可以进行形状插值：实现光滑的形状变换

## Modeling

DiffPD. 

物理仿真平台：
1. Computational design
2. Perception and scensing
3. Plan and control
4. multi-agent

前传的数值技巧可以应用于反传

Background: Implicit time Integration

=> 变为求解非线性方程组

Bottleneck: Solve the matrix.

$$ L_y = L_{x_{i+1}} {x_{i+1}}_y \implies A z =  L_{x_{i+1}}\quad A x = \nabla F $$

Speed up: use pd to solve $z$

Idea: Efficient forward => Efficient backward

Applications: 
1. System Identification

## Parameterization

- Desired performance
- Modeling
- Parameterization: Control?

Challenge: Input is video.


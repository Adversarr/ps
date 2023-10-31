---
title: Affine Particle-In-Cell Method
date: 2022-10-30
paperAuthor: Chenfanfu Jiang
paperYear: 2015
paperSource: SIGGRAPH
tags: 
   - Fluid​​
   - MPM​​
---

Affine PIC 方法，相比于之前的方法

1. 保留了 PIC 的稳定性，但解决了耗散/误差问题
2. 保留了 FLIP 的动量、角动量守恒特性，但解决了不稳定的问题

主要思想：用一个仿射变换来代替原本的简单插值，从而解决p->g阶段的数据丢失。

<!-- more -->

# Affine Particle-In-Cell Method

## Introduction


### MPM

1. 欧拉网格
   1. 求力简单：均匀网格上的拉普拉斯算子容易计算
   2. 求运动困难
2. 拉格朗日粒子
   1. 求运动简单
   2. 容易让物理量守恒
   3. 求力困难：难以离散化、邻居查找较为困难

建立从Euler Grid到Lagrange Particle的信息传递，来描述一个连续体介质。

问题出现在信息传递过程中：存在信息丢失的情况（维数不同，会产生降维的情况）

### PIC

P→G：

1. mass: $m_i^n = \sum_p w_{ip}^n m_p$
2. velocity/linear momentum: $m_i^n \mathbf v_i ^ n = \sum_p w_{ip}^n m_p \mathbf v_p^n$

G update: use NS-equation and backward-euler.

1. velocity: $\mathbf v_i ^n \rightarrow \mathbf v_i ^{n+1}$

G→P:

1. velocity: $\mathbf v_p^{n+1} = \sum_i w_{ip}^n \mathbf v_i ^ {n+1}$

P update: newton equations:

1. position: $\mathbf x = \mathbf x + \mathbf v \Delta t$

P→G保角动量，但G→P只传递动量，角动量不保持。

### FLIP

## APIC

### RPIC

在每一个particle上添加角动量$L _ p ^ n$，并用动量相同的方法执行P→G

P→G:

1. Angular Momentum: $m_i^n \mathbf v_i ^ n = \sum _ p w_{ip}^n m _ p (\mathbf v_p ^ n + ((\mathbf K_p^n)^{-1}\mathbf L _ p ^ n)\times (\mathbf x_i^n - \mathbf x _ p ^ n))$

> 其中 $\mathbf K$ 是转动惯量张量，且$\mathbf \omega = (\mathbf K)^{-1} \mathbf L$

G→P:

1. Angular Momentum: $L_p^{n+1}= \sum_i w _{ip} ^ n (\mathbf x_i^n - \mathbf x _ p ^n)\times m_p \mathbf v _{i}^{n+1}$

简单粗暴的保持角动量的方法。

至此，转动动能保持、平动动能保持。对于刚体运动，其能量能够保持，信息无损失。

但考虑到流体不具有刚性，从而还需要保持shearing mode下的运动。

### Affine PIC

核心：粒子的速度场是分片仿射的。

解决RPIC中无法进行shearing的问题。

$$
P\rightarrow G: \mathbf v_i^n = \sum_p w_{ip}^n \mathbf (v_p^n +C_p^n (\mathbf x_i - \mathbf x_p))
$$

Problem: How to define $C$ efficiently. see [tech-doc](https://www.math.ucla.edu/~cffjiang/research/apic/tech-doc.pdf).

P→G:

1. mass
2. momentum: $m_i\mathbf v_i ^n = \sum_p w_{ip}^n m_p(\mathbf v_p^n +B_p ^n(D_p^n)^{-1}(\mathbf x_i^n - \mathbf x_i^p))$

G→P:

1. update: $B _ p ^{n+1} = \sum _ i w_{ip}^{n}\mathbf v_i^{n+1}(\mathbf x_i^n - \mathbf x_p^n)^T$
2. velocity.

---
paperSource: ICLR
paperAuthor: "Yuanming Hu†, Luke Anderson†, Tzu-Mao Li∗, Qi Sun‡, Nathan Carr‡, Jonathan Ragan-Kelley∗, Frédo Durand†"
paperYear: 2020
doi: 
title: "DiffTaichi: Differentiable Programming For Physical Simulation"
date: 2023-11-04
tags: 
  - Differentiable Simulation
  - Programming Language
---

我们介绍了 DiffTaichi，这是**一种新的可微编程语言**，专为构建高性能可微物理模拟器而设计。基于命令式编程语言，DiffTaichi 使用源代码转换生成仿真步骤的梯度，从而保持算术强度和并行性。**使用轻量级Tape记录整个仿真程序结构**，并以相反的顺序回放梯度内核，以实现端到端的反向传播。我们在 10 个不同的物理模拟器上展示了我们的语言在基于梯度的学习和优化任务中的性能和生产力。例如，用我们的语言编写的可微弹性对象模拟器比手工设计的 CUDA 版本短 4.2×但运行速度却一样快，比 TensorFlow 实现快 188 ×。使用我们的可微分程序，神经网络控制器通常只需数十次迭代即可进行优化。

<!-- more -->


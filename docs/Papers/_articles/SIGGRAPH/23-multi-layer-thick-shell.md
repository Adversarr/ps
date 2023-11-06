---
paperSource: SIGGRAPH
paperAuthor: "Yunuo Chen UCLA"
paperYear: 2023
doi: 
title: "Multi-Layer Thick Shells"
date: 2023-11-06
tags: 
  - Shell
---

实现了Thick Shell的模拟，实现了一定的褶皱，并且提出了一个交替方法来快速求解。

1. Reduced Prism Elements：三棱柱+中轴面建模 **Thick** Shell ⇒ 解决 Shell Locking
2. Complementary Wrinkle Coupling：褶皱耦合系统
3. Alternating Minimization：交替最小化，先固定低频信息（PN+Cholesky）、再处理高频信息（PN+CG）。

例子：瑜伽垫、皮衣、记忆枕等

<!-- more -->

---
paperSource: TOG
paperAuthor: ""
paperYear: 2023
doi: 
title: "Hierarchical Optimization Time Integration for CFL-Rate MPM Stepping"
date: 2024-03-14
tags: 
  - MPM
  - Optimization
  - Quasi-Newton
---

### Basic Information

- **Title:** Hierarchical Optimization Time Integration for CFL-Rate MPM Stepping
- **Authors:** Xinlei Wang, Minchen Li, Yu Fang, Xinxin Zhang, Ming Gao, Min Tang, Danny M. Kaufman, Chenfanfu Jiang
- **Affiliations:** Zhejiang University, University of Pennsylvania, Adobe Research, Tencent
- **Publication Date:** March 28, 2020
- **Journal:** arXiv:1911.07913v3 [cs.GR]
- **Keywords:** Material Point Method (MPM), Optimization Integrator, Quasi-Newton, Multigrid

### Introduction

This study introduces the Hierarchical Optimization Time (HOT) integration method for efficiently simulating the Material Point Method (MPM) irrespective of simulated materials and conditions. HOT leverages a hierarchical optimization algorithm that solves nonlinear time step problems for large-scale MPM systems near the CFL-limit, offering "out-of-the-box" convergent simulations across a wide variety of materials and computational resolutions without the need for parameter tuning.

### Overview

HOT is an implicit MPM time stepper accelerated by a custom-designed Galerkin multigrid wrapped in a quasi-Newton solver. It is highly parallelizable and robustly convergent, maintaining consistent and efficient performance across a broad range of finite strain elastodynamic and plastic examples. The method significantly outperforms existing state-of-the-art implicit MPM codes with up to 10× performance speedup across a wide range of challenging benchmark test simulations.

### Contributions

- A novel MPM-specific multigrid model exploiting the regularity of the background grid, constructing a Galerkin coarsening operator consistent with re-discretization via particle quadrature.
- Development of a new node-wise Characteristic Norm (CN) measure for MPM, enabling unified tolerancing across varying simulation resolutions, material parameters, and heterogeneous systems for both termination of inner solves in inexact Newton and convergence determination across methods.
- Construction of HOT as an "out-of-the-box" implicit MPM time integrator, employing the multigrid as an efficient inner initializer inside a performant quasi-Newton MPM time step solve.
- Extensive benchmark studies demonstrating the efficiency and accuracy of HOT on a diverse range of numerically challenging simulations.

### Limitations and Future Work

The paper discusses the challenges in building a multigrid hierarchy for MPM and the need for careful selection of tolerances for convergence. It suggests potential future directions in exploring more efficient solvers and extending the approach to other classes of PDEs and problems with graph structures.

### Techniques and Method

HOT integrates a hierarchical optimization algorithm with a quasi-Newton method for solving nonlinear time step problems in MPM. It uses a custom-designed Galerkin multigrid for acceleration, which is parallelizable and robustly convergent. The method includes a novel MPM-specific multigrid model, a new node-wise CN measure for unified tolerancing, and a quasi-Newton loop with a multigrid V-cycle as the inner initializer.

### Conclusion

HOT introduces a significant advancement in the simulation of hyperelastic solids using MPM, offering a stable, efficient, and flexible approach that outperforms existing methods without the need for per-example parameter tuning. It demonstrates the potential for wide applicability in computational sciences, including computational fluid dynamics and solid mechanics.
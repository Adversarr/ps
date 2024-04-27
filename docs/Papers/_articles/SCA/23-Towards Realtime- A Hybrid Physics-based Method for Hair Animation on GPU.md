---
paperSource: SCA
paperAuthor: "Li Huang, Fan Yang, Chendi Wei, Yu Ju (Edwin) Chen, Chun Yuan, Ming Gao"
paperYear: 2023
title: "Towards Realtime: A Hybrid Physics-based Method for Hair Animation on GPU"
date: 2023-11-04
tags: 
  - Preconditioner
---

### Basic Information

- **Title**: Towards Realtime: A Hybrid Physics-based Method for Hair Animation on GPU
- **Authors**: Li Huang, Fan Yang, Chendi Wei, Yu Ju (Edwin) Chen, Chun Yuan, Ming Gao
- **Affiliations**: Digital Content Technology Center, Tencent Games
- **Year**: 2023
- **Conference/Journal**: SCA’23, Aug 04–06 2023, Los Angeles, CA
- **DOI**: https://doi.org/10.1145/3606937

### Introduction

- **Problem Addressed**: Real-time hair simulation challenges in terms of computational efficiency, particularly for collision detection and resolution.
- **Approach**: The paper introduces a hybrid physics-based method leveraging the Material Point Method (MPM) for collision resolution and a semi-implicit Discrete Elastic Rods (DER) model for simulating individual hair strand dynamics, optimized for GPU execution.
- **Significance**: Offers a balance between physical accuracy and computational efficiency, achieving real-time performance with realistic hair dynamics.

### Overview

- **Method Summary**: Combines explicit MPM for handling hair volume preservation and strand-strand collision with semi-implicit DER for individual strand behavior, enhanced by GPU optimization for real-time performance.
- **Performance**: Demonstrated up to 260 frames per second with realistic simulation of over two thousand hair strands on an Nvidia GeForce RTX 3080 GPU.

### Summary

- **Contributions**:
  1. A hybrid method combining MPM and DER for hair simulation.
  2. GPU optimization techniques for efficient real-time performance.
  3. A stability enhancement strategy for dynamic simulations.
- **Key Techniques**:
  - Utilization of explicit MPM for collision resolution.
  - Semi-implicit DER model for simulating strand dynamics.
  - GPU optimizations for efficient computation.

### Contribution Revisited

- The method achieves faster-than-real-time performance in hair animation on consumer-grade GPUs, making it practical for real-time applications.
- The approach significantly reduces the computational burden of hair simulation while preserving physical accuracy.

### Related Works

- The paper discusses previous methods in hair simulation, including mass-spring models and various continuum methods, highlighting their limitations in real-time applications due to computational inefficiency.

### Limitation and Future Work

- Limitations

  :

  - Primarily focuses on hair collision with simple geometries (capsules) without addressing hair-clothing interactions.
  - Computational cost of the DER model may still be prohibitive for certain applications.

- Future Directions

  :

  - Extend the hybrid method to cloth simulation.
  - Improve boundary condition modeling for more complex interactions.
  - Explore adaptation to other parallel computing platforms beyond CUDA.

### Details, Techniques, and Method

- Details the hybrid simulation approach, describing the implementation of MPM and DER on GPUs, and the optimization strategies for real-time performance.
- Introduces a stability test for evaluating the robustness of the simulation under dynamic conditions.

### Experiments and Conclusion

- Demonstrates the effectiveness of the method through various scenarios, including dancing characters and comparison with existing commercial tools, showing superior performance and visual quality.
- The method’s real-time capabilities and visual realism are highlighted as key achievements, with further optimizations and platform adaptations suggested for future research.
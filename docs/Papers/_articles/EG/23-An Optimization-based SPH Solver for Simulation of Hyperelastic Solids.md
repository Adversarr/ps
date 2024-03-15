---
paperSource: "CGF"
paperAuthor: " Min Hyung Kee, Kiwon Um, HyunMo Kang, JungHyun Han"
paperYear: 2023
doi: 10.1111/cgf.14756
title: "An Optimization-based SPH Solver for Simulation of Hyperelastic Solids"
date: 2024-03-14
tags: 
  - SPH
  - Hyperelastic 
  - Optimization
---

### Basic Information

- **Title:** An Optimization-based SPH Solver for Simulation of Hyperelastic Solids
- **Authors:** Min Hyung Kee, Kiwon Um, HyunMo Kang, JungHyun Han
- **Affiliations:** Korea University, Korea; LTCI, Telecom Paris, IP Paris, France
- **DOI:** 10.1111/cgf.14756
- **Publication Date:** 2023
- **Journal:** Computer Graphics Forum, Volume 42, Number 2
- **Keywords:** Smoothed Particle Hydrodynamics (SPH), Hyperelastic Solids, Simulation, Optimization, Neo-Hookean, St. Venant-Kirchoff models, L-BFGS Algorithm

### Introduction

This paper addresses the challenge of simulating hyperelastic solids, extending the capabilities of Smoothed Particle Hydrodynamics (SPH) for elastic solids to include materials like the Neo-Hookean and St. Venant-Kirchoff models. The authors propose reformulating the implicit integration scheme for SPH elastic solids into an optimization problem solved using a quasi-Newton method, specifically the Limited-memory BFGS (L-BFGS) algorithm.

### Overview

The study introduces a novel method that enhances the SPH framework's ability to simulate hyperelastic solids with increased stability and efficiency. The proposed approach simplifies the coupling between solids and fluids, handling collisions more effectively due to the unified SPH representation. It demonstrates the method's effectiveness through various experiments, including the simulation of complex materials and interactions between different material types.

### Summary

- **Problem Addressed:** Simulating hyperelastic solids with SPH, specifically extending the state-of-the-art to include different hyperelastic materials and improving simulation stability and efficiency.
- **Proposed Method:** Reformulation of implicit integration for SPH elastic solids into an optimization problem, solved using the L-BFGS algorithm.
- **Results:** Demonstrated stable and efficient simulations of hyperelastic models within the SPH framework, including complex material interactions and two-way coupling with fluids.

### Contribution Revisited

The paper's primary contribution is the extension of SPH-based simulations to a broader range of hyperelastic materials with an optimization-based approach. This includes:
- A novel optimization problem formulation for SPH simulation of hyperelastic solids.
- Demonstration of the L-BFGS algorithm's effectiveness in solving the proposed optimization problem within the SPH framework.
- Enhanced stability and efficiency in simulating complex hyperelastic materials and their interactions with fluids.

### Related Works

The paper situates its contributions within the context of existing research on SPH for various physical phenomena, particularly highlighting advancements in fluid simulations, deformable solids, and the handling of different material interactions. It builds upon and extends methods for evaluating deformation gradients, suppressing zero-energy modes, and implementing efficient simulation techniques for elastic materials.

### Limitation and Future Work

While the proposed method significantly enhances simulation stability and supports a wider range of materials, it inherits the backward Euler time integration scheme's limitations, such as artificial damping of elastic energy. Future work will explore energy-momentum conserving schemes and more efficient solvers to address scalability and performance challenges, especially for simulations involving a large number of particles or dynamic updates to solid objects' reference configurations.

### Details, Techniques, and Method

The paper details the mathematical formulation of the optimization problem for SPH-based simulation of hyperelastic solids, including the reformulation of implicit integration as an optimization problem, the numerical solution using L-BFGS, and initial Hessian approximation strategies. It also explains the coupled solid-fluid solver implementation and adaptive time-stepping to manage performance issues.

### Describe all the Experiments

Experiments showcase the method's ability to simulate different hyperelastic materials and interactions between solids and fluids. Key experiments include:
- Swinging cloth and stretching cube tests to demonstrate stability and robustness.
- Twisting beam and colliding bunnies to test the solver's performance with various material models and collision handling.
- A melting duck scenario to illustrate the method's capacity to simulate phase changes and material property variations.

### Conclusion

The paper concludes that the proposed optimization-based SPH solver significantly improves the simulation of hyperelastic solids, offering a stable, efficient, and flexible approach suitable for real-time applications. Future work aims to address current limitations and explore stronger coupling mechanisms between elastic solids and fluids within the SPH framework.
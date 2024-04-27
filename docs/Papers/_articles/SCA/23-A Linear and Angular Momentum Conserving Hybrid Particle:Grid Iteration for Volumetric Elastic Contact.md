---
paperSource: SCA
paperAuthor: "Alan Marquez Razon, Yizhou Chen, Yushan Han, Steven Gagniere, Michael Tupek, Joseph Teran"
paperYear: 2023
title: "A Linear and Angular Momentum Conserving Hybrid Particle/Grid Iteration for Volumetric Elastic Contact"
date: 2023-11-04
tags: 
  - Differentiable Simulation
---

The paper "A Linear and Angular Momentum Conserving Hybrid Particle/Grid Iteration for Volumetric Elastic Contact" by Alan Marquez Razon et al. proposes a novel method for simulating volumetric elastic collisions with a focus on conserving linear and angular momentum. Here is a structured summary and analysis:
<!-- more -->

### Basic Information
- **Title**: A Linear and Angular Momentum Conserving Hybrid Particle/Grid Iteration for Volumetric Elastic Contact
- **Authors**: Alan Marquez Razon, Yizhou Chen, Yushan Han, Steven Gagniere, Michael Tupek, Joseph Teran
- **Affiliations**: University of California, Los Angeles, USA; Sandia National Laboratories, USA; University of California, Davis, USA
- **Year**: 2023
- **Journal/Conference**: Proceedings of the ACM on Computer Graphics and Interactive Techniques
- **DOI**: https://doi.org/10.1145/3606924

### Introduction
- **Problem Addressed**: The difficulty of accurately simulating the collision and contact of volumetric elastic solids in a manner that conserves linear and angular momentum.
- **Approach**: The authors propose a hybrid particle/grid iteration method that combines a Lagrangian finite element discretization for volumetric elasticity with impulse-based collision corrections.
- **Significance**: The method promises improved realism in animations involving biomechanical soft tissues and other elastic materials by accurately modeling the physical behaviors during collisions.

### Overview
- **Method Summary**: Utilizes implicit time stepping and a novel grid-based approach to leverage Particle-In-Cell (PIC) techniques for collision prevention, coupled with a classical collision impulse strategy for detailed interaction modeling.
- **Performance**: Demonstrated robustness and efficiency across a number of collision-intensive examples, showcasing the method's practical applicability.

### Summary
- **Contributions**:
  1. A novel method for conserving linear and angular momentum in simulations of volumetric elastic collisions.
  2. A hybrid approach that integrates PIC techniques with impulse-based collision correction.
  3. Techniques to prevent numerical cohesion and accurately model sliding friction.

### Contribution Revisited
- **Key Achievement**: The method enables more realistic and physically accurate simulations of complex interactions in elastic materials, potentially benefiting applications in computer graphics and animation.

### Related Works
- The paper discusses adaptations from computational mechanics and previous efforts in graphics research for simulating elastic deformations, highlighting the unique contributions of their method.

### Limitation and Future Work
- **Limitations**: Specific limitations were not detailed in the provided excerpts, but typically could include computational efficiency in more complex scenarios or integration with broader simulation frameworks.
- **Future Directions**: Possible expansions include enhancing the method for even more complex material interactions or further optimizations for computational performance.

### Details, Techniques, and Method
- The method emphasizes a two-step collision handling process, starting with grid-based collision prevention and concluding with impulse-based collision correction, ensuring momentum conservation throughout.

### Experiments and Conclusion
- **Experiments**: Various scenarios, including collisions between different objects and deformation examples, are presented to validate the method's effectiveness.
- **Conclusion**: The method significantly advances the state-of-the-art in simulating volumetric elastic collisions, providing a solid foundation for future research and application in dynamic animations.

This paper contributes a significant advancement in the simulation of volumetric elastic materials by proposing a method that not only conserves linear and angular momentum but also addresses the computational challenges associated with these simulations.
---
paperSource: TOG
paperAuthor: "Yufeng Zhu, Robert Bridson, Danny M. Kaufman"
paperYear: 2018
doi: 
title: "Blended Cured Quasi-Newton for Distortion Optimization"
date: 
tags: 
  - Optimization
  - Geometry Optimization
  - Hyperelasticity
---

### Basic Information

- **Title:** Blended Cured Quasi-Newton for Distortion Optimization
- **Authors:** Yufeng Zhu, Robert Bridson, Danny M. Kaufman
- **Affiliations:** University of British Columbia & Adobe Research; Autodesk & University of British Columbia; Adobe Research
- **Publication Date:** August 2018
- **Journal:** ACM Transactions on Graphics, Vol. 37, No. 4, Article 40
- **Keywords:** Numerical optimization, geometry optimization, distortion, deformation, elasticity, simulation, preconditioning, fast solvers

### Introduction

The paper introduces the Blended Cured Quasi-Newton (BCQN) method for optimizing distortion energies over meshes in 2D or 3D, which is crucial in physical simulation and geometry processing. BCQN brings together three innovations: a barrier-aware line-search filter that bypasses descent steps blocked by element barrier terms, an adaptive energy proxy blending Sobolev gradients with L-BFGS secant approximation, and a characteristic gradient norm for a robust, mesh- and energy-independent convergence criterion.

### Contributions

- **Adaptive Blended Quadratic Energy Proxy:** Combines Sobolev gradient and quasi-Newton secant approximation, enabling low-cost iterations with second-order acceleration while avoiding secant artifacts.
- **Barrier-aware Line Search Filtering:** Overcomes obstacles from elements nearing collapse, ensuring steady convergence progress.
- **Characteristic Gradient Norm:** Introduces a consistent, largely mesh- and energy-independent criterion for stopping, avoiding premature termination.

### Techniques and Method

BCQN iteratively adjusts the optimization problem's solution by leveraging a combination of the Sobolev gradient for robust initial progress and quasi-Newton updates to incorporate curvature information. This approach dynamically balances between these components for efficient and effective optimization. Additionally, the line-search filter and the characteristic gradient norm facilitate navigating complex energy landscapes and determining convergence.

### Experimental Results

BCQN was tested across various scales and problems, demonstrating significant speed improvements and robustness compared to existing methods. It was generally the fastest and most reliable method, making previously intractable problems practical and offering up to an order of magnitude improvement in others.

### Limitations and Future Work

While BCQN marks a significant advancement, there is room for improvement in understanding the optimal blending strategy for the quadratic energy proxy and in further reducing the computational overhead. Future directions include extending BCQN to more energy types, further refining the line-search filter, and exploring the integration with other optimization frameworks.

### Conclusion

BCQN represents a major step forward in distortion optimization for physical simulation and geometry processing. Its innovative blending of techniques and robust convergence criteria significantly improve upon existing methods, offering a faster, more reliable, and automated solution for optimizing complex nonconvex energies.
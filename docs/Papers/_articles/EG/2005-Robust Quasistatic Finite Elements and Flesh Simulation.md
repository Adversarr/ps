---
paperSource: EG
paperAuthor: "Joseph Teran, Eftychios Sifakis, Geoffrey Irving, Ronald Fedkiw"
paperYear: 2005
doi: 
title: "Robust Quasistatic Finite Elements and Flesh Simulation"
date: 2024-03-14
tags: 
  - Quasistatic simulation
  - FEM
  - Implicit time integration
---

### Basic Information

- **Title:** Robust Quasistatic Finite Elements and Flesh Simulation
- **Authors:** Joseph Teran, Eftychios Sifakis, Geoffrey Irving, Ronald Fedkiw
- **Affiliations:** Stanford University, Intel Corporation, Pixar Animation Studios, Industrial Light & Magic
- **Publication Date:** 2005
- **Journal:** Eurographics/ACM SIGGRAPH Symposium on Computer Animation
- **Keywords:** Quasistatic simulation, Implicit time integration, Finite elements, Flesh simulation, Computer graphics, Deformable models

### Introduction

This paper introduces a novel quasistatic algorithm that significantly improves the simulation of elastic solids in computer graphics, especially for applications involving virtual characters. The authors address the limitations of both quasistatic and implicit methods in handling element inversion and discontinuous contact forces. Their approach allows for fast conjugate gradient solvers during Newton-Raphson iteration by alleviating geometric and material indefiniteness.

### Contributions

- **Quasistatic Algorithm:** Presents a robust quasistatic algorithm for simulating nonlinear elastic materials, effectively handling highly deformed and inverted elements.
- **Positive Definiteness:** Introduces a method to ensure the positive definiteness of the global stiffness matrix, allowing the use of fast conjugate gradient solvers.
- **Collision and Self-Collision:** Proposes a novel strategy for treating collision and self-collision within the quasistatic simulation framework.

### Techniques and Method

The method extends the approach to allow for general nonlinear constitutive models, ensuring forces are smooth enough for iterative methods. The algorithm:
- Ensures positive definiteness by modifying the search path toward equilibrium without changing the set of equilibrium solutions.
- Utilizes a penalty-based formulation for collision handling, enabling efficient integration into the quasistatic formulation.
- Employs a level set approach for computing penetration depth and contact normals for collision response.

### Experimental Results

The paper showcases the algorithm's capabilities through several complex simulation scenarios, including flesh deformation driven by kinematic skeletons and muscle simulation derived from the Visible Human dataset. Results demonstrate the method's robustness and efficiency in handling large deformation, mesh inversion, and collision.

### Conclusion

The presented quasistatic simulation framework offers a robust and efficient approach for simulating nonlinear elastic materials in computer graphics. By addressing the challenges of element inversion and collision handling, the algorithm enables realistic and detailed simulations of flesh and muscle deformation, significantly enhancing the realism of virtual characters in computer-generated imagery.

### Acknowledgements

The research was supported by various grants and fellowships, including an ONR YIP award, a Packard Foundation Fellowship, a Sloan Research Fellowship, and others. The authors thank several individuals and institutions for computing resources and support.

### Performance

Simulations with the quasistatic algorithm are highly efficient, with large simulation meshes being processed in seconds to minutes per frame on standard computing hardware. This represents a significant improvement over fully dynamic simulations and facilitates the simulation of complex deformations at practical computation times.
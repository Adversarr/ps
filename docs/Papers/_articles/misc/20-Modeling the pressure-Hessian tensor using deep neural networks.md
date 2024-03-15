---
paperSource: "Fluids"
paperAuthor: "Nishant Parashar, Balaji Srinivasan, and Sawan S. Sinha"
paperYear: 2020
doi: 
title: "Modeling the pressure-Hessian tensor using deep neural networks"
date: 2024-03-14
tags: 
  - Turbulent flows
  - Deep Learning
---

### Basic Information

- **Title:** Modeling the pressure-Hessian tensor using deep neural networks
- **Authors:** Nishant Parashar, Balaji Srinivasan, and Sawan S. Sinha
- **Affiliations:** Indian Institute of Technology Delhi, New Delhi, India; Indian Institute of Technology Madras, Chennai, India
- **Publication Date:** November 11, 2020
- **Journal:** Physical Review Fluids 5, 114604 (2020)
- **Keywords:** Turbulent flows, Pressure-Hessian tensor, Deep neural networks, Isotropic turbulence, Tensor Basis Neural Network (TBNN), Machine learning

### Introduction

This study focuses on modeling the pressure-Hessian tensor, a critical component in the dynamics of velocity gradients in turbulent flows. The pressure-Hessian and viscous Laplacian govern the Lagrangian evolution of velocity gradients and are challenging to model due to their nonlocal and mathematically unclosed nature. The researchers critique the limitations of the existing fluid deformation closure model (RFDM) and introduce a deep learning approach using Tensor Basis Neural Networks (TBNN) trained on high-resolution direct numerical simulation (DNS) data of isotropic turbulence.

### Contributions

- Development and evaluation of a machine learning model using TBNN to accurately predict the pressure-Hessian tensor from velocity gradient information.
- Demonstrated that the proposed model captures key alignment statistics and unique coefficients of the tensor basis, providing a more sophisticated model than RFDM for the pressure Hessian without changing the velocity gradient information modeling paradigm.
- The approach is validated against different DNS datasets, showing its capability to generalize across isotropic turbulent flows with varying Reynolds numbers.

### Techniques and Method

The TBNN architecture is utilized, leveraging its robustness in mapping tensorial quantities by embedding knowledge of tensor basis and invariants into the network. This model predicts the pressure-Hessian tensor as a linear combination of the integrity basis of strain-rate and rotation-rate tensors, significantly improving the alignment statistics with strain-rate tensors across different Reynolds numbers.

### Experimental Results

- The model was trained on isotropic turbulence data at Reynolds number 433 and tested against several datasets, including data at different Reynolds numbers and conditions.
- Demonstrated significant improvements in alignment statistics between predicted pressure-Hessian eigenvectors and strain-rate eigenvectors compared to RFDM.
- Identified ten unique coefficients of the tensor basis for an effective pressure-Hessian tensor model, with negligible variance among these coefficients, simplifying the prediction process.

### Limitations and Future Work

The study recognizes the need for more advanced normalization strategies and acknowledges potential limitations due to the specific focus on isotropic turbulence. Future work may explore extending the model to anisotropic turbulence and further refining the machine learning architecture for better generalization across different flow conditions.

### Conclusion

The paper introduces a novel, machine learning-based approach to model the pressure-Hessian tensor in isotropic turbulence, leveraging deep neural networks for improved prediction accuracy and alignment statistics. This model provides a promising direction for developing more accurate closure models for the Lagrangian velocity gradient evolution equation in turbulent flows, with potential for significant impact on computational fluid dynamics.
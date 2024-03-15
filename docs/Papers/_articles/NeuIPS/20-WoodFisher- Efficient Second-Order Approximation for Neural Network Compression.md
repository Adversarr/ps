---
paperSource: NeuralIPS
paperAuthor: "Sidak Pal Singh, Dan Alistarh"
paperYear: 2020
doi: 
title: "WoodFisher: Efficient Second-Order Approximation for Neural Network Compression"
date: 2024-03-14
tags: 
  - Second-order optimization
  - Network compression
  - Inverse-Hessian-vector products
---
### Basic Information

- **Title:** WoodFisher: Efficient Second-Order Approximation for Neural Network Compression
- **Authors:** Sidak Pal Singh, Dan Alistarh
- **Affiliations:** ETH Zurich, Switzerland; IST Austria & Neural Magic Inc.
- **Publication Date:** November 25, 2020
- **Journal:** 34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada
- **Keywords:** Second-order optimization, Neural network compression, Pruning, Inverse-Hessian-vector products, Fisher information

### Introduction

The paper introduces WoodFisher, an efficient method for neural network compression leveraging second-order information through approximations of inverse-Hessian-vector products. The technique builds on the optimal brain damage/surgeon framework, significantly outperforming state-of-the-art methods for one-shot and gradual pruning on networks like RESNET-50 and MOBILENETV1 trained on image classification datasets.

### Contributions

- **WoodFisher Method:** Proposes a computationally efficient method to estimate inverse Hessian for neural network pruning, using the empirical Fisher information matrix and the Woodbury matrix identity.
- **Improved Pruning Performance:** Demonstrates superior performance in one-shot and gradual pruning tasks compared to popular methods, enhancing test accuracy and efficiency.
- **Adaptability:** Showcases WoodFisher's capability to automatically set layer-wise pruning thresholds and to perform compression under limited data scenarios.
- **Code Availability:** Makes the implementation publicly available for broader use and further research.

### Techniques and Method

WoodFisher approximates the inverse of the Hessian matrix efficiently for large-scale neural networks, using a combination of the empirical Fisher information matrix and the Woodbury matrix identity. This approach significantly reduces the computational burden, making it practical for network compression. It includes detailed analysis and formulation for removing single and multiple parameters, offering insights into the optimization landscape during pruning.

### Experimental Results

- **One-shot Pruning:** WoodFisher exhibits superior performance in one-shot pruning scenarios, outperforming traditional methods by improving model accuracy after significant parameter reduction.
- **Gradual Pruning:** In gradual pruning scenarios, WoodFisher again surpasses contemporary methods, achieving higher test accuracy at various sparsity levels without extensive hyperparameter tuning.
- **Comparison with State-of-the-Art:** Direct comparisons with methods like L-OBS and K-FAC based pruners highlight WoodFisher's effectiveness and efficiency in pruning tasks.

### Limitations and Future Work

While WoodFisher provides an efficient and effective approach to neural network compression, the method inherits limitations from using the empirical Fisher information matrix, which may not perfectly approximate the Hessian in all scenarios. Future directions include exploring structured pruning, incorporating first-order gradient information for further accuracy gains (WoodTaylor), and extending WoodFisher to unlabeled data scenarios through sampled Fisher information.

### Conclusion

WoodFisher introduces a highly efficient and effective approach to neural network compression, leveraging second-order information to achieve superior pruning performance. Its ability to adapt to various network structures and data availability scenarios makes it a promising tool for optimizing neural networks for deployment in resource-constrained environments.
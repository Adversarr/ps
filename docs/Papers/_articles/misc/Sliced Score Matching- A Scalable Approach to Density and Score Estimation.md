---
paperSource: arxiv
paperAuthor: "Yang Song, Sahaj Garg, Jiaxin Shi, Stefano Ermon"
paperYear: 1984
doi: 
title: "Sliced Score Matching: A Scalable Approach to Density and Score Estimation"
date: 2024-03-14
tags: 
  - 
---

### Basic Information

- **Title:** Sliced Score Matching: A Scalable Approach to Density and Score Estimation
- **Authors:** Yang Song, Sahaj Garg, Jiaxin Shi, Stefano Ermon
- **Affiliations:** Stanford University; Tsinghua University
- **Abstract:** The paper presents sliced score matching (SSM) as a scalable method for estimating unnormalized statistical models. SSM overcomes the challenge of computing Hessians in high-dimensional data by projecting scores onto random vectors. This method allows for the use of complex models and high-dimensional data, offering a practical solution for learning deep score estimators for implicit distributions. SSM demonstrates its effectiveness in various applications, including variational inference with implicit distributions and training Wasserstein Auto-Encoders (WAE).

### Introduction

Score matching is an effective technique for learning unnormalized statistical models. However, its application has been limited to low-dimensional data due to the computational challenges associated with Hessian calculations. SSM addresses this by simplifying the calculation to Hessian-vector products, which can be efficiently implemented using reverse-mode automatic differentiation, making it suitable for complex models and high-dimensional data.

### Contributions

- **Sliced Score Matching:** Introduces a method that scales to deep unnormalized models and high-dimensional data by comparing projected scores along random directions.
- **Theoretical Foundation:** Proves the consistency and asymptotic normality of SSM estimators.
- **Practical Applications:** Demonstrates the utility of SSM in learning deep energy-based models and providing accurate score estimates for variational inference with implicit distributions and training Wasserstein Auto-Encoders.

### Techniques and Method

SSM utilizes a quadratic polynomial proxy whose Hessian is approximated through random vector projections. This approach simplifies the otherwise complex Hessian computation, enabling efficient training of deep models on large datasets. SSM also involves Hessian-vector products for calculations, which are easily implemented in modern automatic differentiation frameworks.

### Experimental Results

SSM's performance is evaluated through experiments on deep kernel exponential families and NICE flow models, showcasing its scalability and effectiveness compared to traditional score matching and its variants. It outperforms existing methods in terms of scalability and accuracy for density estimation and score function estimation tasks.

### Conclusion

SSM provides a scalable and efficient solution for estimating scores in high-dimensional spaces, facilitating the training of complex models on large datasets. Its theoretical foundation ensures consistency and asymptotic normality, making it a robust choice for learning unnormalized models and estimating score functions of implicit distributions.
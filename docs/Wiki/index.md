# Graphics Wiki

## Simulation

### [Fluid](FluidSimulation/index.md)

Common methods:

1. [SPH](FluidSimulation/SPH/)
2. [Material Point Method](FluidSimulation/MPM/)

### [Differentiable](./Differentiable/index.md)

### [Collision Handling](./Collision/index.md)

[之前做的综述](./Collision/综述/碰撞检测总结.md)

## Awesome List

### [CMU-15769-by Minchen Li](https://www.cs.cmu.edu/~15769-f23/)

#### Relevant Courses

- [15-462/662: Computer Graphics](http://15462.courses.cs.cmu.edu/spring2023/)
- [15-464/664: Technical Animation](http://graphics.cs.cmu.edu/nsp/course/15464-s21/www/)
- [More graphics courses at CMU](http://graphics.cs.cmu.edu/?page_id=16)

- [Physics Simulation in Visual Computing (Javascript Implementation)](https://interactivecomputergraphics.github.io/physics-simulation/)
- [Christopher Batty's physics-based animation site](https://www.physicsbasedanimation.com/)
- [Open access to ACM SIGGRAPH-sponsored content](https://www.siggraph.org/learn/conference-content/)
- [Ke-Sen Huang's page](https://kesen.realtimerendering.com/)

#### Relevant Papers

Note: A bullet point with multiple papers is a paper bundle that needs to be presented in one presentation. 

**Optimization-based Time Integration**

- Projective dynamics: Fusing constraint projections for fast simulation (2014)
- Optimization Integrator for Large Time Steps (2015)
- XPBD: Position-Based Simulation of Compliant Constrained Dynamics (2016)
- ADMM ⊇ Projective Dynamics: Fast Simulation of Hyperelastic Models with Dynamic Constraints (2017)
- Quasi-newton methods for real-time simulation of hyperelastic materials (2017)
- A GPU-Based Multilevel Additive Schwarz Preconditioner for Cloth and Deformable Body Simulation (2022)
- Second-order Stencil Descent for Interior-point Hyperelasticity (2023)

**(Adaptive) Spatial Discretization**

- Eulerian solid simulation with contact (2011)
- A material point method for snow simulation (2013)
- Reformulating Hyperelastic Materials with Peridynamic Modeling (2018)
- Hybrid grains: Adaptive coupling of discrete and continuum simulations of granular media (2018)
- Fast Corotated Elastic SPH Solids with Implicit Zero-Energy Mode Control (2021)
- Surface-Only Dynamic Deformables using a Boundary Element Method (2022)
- Multi-Layer Thick Shells (2023)
- High-Order Incremental Potential Contact for Elastodynamic Simulation on Curved Meshes (2023)
- Adaptive Anisotropic Remeshing for Cloth Simulation (2012)

**Contact and Friction**

- Robust treatment of collisions, contact and friction for cloth animation (2002)
- Asynchronous contact mechanics (2009)
- Efficient and Accurate Collision Response for Elastically Deformable Models (2019)
- Non-smooth Newton Methods for Deformable Multi-body Dynamics (2019)
- Incremental Potential Contact: Intersection- and Inversion-free, Large-Deformation Dynamics (2020), Codimensional incremental potential contact (2021)
- Augmented Incremental Potential Contact for Sticky Interactions (2023)
- Efficient BVH-based Collision Detection Scheme with Ordering and Restructuring (2018)
- A Large Scale Benchmark and an Inclusion-Based Algorithm for Continuous Collision Detection (2021)

**Inversion-Robust Elasticity, Anisotropic Elasticity**

- Stable Neo-Hookean Flesh Simulation (2018), Analytic Eigensystems for Isotropic Distortion Energies (2019)
- Stable anisotropic materials (2015)
- Anisotropic elasticity for inversion-safety and element rehabilitation (2019)
- Botanical materials based on biomechanics (2017)

**Spatial Reduction**

- Discrete shells (2003), Discrete elastic rods (2008)
- Efficient and Stable Simulation of Inextensible Cosserat Rods by a Compact Representation (2022)
- Adaptive merging for rigid body simulation (2020)
- A Unified Newton Barrier Method for Multibody Dynamics (2022)
- Pose Space Deformation: A Unified Approach to Shape Interpolation and Skeleton-Driven Deformation (2000)
- Real-time subspace integration for St. Venant-Kirchhoff deformable models (2005)
- Optimizing Cubature for Efficient Integration of Subspace Deformations (2008)
- Real-time large-deformation substructuring (2011)
- Latent-space Dynamics for Reduced Deformable Simulation (2019)
- Medial IPC: Accelerated Incremental Potential Contact With Medial Elastics (2021)
- Model Reduction for the Material Point Method via an Implicit Neural Representation of the Deformation map (2023)
- Homogenized Yarn-Level Cloth (2020)

**Fluids**

- Implicit incompressible SPH (2013), Divergence-free smoothed particle hydrodynamics (2015)
- Surface-Only Liquids (2016)
- Efficient and Conservative Fluids Using Bidirectional Mapping (2019)
- Kinetic-based Multiphase Flow Simulation (2020)
- A Large-Scale Benchmark for the Incompressible Navier-Stokes Equations (2021)
- The power particle-in-cell method (2022)
- A Monte Carlo Method for Fluid Simulation (2022)
- Fluid Cohomology (2023)
- PolyStokes: A Polynomial Model Reduction Method for Viscous Fluid Simulation (2023)

**Solid-Fluid Coupling**

- A Fast Variational Framework for Accurate Solid-Fluid Coupling (2007)
- A Multi-Scale Model for Simulating Liquid-Hair Interactions (2017)
- An Efficient B-Spline Lagrangian/Eulerian Method for Compressible Flow, Shock Waves, and Fracturing Solids (2022)
- A Contact Proxy Splitting Method for Lagrangian Solid-Fluid Coupling (2023)

**High-Performance Simulation**

- QuanTaichi: a Compiler for Quantized Simulations (2021)
- SymX: Energy-based Simulation from Symbolic Expressions (2023)
- Interactive Hair Simulation on the GPU Using ADMM (2023)
- A Sparse Distributed Gigascale Resolution Material Point Method (2023)

**Simulation Applications**

- Design and fabrication of materials with desired deformation behavior (2010)
- FoldSketch: Enriching Garments with Physically Reproducible Folds (2018)
- Two-Scale Topology Optimization with Microstructures (2018)
- Fluid Directed Rigid Body Control using Deep Reinforcement Learning (2018)
- ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics (2019)
- Guaranteed Globally Injective 3D Deformation Processing (2021)
- Deep Physics-aware Inference of Cloth Deformation for Monocular Human Performance Capture (2021)
- Differentiable solver for time-dependent deformation problems with contact (2022)

---
tags:
- Differentiable Simulation
title: Differentiable Simulation
---

# Differentiable Simulation

| Body\Contact              | Penalty, Barrier(Soft)                              | Constraint(Hard)                                         | IPC contact.                                                 |
| ------------------------- | --------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| Rigid Body                | Fast, not Robust, but Friction is difficult to diff | Robust, Accurate, but algorithm is too complex (NP Hard) | Robust, Accurate, and friction is more accurate than Penalty. |
| Soft body(General)        | Penetration may occur, but generally preferrable    | the original implementation is difficult.                | Accurate                                                     |
| Fluid                     | No friction (Free slip-DiffFR)                      | Is that possible for FSI?                                | Need a Lagrangian view.                                      |
| PD                        | No friction is possible.                            | handle static friction only.                             | \                                                            |
| PBD                       | Fast, but mostly inaccurate.                        | impossible, because PBD seeks for performance            | \                                                            |
| Cloth(Topology is simple) | ?                                                   | ?                                                        | \                                                            |
| What                      | is                                                  | the                                                      | Future?                                                      |

We care about two main aspects:

1. Given forwards scheme, how to compute the derivitive efficiently and accurately?
2. Collision, coupling, frictional contact, or constraint, what is the derivative? is the derivative correct?

Overall, the first question is answered, and foreach method, we have a good 

```markmap
# Differentiable Simulation

## By Objects

* Rigid Body
* Cloth
* Deformable
* Fluid

## Contacts

* Friction
* Non-Friction

## Methods

* Forward Method(Dual)
* Graph-Based & Tape Based
* Backward: adjoint method
```

## Objects

“固形物”，按照维度分：

1. 体积元
   1. Rigid-body：大多数
   2. FEM：diffpd
   3. MPM：difftaichi,
2. 面积元：Diff cloth
   1. Mass Spring
   3. FEM
   4. MPM
3. 线元
   1. 头发

流体：

1. 体积法
2. MPM
3. SPH

## [Methods for diff](./backward.md)

1. Forward mode diff. -> use taylor series.
2. Reverse mode diff with Adjoint method
3. Taped diff.  -> use computational sequence/graph, e.g. torch, tensorflow and taichi.

Some libraries:
1. [NVIDIA/warp](https://github.com/NVIDIA/warp/tree/main/examples)
2. [Taichi]
3. [DiffPD]
4. brax (Google DeepMind)

## Collision Handling

Collision, or Interaction is discontinuous, if we use traditional Discrete Collision Detection and handling methods.

一方面，是不连续的，另一方面，存在摩擦（都是间断的）

1. 如果用非同时求解的：一定会带来非连续的导数
2. 如果是同时求解的，导数变化很大？

问题：如果是同时求解，如何求导数？

If-then-else based methods => discontinuous.

更难做的是 Frictional Contact.


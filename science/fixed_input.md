# One fixed, finitely squeezed entangled input survives qualitatively

[Model](model.md) · [Exact threshold](exact_threshold.md) · [Operational bounds](cubic_distance.md)

The explicit high-momentum witnesses in the exact-threshold and cubic-distance proofs require input parameters depending on the time. That does **not** mean that a growing mean-energy budget is required merely to retain *some* NPT entanglement. A single fixed, full-Schmidt-rank, finite-energy input works at every finite time; this is a consequence of standard faithful-state filtering rather than a new dynamical mechanism.

## Statement

Assume $`D,\kappa>0`$, $`\eta=0`$, and finite real $`\omega`$. Fix **any** $`0<\lambda<1`$ and define the two-mode squeezed vacuum in the number basis of $`H_{\rm ref}=(Q^2+P^2)/2=N+1/2`$:

```math
|\Omega_\lambda\rangle
=\sqrt{1-\lambda^2}\sum_{n=0}^\infty
\lambda^n|n\rangle_S|n\rangle_R.
```

Both subsystems have finite mean reference energy

```math
\langle H_{\rm ref}\rangle
=\frac12+\frac{\lambda^2}{1-\lambda^2}<\infty.
```

For **every finite** $`t>0`$, the normal output

```math
(\Phi_t\otimes\operatorname{id}_R)
(|\Omega_\lambda\rangle\langle\Omega_\lambda|)
```

is NPT. The *same* $`\lambda`$ and the *same input state* work for all finite times. This is a qualitative statement with no fixed lower bound on output negativity, postselection probability, quantum capacity or usable recovery fidelity.

## Bounded reference-filter proof

By [the exact threshold theorem](exact_threshold.md), for each fixed finite $`t`$ some pure state $`|\Psi\rangle\in\mathcal H_S\otimes\mathbb C^2`$ has a bounded NPT witness $`W`$ such that

```math
\operatorname{Tr}W(\Phi_t\otimes\operatorname{id}_2)
(|\Psi\rangle\langle\Psi|)<0.
```

Write $`|\Psi\rangle=\sum_{n\ge0}|n\rangle|a_n\rangle`$. Let $`P_M`$ project onto the first $`M+1`$ Fock levels and form the normalized truncation $`|\Psi_M\rangle\propto(P_M\otimes I_2)|\Psi\rangle`$. These input states converge in trace norm to $`|\Psi\rangle`$, and normal channels are trace-norm contractive on state differences. Therefore, for sufficiently large *finite* $`M`$, the output on $`|\Psi_M\rangle`$ still has a negative $`W`$ expectation.

Define the finite-rank reference operator

```math
A_M|n\rangle=\begin{cases}
\dfrac{|a_n\rangle}{\sqrt{1-\lambda^2}\lambda^n},&0\le n\le M,\\
0,&n>M.
\end{cases}
```

It is bounded at fixed $`M`$. Scale it to a contraction $`K_M=A_M/\max(1,\|A_M\|)`$, a legitimate local filter with some strictly positive success probability. Then

```math
(I\otimes K_M)|\Omega_\lambda\rangle
\propto|\Psi_M\rangle.
```

The filter acts **only on the untouched reference**, so it commutes with applying $`\Phi_t`$ to the system. If the output on $`|\Omega_\lambda\rangle`$ were PPT, every bounded local filter would preserve PPT. Yet the successful output is the NPT output on $`|\Psi_M\rangle`$, a contradiction.

All operations are normal and bounded, and only finite-rank filters appear. The two-mode squeezed state has a trace-class partial transpose with norm $`(1+\lambda)/(1-\lambda)`$, so no unnormalizable Choi state or unbounded inverse thermal density operator is used.

## What this does not imply

The filter is a *mathematical certificate*: for large $`t`$ the success probability and detectable NPT signal can be extremely small. A receiver cannot obtain a fixed-fidelity quantum memory merely from nonzero NPT in arbitrarily rare tails. The [uniform diamond estimate](cubic_distance.md) independently shows that the complete channel approaches the EB set at a cubic exponential rate. The two conclusions are compatible and concern different operational notions.

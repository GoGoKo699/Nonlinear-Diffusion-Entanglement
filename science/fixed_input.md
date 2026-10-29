# A fixed finite-energy entangled input that remains NPT

[Exact non-PPT theorem](exact_threshold.md) · [Cubic channel bound](cubic_distance.md)

The growing high-momentum packets in the quantitative lower bound are **not** necessary merely to retain nonzero NPT entanglement. Standard faithful-state filtering gives a single *fixed* two-mode squeezed input whose output remains NPT at every finite time. This adds a useful quantifier, not a new memory mechanism.

## Statement

Assume $D,\kappa>0$, $\eta=0$ and finite real $\omega$. Fix any $0<\lambda<1$, independently of time, and define the two-mode squeezed vacuum relative to the oscillator number basis of $H_{\rm ref}=(Q^2+P^2)/2=N+1/2$:

$$
|\Omega_\lambda\rangle=\sqrt{1-\lambda^2}
\sum_{n=0}^\infty\lambda^n|n\rangle_S|n\rangle_R.
$$

Each subsystem has finite mean reference energy

$$
\langle H_{\rm ref}\rangle=\frac12+\frac{\lambda^2}{1-\lambda^2}.
$$

**For every finite $t>0$,** the output
$(\Phi_t\otimes\mathrm{id}_R)(|\Omega_\lambda\rangle\langle\Omega_\lambda|)$ is NPT. The **same input** works for every finite $t$, at every chosen positive $D,\kappa$ and finite $\omega$.

## Bounded local-filter proof

Fix $t>0$. By [the sharp threshold theorem](exact_threshold.md), some normal pure input $|\Psi\rangle\in\mathcal H_S\otimes\mathbb C^2$ has output with a negative bounded partial-transpose witness $W$. Write

$$|\Psi\rangle=\sum_{n\ge0}|n\rangle_S|a_n\rangle_{\mathbb C^2}.$$

Let $P_M=\sum_{n=0}^M|n\rangle\langle n|$ and normalize
$|\Psi_M\rangle\propto(P_M\otimes I)|\Psi\rangle$. These states converge in trace norm to $|\Psi\rangle$. By channel trace-norm contractivity and boundedness of $W$, for sufficiently large finite $M$ their outputs are also NPT.

Define a finite-rank, hence bounded operator from the bosonic reference to the qubit by

$$
A_M|n\rangle=
\begin{cases}
|a_n\rangle/(\sqrt{1-\lambda^2}\lambda^n),&0\le n\le M,\\
0,&n>M.
\end{cases}
$$

Scale it to a contraction $K_M=A_M/\max(1,\|A_M\|)$, a legitimate local filter with strictly positive success probability. Then

$$
(I\otimes K_M)|\Omega_\lambda\rangle\propto|\Psi_M\rangle.
$$

The filter acts **only on the untouched reference** and commutes with the channel on the system. If the TMSV output were PPT, any bounded local filter on its reference would preserve PPT. Its successful branch is the NPT output on $|\Psi_M\rangle$, a contradiction.

There is no unnormalizable continuous-variable Choi state here. The partial transpose of the input TMSV is trace class with trace norm $(1+\lambda)/(1-\lambda)$, and every filter used is finite rank.

## Operational limitation

The filter may succeed with an arbitrarily small probability when $M$ is large, and the surviving NPT signal can be negligible. This does **not** establish a positive quantum communication rate, constant recovery fidelity, or experimentally detectable long-lived entanglement. The whole channel still approaches the EB set at cubic-exponential order in the energy-unconstrained diamond norm.

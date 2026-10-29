# Exact conditional Gaussian representation

[Model](model.md) · [Exact threshold](exact_threshold.md) · [Cubic bounds](cubic_distance.md)

## Gaussian only after conditioning

Let $B,W,Z$ be independent standard real Brownian motions and define the stochastic shear

$$ S_s=\omega s+\sqrt{2\kappa}\,B_s,\qquad U_{S_s}=e^{-iS_sP^2/2}. $$

Because $U_{S_s}^\dagger Q U_{S_s}=Q+S_sP$, the interaction-picture noise Hamiltonians are $\sqrt{2D}(Q+S_sP)\circ dW_s$ and $\sqrt{2\eta}P\circ dZ_s$. Commutators of any two of these linear quadratures are scalar. For a *fixed* continuous $S$ path, time ordering therefore contributes only a global phase, which disappears in density-operator conjugation. The conditional channel is a shear composed with a centered Gaussian additive-displacement channel:

$$
\Phi_t^{(S)}=\operatorname{Ad}_{U_{S_t}}\circ\mathcal N_{V_S},
\quad
V_S=2D\begin{pmatrix}
\int_0^t S_s^2ds&-\int_0^t S_sds\\
-\int_0^t S_sds&t
\end{pmatrix}
+2\eta t\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

The variance matrix is the *classical physical-displacement covariance* in ordered quadratures $(Q,P)$; the vacuum state's covariance is $I/2$ in the same convention. Its determinant does not depend on the choice of Weyl displacement signs. Averaging over the quadratic shear gives the **non-Gaussian total channel**:

$$ \Phi_t=\mathbb E_B\,\Phi_t^{(S)}. $$

Each component is normal CPTP and the Bochner expectation is a normal CPTP channel on trace-class states. This decomposition does **not** allow the receiver to read the hidden noise trajectory.

## A nonnegative noise-area determinant

Write $\overline S=t^{-1}\int_0^tS_sds$. Direct multiplication gives

$$
\det V_S=4D\eta t^2+
4D^2\left[t\int_0^tS_s^2ds-\left(\int_0^tS_sds\right)^2\right]
=4D\eta t^2+4D^2t\int_0^t(S_s-\overline S)^2ds.
$$

The bracket is nonnegative for every path. For $\kappa>0$, Brownian scaling on $[0,1]$ gives

$$
\det V_S=4D\eta t^2+8D^2\kappa t^3Z_\delta,
\quad
Z_\delta=\int_0^1[Y_u+\delta(u-\tfrac12)]^2du,
$$

where $Y_u=W_u-\int_0^1W_vdv$ and $\delta=\omega\sqrt{t/(2\kappa)}$.

The one-mode Gaussian additive-noise EB condition, inherited from Holevo, is

$$ \mathcal N_V\text{ EB}\quad\Longleftrightarrow\quad \sqrt{\det V}\ge1. $$

For sufficiency write $V=\nu SS^T$, $\det S=1$, $\nu=\sqrt{\det V}$. At $\nu=1$ heterodyne measurement followed by coherent-state preparation gives isotropic noise $I$ (measurement $I/2$ plus preparation $I/2$); more noise or Gaussian unitary conjugation preserves EB. The necessary direction follows from the Gaussian EPR/PPT test. Thus if $4D\eta t^2\ge1$, **every** pathwise channel is EB and so is their mixture. This is only the *upper* direction of the exact cutoff; the mixture-level NPT converse has its own proof.

## Brownian quadratic functional

For centered Brownian motion $Y$ on $[0,1]$ the covariance kernel is

$$ K(u,v)=\min(u,v)-u+\frac{u^2}{2}-v+\frac{v^2}{2}+\frac13. $$

On the mean-zero subspace the covariance operator is the inverse Neumann Laplacian. Its eigenpairs are $\sqrt2\cos(n\pi u)$ and $(n\pi)^{-2}$, $n\ge1$. Consequently, for iid standard Gaussians $g_n$,

$$ Z_0\overset d=\sum_{n\ge1}\frac{g_n^2}{\pi^2n^2},
\qquad \mathbb E Z_0=\frac16. $$

The process $Y$ is not a Brownian bridge, although its integrated square has the same distribution as that of a standard bridge. Euler's product yields

$$
\boxed{\mathbb E e^{-sZ_0}=
\left(\frac{\sqrt{2s}}{\sinh\sqrt{2s}}\right)^{1/2}.}
$$

For deterministic shear use $r=\sqrt{2s}$. The cosine coefficient of $\delta(u-\tfrac12)$ vanishes for even $n$ and equals $-2\sqrt2\delta/(\pi n)^2$ for odd $n$, producing the noncentral transform

$$
\boxed{\mathbb E e^{-sZ_\delta}=
\left(\frac{r}{\sinh r}\right)^{1/2}
\exp\left[-\frac{\delta^2}{2}+
\frac{\delta^2\tanh(r/2)}r\right].}
$$

All expressions at $s=0$ are interpreted by continuity. The transform supplies an explicit Chernoff proof for the energy-unconstrained cubic distance estimate. The Grushin model and Mehler propagator themselves are **inherited** from Speed–Lyu–Schubert; see [source attribution](../references/RELATED_WORK.md).

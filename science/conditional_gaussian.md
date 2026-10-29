# Conditional Gaussian channels and Brownian covariance

[Model](model.md) · [Exact threshold](exact_threshold.md) · [Cubic distance](cubic_distance.md)

The unconditional channel is **not Gaussian** when $`\kappa>0`$. Conditioning on a single stochastic quadratic shear, however, produces an explicitly Gaussian additive-displacement channel. This distinction is essential: a convex mixture of non-EB channels need not be non-EB, and a Gaussian theorem about the *total* channel cannot be applied to a non-Gaussian mixture without proof.

## 1. Factor the stochastic shear

Let $`B,W,Z`$ be independent standard Brownian motions, and write

```math
S_s=\omega s+\sqrt{2\kappa}\,B_s,
\qquad U_{S_s}=e^{-iS_sH}.
```

The shear identity is $`U_{S_s}^{\dagger}QU_{S_s}=Q+S_sP`$. For a fixed continuous $`S`$ path, passing to the interaction picture leaves linear stochastic Hamiltonians $`\sqrt{2D}(Q+S_sP)\circ dW_s`$ and $`\sqrt{2\eta}P\circ dZ_s`$. Their mutual commutators are scalar. Their time ordering changes a global phase but has no effect on density-operator conjugation. Thus the conditional channel takes the exact form

```math
\Phi_t^{(S)}=\mathrm{Ad}_{U_{S_t}}\circ\mathcal N_{V_S},
```

where $`\mathcal N_V`$ adds centered phase-space Gaussian displacements with covariance $`V`$. In the ordered quadratures $`(Q,P)`$,

```math
\boxed{V_S=2D\begin{pmatrix}
\int_0^t S_s^2ds&-\int_0^t S_sds\\
-\int_0^t S_sds&t
\end{pmatrix}
+2\eta t\begin{pmatrix}1&0\\0&0\end{pmatrix}.}
```

This is a *classical displacement covariance*; vacuum state covariance is $`I_2/2`$ with $`[Q,P]=i`$. The signs of off-diagonal entries depend on Weyl conventions but the determinant does not. A fixed final shear is Gaussian unitary conjugation and leaves EB/PPT classification invariant.

Integrating over the quadratic-noise path reconstructs the physical channel:

```math
\Phi_t=\mathbb E_B\,\Phi_t^{(S)}.
```

The stochastic construction defines a normal CPTP map on the trace class. Conditional displacements and final shears are unitary conjugations; the expectation is a Bochner integral on individual trace-class inputs. The random-unitary independent-increment evolution ensures a normal quantum Markov semigroup, with the stated formal generator on the Schwartz finite-rank core.

## 2. A Gram determinant that controls channel classicality

With $`\overline S=t^{-1}\int_0^t S_sds`$,

```math
\begin{aligned}
\det V_S
&=4D\eta t^2+4D^2\left(
 t\int_0^{t} S_s^2\,ds
 -\left(\int_0^{t} S_s\,ds\right)^2\right)\\
&=4D\eta t^2+4D^2t\int_0^{t}(S_s-\overline S)^2\,ds.
\end{aligned}
```

The second term is nonnegative. More explicitly, with $`u=s/t`$ and a standard Brownian motion $`W_u`$ on $`[0,1]`$, define

```math
Y_u=W_u-\int_0^1 W_vdv,
\quad \delta=\omega\sqrt{\frac{t}{2\kappa}},
\quad Z_\delta=\int_0^1[Y_u+\delta(u-\tfrac12)]^2du.
```

Brownian scaling gives

```math
\det V_S=4D\eta t^2+8D^2\kappa t^3 Z_\delta.
```

For $`\omega=0`$, $`Z=Z_0`$ is the squared $`L^2`$ norm of Brownian motion after subtraction of its *time average*. This centered Brownian process is **not itself a Brownian bridge**, though its integrated square has the same distribution as the integrated square of a Brownian bridge.

## 3. Gaussian entanglement-breaking criterion

A one-mode additive-displacement Gaussian channel $`\mathcal N_V`$ is EB if and only if

```math
\sqrt{\det V}\ge1.
```

This is the standard one-mode specialization of Holevo's Gaussian-channel EB criterion. Sufficiency, used repeatedly below, can be seen without an infinite-dimensional Choi vector. Williamson reduction writes $`V=\nu SS^T`$ with $`\det S=1`$, $`\nu=\sqrt{\det V}`$. At $`\nu=1`$, isotropic noise is heterodyne measurement followed by coherent-state preparation, whose measurement and preparation each contribute vacuum noise $`I/2`$. Extra positive Gaussian noise and symplectic unitary conjugations preserve the EB property. Necessity follows from the Gaussian two-mode EPR test or the same general criterion; see [related work](../references/RELATED_WORK.md).

It follows immediately that every conditional component is EB whenever $`4D\eta t^2\ge1`$. Since an average of EB channels is EB, this already proves the **upper half** of the sharp threshold. The converse that no mixture-level EB occurs earlier is **not** a consequence of conditioning; it is separately proved using an actual entangled input in [the threshold proof](exact_threshold.md).

## 4. A Brownian small-ball event and its exact transform

For $`\eta=\omega=0`$, the event on which a conditional channel may not be EB is

```math
\mathcal A_t=\{8D^2\kappa t^3Z<1\}.
```

The covariance kernel of $`Y`$ is

```math
K(u,v)=\min(u,v)-u+\tfrac12u^2-v+\tfrac12v^2+\tfrac13.
```

On mean-zero functions, its eigenvectors are $`\sqrt2\cos(n\pi u)`$ and its nonzero eigenvalues are $`(n\pi)^{-2}`$. Hence

```math
Z\overset d=\sum_{n\ge1}\frac{g_n^2}{n^2\pi^2},
\qquad g_n\overset{\mathrm{iid}}\sim N(0,1),
\qquad \mathbb EZ=\frac16.
```

The Euler product for $`\sinh`$ then gives

```math
\boxed{\mathbb E e^{-sZ}
=\left[\frac{\sqrt{2s}}{\sinh\sqrt{2s}}\right]^{1/2},
\quad s\ge0.}
```

The $`s=0`$ expression is interpreted continuously as one. For nonzero deterministic shear, expanding the centered line $`\delta(u-1/2)`$ in the same cosine basis gives the noncentral transform, with $`r=\sqrt{2s}`$,

```math
\boxed{\mathbb E e^{-sZ_\delta}
=\left(\frac r{\sinh r}\right)^{1/2}
\exp\left[-\frac{\delta^2}{2}
+\frac{\delta^2\tanh(r/2)}r\right].}
```

One may derive the extra exponent using the fact that the cosine coefficients of $`\delta(u-1/2)`$ vanish for even $`n`$ and equal $`-2\sqrt2\delta/(n\pi)^2`$ for odd $`n`$. No stochastic small-ball theorem is needed for the explicit exponential *upper* bound in the [distance proof](cubic_distance.md); Chernoff's inequality and the exact transform suffice.

## 5. What is and is not inherited

The exact model, its Grushin/Fokker–Planck representation and Mehler solution are from Speed–Lyu–Schubert. The one-mode Gaussian EB criterion is inherited from Holevo, and the Gaussian QBM comparison from Riedel. Here these established methods are assembled to compute a pathwise noise determinant and then supplemented by new finite-energy converse witnesses. **The pathwise upper theorem alone is not an exact criterion for the mixture.**

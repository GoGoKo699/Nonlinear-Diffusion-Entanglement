# An exact entanglement-breaking time for nonlinear diffusion

[Model](model.md) · [Conditional mixture](conditional_gaussian.md) · [Gaussian comparison](interpretation.md)

## Theorem and significance of the quantifiers

For a single continuous-variable system with $`[Q,P]=i`$ and the normal random-unitary semigroup

```math
\mathcal L=-i\omega\operatorname{ad}_{P^2/2}
-D\operatorname{ad}_Q^2-\kappa\operatorname{ad}_{P^2/2}^2
-\eta\operatorname{ad}_P^2,
\quad D,\kappa>0,\ \eta\ge0,\ \omega\in\mathbb R,
```

the exact entanglement-breaking time is

```math
\boxed{t_{\mathrm{EB}}=
\begin{cases}
\dfrac{1}{2\sqrt{D\eta}},&\eta>0,\\[3pt]
\infty,&\eta=0.
\end{cases}}
```

For $`\eta>0`$, $`\Phi_t`$ is EB for every $`t\ge t_{\mathrm{EB}}`$, including equality. For every strictly earlier $`t>0`$ (every finite $`t>0`$ when $`\eta=0`$), the channel is **not PPT-inducing**. The converse uses a *normalizable, finite-reference-energy* state on the system and a qubit reference. Consequently the EB and PPT-inducing time intervals coincide in this specified family. No positive quantum-capacity or fixed-quality memory theorem is claimed.

The upper proof uses a Gaussian measure-and-prepare representation for *each* conditional channel. The lower proof treats the unconditional mixture directly by an NPT witness. Both steps are necessary.

## 1. Pathwise measure and preparation: the upper proof

With the Brownian shear $`S_s=\omega s+\sqrt{2\kappa}B_s`$, [the conditional-Gaussian representation](conditional_gaussian.md) gives

```math
\det V_S=4D\eta t^2
+4D^2t\int_0^t(S_s-\overline S)^2ds
\ge4D\eta t^2.
```

Under the convention vacuum covariance $`I/2`$, any one-mode additive Gaussian noise channel is EB when $`\sqrt{\det V_S}\ge1`$. The trailing shear is unitary. If $`t\ge(2\sqrt{D\eta})^{-1}`$, the criterion holds for **every path** $`S`$, including at equality. Averaging these normal EB channels remains EB because separable output states form a closed convex set. This establishes the upper bound without invoking a Gaussian criterion for the non-Gaussian total channel.

## 2. Exact momentum-space kernel

Momentum-space kernels provide an independent method for the lower theorem. Set $`s=(p+p')/2`$ and $`y=p-p'`$. The master equation on the Schwartz core becomes

```math
\partial_t\rho(s,y)
=D\partial_s^2\rho(s,y)
-\kappa y^2s^2\rho(s,y)
-i\omega ys\rho(s,y)
-\eta y^2\rho(s,y).
```

For $`y\ne0`$ define

```math
a=\sqrt{\kappa/D}\,|y|,\qquad b=\sqrt{D\kappa}\,|y|.
```

The (known) harmonic-heat or Mehler kernel for $`\omega=\eta=0`$ is

```math
K_y^0(t;s,r)=\sqrt{\frac a{2\pi\sinh(2bt)}}
\exp\left[-\frac{a[(s^2+r^2)\cosh(2bt)-2sr]}{2\sinh(2bt)}\right].
```

Its continuous $`y=0`$ limit is the heat kernel $`(4\pi Dt)^{-1/2}\exp[-(s-r)^2/(4Dt)]`$. Completing the square in the harmonic potential and linear imaginary drift gives the exact *full* kernel

```math
\begin{aligned}
K_y^{\omega,\eta}(t;s,r)=\;&K_y^0(t;s,r)
\exp[-\eta ty^2]\\
&\times\exp\left[-\frac{\omega^2}{4\kappa}
\left(t-\frac{\tanh(bt)}b\right)\right]\\
&\times\exp\left[-i\frac{\omega\operatorname{sgn}(y)}{2\sqrt{D\kappa}}
(s+r)\tanh(bt)\right].
\end{aligned}
```

The $`y=0`$ limit again has the usual heat kernel. The exact-solvability machinery and model are inherited from [Speed–Lyu–Schubert](../references/RELATED_WORK.md#closest-model-predecessor); this page uses it to derive the new entanglement criterion. The real drift correction is between zero and one; in particular $`|K_y^{\omega,\eta}|\le K_y^0\le K_0`$ when $`\eta\ge0`$, the last inequality following from the Feynman–Kac comparison with a nonnegative killing potential.

## 3. An actual finite-energy system–reference witness

For $`A>0`$ and $`\delta>0`$, let

```math
f_\pm(p)=(\pi\delta^2)^{-1/4}
\exp\left[-\frac{(p\mp A)^2}{2\delta^2}\right].
```

The input and partial-transpose test vector, with two orthogonal reference labels, are

```math
|\Psi\rangle=\frac{|f_+\rangle|0\rangle+|f_-\rangle|1\rangle}{\sqrt2},
\quad
|v\rangle=\frac{|f_+\rangle|1\rangle-|f_-\rangle|0\rangle}{\sqrt2}.
```

Both are normalized despite the nonzero overlap of $`f_+`$ and $`f_-`$, since their reference labels are orthogonal. Each packet has finite reference-oscillator energy

```math
\langle H_{\rm ref}\rangle_{f_\pm}
=\frac{A^2}{2}+\frac{\delta^2}{4}
+\frac1{4\delta^2},
\qquad H_{\rm ref}=\frac{Q^2+P^2}{2}.
```

Set

```math
\begin{aligned}
c_A&=\langle f_+|\Phi_t(|f_+\rangle\langle f_-|)|f_-\rangle,\\
d_A&=\langle f_+|\Phi_t(|f_-\rangle\langle f_-|)|f_+\rangle.
\end{aligned}
```

The opposite diagonal term is equal to $`d_A`$ by parity covariance, and the off-diagonal term has real positive value by the Gaussian integrations below. The partial transpose on the reference obeys

```math
\langle v|[(\Phi_t\otimes\operatorname{id}_2)
(|\Psi\rangle\langle\Psi|)]^{\Gamma_R}|v\rangle
=\frac{d_A-\operatorname{Re}c_A}{2}.
```

Thus $`c_A>d_A`$ exhibits NPT and excludes every EB/PPT-inducing description at that time.

## 4. Positive one-dimensional integral reduction

For $`y\ge0`$, put $`a(y)=\sqrt{\kappa/D}y`$, $`b(y)=\sqrt{D\kappa}y`$, and

```math
U(y)=\delta^{-2}+\tfrac12a(y)\tanh[b(y)t],
\quad V(y)=\delta^{-2}+\tfrac12a(y)\coth[b(y)t].
```

Define $`h(y)>0`$ by its continuous formula at $`y=0`$,

```math
\begin{aligned}
h(y)={}&\frac{1}{\delta^2\sqrt{U(y)V(y)}}
\sqrt{\frac{a(y)}{2\pi\sinh[2b(y)t]}}\\
&\times\exp\left[-\eta t y^2
-\frac{\omega^2}{4\kappa}
\left(t-\frac{\tanh[b(y)t]}{b(y)}\right)
-\frac{\omega^2\tanh^2[b(y)t]}{8D\kappa U(y)}\right].
\end{aligned}
```

Extending $`h`$ evenly, exact Gaussian integration in $`(s+r)/\sqrt2`$ and $`(s-r)/\sqrt2`$ gives

```math
\boxed{\begin{aligned}
c_A&=\int_{\mathbb R}e^{-(y-2A)^2/(2\delta^2)}h(|y|)\,dy,\\
d_A&=\int_{\mathbb R}e^{-y^2/(2\delta^2)}h(|y|)
\exp\left[-\frac{A^2a(|y|)\coth[b(|y|)t]}
{1+\frac12\delta^2a(|y|)\coth[b(|y|)t]}\right]dy.
\end{aligned}}
```

Both are explicitly positive for any finite $`t`$, including nonzero drift; the oscillatory kernel phase has already been integrated out as a positive Gaussian factor. The formulas follow from the initial four packet factors, the Mehler kernel, and the identity $`\tanh z+\coth z=2\coth(2z)`$. The denominator factors $`U,V`$ and the phase-suppression term matter for the exact constants; [verification](../verification/README.md) checks them numerically.

### Universal upper bound on the wrong-sign diagonal

Since $`a\coth(bt)\ge1/(Dt)`$ and $`u/(1+\delta^2u/2)`$ increases with $`u\ge0`$, while the remaining $`A=0`$ integral is a survival probability no greater than one,

```math
\boxed{d_A\le\exp\left[-\frac{A^2}{Dt+\delta^2/2}\right].}
```

### Explicit lower bound on coherence

Assume $`2A>\delta`$ and define

```math
\begin{aligned}
a_\pm&=\sqrt{\kappa/D}(2A\pm\delta),\\
b_\pm&=\sqrt{D\kappa}(2A\pm\delta).
\end{aligned}
```

Restrict the coherence integral to $`|y-2A|\le\delta`$. The prefactor, $`\sinh`$ and $`\coth`$ inequalities give the fully elementary lower bound

```math
\boxed{\begin{aligned}
c_A\ge L_A={}&\frac{2\delta e^{-1/2}\sqrt{a_-/\pi}}
{1+\frac12\delta^2a_+\coth(b_-t)}\\
&\times\exp\left[-\eta t(2A+\delta)^2-b_+t
-\frac{\omega^2t}{4\kappa}
-\frac{\omega^2\delta^2}{8D\kappa}\right].
\end{aligned}}
```

In particular, $`L_A>\exp[-A^2/(Dt+\delta^2/2)]`$ is a completely explicit **finite-energy NPT certificate**.

## 5. Prove the exact threshold (including its endpoint)

For any fixed $`t>0`$ set $`\delta=A^{-1}`$ and send the *finite parameter* $`A`$ to arbitrarily large values. The logarithm of the explicit coherence lower bound obeys

```math
\log L_A=-4\eta t A^2
-2\sqrt{D\kappa}\,tA-\tfrac12\log A+O_{D,\kappa,\eta,\omega,t}(1),
```

while the negative logarithm of the diagonal upper bound is

```math
\frac{A^2}{Dt+\delta^2/2}=\frac{A^2}{Dt}+O(1).
```

Their logarithmic ratio therefore has the sign of the leading term

```math
\left[\frac1{Dt}-4\eta t\right]A^2
-2\sqrt{D\kappa}\,tA+O(\log A).
```

If $`t<(2\sqrt{D\eta})^{-1}`$, the coefficient in square brackets is positive. This includes **every finite time** when $`\eta=0`$. Taking a sufficiently large but *finite* $`A`$ proves $`c_A>d_A`$ and hence NPT. Conversely, the pathwise Gaussian proof makes the channel EB already at equality $`t=(2\sqrt{D\eta})^{-1}`$. There is no unresolved endpoint interval. The argument also gives the exact PPT-inducing boundary, since the converse is specifically NPT.

The dependence on $`\kappa>0`$ is essential: for fixed kernel centers, the negative logarithm of the harmonic Mehler kernel grows linearly in large $`|y|`$, up to logarithmic terms. The kernel itself decays exponentially in $`|y|`$, not linearly. This permits the coherence–leakage comparison above. It is not legal to set $`\kappa=0`$ in the Mehler-based converse; that separate Gaussian model has a different threshold when $`\omega\ne0`$.

## 6. Independent finite-parameter checks and boundaries

The [reproduction script](../verification/check_threshold.py) evaluates the exact packet integrals using quadrature and Gauss–Hermite nodes, alongside the explicit elementary inequalities. For example, at $`D=2,\kappa=0.3,\eta=0.125,\omega=0.7`$, the theorem predicts $`t_{\mathrm{EB}}=1`$. At $`A=20,\delta=0.05`$, its finite witness has negative partial-transpose expectation at $`t=0.5`$ and $`0.9`$, and is nonnegative at $`1.0`$ and $`1.1`$. The latter observation is **not** used as proof of the EB side, which already follows analytically.

For any $`\eta>0`$, the detector may require extremely high but finite $`A`$ as $`t`$ approaches the boundary. Neither the existence of a witness nor NPT itself supplies positive unassisted quantum capacity, a recoverable logical qubit, or a lower bound on a practical experiment's sensitivity. The fixed-input result is discussed [separately](fixed_input.md).

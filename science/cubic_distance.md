# Cubic-exponential operational classicalization

[Model](model.md) · [Brownian mixture](conditional_gaussian.md) · [Exact cutoff](exact_threshold.md)

## Theorem

Set $`\eta=0`$. In canonical units $`D=\kappa=1`$ and at fixed real drift $`\omega`$, define

```math
e(t)=\inf_{\Psi\in\mathrm{EB}}\tfrac12
\|\Phi_t-\Psi\|_\diamond.
```

For every $`t\ge1`$,

```math
\boxed{\frac{c_*}{1+\omega^2}
\exp(-4t^3-\omega^2t/2)
\le e(t)\le
\min\!\left\{1,
\sqrt{\frac{8t^3}{1-e^{-8t^3}}}e^{-t^3}\right\},}
```

with the explicit positive constant

```math
\boxed{c_*=\frac{2/3+5/\pi^2}{32}
\left[\cos(1/32)\sqrt{\frac{31}{8\pi}}e^{-5/32}
-\frac{e^{1/4}}{2\sqrt\pi}\right]
=0.02153222609588753\ldots>0.}
```

Thus $`-\log e(t)=\Theta(t^3)`$ at fixed $`\omega`$. For general $`D,\kappa>0`$, the canonical time and drift are

```math
\tau=D^{2/3}\kappa^{1/3}t,
\quad \Omega=\frac{\omega}{D^{1/3}\kappa^{2/3}},
```

so the exponent is of order $`D^2\kappa t^3`$ at fixed physical parameters. The upper and lower cubic coefficients (one and four in canonical units) do not match; **the exact large-time exponent coefficient is not established**.

The upper bound covers *every input energy and all references*. The lower is witnessed by an explicitly normalized state with a qubit reference and finite, although growing, preparation energy. No claim of useful quantum-memory fidelity follows.

## 1. Uniform upper bound by removing exceptional Brownian paths

[The conditional channel](conditional_gaussian.md) has displacement covariance determinant $`8t^3Z_\delta`$ with $`\delta=\omega\sqrt{t/2}`$ when $`D=\kappa=1`$. Every conditional channel is EB on the **good event** $`\{8t^3Z_\delta\ge1\}`$. Let $`p_t`$ be the probability of its complement. Replace the conditional channel on the bad event by a fixed normal EB preparation channel, keeping it unchanged on good paths. Convexity and closedness of separable states make the resulting averaged $`\Psi_t`$ EB. For every joint input on the system and an arbitrary reference,

```math
\frac12\|\Phi_t-\Psi_t\|_\diamond\le p_t.
```

The bound follows by integrating the half trace-norm difference of two channels, which is at most one on the bad event. There is **no dimension factor, input-energy cutoff or ancillary-system assumption**. The same argument works in the energy-unconstrained norm.

For nonzero drift, Anderson's inequality for centered Gaussian measures on Hilbert space and convex symmetric $`L^2`$ balls gives

```math
\Pr(Z_\delta\lt x)\le\Pr(Z_0\lt x),\qquad x\gt0.
```

Alternatively, the explicit noncentral Laplace transform in [the mixture chapter](conditional_gaussian.md) is bounded above by the centered transform because $`\tanh(r/2)\le r/2`$; applying the same Chernoff bound directly yields the displayed result, without needing a separate Anderson inequality.

Write $`Z=Z_0`$. Its exact Laplace transform is

```math
\mathbb Ee^{-sZ}=
\left[\frac{\sqrt{2s}}{\sinh\sqrt{2s}}\right]^{1/2}.
```

Chernoff's inequality at $`x=(8t^3)^{-1}`$ and $`s=8t^6`$ gives

```math
\begin{aligned}
p_t&\le\exp(t^3)
\left[\frac{4t^3}{\sinh(4t^3)}\right]^{1/2}\\
&=\sqrt{\frac{8t^3}{1-e^{-8t^3}}}\,e^{-t^3}.
\end{aligned}
```

Together with the trivial upper bound one, this proves the theorem's right-hand inequality. The output EB approximant varies with time; the channel need not converge to a fixed equilibrium preparation map.

## 2. Exactly orthogonal, finite-energy momentum packets

For $`w>0`$ define a real, compactly supported normalized packet

```math
f_w(p)=\begin{cases}
w^{-1/2}\cos(\pi p/(2w)),&|p|\le w,\\
0,&|p|>w.
\end{cases}
```

It has a square-integrable weak derivative; its reference energy is finite. For $`a>w`$, define $`f_\pm(p)=f_w(p\mp a)`$. The supports are disjoint; hence $`f_+,f_-`$ are exactly orthonormal. Prepare

```math
|\Psi\rangle=\frac{|f_+\rangle|0\rangle+|f_-\rangle|1\rangle}{\sqrt2}
```

and test the output with $`W=(|\chi\rangle\langle\chi|)^{\Gamma_R}`$, where

```math
|\chi\rangle=\frac{|f_-\rangle|0\rangle-|f_+\rangle|1\rangle}{\sqrt2}.
```

Because $`\chi`$ has two equal orthogonal Schmidt coefficients, $`\|W\|_\infty=1/2`$. Every separable output has nonnegative expectation of $`W`$. Define

```math
\begin{aligned}
D_t&=\langle f_-|\Phi_t(|f_+\rangle\langle f_+|)|f_-\rangle,\\
C_t&=\langle f_+|\Phi_t(|f_+\rangle\langle f_-|)|f_-\rangle.
\end{aligned}
```

Parity symmetry and the reference partial transpose give

```math
\mathrm{Tr}(W\Sigma_t)=\tfrac12(D_t-\mathrm{Re}\,C_t),
\qquad \Sigma_t=(\Phi_t\otimes\mathrm{id})(|\Psi\rangle\langle\Psi|).
```

Consequently

```math
e(t)\ge\tfrac12(\mathrm{Re}\,C_t-D_t).
```

This is a lower bound on the *same* half-diamond distance as in the uniform upper proof. It does not rely on a nonnormal infinitely squeezed Choi state.

## 3. Shared weight and Mehler bounds

Insert the kernel from [the exact-threshold chapter](exact_threshold.md) at $`D=\kappa=1`$, $`\eta=0`$. After translating packet centers, both quantities are three-dimensional integrals against the same nonnegative weight

```math
G_w(x,y,r)=f_w(x)f_w(y)
f_w(r+(x-y)/2)f_w(r-(x-y)/2).
```

The integral of this weight has an exact value

```math
J_w=\iiint G_w\,dx\,dy\,dr
=w\,c_f,\qquad c_f=\frac23+\frac5{\pi^2}.
```

For completeness, the autocorrelation of the unit-width packet is

```math
A(v)=\left(1-\frac{|v|}{2}\right)\cos(\pi|v|/2)
+\frac{\sin(\pi|v|/2)}\pi,
\quad |v|\le2,
```

and $`c_f=\int_{-2}^2 A(v)^2dv`$. The four packet factors contribute $`w^{-2}`$ and the three integration variables $`w^3`$, explaining the single factor of $`w`$.

For the diagonal transition, output and input momentum centers are separated by $`2a`$. Feynman–Kac domination of the Mehler kernel by the free heat kernel gives

```math
\boxed{D_t\le\frac{J_w}{\sqrt{4\pi t}}
\exp[-(a-w)^2/t].}
```

For the coherence, the input and output kernel centers stay within $`w`$ of zero, while its momentum difference satisfies $`2a-2w\le |y|\le2a+2w`$. Using $`\sinh(2|y|t)\le e^{2|y|t}/2`$, the Mehler exponent identity

```math
\coth(2z)+\mathrm{csch}(2z)=\coth z,
```

and bounding the drift phase by $`|\omega|w`$, one obtains, provided $`|\omega|w<\pi/2`$,

```math
\boxed{\begin{aligned}
\mathrm{Re}\,C_t\ge{}&J_w\cos(|\omega|w)
\sqrt{\frac{2a-2w}{\pi}}\\
&\times\exp\left[-(2a+2w)t-
\frac{\omega^2t}{4}
-(2a+2w)w^2\coth((2a-2w)t)\right].
\end{aligned}}
```

No oscillatory-integral sign assumption is hidden: the phase's real cosine is positive on the support by the displayed restriction. The real drift damping is bounded below by $`e^{-\omega^2t/4}`$.

## 4. Parameter choice and a positive universal constant

For $`t\ge1`$, choose

```math
a=2t^2+\omega^2/8,
\qquad w=\frac1{16t(1+\omega^2)}.
```

Elementary inequalities then give $`a>w`$, $`2wt\le1/8`$, $`2a-2w\ge31t^2/8`$, $`|\omega|w\le1/32`$ and

```math
(2a+2w)w^2\coth((2a-2w)t)\le\frac1{32}.
```

Moreover $`2aw/t\le1/4`$ and

```math
\frac{(a-w)^2}{t}
\ge 4t^3+\frac{\omega^2t}{2}-\frac14.
```

Substitute these bounds into the previous two displays, use $`J_w=c_fw`$, and compare the positive coherence with the diagonal leakage. The resulting coefficient is precisely

```math
\frac{c_f}{32(1+\omega^2)}
\left[\cos(1/32)\sqrt{\frac{31}{8\pi}}e^{-5/32}
-\frac{e^{1/4}}{2\sqrt\pi}\right]>0.
```

This proves the theorem's left inequality and also supplies an NPT witness for every $`t\ge1`$. Because later local channels preserve PPT outputs, if $`\Phi_s`$ were PPT-inducing for some $`s<1`$, then $`\Phi_1=\Phi_{1-s}\circ\Phi_s`$ would be PPT-inducing, contradicting the witness. Therefore $`\Phi_t`$ is not PPT-inducing for **any** finite positive time. The exact threshold proof gives a second, independent direct witness for the same conclusion.

## 5. Physical resource and general-rate scaling

The compact packet has

```math
\langle P^2\rangle=a^2+w^2\left(\frac13-\frac2{\pi^2}\right),
\quad \langle Q^2\rangle=\frac{\pi^2}{4w^2}.
```

With the displayed late-time parameters its reference energy $`\langle(Q^2+P^2)/2\rangle`$ grows as $`O_\omega(t^4)`$. This is a **sufficient preparation cost for the explicit quantitative witness**; it is not an energy lower bound for qualitative survival. [The fixed-input corollary](fixed_input.md) explains why one fixed finite-energy entangled state can remain NPT even though its detectable signal has no positive uniform bound.

Finally, a symplectic scaling maps general positive $`D,\kappa`$ into canonical units with $`\tau=D^{2/3}\kappa^{1/3}t`$ and $`\Omega=\omega/(D^{1/3}\kappa^{2/3})`$. This is a unitary equivalence, so both exact EB status and the unconstrained diamond distance are invariant under the change of units. The cubic variable is $`\tau^3=D^2\kappa t^3`$.

## 6. Limits of the proof

Neither bound supplies the best cubic exponent coefficient or an exact negativity asymptotic. NPT can be arbitrarily weak, especially when the witness energy grows; the upper bound already rules out a high-quality fixed-dimensional memory with error bounded away from its EB baseline at large times. We do **not** infer the energy-unconstrained quantum capacity by extending finite-dimensional diamond-continuity estimates, nor do we assert a finite-spin theorem from the oscillator calculation.

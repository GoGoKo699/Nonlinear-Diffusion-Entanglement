# Uniform cubic-exponential proximity to entanglement-breaking channels

[Model](model.md) · [Brownian mixture](conditional_gaussian.md) · [Sharp EB time](exact_threshold.md)

## Statement and conventions

Take $\eta=0$. In canonical units $D=\kappa=1$, with fixed drift $\omega\in\mathbb R$, define the energy-unconstrained distance

$$e(t)=\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_t-\Psi\|_\diamond.$$

For all $t\ge1$,

$$
\boxed{
\frac{c_*}{1+\omega^2}e^{-4t^3-\omega^2t/2}
\le e(t)\le
\min\left\{1,\sqrt{\frac{8t^3}{1-e^{-8t^3}}}\,e^{-t^3}\right\},
}
$$

where

$$
\boxed{
c_*=\frac{2/3+5/\pi^2}{32}
\left[\cos(1/32)\sqrt{\frac{31}{8\pi}}e^{-5/32}
-\frac{e^{1/4}}{2\sqrt\pi}\right]
=0.02153222609588753\ldots>0.
}
$$

Consequently $-\log e(t)=\Theta(t^3)$ at fixed $\omega$. The two cubic exponent coefficients (one and four) are **not equal**; their optimal coefficient is not known. This is stronger than decay of a selected observable because the upper inequality bounds the channel on **every input and reference without an energy cutoff**.

## 1. The uniform upper estimate

By [the mixture representation](conditional_gaussian.md), conditioned on the quadratic shear the displacement covariance has

$$
\det V_S=8t^3Z_\delta,\quad
Z_\delta=\int_0^1[Y_u+\delta(u-\tfrac12)]^2du,\quad
\delta=\omega\sqrt{t/2}.
$$

Let $A_t=\{8t^3Z_\delta<1\}$ be the bad event. On its complement each conditional channel is EB by the one-mode Gaussian EB criterion. Construct a normal EB channel $\Psi_t$ by keeping the actual conditional channels on the good paths and replacing the bad paths by any fixed state-preparation EB channel. Since the half trace-norm difference of two channels on any input is at most one,

$$
\frac12\|\Phi_t-\Psi_t\|_\diamond\le\mathbb P(A_t).
$$

Convex/closed separability makes the average of good conditional channels and bad-path replacement EB. This bound holds for arbitrary references.

The [noncentral Laplace transform](conditional_gaussian.md) is no larger than its centered counterpart because $\tanh(r/2)\le r/2$. Chernoff therefore yields, for $x>0,s>0$,

$$
\mathbb P(Z_\delta<x)\le e^{sx}
\left(\frac{\sqrt{2s}}{\sinh\sqrt{2s}}\right)^{1/2}.
$$

Choose $x=(8t^3)^{-1}$ and $s=8t^6$. Then

$$
\begin{aligned}
e(t)&\le\mathbb P(A_t)\\
&\le e^{t^3}\left(\frac{4t^3}{\sinh(4t^3)}\right)^{1/2}
=\sqrt{\frac{8t^3}{1-e^{-8t^3}}}\,e^{-t^3}.
\end{aligned}
$$

The trivial bound $e(t)\le1$ completes the upper inequality. The EB comparator is time dependent: the result is not convergence to a fixed stationary state. The conditional decomposition is a **proof**, not side information available to a physical decoder.

## 2. Exactly orthogonal finite-energy packets

Use a real compactly supported momentum state,

$$
f_w(p)=\begin{cases}
w^{-1/2}\cos(\pi p/(2w)),&|p|\le w,\\
0,&|p|>w.
\end{cases}
$$

It has $\|f_w\|_2=1$ and a square-integrable weak derivative. For $a>w$ let $f_\pm(p)=f_w(p\mp a)$; their supports are disjoint and the two states exactly orthonormal.

Prepare a Bell-like state with a qubit reference,

$$
|\Psi\rangle=\frac{|f_+\rangle|0\rangle+|f_-\rangle|1\rangle}{\sqrt2},
\quad
|\chi\rangle=\frac{|f_-\rangle|0\rangle-|f_+\rangle|1\rangle}{\sqrt2},
\quad W=(|\chi\rangle\langle\chi|)^{\Gamma_R}.
$$

The test operator has $\|W\|_\infty=1/2$ and nonnegative expectation on every separable state. Put

$$
D_t=\langle f_-|\Phi_t(|f_+\rangle\langle f_+|)|f_-\rangle,\quad
C_t=\langle f_+|\Phi_t(|f_+\rangle\langle f_-|)|f_-\rangle.
$$

Parity invariance and the partial transpose yield

$$
\operatorname{Tr}W(\Phi_t\otimes\mathrm{id})(|\Psi\rangle\langle\Psi|)
=\frac{D_t-\operatorname{Re}C_t}{2}.
$$

For any EB comparator the witness expectation is nonnegative; Hölder's inequality with $\|W\|_\infty=1/2$ gives

$$e(t)\ge\frac{\operatorname{Re}C_t-D_t}{2}.$$

This is a lower bound on the **same energy-unconstrained diamond metric** as in the upper argument. The state has finite preparation energy and uses no distributional oscillator Choi vector.

## 3. Exact common weight and Mehler inequalities

Insert the inherited Mehler kernel in [the threshold chapter](exact_threshold.md) at $D=\kappa=1,\eta=0$. Translation of packet centers reduces $D_t,C_t$ to integrals against the *same* nonnegative four-packet weight

$$
G_w(x,y,r)=f_w(x)f_w(y)
f_w\left(r+\frac{x-y}{2}\right)
f_w\left(r-\frac{x-y}{2}\right).
$$

Its integral is exactly

$$
J_w=\iiint G_w\,dx\,dy\,dr=c_fw,\qquad
c_f=\frac23+\frac5{\pi^2}.
$$

To verify, the unit-width cosine packet's autocorrelation is

$$
A(v)=\left(1-\frac{|v|}{2}\right)\cos\frac{\pi|v|}{2}
+\frac{\sin(\pi|v|/2)}{\pi},\qquad |v|\le2,
$$

and $c_f=\int_{-2}^{2}A(v)^2\,dv$. Four packet amplitudes give $w^{-2}$, three integration variables $w^3$, so the scaling is **$w$**, not $w^2$.

For the diagonal term, the input and output packet centers differ by $2a$; Feynman–Kac domination of the harmonic heat kernel by the free heat kernel gives

$$
\boxed{
D_t\le\frac{J_w}{\sqrt{4\pi t}}
\exp[-(a-w)^2/t].
}
$$

For the coherence, the momentum difference obeys
$2a-2w\le |y|\le2a+2w$ and both kernel centers remain within $w$ of zero. Using $\sinh(2|y|t)\le e^{2|y|t}/2$, the identity $\coth(2z)+\operatorname{csch}(2z)=\coth z$, and bounding the drift phase by $|\omega|w$, one finds for $|\omega|w<\pi/2$,

$$
\boxed{\begin{aligned}
\operatorname{Re}C_t\ge{}&
J_w\cos(|\omega|w)\sqrt{\frac{2a-2w}{\pi}}\\
&\times\exp\left[
-(2a+2w)t-\frac{\omega^2t}{4}
-(2a+2w)w^2\coth((2a-2w)t)
\right].
\end{aligned}}
$$

This is a bound on an actual oscillatory integral: on the packet support the real part of the phase stays positive. The other drift damping is bounded below by $e^{-\omega^2t/4}$. Both displays apply for each finite $a,w,t$ satisfying their assumptions.

## 4. Choose the packet parameters

For $t\ge1$ set

$$
a=2t^2+\frac{\omega^2}{8},
\qquad w=\frac{1}{16t(1+\omega^2)}.
$$

Then $a>w$, $2wt\le1/8$, $|\omega|w\le1/32$, $2a-2w\ge31t^2/8$ and

$$
(2a+2w)w^2\coth((2a-2w)t)\le1/32,
\qquad
\frac{(a-w)^2}{t}\ge4t^3+\frac{\omega^2t}{2}-\frac14.
$$

Substituting into the two previous kernel estimates and then into
$e(t)\ge(\operatorname{Re}C_t-D_t)/2$ gives the explicit positive $c_*$ in the theorem. The [verification code](../verification/README.md) checks the finite integrals and elementary constants; the general bound comes from the displayed inequalities.

The positive lower bound exhibits an NPT output for every $t\ge1$. If an earlier $\Phi_s$ with $0<s<1$ were PPT-inducing, then $\Phi_1=\Phi_{1-s}\circ\Phi_s$ would also be PPT-inducing, since local postprocessing preserves PPT. Hence **no finite time is PPT-inducing or EB**, in agreement with the independent sharp-threshold theorem at $\eta=0$.

## 5. Energy and general positive strengths

The compact cosine packet has

$$
\langle P^2\rangle=a^2+w^2\left(\frac13-\frac2{\pi^2}\right),
\qquad
\langle Q^2\rangle=\frac{\pi^2}{4w^2}.
$$

Thus $\langle (Q^2+P^2)/2\rangle=O_\omega(t^4)$ for this explicit *quantitative* witness. It is a sufficient construction, not a lower bound on the energy needed for any nonzero entanglement; [one fixed finite-energy input](fixed_input.md) already gives qualitative survival.

For general $D,\kappa>0$, a symplectic scaling and time change give canonical
$\tau=D^{2/3}\kappa^{1/3}t$ and $\Omega=\omega/(D^{1/3}\kappa^{2/3})$. EB status and diamond distance are invariant under the unitary equivalence. Accordingly the cubic scale is $\tau^3=D^2\kappa t^3$.

## What is not proved

The cubic exponent's leading coefficient remains between the displayed bounds; no exact asymptotic constant, positive quantum capacity, experimental advantage, fixed-error memory or finite-spin transfer is established. The result concerns the complete channel despite arbitrarily small remaining NPT.

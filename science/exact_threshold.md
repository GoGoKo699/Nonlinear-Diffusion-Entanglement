# Sharp entanglement-breaking and PPT-inducing threshold

[Model](model.md) · [Conditional Gaussian channel](conditional_gaussian.md) · [Interpretation](interpretation.md)

## Exact theorem

For $D,\kappa>0$, $\eta\ge0$ and finite real $\omega$, let

$$
\mathcal L=-i\omega\,\operatorname{ad}_{P^2/2}
-D\operatorname{ad}_Q^2-\kappa\operatorname{ad}_{P^2/2}^2
-\eta\operatorname{ad}_P^2.
$$

Then

$$
\boxed{t_{\mathrm{EB}}=\begin{cases}
(2\sqrt{D\eta})^{-1},&\eta>0,\\
\infty,&\eta=0.
\end{cases}}
$$

At and after the finite threshold the channel is EB. For every strictly earlier positive time an *explicit normalizable state with a qubit reference and finite oscillator preparation energy* has NPT output. Hence the EB and PPT-inducing intervals coincide for this model. NPT by itself is **not** a proof of positive quantum capacity.

## Upper proof: a pathwise Gaussian measurement

By [conditional covariance](conditional_gaussian.md),

$$
\det V_S=4D\eta t^2+4D^2t\int_0^t(S_s-\overline S)^2ds
\ge4D\eta t^2.
$$

At $t\ge(2\sqrt{D\eta})^{-1}$ every conditional additive Gaussian channel has $\sqrt{\det V_S}\ge1$, so it is EB by the known one-mode Gaussian criterion. Gaussian unitary shears preserve EB, and averaging normal EB channels produces an EB channel. The statement includes the **endpoint** because the criterion includes equality. No Gaussian criterion has been applied incorrectly to the *unconditional non-Gaussian mixture*.

## Independent momentum-kernel calculation

Set $s=(p+p')/2$ and $y=p-p'$ in the momentum density kernel. On the Schwartz core the evolution is

$$
\partial_t\rho(s,y)=D\partial_s^2\rho
-\kappa y^2s^2\rho-i\omega ys\rho-\eta y^2\rho.
$$

For $y\neq0$ write $a(y)=\sqrt{\kappa/D}|y|$ and $b(y)=\sqrt{D\kappa}|y|$. The inherited harmonic heat/Mehler kernel is

$$
K_y^0(t;s,r)=
\sqrt{\frac{a}{2\pi\sinh(2bt)}}
\exp\left[-\frac{a[(s^2+r^2)\cosh(2bt)-2sr]}
{2\sinh(2bt)}\right].
$$

Here $a=a(y),b=b(y)$. Its continuous $y=0$ limit is $(4\pi Dt)^{-1/2}\exp[-(s-r)^2/(4Dt)]$. Completing the square in the imaginary drift gives the full kernel

$$
\begin{aligned}
K_y^{\omega,\eta}(t;s,r)
={}&K_y^0(t;s,r)\,e^{-\eta ty^2}
\exp\left[-\frac{\omega^2}{4\kappa}
\left(t-\frac{\tanh(bt)}b\right)\right]\\
&\times\exp\left[-i\frac{\omega\operatorname{sgn}y}
{2\sqrt{D\kappa}}(s+r)\tanh(bt)\right].
\end{aligned}
$$

The drift real factor lies in $[e^{-\omega^2t/(4\kappa)},1]$. The exact model and Mehler solvability are from **Speed, Lyu and Schubert**; the entanglement criterion proved below is the additional conclusion.

## Normalized finite-energy reference witness

Choose momentum Gaussians, with $A,\delta>0$,

$$
f_\pm(p)=(\pi\delta^2)^{-1/4}
\exp[-(p\mp A)^2/(2\delta^2)].
$$

Let $|\Psi\rangle=(|f_+\rangle|0\rangle+|f_-\rangle|1\rangle)/\sqrt2$ and $|v\rangle=(|f_+\rangle|1\rangle-|f_-\rangle|0\rangle)/\sqrt2$. The reference labels make both states normalized regardless of packet overlap. Each system packet has

$$
\langle (Q^2+P^2)/2\rangle=
\frac{A^2}{2}+\frac{\delta^2}{4}+\frac1{4\delta^2}<\infty.
$$

Define the coherence and wrong-sign diagonal terms

$$
c_A=\langle f_+|\Phi_t(|f_+\rangle\langle f_-|)|f_-\rangle,\quad
d_A=\langle f_+|\Phi_t(|f_-\rangle\langle f_-|)|f_+\rangle.
$$

Parity covariance and partial transposition on the qubit give

$$
\langle v|[(\Phi_t\otimes\mathrm{id}_2)(|\Psi\rangle\langle\Psi|)]^{\Gamma_R}|v\rangle
=\frac{d_A-\operatorname{Re}c_A}{2}.
$$

Thus it suffices to show $c_A>d_A$ for a sufficiently large finite $A$.

## Exact positive integral formulas

For $y\ge0$ put $a=a(y)$, $b=b(y)$ and

$$
U(y)=\delta^{-2}+\frac a2\tanh(bt),\qquad
V(y)=\delta^{-2}+\frac a2\coth(bt).
$$

Define the positive, even function $h$ by

$$
\begin{aligned}
h(y)={}&
\frac{\sqrt{a/(2\pi\sinh(2bt))}}{\delta^2\sqrt{UV}}\,
\exp\left[-\eta ty^2-
\frac{\omega^2}{4\kappa}\left(t-\frac{\tanh(bt)}b\right)
-\frac{\omega^2\tanh^2(bt)}{8D\kappa U}\right].
\end{aligned}
$$

All formulas extend continuously to $y=0$. Performing Gaussian integrals in $(s+r)/\sqrt2$ and $(s-r)/\sqrt2$ yields

$$
\boxed{\begin{aligned}
c_A&=\int_{\mathbb R} e^{-(y-2A)^2/(2\delta^2)}h(|y|)\,dy,\\
d_A&=\int_{\mathbb R} e^{-y^2/(2\delta^2)}h(|y|)
\exp\left[-\frac{A^2a(|y|)\coth(b(|y|)t)}
{1+\frac12\delta^2a(|y|)\coth(b(|y|)t)}\right]\,dy.
\end{aligned}}
$$

Both are real and nonnegative even when $\omega\ne0$: the complex kernel phase becomes the explicit positive Gaussian damping factor in $h$. This reduction is checked at finite parameters by the [numerical verifier](../verification/README.md); the analytical proof uses exact integration.

**Diagonal upper estimate.** Since $a\coth(bt)\ge1/(Dt)$ and $u/(1+\delta^2u/2)$ increases with $u$, the exponential leakage factor is at most $\exp[-A^2/(Dt+\delta^2/2)]$. The rest of the integral equals the $A=0$ return probability, bounded by one. Thus

$$
\boxed{d_A\le\exp[-A^2/(Dt+\delta^2/2)].}
$$

**Coherence lower estimate.** Assume $2A>\delta$ and set $a_\pm=\sqrt{\kappa/D}(2A\pm\delta)$ and $b_\pm=\sqrt{D\kappa}(2A\pm\delta)$. Restrict the first integral to $|y-2A|\le\delta$. The elementary hyperbolic bounds yield

$$
\boxed{\begin{aligned}
c_A\ge L_A={}&
\frac{2\delta e^{-1/2}\sqrt{a_-/\pi}}
{1+\frac12\delta^2a_+\coth(b_-t)}\\
&\times\exp\left[-\eta t(2A+\delta)^2-b_+t
-\frac{\omega^2t}{4\kappa}
-\frac{\omega^2\delta^2}{8D\kappa}\right].
\end{aligned}}
$$

The two inequalities form a finite-energy NPT certificate whenever
$L_A>\exp[-A^2/(Dt+\delta^2/2)]$.

## Match the bounds and prove sharpness

Fix a positive $t$ strictly below $(2\sqrt{D\eta})^{-1}$ (any finite $t$ when $\eta=0$), choose $\delta=A^{-1}$, and let the **finite** $A$ grow. The bounds give

$$
\begin{aligned}
\log L_A&=-4\eta tA^2-2\sqrt{D\kappa}\,tA-\tfrac12\log A+O(1),\\
-\log d_A&\ge\frac{A^2}{Dt}+O(1).
\end{aligned}
$$

Their logarithmic ratio is bounded below by

$$
\left[\frac1{Dt}-4\eta t\right]A^2
-2\sqrt{D\kappa}\,tA+O(\log A).
$$

The quadratic coefficient is positive **exactly** when $t<(2\sqrt{D\eta})^{-1}$. It dominates the linear term at sufficiently large *finite* $A$, proving NPT throughout the open pre-threshold interval. Combined with the upper proof (including equality), this establishes the exact EB/PPT boundary.

Positivity of $\kappa$ is essential in this converse. At $\kappa=0$ the channel is Gaussian and its threshold may be earlier because deterministic shear spreads the position noise. Do not set $\kappa=0$ inside this Mehler asymptotic.

## Numerical check and scope

For $D=2,\kappa=0.3,\eta=0.125,\omega=0.7$, the predicted exact threshold is $t=1$. At $A=20,\delta=0.05$, independently evaluated logarithmic packet integrals satisfy $c_A>d_A$ at $t=0.5$ and $0.9$, but not at $1$ and $1.1$, as expected. Other checked cases include negative drift and very small positive $\kappa$. These finite computations check factors and inequality directions; they **do not** establish the universal statement or the endpoint. No quantum-capacity, efficient decoding, or fixed-energy lower bound follows from NPT alone.

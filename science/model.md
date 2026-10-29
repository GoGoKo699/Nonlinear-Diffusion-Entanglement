# Model, conventions, and precise claims

## Normal random-unitary quantum Markov semigroup

The system Hilbert space is $`\mathcal H=L^2(\mathbb R)`$. The standard Schrödinger pair $`Q,P`$ obeys $`[Q,P]=iI`$ on a common core; $`H=P^2/2`$ is free kinetic energy. Fix $`D>0`$, $`\kappa>0`$, $`\eta\ge0`$, and $`\omega\in\mathbb R`$. In formal double-commutator notation,

```math
\mathcal L=-i\omega\operatorname{ad}_{H}
-D\operatorname{ad}_{Q}^2
-\kappa\operatorname{ad}_{H}^2
-\eta\operatorname{ad}_{P}^2.
```

These coefficients are fixed and finite unless a limit is explicitly stated. **The channel is defined through a normal, trace-preserving random-unitary process**: independent standard real Brownian motions $`B,W,Z`$ multiply the self-adjoint generators $`H,Q,P`$ with Stratonovich increments

```math
\omega H\,dt+\sqrt{2\kappa}\,H\circ dB_t
+\sqrt{2D}\,Q\circ dW_t
+\sqrt{2\eta}\,P\circ dZ_t.
```

One may equivalently define the average channel by the conditional Gaussian integral in [the next chapter](conditional_gaussian.md), avoiding a formal exponential of unbounded superoperators. The resulting random-unitary propagator is strongly defined through Weyl displacements and metaplectic shears. Averaging the increments gives the displayed generator on a suitable Schwartz finite-rank core; independent Brownian increments give the semigroup property. For $`\eta=0`$ the $`Z`$ process is absent.

The stochastic environment is *not measured*. Random paths are not free classical side information for decoding. No additional quantum carrier crosses the noise interval, and no intermediate correction is built into the one-use channel. The final receiver may act jointly on the output with arbitrary ancillas under the usual operational definitions.

## Distances and exact loss of entanglement

A channel $`\Phi`$ is **entanglement breaking (EB)** if $`(\Phi\otimes\operatorname{id}_R)(\rho_{SR})`$ is separable for every (possibly infinite-dimensional) reference $`R`$ and normal state. Separability means the trace-norm closed convex hull of product states. It is **PPT-inducing** if all such outputs are positive under reference partial transpose; EB implies PPT-inducing.

Define the energy-*unconstrained* operational distance

```math
e(t)=\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_t-\Psi\|_\diamond.
```

The diamond norm is the completely bounded trace norm on trace-class input, including arbitrary reference dimensions. Every EB mixture used below is an actual normal channel; no distributional maximally entangled oscillator vector is introduced. A sufficient reference-energy measure for explicit witnesses is $`H_{\mathrm{ref}}=(Q^2+P^2)/2`$ (the unit-frequency oscillator), **not** the dynamical free Hamiltonian $`H=P^2/2`$.

## Proven statements and quantifiers

**Theorem A (exact cutoff).** For the displayed model with $`\kappa>0`$, the first EB time is $`(2\sqrt{D\eta})^{-1}`$ if $`\eta>0`$, and is infinite when $`\eta=0`$. At and after a finite first EB time the channel is EB. Every strictly earlier positive time admits an input entangled with a *qubit* reference, of finite $`H_{\mathrm{ref}}`$ energy, with an NPT output. The same interval is the complement of the PPT-inducing interval. [Proof](exact_threshold.md).

**Theorem B (cubic operational proximity).** For $`\eta=0`$ and $`D=\kappa=1`$, at every $`t\ge1`$,

```math
\frac{c_*}{1+\omega^2}\,e^{-4t^3-\omega^2t/2}
\ \le e(t)\le
\min\left\{1,\sqrt{\frac{8t^3}{1-e^{-8t^3}}}\,e^{-t^3}\right\},
```

where $`c_*=0.02153222609588753\ldots>0`$ has an exact elementary expression in [the proof](cubic_distance.md). In general units, the cubic variable is $`D^2\kappa t^3`$. Consequently $`-\log e(t)=\Theta(D^2\kappa t^3)`$ at fixed $`D,\kappa,\omega`$ as $`t\to\infty`$. No optimal leading exponent coefficient is claimed.

**Corollary C (fixed input).** For $`\eta=0`$, every fixed two-mode squeezed vacuum of nonzero *finite* squeezing has NPT output after applying $`\Phi_t`$ to one factor, at every finite $`t>0`$. The statement is qualitative and does not bound the size of surviving entanglement. [Proof](fixed_input.md).

**Weak-noise consequence.** At fixed $`D>0`$, $`\omega\ne0`$, $`\eta=0`$ and any time strictly beyond the Gaussian cutoff, the distance satisfies $`e(t)\le C\exp(-c/\kappa)`$ for some positive $`C,c`$ independent of sufficiently small $`\kappa>0`$. This is a one-sided bound, not a matched weak-noise asymptotic. [Derivation](interpretation.md#3-weak-quadratic-dephasing-the-discontinuity-is-operationally-tiny).

**Gaussian comparison ($`\kappa=0`$).** This is a separate model: the first EB time is the first nonnegative root of $`4D\eta t^2+D^2\omega^2t^4/3=1`$ (infinite when the left side is identically zero). [Derivation](interpretation.md).

These statements do **not** imply quantum capacity, fixed-quality storage, a practical error-correction protocol, a general nonlinear Lindblad classification, a finite-spin result, or a norm-small perturbation when changing the coefficient of an unbounded noise generator.

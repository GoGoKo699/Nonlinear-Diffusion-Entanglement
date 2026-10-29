# Learning nonlinear diffusion and entanglement

[Project](../README.md) · [30 milestones](MILESTONES.md) · [Rivas–Huelga bridge](RIVAS_HUELGA_BRIDGE.md) · [Exact science](../science/README.md)

## The question

Imagine storing one half of an entangled pair in a freely moving quantum particle. Its momentum receives random kicks, and its free motion is also randomly sped up or slowed down. The environment does not reveal these fluctuations. We ask two different questions: when does the noise destroy **every possible input's entanglement**, and how close is the whole noisy channel to an operation that measures a state and prepares a new one?

These questions need not have the same answer. This project identifies their precise separation for one specified non-Gaussian diffusion model. The result concerns the channel, not only a chosen initial state or a variance of position.

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (Springer, 2012)**. The [source bridge](RIVAS_HUELGA_BRIDGE.md) maps the printed book to its freely available author version, translates conventions, and supplies the additional continuous-variable and entanglement ideas needed here. The primary papers cited in the scientific account supply research ingredients; they are not additional educational anchors.

The [settled map](MILESTONES.md) contains **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The first phase assembles states, channels, noise and reference-assisted tests into one operational question. The second builds the conditional covariance, sharp threshold and two-sided distance bounds into the complete scientific conclusion. The map describes shared understanding targets, not personal assessment history or a requirement to master every technical lemma.

## 1. State, reference, channel

A density operator describes the probabilities of all measurements on a quantum system. A channel is a linear, completely positive, trace-preserving map on these states. Complete positivity means that the map remains physically valid when the system is entangled with an untouched reference. This reference is a test of the stored quantum information, not a noiseless memory available to the receiver.

A channel is **entanglement breaking (EB)** if its output is separable from the reference for every joint input. A measure-and-prepare procedure has this property: it extracts a classical outcome and prepares an output state depending on that outcome. A negative expectation after partially transposing the reference provides an **NPT witness** and disproves EB for that channel. Nonnegative partial transpose alone does not generally prove separability.

The distance used here is

```math
e(t)=\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_t-\Psi\|_\diamond.
```

It compares the noisy channel with the best EB comparator, allowing arbitrary input states and references. A small value means that no channel-discrimination experiment can distinguish the two with large advantage. It does not assert that the noisy channel is exactly EB. The comparator may depend on time.

## 2. A complete two-level example

First consider a qubit, only as a teaching model. Let $Z=\mathrm{diag}(1,-1)$ and let its noise generator be $-\gamma[Z,[Z,\rho]]$, with $\gamma>0$. Diagonal entries do not change. An off-diagonal entry connects eigenvalues differing by two, so it is multiplied by

```math
q(t)=e^{-4\gamma t}.
```

Prepare $|\beta\rangle=(|00\rangle+|11\rangle)/\sqrt2$, expose the first qubit to the noise, and leave the second untouched. In the ordered basis $00,01,10,11$, the output is

```math
\rho_t=\frac12\begin{pmatrix}
1&0&0&q(t)\\
0&0&0&0\\
0&0&0&0\\
q(t)&0&0&1
\end{pmatrix}.
```

After transposing only the reference index, the middle two-dimensional block has eigenvalues $q(t)/2$ and $-q(t)/2$. The negative value proves entanglement at every finite time. Nevertheless $q(t)$ tends to zero and the output approaches the separable mixture of $00$ and $11$. Equivalently, the witness obtained by partially transposing the projector onto $(|01\rangle-|10\rangle)/\sqrt2$ has expectation $-q(t)/2$ on the physical output; partial transposition is a mathematical test, not a physical operation we perform.

This example shows why residual entanglement and operational proximity must be distinguished. It does **not** prove the project's continuous-variable threshold or cubic decay law. The [learning checks](../verification/check_learning.py) independently build this matrix and test the factors of two.

## 3. What the three noise coefficients do

The project's carrier is $L^2(\mathbb R)$, with dimensionless quadratures satisfying $[Q,P]=i$ and free kinetic Hamiltonian $H=P^2/2$. Its formal generator is

```math
\mathcal L(\rho)=-i\omega[H,\rho]
-D[Q,[Q,\rho]]-\kappa[H,[H,\rho]]-\eta[P,[P,\rho]].
```

The $D$ term is dephasing in position and diffusion of momentum. The $\eta$ term is dephasing in momentum and diffusion of position. The $\kappa$ term randomizes the free-motion shear itself. These descriptions name different aspects of the same terms; momentum **dephasing** is not momentum **diffusion**.

The dynamics remain linear in the density operator. The word nonlinear refers to the quadratic noise operator and resulting phase-space diffusion, not a nonlinear modification of quantum mechanics. All three noises are unobserved. The deterministic frequency-like coefficient $\omega$ multiplies free kinetic motion; it is not a harmonic-trap frequency.

An explicit state's preparation energy is measured by $(Q^2+P^2)/2$. That auxiliary oscillator cost is different from the Hamiltonian generating the dynamics. The channel-distance optimization itself has no energy constraint.

## 4. Condition on the hidden shear, then average

For one fixed shear path $S_s=\omega s+\sqrt{2\kappa}B_s$, the remaining noises are linear quadrature displacements. Their conditional channel is Gaussian, followed by a known mathematical shear. Its displacement covariance obeys

```math
\det V_S=4D\eta t^2+
4D^2t\int_0^t(S_s-\overline S)^2\,ds,
\qquad \overline S=\frac1t\int_0^tS_s\,ds.
```

The integral is nonnegative. In this project's convention, a one-mode additive Gaussian channel is EB precisely when $\sqrt{\det V_S}\ge1$. Thus $4D\eta t^2\ge1$ makes every conditional channel EB, including at equality; their unobserved mixture is then EB too.

The reverse argument is not valid: finding some non-EB conditional paths does not prove that their mixture is non-EB. Averaging can erase entanglement. The [sharp-threshold proof](../science/exact_threshold.md) instead constructs a normalized system–qubit input and compares two actual matrix elements of the averaged channel.

As a numerical normalization example, take $D=1$, $\eta=1/4$ and any $\kappa>0$. The exact threshold is $t=1$. The covariance floor alone proves EB at and after that time. Only the independent witness proof establishes that every earlier positive time is outside the EB set. At $\kappa=0$, deterministic shear can give an earlier Gaussian threshold; that is a separate case.

## 5. Why the two main proofs need different witnesses

For the exact threshold, Gaussian momentum packets centered at $\pm A$ have finite preparation energy for every finite $A$ and width $\delta>0$. Below threshold, the wrong-packet leakage decays faster with $A$ than the surviving coherence. Choosing $A$ sufficiently large proves NPT. This need not give a practically detectable signal or a uniform energy budget.

For the channel-distance lower bound, compact cosine packets have disjoint support and are exactly orthogonal. Their witness has a controlled operator norm, which converts its negative expectation into a quantitative distance from **every** EB channel. Choosing the centers and widths as functions of time gives a lower bound with a cubic exponential.

The upper bound uses a different idea. At late times most conditional Gaussian channels are already EB. Replace the exceptional paths by a state-preparation channel. This produces a genuine EB comparator, and the total probability of the replaced paths bounds the half-diamond error for all inputs. A Brownian quadratic-functional estimate makes that probability cubic-exponentially small.

Together these arguments prove logarithmic order, not a common optimal exponential constant. The [canonical theorem](../science/cubic_distance.md) retains its exact constants and domains.

## 6. Read the conclusions with their quantifiers

At $\eta=0$, no finite time is EB when $D,\kappa>0$, but $-\log e(t)=\Theta(D^2\kappa t^3)$ at fixed rates and large time. A fixed finite-energy two-mode squeezed input also remains NPT at every finite time. Its qualitative survival follows by bounded local filtering; the filter's success probability need not stay appreciable.

For a deterministic encoding of a fixed $d$-level register into the single carrier and final recovery, with no quantum bypass, the project gives $F_e\le1/d+e(t)$. Thus exact residual entanglement is compatible with a strong one-use memory limitation. No positive quantum capacity, useful long-time entanglement amount or experimental advantage is inferred.

Follow [M01–M12](MILESTONES.md#backgroundpreliminaries-m01m12) to assemble the prerequisites, then [M13–M30](MILESTONES.md#narrativeinnovation-m13m30) for the mechanism and its limits. Specialists can go directly to the [topic-based proof map](../science/README.md).

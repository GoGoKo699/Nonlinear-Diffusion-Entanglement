# Application to rank-two spin diffusion

[Conditional covariance](conditional_gaussian.md) · [Finite-energy converse](exact_threshold.md) · [Cubic distance](cubic_distance.md)

The sister project [Spin-Diffusion-Classicalization](https://github.com/GoGoKo699/Spin-Diffusion-Classicalization) gives this nonlinear channel a controlled finite-spin application. A squeezed local contraction transfers the oscillator's reference-entanglement witness to growing spins. It does **not** transfer the oscillator's all-input EB upper bound to the whole spin channel.

The full contraction proof, the independent finite-spin witness and the separate global comparison have their authoritative home in the sister's [rank-two account](https://github.com/GoGoKo699/Spin-Diffusion-Classicalization/blob/bf31418c10302d1786451ddee9b9840f4d9983c8/science/rank_two_diffusion.md). This page fixes the assumptions, parameter conversion and consequence needed to read this application independently. The nonlinear channel, conditional covariance and packet witnesses remain defined and proved in this repository.

## 1. The finite-spin question

Let $`n=2j`$ and let $`\mathcal H_j`$ be one irreducible spin representation. Fix $`b,c>0`$ and define

```math
\mathcal L^{(j)}=-b\,\mathrm{ad}_{J_y}^2
-c\,\mathrm{ad}_{J_z}^2,\qquad
\Phi_t^{(j)}=e^{t\mathcal L^{(j)}},\qquad
e_j(t)=\inf_{\Psi\in\mathrm{EB}}\tfrac12
\|\Phi_t^{(j)}-\Psi\|_\diamond.
```

The missing diffusion axis is $`x`$, while the local pole is $`z`$. The reference is untouched; no environmental record or intermediate correction is supplied. As usual, $`\mathrm{ad}_A(X)=[A,X]`$. Here $`t`$ is the physical spin time, and $`s`$ below is a fixed scaled time.

At $`t=s n^{-2/3}`$, ordinary bounded-excitation pole states miss the relevant anisotropy. The contraction instead uses squeezing with quadrature dilation $`n^{1/6}`$. Its encoded states have excitation moments

```math
\langle N^r\rangle=O(n^{r/3}),\qquad N=j-J_z,
```

for each fixed moment order $`r`$. Thus the typical excitation grows as $`n^{1/3}`$, while remaining small relative to $`n`$.

## 2. Controlled local limit and the parameter dictionary

Embed the spin ladder as oscillator levels $`0,\ldots,n`$, with projection $`\Pi_n`$. Write $`q,p`$ for the oscillator quadratures before squeezing. Choose $`S_n`$ so that

```math
S_n^*qS_n=n^{1/6}Q,\qquad
S_n^*pS_n=n^{-1/6}P,\qquad [Q,P]=i.
```

After the time rescaling and removal of scalar terms, the two noise generators are

```math
A_n=n^{-1/3}S_n^*\Pi_nJ_y\Pi_nS_n
\longrightarrow P/\sqrt2,
\qquad
C_n=-\tfrac12(Q^2+n^{-2/3}P^2)
\longrightarrow-Q^2/2.
```

The limiting channel $`\Xi_s`$ consequently has generator

```math
\mathcal G=-\frac b2\,\mathrm{ad}_P^2
-c\,\mathrm{ad}_{Q^2/2}^2.
```

The canonical exchange $`(Q',P')=(P,-Q)`$ puts it in this repository's convention:

| Parameter in the nonlinear model | Value in the spin contraction |
|---|---|
| $`D`$ | $`b/2`$ |
| $`\kappa`$ | $`c`$ |
| $`\eta,\omega`$ | $`0,0`$ |
| Nonlinear evolution time | $`s=n^{2/3}t`$ |
| Cubic variable $`D^2\kappa s^3`$ | $`b^2c\,n^2t^3/4`$ |

The precise convergence statement concerns any **fixed finite-dimensional span of Schwartz vectors**, any fixed finite reference, and $`0\le s\le T`$ for fixed $`T<\infty`$. Polar normalization of $`\Pi_nS_n`$ on that span gives an exact isometric spin encoding. Embed the actual spin output in the oscillator and undo $`S_n`$. Its trace-norm difference from $`\Xi_s`$ applied to the original input is

```math
O_{T,b,c,\mathrm{span}}(n^{-2/3}).
```

The constant depends on sufficiently many Schwartz seminorms of the fixed span. Projection is not postselection. The proof controls both generators and their squares on those vectors and then their actual semigroup outputs; formal convergence of a commutator is insufficient. No claim is made uniformly over all oscillator energies, all spin inputs or scaled times growing with $`n`$.

## 3. What conditional covariance contributes

In the exchanged quadratures, condition on $`S_u=\sqrt{2c}B_u`$ as in the [conditional representation](conditional_gaussian.md). The displacement covariance is

```math
V_S=b\begin{pmatrix}
\int_0^s S_u^2du&-\int_0^s S_udu\\
-\int_0^s S_udu&s
\end{pmatrix},\qquad
\det V_S=2b^2c\,s^3 Z,
```

where $`Z`$ is the integrated square of Brownian motion after subtracting its temporal mean. The Gaussian components are EB when this determinant is at least one. Replacing the exceptional components by preparation gives an actual EB approximant to **the limiting oscillator channel**, with the [cubic-exponential bound](cubic_distance.md). This explains why $`n^2t^3`$ is the natural candidate variable.

For the finite spin, conditioned linear spin generators still have noncentral commutators. Their time ordering cannot be discarded as a scalar phase. Nor is a locally EB oscillator component an EB map defined on all of $`\mathcal H_j`$. The exceptional-path construction therefore does not establish a global finite-spin bound by substitution of the parameter dictionary.

## 4. A genuine finite-spin consequence

For $`D,\kappa>0`$ and $`\eta=0`$, the [Gaussian-packet converse](exact_threshold.md) supplies a strictly negative partial-transpose witness at every fixed finite time. Its packet and test vectors are Schwartz. Encode their fixed finite span and the qubit reference as above. Trace-norm convergence preserves the strictly negative margin for sufficiently large $`n`$. A bounded witness then implies

```math
\boxed{\text{For every fixed }s>0,\quad
\liminf_{n\to\infty}e_{n/2}(s n^{-2/3})>0.}
```

The positive constant depends on $`s,b,c`$ and the chosen witness; it can be very small. Since distance to EB is nonincreasing under semigroup postprocessing, any sequence with $`e_{n/2}(t_n)\to0`$ must satisfy

```math
n^2t_n^3\longrightarrow\infty.
```

Thus $`n^{-2/3}`$ cannot be a fixed-coefficient threshold for vanishing EB distance. The contraction establishes a necessary scaling condition and a useful local mechanism. Sufficiency remains open.

A separate result in the sister account constructs a global EB comparator for **equal positive rates** $`b=c`$, giving $`e_j(t)\le\min\{1,C_b/(\sqrt n\,t)\}`$ at small positive $`t`$. Hence $`t\sqrt n\to\infty`$ is sufficient there. This weaker upper regime leaves a real gap from the necessary condition; it does not settle the proposed crossover.

## 5. Ownership and inherited mechanisms

The nonlinear model and its Grushin/Mehler solution are inherited from Speed–Lyu–Schubert. Gaussian EB theory is inherited from Holevo. Commutator-generated spreading and delayed decoherence are established hypoelliptic mechanisms; Schubert–Plastow and Baudoin–Bonnefont supply relevant primary precedents. The [attribution map](../references/RELATED_WORK.md#the-rank-two-spin-application) distinguishes these ingredients from the controlled transfer.

This repository owns the nonlinear covariance, exceptional-path EB bound and oscillator witnesses. The sister rank-two account owns the growing-excitation contraction, finite-spin witnesses and global spin comparison. Neither a local contraction nor a finite NPT calculation determines positive quantum capacity, useful memory fidelity or a uniform global EB upper bound at the conjectured scale.

"""Reproduce exact finite-energy NPT witness integrals and analytic bounds.

SciPy quadrature and Gauss-Hermite nodes are used on selected finite cases.
These checks do not replace the all-time analytical proof.
"""
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_hermitenorm, logsumexp


def log_h(y, t, delta, diffusion, kinetic, eta, omega):
    y = abs(float(y))
    a = np.sqrt(kinetic / diffusion) * y
    b = np.sqrt(diffusion * kinetic) * y
    z = b * t
    tanh = np.tanh(z)
    if z < 1e-5:
        acoth = 1 / (diffusion * t) + kinetic * y*y*t / 3
        acoth -= diffusion * kinetic**2 * y**4 * t**3 / 45
        logk = -.5 * np.log(4*np.pi*diffusion*t) - z*z/3
        drift = t * (z*z/3 - 2*z**4/15)
    else:
        acoth = a / tanh
        logsinh = 2*z - np.log(2) + np.log1p(-np.exp(-4*z))
        logk = .5 * (np.log(a) - np.log(2*np.pi) - logsinh)
        drift = t - tanh/b
    u = delta**-2 + a*tanh/2
    v = delta**-2 + acoth/2
    value = logk - 2*np.log(delta) - .5*np.log(u*v)
    value -= eta*t*y*y + omega*omega*drift/(4*kinetic)
    value -= omega*omega*tanh*tanh/(8*diffusion*kinetic*u)
    return value, acoth


def compute(diffusion, kinetic, eta, omega, t, amplitude):
    delta = 1 / amplitude
    args = (t, delta, diffusion, kinetic, eta, omega)
    zs, ws = roots_hermitenorm(200)
    log_cross = np.log(delta) + logsumexp(
        np.log(ws) + [log_h(2*amplitude+delta*z, *args)[0] for z in zs]
    )
    h0, ac0 = log_h(0, *args)
    base = h0 - amplitude**2 * ac0/(1+delta**2*ac0/2)
    scale = 1/np.sqrt(delta**-2 + 2*amplitude**2*kinetic*t/3)

    def integrand(u):
        y = scale*u
        h, ac = log_h(y, *args)
        val = -y*y/(2*delta*delta) + h
        val -= amplitude**2*ac/(1+delta**2*ac/2)
        return np.exp(val-base)

    integral, _ = quad(integrand, 0, np.inf, epsabs=1e-12)
    log_diagonal = base + np.log(2*scale*integral)
    am = np.sqrt(kinetic/diffusion)*(2*amplitude-delta)
    ap = np.sqrt(kinetic/diffusion)*(2*amplitude+delta)
    bm = np.sqrt(diffusion*kinetic)*(2*amplitude-delta)
    bp = np.sqrt(diffusion*kinetic)*(2*amplitude+delta)
    log_lower = np.log(2*delta) - .5 + .5*np.log(am/np.pi)
    log_lower -= np.log(1+delta*delta*ap/(2*np.tanh(bm*t)))
    log_lower -= eta*t*(2*amplitude+delta)**2 + bp*t
    log_lower -= omega*omega*t/(4*kinetic)
    log_lower -= omega*omega*delta*delta/(8*diffusion*kinetic)
    log_upper = -amplitude**2/(diffusion*t+delta*delta/2)
    return {
        "D": diffusion, "kappa": kinetic, "eta": eta,
        "omega": omega, "t": t, "A": amplitude, "delta": delta,
        "t_EB": 1/(2*np.sqrt(diffusion*eta)) if eta else None,
        "log_C": float(log_cross), "log_d": float(log_diagonal),
        "log_cross_lower": float(log_lower), "log_diagonal_upper": float(log_upper),
        "integral_witness_NPT": bool(log_cross > log_diagonal),
        "elementary_certificate_NPT": bool(log_lower > log_upper),
        "cross_bound_valid": bool(log_lower <= log_cross + 1e-10),
        "diagonal_bound_valid": bool(log_diagonal <= log_upper + 1e-10),
    }


def run_checks():
    cases = [
        (2, .3, .125, .7, .5, 20),
        (2, .3, .125, .7, .9, 20),
        (2, .3, .125, .7, 1, 20),
        (2, .3, .125, .7, 1.1, 20),
        (1, .05, 1, -2, .4, 10),
        (1, .0001, .25, 1, .75, 100),
    ]
    output = [compute(*case) for case in cases]
    assert all(r["cross_bound_valid"] and r["diagonal_bound_valid"] for r in output)
    assert all(r["elementary_certificate_NPT"] == r["integral_witness_NPT"] for r in output)
    assert [r["integral_witness_NPT"] for r in output] == [True, True, False, False, True, True]
    for r in output:
        assert r["log_cross_lower"] <= r["log_C"] + 1e-8
        assert r["log_d"] <= r["log_diagonal_upper"] + 1e-8
    return output


if __name__ == "__main__":
    for result in run_checks():
        print(json.dumps(result, sort_keys=True))

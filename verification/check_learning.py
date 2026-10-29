"""Finite checks for the learning bridge; no universal theorem is inferred."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm


def run_checks():
    z = np.diag([1., -1.])
    eye = np.eye(2)
    comm = np.kron(eye, z) - np.kron(z.T, eye)
    bell = np.array([1., 0., 0., 1.]) / math.sqrt(2)
    beta = np.outer(bell, bell)
    singlet = np.array([0., 1., -1., 0.]) / math.sqrt(2)
    project = np.outer(singlet, singlet)
    witness = project.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    assert np.isclose(np.linalg.norm(witness, 2), .5)
    qubit = []
    for gamma, t in ((.1, 0.), (.1, .4), (.7, .3), (.7, 2.)):
        superoperator = expm(-gamma * t * comm @ comm)
        out = np.zeros((4, 4))
        for i in range(2):
            for j in range(2):
                unit = np.zeros((2, 2)); unit[i, j] = 1
                mapped = (superoperator @ unit.reshape(-1, order='F')).reshape(2, 2, order='F')
                out += np.kron(mapped, beta[2*i:2*i+2, 2*j:2*j+2])
        q = math.exp(-4 * gamma * t)
        expected = np.zeros((4, 4)); expected[0, 0] = expected[3, 3] = .5
        expected[0, 3] = expected[3, 0] = q / 2
        assert np.allclose(out, expected, atol=1e-13)
        pt = out.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
        minimum = np.linalg.eigvalsh(pt)[0]
        assert np.isclose(minimum, -q/2, atol=1e-13)
        assert np.isclose(np.trace(witness @ out), -q/2, atol=1e-13)
        qubit.append({'gamma': gamma, 't': t, 'minimum_pt_eigenvalue': float(minimum)})

    covariance_cases = 0
    for D, eta, omega, curvature, t in ((1., .25, 0., 0., 1.),
                                       (2., .125, .7, 1.2, .9),
                                       (.3, .5, -2., .4, 2.)):
        shear = lambda s: omega*s + curvature*s*s
        first = quad(shear, 0, t)[0]
        second = quad(lambda s: shear(s)**2, 0, t)[0]
        covariance = 2*D*np.array([[second, -first], [-first, t]])
        covariance[0, 0] += 2*eta*t
        det = np.linalg.det(covariance)
        formula = 4*D*eta*t*t + 4*D*D*(t*second-first*first)
        assert np.isclose(det, formula, atol=1e-12)
        assert det >= 4*D*eta*t*t - 1e-12
        covariance_cases += 1
    assert math.isclose(1/(2*math.sqrt(1*.25)), 1)

    # Canonical rescaling Q'=alpha Q, P'=P/alpha and tau=rate*t.
    scaling_cases = 0
    for D, kinetic, omega in ((2., .3, .7), (.1, 4., -2.), (1., 1., 0.)):
        alpha = (D/kinetic)**(1/6)
        rate = D**(2/3)*kinetic**(1/3)
        assert np.isclose(D/alpha**2, rate)
        assert np.isclose(kinetic*alpha**4, rate)
        assert np.isclose(omega*alpha**2/rate, omega/(D**(1/3)*kinetic**(2/3)))
        assert np.isclose(rate**3, D*D*kinetic)
        scaling_cases += 1

    trace = quad(lambda u: u*u-u+1/3, 0, 1)[0]
    assert math.isclose(trace, 1/6, abs_tol=1e-14)
    packet_norm = quad(lambda p: math.cos(math.pi*p/2)**2, -1, 1)[0]
    packet_p2 = quad(lambda p: p*p*math.cos(math.pi*p/2)**2, -1, 1)[0]
    packet_q2 = quad(lambda p: (math.pi/2*math.sin(math.pi*p/2))**2, -1, 1)[0]
    assert np.allclose([packet_norm, packet_p2, packet_q2],
                       [1, 1/3-2/math.pi**2, math.pi**2/4], atol=1e-13)

    # Finite-rank bounded filter applied to a faithful squeezed state.
    squeezed_cases = []
    for lam in (.2, .5, .8):
        n = np.arange(300)
        prob = (1-lam*lam)*lam**(2*n)
        assert np.isclose(prob.sum(), 1, atol=1e-13)
        mean = float(np.sum((n+.5)*prob))
        assert np.isclose(mean, .5+lam*lam/(1-lam*lam), atol=1e-12)
        coeff = np.array([[1., 0.], [0., 2.], [1., -1.], [.5, .25]])
        coeff /= np.linalg.norm(coeff)
        schmidt = math.sqrt(1-lam*lam)*lam**np.arange(4)
        operator = (coeff/schmidt[:, None]).T
        normalization = max(1., np.linalg.norm(operator, 2))
        contraction = operator/normalization
        recovered = schmidt[:, None]*contraction.T
        assert np.linalg.norm(contraction, 2) <= 1+1e-13
        assert np.allclose(recovered*normalization, coeff, atol=1e-13)
        squeezed_cases.append({'lambda': lam, 'mean_reference_energy': mean,
                               'finite_filter_success_probability': float(np.linalg.norm(recovered)**2)})
    return {'all_assertions_passed': True, 'qubit_cases': qubit,
            'covariance_cases': covariance_cases, 'scaling_cases': scaling_cases,
            'centered_brownian_mean_square': trace,
            'packet_moments': [packet_norm, packet_p2, packet_q2],
            'squeezed_cases': squeezed_cases}


if __name__ == '__main__':
    import json
    print(json.dumps(run_checks(), indent=2, allow_nan=False))

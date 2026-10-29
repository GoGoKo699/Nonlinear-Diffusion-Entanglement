"""Check the unreduced Mehler kernel independently of the packet reduction.

Deterministic quadrature and finite differences are finite checks, not proofs.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_hermitenorm
from check_threshold import log_h


def kernel(t, s, r, y, D, kappa, eta, omega):
    """Full complex kernel, using the continuous heat limit at y=0."""
    a = math.sqrt(kappa / D) * abs(y)
    b = math.sqrt(D * kappa) * abs(y)
    if y == 0:
        return np.exp(-(s-r)**2/(4*D*t))/math.sqrt(4*math.pi*D*t)
    z = b*t
    log_prefactor = .5*(math.log(a)-math.log(2*math.pi)-math.log(math.sinh(2*z)))
    real = -a*((s*s+r*r)*math.cosh(2*z)-2*s*r)/(2*math.sinh(2*z))
    real -= eta*t*y*y + omega*omega/(4*kappa)*(t-math.tanh(z)/b)
    phase = -omega*np.sign(y)*(s+r)*math.tanh(z)/(2*math.sqrt(D*kappa))
    return np.exp(log_prefactor + real + 1j*phase)


def run_checks():
    D, kappa, eta, omega, t, width, A = 1.3, .4, .07, -.8, .6, .4, .9
    x, w = roots_hermitenorm(48)
    u = width*x/math.sqrt(2)
    weights = np.outer(w,w)/(2*math.pi)
    reductions = []
    for y in (0., .05, -.05, .8, 2.):
        c = np.sum(weights*kernel(t,u[:,None],u[None,:],y,D,kappa,eta,omega))
        d = np.sum(weights*kernel(t,A+u[:,None],-A+u[None,:],y,D,kappa,eta,omega))
        log_value, acoth = log_h(y,t,width,D,kappa,eta,omega)
        c_exact = math.exp(log_value)
        d_exact = math.exp(log_value-A*A*acoth/(1+width*width*acoth/2))
        err = max(abs(c-c_exact),abs(d-d_exact))
        assert err < 2e-12, (y,c,d,c_exact,d_exact)
        reductions.append({'y':y,'max_absolute_error':float(err)})
    pde = []
    for y, s, r in ((.8,.3,-.7),(-1.2,-.4,.2),(0.,.3,-.7)):
        h, dt = 2e-4, 1e-5
        f = kernel(t,s,r,y,D,kappa,eta,omega)
        lhs = (kernel(t+dt,s,r,y,D,kappa,eta,omega)-kernel(t-dt,s,r,y,D,kappa,eta,omega))/(2*dt)
        lap = (kernel(t,s+h,r,y,D,kappa,eta,omega)-2*f+kernel(t,s-h,r,y,D,kappa,eta,omega))/(h*h)
        rhs = D*lap-(kappa*y*y*s*s+1j*omega*y*s+eta*y*y)*f
        error = float(abs(lhs-rhs))
        assert error < 2e-7, (y,error)
        pde.append({'y':y,'absolute_residual':error})
    composition = []
    for y in (0., .8, -1.2):
        f = lambda u: kernel(.35,.3,u,y,D,kappa,eta,omega)*kernel(.25,u,-.7,y,D,kappa,eta,omega)
        direct = quad(lambda u: float(np.real(f(u))),-np.inf,np.inf,epsabs=1e-12)[0]
        direct += 1j*quad(lambda u: float(np.imag(f(u))),-np.inf,np.inf,epsabs=1e-12)[0]
        error = float(abs(direct-kernel(.6,.3,-.7,y,D,kappa,eta,omega)))
        assert error < 2e-11, (y,error)
        composition.append({'y':y,'absolute_error':error})
    return {'packet_reductions':reductions,'generator_residuals':pde,
            'semigroup_composition':composition,'all_assertions_passed':True}

if __name__ == '__main__':
    import json
    print(json.dumps(run_checks(),indent=2,allow_nan=False))

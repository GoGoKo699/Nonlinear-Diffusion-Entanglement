"""Finite checks of spectral Laplace law, cosine-packet overlap and covariance.

No finite sample is treated as an analytical proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def c_f_exact():
    return 2 / 3 + 5 / (math.pi**2)


def autocorr(v):
    v = abs(v)
    if v > 2:
        return 0.0
    return (1-v/2)*math.cos(math.pi*v/2)+math.sin(math.pi*v/2)/math.pi


def log_laplace(s, delta=0.0):
    if s == 0:
        return 0.0
    r = math.sqrt(2*s)
    return .5*(math.log(r)-math.log(math.sinh(r))) - delta**2/2 + delta**2*math.tanh(r/2)/r


def truncated_log_laplace(s, delta=0.0, terms=30000):
    n=np.arange(1,terms+1,dtype=np.float64)
    eigen=1/(np.pi*n)**2
    main=-.5*np.log1p(2*s*eigen).sum()
    c2=np.where((n%2)==1,8*delta**2/(np.pi*n)**4,0.0)
    return float(main-s*(c2/(1+2*s*eigen)).sum())


def lower_constant():
    return c_f_exact()/32*(math.cos(1/32)*math.sqrt(31/(8*math.pi))
         *math.exp(-5/32)-math.exp(1/4)/(2*math.sqrt(math.pi)))


def finite_gaussian_det(D,eta,omega,t):
    cov = 2*D*np.array([[omega**2*t**3/3,-omega*t*t/2],
                         [-omega*t*t/2,t]],dtype=float)
    cov[0,0] += 2*eta*t
    return float(np.linalg.det(cov))


def run_checks():
    integral = 2*quad(lambda v:autocorr(v)**2,0,2,epsabs=5e-13)[0]
    assert abs(integral-c_f_exact())<1e-12
    values=[]
    for s,delta in ((.1,0),(1.,0),(4.,0),(.5,1.2),(2.,.7)):
        exact=log_laplace(s,delta)
        approx=truncated_log_laplace(s,delta)
        assert abs(exact-approx)<5e-5, (s,delta,exact,approx)
        values.append(dict(s=s,delta=delta,exact=exact,finite_spectral=approx,
                           abs_error=abs(exact-approx)))
    for t in (.4,1,1.1):
        D,eta,omega=2.,.125,.7
        det=finite_gaussian_det(D,eta,omega,t)
        explicit=4*D*eta*t*t+(D*omega)**2*t**4/3
        assert abs(det-explicit)<1e-12
    t_G=3**.25/math.sqrt(2*.7)
    assert abs(finite_gaussian_det(2,0,.7,t_G)-1)<2e-12
    for t in (1.,2.,3.):
        for omega in (0.,.7,2.):
            a=2*t*t+omega*omega/8
            w=1/(16*t*(1+omega*omega))
            assert a>w and abs(omega)*w<math.pi/2
            vmin=2*a-2*w
            vmax=2*a+2*w
            assert vmin>=31*t*t/8-1e-12
            assert vmax*w*w/math.tanh(vmin*t)<1/32
            assert 2*a*w/t<=.25+1e-12
            assert (a-w)**2/t>=4*t**3+omega**2*t/2-.25-1e-12
    assert lower_constant()>.0215
    return {"c_f_integral":integral,"c_f_exact":c_f_exact(),
            "c_star":lower_constant(),"gaussian_threshold_t":t_G,
            "brownian_laplace_tests":values,"all_assertions_passed":True}


if __name__ == '__main__':
    import json
    print(json.dumps(run_checks(), indent=2,sort_keys=True))

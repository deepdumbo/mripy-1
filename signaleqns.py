
#### Signal Equations
def spgr(t1, tr, angle,m0=1.):
    e1 = np.exp(-tr/t1)
    alpha = angle/180.*np.pi
    return (1-e1)*np.sin(alpha)/(1-e1*np.cos(alpha))


def twospgr(angle=135.,tr=np.array([100, 70, 50, 30, 20, 15.5, 25, 35, 40]), t1a = 30.,t1b = 10.,m0a = .5, m0b = 0.5):
    spgr1 = spgr(t1a,tr,angle)
    spgr2 = spgr(t1b,tr,angle)
    spgrsum = m0a*spgr1+m0b*spgr2
    return spgrsum


def bssfp(t1,tr,angle,te, t2,m0=1.):
    e1 = np.exp(-tr/t1)
    e2 = np.exp(-te/t2)
    alpha = angle/180.*np.pi
    return m0*(np.sqrt(e2*np.sin(alpha)*(1-e1)))/(1-(e1-e2)*np.cos(alpha)-e1*e2)


def ssfpfid(t1,tr,angle,te, t2,m0=1.):
    e1 = np.exp(-tr/t1)
    e2 = np.exp(-tr/t2)
    alpha = angle/180.*np.pi
    p = (1-e1*np.cos(alpha))
    q = e2*(e1-np.cos(alpha))
    r = (1-e2**2)/np.sqrt(p**2-q**2)
    signal = m0*np.tan(alpha/2)*(1-(e1-np.cos(alpha)))
    return signal

def ssfpecho(t1,tr,angle,te, t2,m0=1.):
    e1 = np.exp(-tr/t1)
    e2 = np.exp(-te/t2)
    alpha = angle/180.*np.pi
    p = (1-e1*np.cos(alpha))
    q = e2*(e1-np.cos(alpha))
    r = (1-e2**2)/np.sqrt(p**2-q**2)
    signal = m0*np.tan(alpha/2)*(1-(1-np.cos(alpha)))
    
    return signal

def ssfpboth(t1,tr,angle,te,t2,m0=1.):
    echosig = ssfpecho(t1,tr,angle,te, t2,m0)
    fidsig = ssfpfid(t1,tr,angle,te, t2,m0)
    return echosig+fidsig
    
def Mxyss (t1, tr, t2, te, flipangle, phaseangle, domega=0.):
    e1 = np.exp(-tr/t1)
    e2 = np.exp(-tr/t2)
    alpha = flipangle/180.*np.pi
    theta = phaseangle/180.*np.pi+domega*tr
    f1 = (1.-e1)*e2*sin(alpha)*sin(theta)
    f2 = (1.-e1*cos(alpha))*(1-e2*cos(theta))-e2*(e1-cos(alpha))*(e2-cos(theta))
    f3 = (1.-e1)*e2*sin(alpha)*(cos(theta)-e2)
    f4 = (1.-e1*cos(alpha))*(1-e2*cos(theta))-e2*(e1-cos(alpha))*(e2-cos(theta))
    return f1/f2, f3/f4, f1/f2+1j*f3/f4    

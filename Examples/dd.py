
### Functions ###

# Annihilation operator
def a(n, m):
    if n == m + 1:
        return math.sqrt(n)
    else:
        return 0

# Potential
def potential(x):
    return   h * w * np.power(x, 2) + alpha * np.power(x, 3) + beta * np.power(x, 4)

# Array containing <H_i(x)>

def hermite_array(x):
    norml = ( m * w /(np.p i *h) )* *( 1 /4)
    fr = math.sqrt( m * w /h)
    return np.array([

        norm l *(1 / math.sqrt(2 ** k * math.factorial(k))) * eval_hermite(k, f r *x) * np.exp(-x ** 2 / 2)

        for k in range(0, N)])

def expectation(x, phi):
    normal = np.sum(phi)
    return np.matmul(x.T ,phi ) /normal

def gamma(t):
    np.abs(matmul(psi_kick.T, matmul(U( t *time_step), psi_kick)))

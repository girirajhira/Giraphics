

def lorentz(x0,y0,z0,N, a = 1 , s= 1, b =1 , eps = 0.01):
    X, Y, Z = [x0], [y0], [z0]
    x, y, z = 0,0,0
    for i in range(0,N):
        x += eps*s*(Y[i]- X[i])
        y += eps*X[i]*(a-Z[i])-Y[i]*eps
        z += eps*X[i]*Y[i] - eps*b*Z[i]
        X.append(x)
        Y.append(y)
        Z.append(z)
    return (np.array(X),np.array(Y),np.array(Z))
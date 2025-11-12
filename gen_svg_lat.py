from giraphics.graphing.graph import Graph

G = Graph(70, 70, 12,4,'poster2/bow.svg')


expr = r'\[ q \]'
expr = r'\[ r^2 W(r) \]'
expr = r'\[\partial_\theta P_n \approx \mathbb{E}[W_n(\alpha_i)] \approx \mathbb{E}[\Lambda(|\alpha_i|^2-n)]  \approx \mathbb{E}[\Pi(|\alpha_i|^2-n)]  \]'
expr = r'\[\implies \]'
expr = r'\[\ket{n}\bra{n}  \to W_n(\alpha, \alpha^*)\]'
expr = r'\[\partial_\theta \approx \frac{P}{\epsilon}\]'
expr = r'\[\ket{\psi}\]'
expr = r'\[W(q,p;t) =  W_0(q(t), p(t))\]'
expr = r'\[\nabla W\]'
expr = r'\[\hat{H}(\theta) =\frac{\hbar\theta}{2}\left( \hat{a}^\dagger_1\hat{a}_1 -\hat{a}^\dagger_2\hat{a}_2 \right) \]'
expr = r'\[ F_C\leq F_Q \]'
expr = r'\[ F_C = \sum_n \frac{(\partial_\theta P_n)^2}{P_n}\]'
expr = r'\[ \partial_\theta P_n \]'
expr = r'\[\epsilon = \frac{\int_0^\infty [1 - F(r)]f(r)g(r)/r^2 dr}{\int_0^\infty f(r)g(r)/r^2 dr} \]'
expr = r'\[\mu \to \mu(r) =  \mu\ F(r)  \]'
expr = r'\[ \Gamma \alpha\beta\delta \zeta \sum \int dx  = 1 \ 1 2\ 1 \sum \zeta  \beta \text{long text, so long} \]'

expr = r'\[ A_{10}(x) \]'

expr = r'\[\Delta E  = \Delta E_{0} + \Delta E_{\text{BW}} + \Delta E_{\text{QED}} \]'
# expr = r'\[1s\]'
expr = r'\[^{208}\text{Bi}^{82+}\]'


# expr = r'\[\begin{pmatrix}  0 & 0 & 0  & 0 \\    0 & 0 & 0  & 0 \\   0 & 0 & 0  & 0  \\   0 & 0 & 0  & 0  \end{pmatrix}\]'

G.add_latex(expr, 7,0, scale=.8, cleanup=False)

G.save()




# expr = r'\epsilon  = M_1 \langle R_m ^2 \rangle  + M_2 \langle R_m ^4 \rangle  +  M_3 \langle R_m ^6  \rangle + \dots'
# expr = r'(1-\epsilon)\Delta E'
# expr = r'\ev{R^n_m} \equiv \int_0^\infty |u(R_m)|^2R^n_m\ R^2_m dR_m'
# expr = r'\[\begin{pmatrix}\ev{R_m^2} \\ \ev{R_m^4} \\ \vdots \\ R^{2N}_m \end{pmatrix}\]'
# expr = r'\[\begin{pmatrix} \ev{R_m^2} \\ \vdots \\ \ev{R_m^i} \\ \vdots \\ \ev{R_m^{2N}}  \end{pmatrix}\]'
# expr = r'\[\begin{pmatrix} \epsilon^{(1)} \\ \vdots \\ \epsilon^{(i)} \\ \vdots \\ \epsilon^{(2N)}  \end{pmatrix}\]'
# expr = r'\[M^{-1}\]'
# expr = r'\[M_i\]'
# expr = r'\[\ev{R_m^{5}}}\]'
# expr = r'\[R_m\]'
# expr = r'$$  F_Q = \langle \dot{\psi} | \dot{\psi} \rangle - |\langle \dot{\psi} | \psi \rangle|^2 $$'
# expr = r' V_\theta = \begin{pmatrix} \partial_\theta q \\ \partial_\theta p \end{pmatrix}'
# # expr = r'\[ F_Q = 4\pi\hbar\int_{\mathbb{R}^2} \left( V_\theta \cdot \nabla W \right)^2 dp dq \]'
# expr = r'\[ P_n = \pi \int_{\mathbb{R}^2}\ \  d^2\alpha \]'
# expr = r'\[ W(q,p)\]'
# expr = r'\[F_Q = \mathbb{E}\left[(\ )^2\right]\]'
# expr = r'\[ W_n(\alpha,\alpha^*)\]'
# expr = r'\[ P_n\]'
# expr = r'\[ V_\theta \cdot \nabla W\]'
# expr = r'\[ F_Q =  0\]'
# expr = r'\[ \hbar \to 0 \]'
# expr = r'\[ r = \sqrt{q^2 + p^2} \]'
# expr = r'\[ r^2 W(r) \]'
# expr = r'\[V = \begin{pmatrix} \end{pmatrix} \]'
# expr = r'\[ q \]'

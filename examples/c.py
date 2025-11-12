def plot_surface(self, X, Y, Z, R=np.eye(3), color='Blue', cmap=None, cmesh=None, strokewidth=.05,
                 strokecolor="white", strokeopacity=1, axes=False, box=False, colorbar=False):
    nx, ny = Z.shape
    nf = (nx - 1) * (ny - 1)  # number of faces
    # faces_array = np.zeros((nx - 1, ny - 1, 4, 3))

    points = np.stack((X, Y, Z), axis=-1)

    # Get each of the 4 corners of the quads using slicing
    p0 = points[:-1, :-1]  # top-left
    p1 = points[1:, :-1]  # bottom-left
    p2 = points[1:, 1:]  # bottom-right
    p3 = points[:-1, 1:]  # top-right

    # Stack them into the faces_array: shape (nx-1, ny-1, 4, 3)
    faces_array = np.stack((p0, p1, p2, p3), axis=2)
    # Convert faces to list for easier use
    faces = np.reshape(faces_array, (nf, 4, 3))

    # Centre of the face
    face_centres = np.mean(faces, axis=1)

    maxz, minz = np.max(face_centres[:, -1]), np.min(face_centres[:, -1])
    zinterp = (face_centres[:, -1] - minz) / (maxz - minz)

    # Rotate Faces
    faces = faces @ R.T

    # get draw order, after rotation
    face_centres = np.mean(faces, axis=1)
    view_pos = [0, 0, 1]
    light_pos = np.array([0, 2, 10])

    view_pos = np.sqrt(2 ** 2 + 2 ** 2 + 1 ** 2) * ([0, 0, 1] @ np.eye(3))
    dist_cam = np.sum((view_pos - face_centres) ** 2, axis=1)

    # Reorder according to distance from the camera
    order = np.argsort(dist_cam)[::-1]
    faces = faces[order]
    zinterp = zinterp[order]
    color_range = np.zeros_like(zinterp)

    # Compute edge vectors
    v1 = faces[:, 0, :] - faces[:, 1, :]
    v2 = faces[:, 0, :] - faces[:, 2, :]

    # Compute cross product using np.cross (broadcasted)
    face_normal = np.cross(v1, v2)

    face_reflectance = (face_normal @ light_pos.T)

    maxr, minr = np.max(face_reflectance), np.min(face_reflectance)
    normalised_reflectance = (face_reflectance - minr) / (maxr - minr)
    if cmap is None:
        cmap = generate_cmap([ColourObj('#0000FF'), ColourObj('#0000FF')])

    if cmesh is None:
        cscale, opacscale = cmap(zinterp)
    else:
        cscale, opacscale = cmap(cmesh)
    # if strokeopacity is None:
    #     strokeopacity = [1 for _ in range(nf)]
    # elif not
    #

    # Plot the faces
    for i in range(nf):
        self.area(faces[i, :, 0], faces[i, :, 1],
                  fill_colour=cscale[i], opac=opacscale[i], strokewidth=strokewidth,
                  colour=strokecolor, fill_opacity=opacscale[i])

    if axes:
        centre = [X[0, 0], Y[0, 0], Z[0, 0]] @ R.T
        xaxis = [X[0, -1], Y[0, 0], Z[0, 0]] @ R.T
        yaxis = [X[0, 0], Y[-1, 0], Z[0, 0]] @ R.T
        zaxis = [X[0, 0], Y[0, 0], maxz] @ R.T
        self.draw_arrow(centre[0], centre[1], xaxis[0], xaxis[1], colour='black', strokewidth=0.5, scale=.2)
        self.draw_arrow(centre[0], centre[1], yaxis[0], yaxis[1], colour='black', strokewidth=0.5, scale=.2)
        self.draw_arrow(centre[0], centre[1], zaxis[0], zaxis[1], colour='black', strokewidth=0.5, scale=.2)
    if box:
        b1 = [X[0, 0], Y[0, 0], Z[0, 0]] @ R.T
        b2 = [X[0, -1], Y[0, 0], Z[0, 0]] @ R.T
        b3 = [X[0, 0], Y[-1, 0], Z[0, 0]] @ R.T
        b4 = [X[0, -1], Y[0, 0], Z[0, 0]] @ R.T
        b5 = [X[0, 0], Y[0, 0], Z[0, 0]] @ R.T
        b6 = [X[0, -1], Y[0, 0], Z[0, 0]] @ R.T


    def VectorField(self, X,Y, U,V, gridint=None, scale=0.08, strokewidth=1.25, stroke="white", arrow=True,
                            constColour=False,
                            initColour=[0, 130, 50], endColour=[2, 66, 130],
                            constLength=False, tail_length=1, arrow_scale=1, grid_multiplier=1):
        """
        :type gridint: int
        """

        # if gridint is None:
        #     gridint = []
        #     if self.xlim < 5:
        #         gridint.append(round(2 * self.xlim * grid_multiplier))
        #     else:
        #         gridint.append(2 * self.xlim)
        #     if self.ylim < 5:
        #         gridint.append(round(2 * self.ylim * grid_multiplier))
        #     else:
        #         gridint.append(2 * self.ylim)

        nx, ny = X.shape
        epsx = self.xlim / nx
        epsy = self.ylim / ny

        fl = 1
        if not constLength:
            fl = 0
        if constColour:
            if not arrow:
                arrow_scale = 0

            for i in range(0, nx):
                for j in range(0,ny):
                    x, y = X[i,j], Y[i,j]
                    fx, fy = U[i,j], V[i,j]
                    x2 = self.tranx(x + (fx) * tail_length)
                    y2 = self.trany(y + (fy) * tail_length)
                    if abs(fx) <= 0.05 and abs(fy) <= 0.05:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=stroke,
                                            strokewidth=strokewidth, scale=arrow_scale)

        else:
            cl = linear(initColour, endColour)
            if not arrow:
                arrow_scale = 0
            L = []
            for i in range(0, nx):
                for j in range(0, ny):
                    x, y = X[i,j], Y[i,j]
                    fx, fy = U[i,j], V[i,j]
                    L.append(norm([fx, fy]))
            M = max(L)
            for i in range(0, nx):
                for j in range(0,ny):
                    x, y = X[i,j], Y[i,j]
                    fx, fy = U[i,j], V[i,j]
                    fn = norm([fx,fy]) * fl * nx / (2 * self.xlim) if norm([fx,fy]) * fl != 0 else 1
                    x2 = self.tranx(x + (fx) * tail_length / fn)
                    y2 = self.trany(y + (fy) * tail_length / fn)
                    if fx == 0 and fy == 0:
                        pass
                        # self.svg.draw_circ(self.tranx(x), self.trany(y), scale * 70, fill=vec_to_hex(endColour),
                        #                    strokewidth=0)
                    else:
                        self.svg.draw_arrow(self.tranx(x), self.trany(y), x2, y2, stroke=cl((norm([fx,fy])) / M),
                                            strokewidth=strokewidth, scale=arrow_scale)

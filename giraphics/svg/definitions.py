import numpy as np

def linear_gradient(id, start_color="red", start_opacity = 1,stop_color="yellow", stop_opacity = 1,
                    dir=np.array([[0,0],[100,0]]), start_offset=0, stop_offset = 100):
    dir = np.array(dir)
    txt = f'''
    <defs>
        <linearGradient id="{id}" x1="{dir[0,0]}%" y1="{dir[0,1]}%" x2="{dir[1,0]}%" y2="{dir[1,1]}%">
          <stop offset="{start_offset}%" stop-color="{start_color}" stop-opacity="{start_opacity}" />
          <stop offset="{stop_offset}%" stop-color="{stop_color}" stop-opacity="{stop_opacity}" />
        </linearGradient >
    </defs>
    '''
    return txt

def radial_gradient(id, start_color="red", start_opacity = 1,stop_color="purple", stop_opacity = 1,
                    cx=0, cy=0, r = 2, fx = 100, fy=100, start_offset=0, stop_offset = 100):
    txt = f'''
    <defs>
        <radialGradient id="{id}" cx="{cx}%" cy="{cy}%" r="{r}%" fx="{fx}%" fy="{fy}%">
          <stop offset="{start_offset}%" stop-color="{start_color}" stop-opacity="{start_opacity}" />
          <stop offset="{stop_offset}%" stop-color="{stop_color}" stop-opacity="{stop_opacity}" />
        </radialGradient>
    </defs>
    '''
    return txt
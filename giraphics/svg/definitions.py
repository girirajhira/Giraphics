def linear_gradient(id, start_color=[255,255,0], start_opacity = 1,stop_color=[255,255,0], stop_opacity = 1, ):
    txt = f'''
    <defs>
    <linearGradient id = "{id}", x1 = "0%", y1 = "0%", x2 = "100%" y2 = "0%">
    <stop offset = "0%" style = "stop-color:rgb({start_color[0],start_color[1],start_color[2]}); stop-opacity:{start_opacity}"/>
    <stop offset = "100%" style = "stop-color:rgb({stop_color[0], stop_color[1], stop_color[2]});stop-opacity:{stop_opacity}"/>
    </linearGradient >
    </defs>
    '''
    return txt

def radial_gradient(id, start_color=[255,255,0], start_opacity = 1,stop_color=[255,255,0], stop_opacity = 1, ):
    txt = f'''
    <defs>
    <linearGradient id = "{id}", x1 = "0%", y1 = "0%", x2 = "100%" y2 = "0%">
    <stop offset = "0%" style = "stop-color:rgb({start_color[0],start_color[1],start_color[2]}); stop-opacity:{start_opacity}"/>
    <stop offset = "100%" style = "stop-color:rgb({stop_color[0], stop_color[1], stop_color[2]});stop-opacity:{stop_opacity}"/>
    </linearGradient >
    </defs>
    '''
    return txt

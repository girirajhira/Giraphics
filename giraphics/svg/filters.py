def lighting(id,pos, colour="white", spec_exp=20, type="SourceGraphic"):
    '''
    Defines a lighting effect in svg
    :param id: name
    :param pos: position of line
    :param colour: of light
    :param spec_exp: specular exponent
    :param type: SourceGraphic or SourceAlpha
    :return:
    '''
    txt = f'''
    <filter id="{id}">
    <feSpecularLighting
      result="specOut"
      specularExponent="20"
      lighting-color="{colour}">
      <fePointLight x="{pos[0]}" y="{pos[1]}" z="{pos[2]}" />
    </feSpecularLighting>
    <feComposite
      in="{type}"
      in2="{id}"
      operator="arithmetic"
      k1="0"
      k2="1"
      k3="1"
      k4="0" />
  </filter>
  <circle cx="110" cy="110" r="100" style="filter:url(#filter)" />"
  '''
    return txt

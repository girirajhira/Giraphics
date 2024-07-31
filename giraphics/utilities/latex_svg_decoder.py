from xml.dom import minidom


def get_svg_symbol_ids(svg_code):
    '''
    :param svg_code:
    :return:
    '''
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('id') for symb in doc.getElementsByTagName('symbol')]
    doc.unlink()
    return symbols


def get_svg_clip_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('id') for symb in doc.getElementsByTagName('clipPath')]
    doc.unlink()
    return symbols

# def get_svg_glyph_ids(svg_code):
#     doc = minidom.parseString(svg_code)
#     symbols = [symb.getAttribute('id') for symb in doc.getElementsByTagName('glyph')]
#     doc.unlink()
#     return symbols


def get_g_elements_ids(svg_code):
    '''
    Find id of <g> tags
    :param svg_code:
    :return:
    '''
    doc = minidom.parseString(svg_code)
    g_elements = doc.getElementsByTagName('g')
    ids = [g.getAttribute('id') for g in g_elements if g.hasAttribute('id')]
    doc.unlink()
    return ids
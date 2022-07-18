from xml.dom import minidom


def get_svg_symbol_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('id') for symb in doc.getElementsByTagName('symbol')]
    doc.unlink()
    return symbols


def get_svg_clip_ids(svg_code):
    doc = minidom.parseString(svg_code)
    symbols = [symb.getAttribute('id') for symb in doc.getElementsByTagName('clipPath')]
    doc.unlink()
    return symbols



def get_name(text, r_ext = False, underscore = True) -> str:
    if '/' in text:
        text = text.split('/')[-1]

    if r_ext:
        if '.' in text:
            text = text.split('.')[0]

    if underscore:
        text = text.replace('-', '_')

    text = text.replace(' ', '')

    return text
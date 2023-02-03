def article_shorten(text):
    text = str(text).rstrip()

    if len(text) <= 25:
        return text

    short_text = ''
    for word in text.split(' '):
        if len(short_text + f'{word}...') <= 25:
            short_text += f'{word} '
        else:
            short_text = f'{short_text.rstrip()}...'
            break

    return short_text

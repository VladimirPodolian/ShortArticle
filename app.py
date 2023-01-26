from textwrap import shorten


def article_shorten(text):
    """ Python has internal realisation for solving this task """
    return shorten(str(text), width=25, placeholder='...')

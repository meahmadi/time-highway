from settings import BASE_URL


def url(u):
    if BASE_URL == '/':
        return u
    return BASE_URL + u

class DevelopmentConfig(object):
    DATABASE_URI = \
        "postgresql://richvincent:f5742db8d0c44e93d57bae180cce6053@localhost:5432/posts"
    DEBUG = True


class TestingConfig(object):
    DATABASE_URI = \
        "postgresql://richvincent:f5742db8d0c44e93d57bae180cce6053@localhost:5432/posts-test"
    DEBUG = True

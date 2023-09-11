


class BaseConfig:
    '''Base Configuration'''
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 12          # 2^log_rounds computational iterations for hashing pw. Higher values means more secure but more computational resources. Security-performance tradeoff.
    


class DevelopmentConfig(BaseConfig):
    '''Development Configuration'''
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
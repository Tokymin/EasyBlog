import os

here = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    配置基类
    """
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'GeekTeam'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = 'toky_eternity@126.com'
    FLASK_POSTS_PER_PAGE = 15
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'toky_eternity@126.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'ilyw5730'
    FLASK_MAIL_SENDER = 'GeekTeam<toky_eternity@126.com>'
    FLASK_MAIL_SUBJECT_PREFIX = '[WeGeek]'
    UPLOADED_FOLDER = os.getcwd() + "\\app\static\headimg"  # 设置保存的位置 上传到当前 目录下面
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024


class DevelopmentConfig(Config):
    """
    开发状态
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-dev.sqlite')


class TestingEmptyConfig(Config):
    """
    测试状态：数据库无数据
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-test-empty.sqlite')


class TestingFullConfig(TestingEmptyConfig):
    """
    测试状态：数据库有数据
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-test-full.sqlite')


class ProductionConfig(Config):
    """
    生产状态
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-prod.sqlite')


class HerokuConfig(Config):
    """
    Heroku平台配置
    """
    SSL_DISABLE = False  # 启动 SLL 安全检查
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        # 将日志输出到 stderr
        import logging
        file_handler = logging.StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        # 处理代理服务器首部。在 Heroku 中，客户端没有直接托管程序，而是连接反向服务
        # 代理器，最后把请求重定向到程序上。这种连接方式中，只在代理服务器中运行 SSL 模式。
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


config = {'development': DevelopmentConfig, 'testing-empty': TestingEmptyConfig, 'testing-full': TestingFullConfig,
          'production': ProductionConfig, 'heroku': HerokuConfig, 'default': DevelopmentConfig}

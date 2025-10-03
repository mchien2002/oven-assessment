class DbRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    @staticmethod
    def db_for_read(model, **hints):
        if hasattr(model, 'Router'):
            return model.Router.db_name
        return "default"

    @staticmethod
    def db_for_write(model, **hints):
        if hasattr(model, 'Router'):
            return model.Router.db_name
        return "default"

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        return True

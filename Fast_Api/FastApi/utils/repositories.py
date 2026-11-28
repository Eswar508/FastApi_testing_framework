from FastApi.utils.helper_fun import STORAGE_DIR,get_data,post_data
class JsonRepository:
    path=STORAGE_DIR/"user_registry.json"
    @classmethod
    def get_all(cls):
        return get_data(cls.path)
    @classmethod
    def save_all(cls,data):
        post_data(cls.path,data)
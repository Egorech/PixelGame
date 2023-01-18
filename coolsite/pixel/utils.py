menu = [{'title': "Категории", 'url_name': "categorie"},
        {'title': "Лучшее", 'url_name': "best"},
        {'title': "О нас", 'url_name': "about"}]

class DataMixin:
    def get_user_content(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
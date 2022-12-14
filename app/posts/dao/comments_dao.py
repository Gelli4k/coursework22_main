import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def _load_comments(self):
        """ Загружаем комментарии """
        with open(self.path, "r", encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_by_posts_pk(self, post_pk):
        """ Получаем комментарий к определенному посту """

        comments = self._load_comments()
        comments_by_pk = []
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_by_pk.append(comment)
        return comments_by_pk

import pytest

from coursework2.coursework2.coursework22.app.posts.dao.comments_dao import CommentsDAO


class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO("tests/mock/comments.json")

    @pytest.fixture
    def key_expected(self):
        return {"post_pk", "commenter_name", "pk"}

    # Получение комментариев к посту

    def test_get_by_post_pk_check_type(self, comments_dao):
        comments = comments_dao.get_by_posts_pk(1)
        assert type(comments) == list, "Результат должен быь списком"
        assert type(comments[0]) == dict, "Результат должен быь словарем"

    def test_get_by_post_pk_check_keys(self, comments_dao, key_expected):
        comment = comments_dao.get_by_posts_pk(1)[8]
        comment_keys = set(comment.keys())
        assert comment_keys == key_expected, "Список ключей не соответствует"

    parameters_for_posts_and_comments = [
        (1, {1, 2}),
        (2, {7}),
        (0, set()),
    ]

    @pytest.mark.parametrize("post_pk, correct_comments_pks", parameters_for_posts_and_comments)
    def test_get_by_post_pk_check_match(self, comments_dao, post_pk, correct_comments_pks):
        comments = comments_dao.get_by_posts_pk(post_pk)
        comment_pks = set([comment["pk"] for comment in comments])
        assert comment_pks == correct_comments_pks, f"не совпадают pk комментов для поста {post_pk}"

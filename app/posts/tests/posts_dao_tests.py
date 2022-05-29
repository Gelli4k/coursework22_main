import os


import pytest
from coursework2.coursework2.coursework2.app.posts.dao.posts_dao import PostsDAO


class TestPostDao:
    """ Получение всех постов """

    @pytest.fixture
    def posts_dao(self):
        print(os.getcwd())
        return PostsDAO("data/posts.json")


@pytest.fixture
def key_expected():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def get_all_check_type(posts_dao):
    posts = posts_dao.get_all()
    assert type(posts) == list, "Список постов должен быть списком"
    assert type(posts[0]) == dict, "Каждый пост должен быть словарем"


def test_get_all_has_keys(posts_dao, keys_expected):
    posts = posts_dao.get.all()
    first_post = posts[0]
    first_post_keys = set(first_post.keys())
    assert first_post_keys == keys_expected, "Полученные ключи неверны"


""" Получение одного поста """


def test_get_one_check_type(posts_dao):
    post = posts_dao.get_by_pk(1)
    assert type(post) == dict, "Пост должен быть словарем"


def test_get_one_has_keys(posts_dao, keys_expected):
    post = posts_dao.get_by_pk(1)
    post_keys = set(post.keys())
    assert post_keys == keys_expected, "Полученные ключи неверны"


parameters_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.parametrize('post_pk', parameters_to_get_by_pk)
def test_get_one_check_type_has_correct_pk(posts_dao, post_pk):
    post = posts_dao.get_by_pk(post_pk)
    assert post["pk"] == post_pk, "Номер получаемого поста не соответствует номеру"


# Поиск

def test_by_search_check_type(posts_dao):
    posts = posts_dao.search("a")
    assert type(posts) == list, "Результат поиска должен быть списком"
    assert type(posts[0]) == dict, "Элементы найденные поиском должны быть словарем"


def test_search_has_keys(posts_dao, keys_expected):
    post = posts_dao.search("a")[0]
    post_keys = set(post.keys())
    assert post_keys == keys_expected, "Полученные ключи неверны"


queries_and_responses = [
    ("0000000", []),
    ("еда", [1]),
    ("дом", [2, 7, 8]),
    ("Дом", [2, 7, 8]),
    ("а", list(range(1, 8 + 1)))
]


@pytest.mark.parametrize("query, post_pks", queries_and_responses)
def test_search_correct_match(posts_dao, query, post_pks):
    posts = posts_dao.search(query)

    pks = []
    for post in posts:
        pks.append(post["pk"])

    assert pks == post_pks, f"Неверный поиск по запросу {query}"


# Получение по пользователю

def test_get_by_user_check_type(posts_dao):
    posts = posts_dao.get_by_user("leo")
    assert type(posts) == list, "Результат поиска по пользователю должен быть списком"
    assert type(posts[0]) == dict, "Элементы, найденные поиском по пользователю должны быть словарем"


def test_get_by_user_has_keys(posts_dao, keys_expected):
    post = posts_dao.get_by_user("leo")[0]
    post_keys = set(post.keys())
    assert post_keys == keys_expected, "Полученные ключи неверны"


parameters_to_get_by_user = [
    ("leo", [1, 5]),
    ("hank", [3, 7]),
    ("johnny", [2, 6]),
    ("lll", [])
]


@pytest.mark.parametrize("user_name, post_pks", parameters_to_get_by_user)
def test_get_by_user_correct_match(posts_dao, user_name, post_pks):
    posts = posts_dao.get_by_user(user_name)

    pks = []
    for post in posts:
        pks.append(post["pk"])

    assert pks == post_pks, f"Неверный список постов для пользователя {user_name}"

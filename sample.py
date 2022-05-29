from pprint import pprint as pp
from coursework2.coursework2.coursework2.app.posts.dao.posts_dao import PostsDAO

d = PostsDAO("data/posts.json")

p = d.get_by_pk(1)

pp(p)

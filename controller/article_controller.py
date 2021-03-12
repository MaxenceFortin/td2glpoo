import re

from model.dao.article_dao import ArticleDAO
from exceptions import Error, InvalidData


class ArticleController:
    """
    Article actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_articles(self):
        with self._database_engine.new_session() as session:
            articles = ArticleDAO(session).get_all()
            articles_data = [member.to_dict() for member in articles]
        return articles_data

    def get_article(self, article_id):
        with self._database_engine.new_session() as session:
            article = ArticleDAO(session).get(article_id)
            article_data = article.to_dict()
        return article_data

    def create_article(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                article = ArticleDAO(session).create(data)
                article_data = article.to_dict()
                return article_data
        except Error as e:
            # log error
            raise e

    def update_article(self, article_id, article_data):

        self._check_profile_data(article_data, update=True)
        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            article = article_dao.get(article_id)
            article = article_dao.update(article, article_data)
            return article.to_dict()

    def delete_article(self, article_id):

        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            article = article_dao.get(article_id)
            article_dao.delete(article)

    def search_article(self, name):

        # Query database
        with self._database_engine.new_session() as session:
            article_dao = ArticleDAO(session)
            article = article_dao.get_by_name(name)
            return article.to_dict()

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        mandatories = {
            'name': {"type": str, "regex": name_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)

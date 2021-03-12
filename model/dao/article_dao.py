from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.member import Member
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class ArticleDAO(DAO):
    """
    Article Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Article.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Article).order_by(Article.firstname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, firstname: str, lastname: str):
        try:
            return self._database_session.query(Member).filter_by(firstname=firstname, lastname=lastname)\
                .order_by(Member.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            member = Member(name=data.get('name'), description=data.get('description'), price=data.get('price'))
            self._database_session.add(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Article already exists")
        return member

    def update(self, member: Member, data: dict):
        if 'name' in data:
            member.firstname = data['name']
        if 'description' in data:
            member.lastname = data['description']
        if 'price' in data:
            member.email = data['price']
        try:
            self._database_session.merge(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return member

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))

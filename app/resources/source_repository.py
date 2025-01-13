from re import match, findall
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.database import db_session
from app.models import SourceRecord


class SourceRepository:
    model = SourceRecord
    url_pattern = r"(http|https):\/\/([a-z0-9-]+\.)+[a-z]+\/.*"
    domain_pattern = r"(http|https):\/\/(([a-z0-9-]+\.)+[a-z]+)\/"

    def create_instance(self, data):
        url = data.get('domain')
        self.validate_url(url)
        source = SourceRecord(domain=self.get_domain(url), verdict=data.get('verdict'))
        try:
            db_session.add(source)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise RuntimeError(str(e))
        return source

    def validate_url(self, url):
        if not match(self.url_pattern, url):
            raise ValidationError("Invalid url pattern")

    def get_domain(self, url):
        match = findall(self.domain_pattern, url)
        return match[0][1]   if match else None

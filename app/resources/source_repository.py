from re import match, findall
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.database import db_session
from app.models import SourceRecord


class SourceRepository:
    model = SourceRecord
    url_pattern = r"(http|https):\/\/([a-z0-9-]+\.)+[a-z]+\/.*"
    domain_pattern = r"(http|https):\/\/(([a-z0-9-]+\.)+[a-z]+)\/"

    def create_instance(self, data):
        url = data.get('domain')
        self.validate_url(url)
        domain = self.get_domain(url)

        existing_instance = self.get_instance(domain)
        if existing_instance:
            raise ValidationError("A source record already exists for this domain.")

        source = SourceRecord(domain=domain, verdict=data.get('verdict'))
        try:
            db_session.add(source)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise RuntimeError(str(e))
        return source

    def get_instance(self, domain):
        instance = db_session.query(SourceRecord).filter_by(domain=domain).first()
        return instance

    def delete_instance(self, domain):
        instance = self.get_instance(domain)
        if not instance:
            raise ValidationError("A source record with this domain does not exist.")
        db_session.delete(instance)
        db_session.commit()

    def validate_url(self, url):
        if not match(self.url_pattern, url):
            raise ValidationError("Invalid url pattern")

    def get_domain(self, url):
        match = findall(self.domain_pattern, url)
        return match[0][1]  if match else None

from unittest import TestCase
from app.app import create_app
from app.database import db_session
from app.models import SourceRecord


class CreateSourceTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update({
            "TESTING": True,
        })
        self.client = self.app.test_client()

    def test_create_source(self):
        data = {"domain": "https://flask.palletsprojects.com/en/stable/testing/", "verdict": "malware"}
        response = self.client.post("/sources", data=data)
        response_data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response_data["domain"] in data["domain"])
        self.assertEqual(response_data["verdict"], data["verdict"])
        query = SourceRecord.query.all()
        self.assertEqual(len(query), 1)


    def tearDown(self):
        db_session.query(SourceRecord).delete()
        db_session.commit()
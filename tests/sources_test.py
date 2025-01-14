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
        self.test_data = {"domain": "https://flask.palletsprojects.com/en/stable/testing/", "verdict": "malware"}
        self.domain = "flask.palletsprojects.com"

    def test_create_source(self):
        response = self.client.post("/sources", data=self.test_data)
        response_data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response_data["domain"] in self.test_data["domain"])
        self.assertEqual(response_data["verdict"], self.test_data["verdict"])
        query = SourceRecord.query.all()
        self.assertEqual(len(query), 1)

    def test_get_source(self):
        self.client.post("/sources", data=self.test_data)
        response = self.client.get(f"/sources/{self.domain}")
        response_data = response.get_json()
        print(response_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["domain"], self.domain)
        self.assertEqual(response_data["verdict"], self.test_data["verdict"])

    def test_delete_source(self):
        response = self.client.delete(f"/sources/{self.domain}")
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        get_response = self.client.get(f"/sources/{self.domain}")
        self.assertEqual(get_response.status_code, 404)


    @classmethod
    def tearDownClass(cls):
        db_session.query(SourceRecord).delete()
        db_session.commit()
import uuid
from django.core.management import call_command
from unittest import skip
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

class ApiTestCases(APITestCase):
    api_url = "/api/"

    def setUp(self):
        """
        Setup tests for membership by registering a user and then
        logging in that user
        """
        self.register_data = {
            "data": 
                [ 
                    {"id": 3, "passenger": 56}, 
                    {"id": 5, "passenger": 14}, 
                    {"id": 6, "passenger": 18}, 
                    {"id": 8, "passenger": 30}, 
                    {"id": 12, "passenger": 65}, 
                    {"id": 32, "passenger": 21}, 
                    {"id": 15, "passenger": 16}, 
                    {"id": 18, "passenger": 45}, 
                    {"id": 14, "passenger": 12}, 
                    {"id": 17, "passenger": 18}
                ]
            }

    def test_no_membership_objects(self):
        """
        Test to verify api
        """
        response = self.client.post(self.api_url,self.register_data,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

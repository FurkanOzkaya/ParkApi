

from django.urls import reverse
from rest_framework import status
from app.models import ParkModel
from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.


class TestParkApi(APITestCase):
    """
        Park Api Test Cases
    """
    def setUp(self):
        ParkModel.objects.create(latitude=38.2377362, longitude=27.831231270, comment="Create data 1 Comment", created_by="Test User")
        ParkModel.objects.create(latitude=32.2127362, longitude=23.831231270, comment="Create data 2 Comment", created_by="Test User")
        ParkModel.objects.create(latitude=33.2377362, longitude=28.831231270, comment="Create data 3 Comment",created_by="Test User")
        ParkModel.objects.create(latitude=34.2377362, longitude=25.831231270, comment="Create data 4 Comment",created_by="Test User")

    def test_case_add_park_areas(self):
        url = '/api/add_park_areas'
        data = {"latitude":38.677362,
                "longitude":27.861270,
                "comment":"Test Case Comment",
                "created_by":"Test Case User"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_case_display_close_areas(self):
        url = '/api/display_close_areas'
        data = {"latitude":38.677362,
                "longitude":27.861270,
                "distance":8000}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_get_spesific_park_area(self):
        url = '/api/get_spesific_park_areas/1'
        data = {"id":1,
                "latitude":38.2377362, 
                "longitude":27.831231270,
                "comment":"Create data 1 Comment",
                "created_by":"Test User"}
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
    
    def test_case_delete_areas(self):
        url = '/api/delete_areas/1'
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
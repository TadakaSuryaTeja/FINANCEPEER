from unittest import mock

from django.test import TestCase

# Create your tests here.
from customerapp.views.login import Login


@mock.patch('customerapp.views.login.render')
class test_login(TestCase):

    def test_login_get(self, mock_render):
        mock_request = mock.Mock()
        mock_self = mock.Mock()
        Login.get(mock_self, mock_request)
        mock_render.assert_called_with(mock_request, 'customerapp/login.html')

# TODO Need to add unittests

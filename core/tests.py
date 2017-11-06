from unittest import TestCase
from tciminne.models import Client, Token, Score, drop_all

from core import app
from core import views  # noqa: F401


class BaseTest(TestCase):
    def setUp(self):
        self.token = Token(client=Client(name='Testy').save(), language='en',
                           provider='a1b2c3').save()
        self.client = app.test_client()
        self.client.testing = True

    def tearDown(self):
        drop_all()


class TCIAccessTest(BaseTest):
    def test_access_without_token_displays_error(self):
        result = self.client.get('/', follow_redirects=True)
        self.assertEqual(result.status_code, 401)
        self.assertIn('Could not load test', result.get_data(as_text=True))

    def test_wrong_token_displays_error(self):
        result = self.client.get('/wrongtoken/', follow_redirects=True)
        self.assertEqual(result.status_code, 401)
        self.assertIn('Could not load test', result.get_data(as_text=True))


class TciTest(BaseTest):
    def test_access_should_display_questions(self):
        result = self.client.get(f'/{self.token.key}/run/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Definitely True', result.get_data(as_text=True))

    def test_post_data(self):
        data = {'token': self.token.key,
                'answers': '2,3,4',
                'times': '1000,1500,1600'
                }
        self.assertEqual(Score.objects.count(), 0)
        result = self.client.post('/end/', data=data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'completing the test', result.data)
        self.assertEqual(Score.objects.count(), 1)
        score = Score.objects.first()
        self.assertEqual(score.answers, [2, 3, 4])
        self.assertEqual(score.times, [1000, 1500, 1600])
        token = Token.objects.first()
        self.assertEqual(score.client, token.client)
        self.assertFalse(token.is_valid())

    def test_run_tci_with_page_reload(self):
        self.client.get(f'/{self.token.key}/')
        result = self.client.get(f'/{self.token.key}/')
        self.assertIn(b'Start the test', result.data)

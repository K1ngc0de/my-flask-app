import os
import unittest
from app import app  # импортируем ваше приложение из файла app.py

class FlaskAppTestCase(unittest.TestCase):
    
    # Устанавливаем тестовую среду
    def setUp(self):
        # Устанавливаем переменные окружения
        os.environ["PORT"] = "5002"
        self.app = app.test_client()
        self.app.testing = True

    # Тестируем домашнюю страницу
    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"index.html", response.data)

if __name__ == "__main__":
    unittest.main()

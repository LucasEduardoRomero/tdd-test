import unittest

from app import web_app


class TestHome(unittest.TestCase):

        def setUp(self):
            app = web_app.test_client()
            self.response = app.get('/')

        def test_get(self):            
            self.assertEqual(200, self.response.status_code)

        def test_content_type(self):
            self.assertIn('text/html', self.response.content_type)

        def test_content(self):
            self.assertIn('<h2>Olá, Bem vindo</h2>', self.response.data.decode('utf-8'))
            self.assertIn('<h3>Você está visitando o TDD-Test !</h3>', self.response.data.decode('utf-8'))

        def test_bootstrap_css(self):
            response_str = self.response.data.decode('utf-8')
            self.assertIn('bootstrap.min.css', response_str)


        def test_link(self):            
            response_str = self.response.data.decode('utf-8')
            self.assertIn('href="https://github.com/LucasEduardoRomero"', response_str)
            self.assertIn('>Me siga no Github</a>', response_str)

        def test_profile_img(self):
            """
            usando regex pois o response.decode(utf-8) tem '\n' e isso altera o resultado
            """
            response_str = self.response.data.decode('utf-8')
            #self.assertRegex(response_str, '[\\<img.,-]+\\s+[\\src=".,-]+=',)
            self.assertIn('<img', response_str)

if __name__ == '__main__':
    unittest.main()
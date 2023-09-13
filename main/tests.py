from django.test import TestCase,Client
# from django.urls import reverse

# from main.models import Product

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_item_stock_is_exist(self): # Periksa apakah stok buku masih ada
        response = Client().get('/main/')
        self.assertNotEqual(response.context['amount1'], 0)
        self.assertNotEqual(response.context['amount2'], 0)
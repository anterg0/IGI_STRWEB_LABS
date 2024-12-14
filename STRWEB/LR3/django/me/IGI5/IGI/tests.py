from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from .models import Article, Product, PromoCode, FAQModel, Job, Review
from .forms import ArticleForm
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse

class ModelTestCase(TestCase):
    def test_article_creation(self):
        article = Article.objects.create(
            title="Test Article",
            full_text="This is a test article. It has multiple sentences.",
            date=timezone.now()
        )
        self.assertEqual(article.first_sentence, "This is a test article.")

    def test_product_str(self):
        product = Product.objects.create(name="Test Product", price=99.99)
        self.assertEqual(str(product), "Test Product")

    def test_promo_code_discount_validation(self):
        with self.assertRaises(Exception):
            PromoCode.objects.create(name="Invalid Promo", discount=1.5)  # Discount should be 1 or 0.XX

    def test_faq_str(self):
        faq = FAQModel.objects.create(question="Test Question?", answer="Test Answer.")
        self.assertEqual(str(faq), "Test Question?")

    def test_job_get_absolute_url(self):
        job = Job.objects.create(job_name="Test Job", description="Test description.")
        self.assertEqual(job.get_absolute_url(), f"/jobs/{job.id}/")

    def test_review_rating_validation(self):
        with self.assertRaises(Exception):
            Review.objects.create(review_text="Test review", rating=6)  # Rating should be between 1 and 5

class NewsDetailViewTestCase(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            full_text="This is a test article.",
            date=timezone.now()
        )

    def test_news_detail_view_status_code(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view_context(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertTrue('article' in response.context)
        self.assertEqual(response.context['article'], self.article)

class ArticleFormTestCase(TestCase):
    def test_article_form_valid_data(self):
        form_data = {
            'title': "Test Article",
            'full_text': "This is a test article.",
            'date': timezone.now().date()
        }
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_article_form_invalid_data(self):
        form_data = {
            'title': "",  # Empty title
            'full_text': "This is a test article.",
            'date': timezone.now().date()
        }
        form = ArticleForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_get(self):
        self.client.logout()  # Ensure user is logged out
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):
        self.client.logout()
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('home'))  # Redirect to home after successful login
        self.assertTrue(self.client.login(username='testuser', password='testpassword'))

    def test_login_view_post_failure(self):
        self.client.logout()
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(self.client.login(username='testuser', password='wrongpassword'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Некорректные данные')

class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_logout_view(self):
        response = self.client.get(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('home'))  # Redirect to home after logout
        self.assertFalse(self.client.login(username='testuser', password='testpassword'))  # Check if user is logged out

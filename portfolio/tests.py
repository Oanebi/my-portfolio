
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_returns_successful_response(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "portfolio/home.html")

    def test_homepage_displays_profile_headline(self):
        response = self.client.get(reverse("home"))
        self.assertContains(
            response,
            "From understanding the Earth to building intelligent solutions.",
        )

    def test_homepage_displays_developer_interests(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Full-stack development")
        self.assertContains(response, "AI-native engineering")

    def test_homepage_displays_geology_background(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "background in geology")

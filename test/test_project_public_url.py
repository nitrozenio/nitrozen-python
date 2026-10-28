import unittest

from nitrozenio.models.project import Project


class TestProjectPublicUrl(unittest.TestCase):
    def test_public_url_is_parsed(self):
        p = Project.from_dict({"id": 1, "slug": "textproxyz", "public_url": "https://nitrozen.io/c/textproxyz"})
        self.assertEqual(p.public_url, "https://nitrozen.io/c/textproxyz")

    def test_public_url_is_read_only_on_serialize(self):
        p = Project.from_dict({"id": 1, "public_url": "https://nitrozen.io/c/textproxyz"})
        self.assertNotIn("public_url", p.to_dict())


if __name__ == "__main__":
    unittest.main()

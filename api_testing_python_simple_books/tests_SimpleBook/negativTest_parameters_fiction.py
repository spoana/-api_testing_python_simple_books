import unittest

from requests_SimpleBook.query_parameters_request import BooksApi


class BooksTests(unittest.TestCase):


    def setUp(self) -> None:
        self.books = BooksApi()


    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="fiction", limit="4")
        expected_number = 2
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
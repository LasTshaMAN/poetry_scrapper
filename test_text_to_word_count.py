from unittest import TestCase

import nltk

from processing import text_to_word_count, filter_stop_words


class TestProcessing(TestCase):
    input_text = \
        'Once upon a midnight dreary, while I pondered, weak and weary, ' \
        'while once upon midnight —\n' \
        'weak and weary.'

    def test_filter_stop_words(self):
        words = nltk.word_tokenize(self.input_text)
        exp = ['Once', 'upon', 'midnight', 'dreary', 'I', 'pondered', 'weak', 'weary', 'upon', 'midnight', 'weak', 'weary']

        act = filter_stop_words(words)

        self.assertListEqual(exp, act)

    def test_text_to_word_count(self):
        exp = {
            'upon': 2,
            'midnight': 2,
            'weak': 2,
            'weary': 2,
            'dreary': 1,
            'pondered': 1,
        }

        act = text_to_word_count(self.input_text)

        self.assertDictEqual(exp, act)

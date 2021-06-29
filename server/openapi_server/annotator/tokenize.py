from typing import Tuple
from nltk import TreebankWordTokenizer
from openapi_server.annotator.label_spans import Tokens, Spans


class Tokenizer:
    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()

    def get_tokens_and_spans(self, text: str) -> Tuple[Tokens, Spans]:
        """Get a list of tokens & a list of labels (one for each token)
        """
        # Prevent bugging out on empty text
        if text == '':
            return [''], [(0, 0)]

        # Get tokens and spans for non-empty text
        tokens = self.tokenizer.tokenize(text)
        spans = self.tokenizer.span_tokenize(text)
        return tokens, spans

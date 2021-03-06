from openapi_server.annotator.label_spans import label_tokens


TEXT = "Hi my name is John Smith"
SPANS = [(0, 2), (3, 5), (6, 10), (11, 13), (14, 18), (19, 24)]
TOKENS = [TEXT[start:end] for start, end in SPANS]
ANNOTATION_SET_ONE = [{'TYPE': 'AGE', 'start': 14, 'end': 18},
                      {'TYPE': 'AGE', 'start': 19, 'end': 24}]
ANNOTATION_SET_TWO = [{'TYPE': 'DATE', 'start': 14, 'end': 24}]
OVERLAPPING_ANNOTATION_SET_ONE = [
    {'TYPE': 'DATE', 'start': 14, 'end': 20},
    {'TYPE': 'AGE', 'start': 19, 'end': 24},
]
OVERLAPPING_ANNOTATION_SET_TWO = [
    {'TYPE': 'AGE', 'start': 14, 'end': 20},
    {'TYPE': 'DATE', 'start': 19, 'end': 24},
]


def test_label_span_one():
    labels = label_tokens(TOKENS, SPANS, ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_two():
    labels = label_tokens(TOKENS, SPANS, ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_three():
    labels = label_tokens(TOKENS, SPANS, OVERLAPPING_ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_four():
    labels = label_tokens(TOKENS, SPANS, OVERLAPPING_ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1]

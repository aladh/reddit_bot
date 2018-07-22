from src.word_filter import WordFilter


def test_returns_true_if_blocked_word_is_present():
    word_filter = WordFilter(['apple', 'pear'])
    assert word_filter.is_blocked('i ate an apple') == True
    assert word_filter.is_blocked('i like pears more') == True
    assert word_filter.is_blocked('i ate an orange') == False


def test_handles_different_case():
    word_filter = WordFilter(['apple'])
    assert word_filter.is_blocked('i ate an Apple') == True

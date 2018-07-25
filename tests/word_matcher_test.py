from src.word_matcher import WordMatcher

t = WordMatcher(['foo', 'bar'])


def test_returns_true_if_trigger_present():
    assert t.is_present('le foo') == 'foo'
    assert t.is_present('chocolate bar') == 'bar'


def test_only_matches_whole_words():
    assert t.is_present('foot') is None
    assert t.is_present('rebar') is None


def test_handles_different_case():
    assert t.is_present('Foo') == 'foo'

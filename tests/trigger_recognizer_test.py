from src.trigger_recognizer import TriggerRecognizer

t = TriggerRecognizer(['foo', 'bar'])


def test_returns_true_if_trigger_present():
    assert t.has_trigger('le foo') == 'foo'
    assert t.has_trigger('chocolate bar') == 'bar'


def test_only_matches_whole_words():
    assert t.has_trigger('foot') is None
    assert t.has_trigger('rebar') is None


def test_handles_different_case():
    assert t.has_trigger('Foo') == 'foo'

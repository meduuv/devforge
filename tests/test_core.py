from devforge import changed_files, normalize_version


def test_changed_files():
    assert changed_files(["a", "b"], ["b", "c"]) == {"added": ["c"], "removed": ["a"]}


def test_normalize_version():
    assert normalize_version("v1.2.3") == "1.2.3"

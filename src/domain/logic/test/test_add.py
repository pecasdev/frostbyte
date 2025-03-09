from src.domain.logic.add import add


class TestAdd:
    def test_foo(self):
        result = add(1, 1)
        assert result == 2

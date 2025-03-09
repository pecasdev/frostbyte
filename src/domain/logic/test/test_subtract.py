from src.domain.logic.subtract import subtract



class TestSubtract:
    def test_bar(self):
        result = subtract(1, 1)
        assert result == 0



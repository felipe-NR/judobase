from datetime import datetime, timezone

import pytest

from judobase import Competition


class TestCompetition:
    """Test cases for the Competition schema validators."""

    def test_updated_at_none(self, get_test_data):
        """Test that an explicit null updated_at stays None."""
        payload = get_test_data("get_competition_info.json")["mock_response"]
        competition = Competition(**{**payload, "updated_at": None})
        assert competition.updated_at is None

    def test_parse_date_with_datetime(self):
        """Test that parse_date attaches UTC to a datetime value."""
        result = Competition.parse_date(datetime(2024, 7, 27))
        assert result == datetime(2024, 7, 27, tzinfo=timezone.utc)

    def test_parse_date_invalid_format(self):
        """Test that parse_date rejects an unknown date format."""
        with pytest.raises(ValueError, match="Invalid date format: 27.07.2024"):
            Competition.parse_date("27.07.2024")

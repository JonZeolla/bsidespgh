"""
Tests for the main module vibe functionality.
"""

from unittest.mock import Mock, patch

import pytest

from main import create_parser, generate_vibe, main


class TestMainVibeFeatures:
    """Test cases for vibe-related features in main."""

    def test_create_parser_includes_vibe_options(self):
        """Test that the parser includes all vibe-related options."""
        parser = create_parser()

        # Parse some test arguments
        args = parser.parse_args(["--vibe", "--vibe-type", "matrix", "--delay", "1.5"])

        assert hasattr(args, "vibe")
        assert hasattr(args, "vibe_type")
        assert hasattr(args, "continuous")
        assert hasattr(args, "delay")
        assert hasattr(args, "stats")

        assert args.vibe is True
        assert args.vibe_type == "matrix"
        assert args.delay == 1.5

    def test_generate_vibe_pattern_type(self):
        """Test generate_vibe with pattern type."""
        vibe_gen = Mock()
        vibe_gen.generate_random_pattern.return_value = "pattern_art"
        vibe_gen.get_vibe_message.return_value = "vibe_message"

        art, message = generate_vibe(vibe_gen, "pattern")

        assert art == "pattern_art"
        assert message == "vibe_message"
        vibe_gen.generate_random_pattern.assert_called_once()
        vibe_gen.get_vibe_message.assert_called_once()

    def test_generate_vibe_matrix_type(self):
        """Test generate_vibe with matrix type."""
        vibe_gen = Mock()
        vibe_gen.generate_cyber_matrix.return_value = "matrix_art"
        vibe_gen.get_vibe_message.return_value = "vibe_message"

        art, message = generate_vibe(vibe_gen, "matrix")

        assert art == "matrix_art"
        assert message == "vibe_message"
        vibe_gen.generate_cyber_matrix.assert_called_once()
        vibe_gen.get_vibe_message.assert_called_once()

    def test_generate_vibe_word_type(self):
        """Test generate_vibe with word type."""
        vibe_gen = Mock()
        vibe_gen.generate_word_art.return_value = "word_art"
        vibe_gen.get_vibe_message.return_value = "vibe_message"

        art, message = generate_vibe(vibe_gen, "word")

        assert art == "word_art"
        assert message == "vibe_message"
        vibe_gen.generate_word_art.assert_called_once()
        vibe_gen.get_vibe_message.assert_called_once()

    def test_generate_vibe_random_type(self):
        """Test generate_vibe with random type."""
        vibe_gen = Mock()
        vibe_gen.generate_full_vibe.return_value = ("random_art", "random_message")

        art, message = generate_vibe(vibe_gen, "random")

        assert art == "random_art"
        assert message == "random_message"
        vibe_gen.generate_full_vibe.assert_called_once()

    @patch("sys.argv", ["main.py", "--stats"])
    @patch("builtins.print")
    @patch("main.config.setup_logging")
    def test_main_stats_mode(self, mock_logging, mock_print):
        """Test main function in stats mode."""
        mock_logging.return_value = Mock(level="INFO")

        main()

        # Check that stats were printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        assert any("Vibe Generator Statistics" in str(call) for call in print_calls)
        assert any("Vibes Generated:" in str(call) for call in print_calls)

    @patch("sys.argv", ["main.py", "--vibe"])
    @patch("builtins.print")
    @patch("main.config.setup_logging")
    def test_main_single_vibe_mode(self, mock_logging, mock_print):
        """Test main function in single vibe mode."""
        mock_logging.return_value = Mock(level="INFO")

        main()

        # Check that a vibe was printed
        assert mock_print.call_count > 0

    @patch("sys.argv", ["main.py", "--vibe", "--continuous"])
    @patch("time.sleep")
    @patch("builtins.print")
    @patch("main.config.setup_logging")
    def test_main_continuous_mode(self, mock_logging, mock_print, mock_sleep):
        """Test main function in continuous mode."""
        mock_logging.return_value = Mock(level="INFO")

        # Simulate KeyboardInterrupt after a few iterations
        mock_sleep.side_effect = [None, None, KeyboardInterrupt]

        main()

        # Check that continuous mode messages were printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        assert any("Starting continuous vibe mode" in str(call) for call in print_calls)
        assert any("Vibe session ended" in str(call) for call in print_calls)

    @patch("sys.argv", ["main.py"])
    @patch("builtins.print")
    @patch("main.config.setup_logging")
    def test_main_help_mode(self, mock_logging, mock_print):
        """Test main function shows help when no args."""
        mock_logging.return_value = Mock(level="INFO")

        main()

        # Check that help was shown
        print_calls = [str(call) for call in mock_print.call_args_list]
        assert any("--vibe" in str(call) for call in print_calls)
        assert any("Tip:" in str(call) for call in print_calls)

    def test_parser_vibe_type_choices(self):
        """Test that vibe-type has correct choices."""
        parser = create_parser()

        # Valid choices should work
        for choice in ["pattern", "matrix", "word", "random"]:
            args = parser.parse_args(["--vibe-type", choice])
            assert args.vibe_type == choice

        # Invalid choice should raise error
        with pytest.raises(SystemExit):
            parser.parse_args(["--vibe-type", "invalid"])

    def test_parser_delay_type(self):
        """Test that delay accepts float values."""
        parser = create_parser()

        args = parser.parse_args(["--delay", "3.5"])
        assert args.delay == 3.5

        args = parser.parse_args(["--delay", "0.1"])
        assert args.delay == 0.1

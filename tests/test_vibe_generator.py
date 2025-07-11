"""
Tests for the vibe generator module.
"""

import pytest

from bsidespgh25.vibe_generator import VibeGenerator


class TestVibeGenerator:
    """Test cases for the VibeGenerator class."""

    def test_vibe_generator_initialization(self):
        """Test that VibeGenerator initializes correctly."""
        vibe_gen = VibeGenerator()
        assert vibe_gen.vibe_count == 0

    def test_generate_random_pattern(self):
        """Test random pattern generation."""
        vibe_gen = VibeGenerator()
        pattern = vibe_gen.generate_random_pattern()

        assert isinstance(pattern, str)
        assert len(pattern) > 0
        assert pattern in vibe_gen.ASCII_PATTERNS

    def test_generate_cyber_matrix(self):
        """Test cyber matrix generation."""
        vibe_gen = VibeGenerator()

        # Test default size
        matrix = vibe_gen.generate_cyber_matrix()
        lines = matrix.strip().split("\n")
        assert len(lines) == 10
        assert all(len(line) == 40 for line in lines)

        # Test custom size
        matrix = vibe_gen.generate_cyber_matrix(width=20, height=5)
        lines = matrix.strip().split("\n")
        assert len(lines) == 5
        assert all(len(line) == 20 for line in lines)

    def test_generate_word_art(self):
        """Test word art generation."""
        vibe_gen = VibeGenerator()
        word_art = vibe_gen.generate_word_art()

        assert isinstance(word_art, str)
        assert "┌" in word_art
        assert "┐" in word_art
        assert "└" in word_art
        assert "┘" in word_art

        # Check that it contains a cyber word
        contains_word = any(word in word_art for word in vibe_gen.CYBER_WORDS)
        assert contains_word

    def test_get_vibe_message(self):
        """Test vibe message retrieval."""
        vibe_gen = VibeGenerator()
        message = vibe_gen.get_vibe_message()

        assert isinstance(message, str)
        assert message in vibe_gen.VIBE_MESSAGES
        # Check that message contains at least one emoji
        emojis = ["✨", "🔐", "🚀", "💻", "🛡️", "⚡", "🌐", "🔍"]
        assert any(emoji in message for emoji in emojis)

    def test_generate_full_vibe(self):
        """Test full vibe generation."""
        vibe_gen = VibeGenerator()
        initial_count = vibe_gen.vibe_count

        art, message = vibe_gen.generate_full_vibe()

        assert isinstance(art, str)
        assert isinstance(message, str)
        assert len(art) > 0
        assert len(message) > 0
        assert vibe_gen.vibe_count == initial_count + 1

    def test_generate_full_vibe_increments_counter(self):
        """Test that generating vibes increments the counter."""
        vibe_gen = VibeGenerator()

        for i in range(5):
            vibe_gen.generate_full_vibe()
            assert vibe_gen.vibe_count == i + 1

    def test_get_stats(self):
        """Test statistics retrieval."""
        vibe_gen = VibeGenerator()

        # Initial stats
        stats = vibe_gen.get_stats()
        assert isinstance(stats, dict)
        assert stats["vibes_generated"] == 0
        assert stats["patterns_available"] == len(vibe_gen.ASCII_PATTERNS)
        assert stats["cyber_words_available"] == len(vibe_gen.CYBER_WORDS)
        assert stats["messages_available"] == len(vibe_gen.VIBE_MESSAGES)

        # After generating vibes
        vibe_gen.generate_full_vibe()
        vibe_gen.generate_full_vibe()
        stats = vibe_gen.get_stats()
        assert stats["vibes_generated"] == 2

    def test_ascii_patterns_are_valid(self):
        """Test that all ASCII patterns are valid strings."""
        vibe_gen = VibeGenerator()

        for pattern in vibe_gen.ASCII_PATTERNS:
            assert isinstance(pattern, str)
            assert len(pattern) > 0

    def test_cyber_words_are_valid(self):
        """Test that all cyber words are valid strings."""
        vibe_gen = VibeGenerator()

        for word in vibe_gen.CYBER_WORDS:
            assert isinstance(word, str)
            assert len(word) > 0
            assert word.isupper()

    def test_vibe_messages_are_valid(self):
        """Test that all vibe messages are valid strings."""
        vibe_gen = VibeGenerator()

        for message in vibe_gen.VIBE_MESSAGES:
            assert isinstance(message, str)
            assert len(message) > 0

    @pytest.mark.parametrize("vibe_type", ["pattern", "matrix", "word"])
    def test_generate_full_vibe_variety(self, vibe_type):
        """Test that different vibe types produce different results."""
        vibe_gen = VibeGenerator()

        # Generate multiple vibes and check they're not all identical
        vibes = []
        for _ in range(10):
            art, message = vibe_gen.generate_full_vibe()
            vibes.append(art)

        # At least some should be different
        unique_vibes = set(vibes)
        assert len(unique_vibes) > 1

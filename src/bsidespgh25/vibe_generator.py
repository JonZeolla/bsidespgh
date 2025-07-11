"""
Vibe generator for creating cybersecurity-themed ASCII art.
"""

import random
from typing import Tuple


class VibeGenerator:
    """Generate cybersecurity-themed ASCII art and messages."""

    ASCII_PATTERNS = [
        """
    ╔═══════════════════════════════════════╗
    ║         BSides Pittsburgh 2025        ║
    ║           Let's ✨vibe✨              ║
    ╚═══════════════════════════════════════╝
        """,
        """
     ▄▄▄▄    ██████  ██▓▓█████▄ ▓█████  ██████
    ▓█████▄▒██    ▒ ▓██▒▒██▀ ██▌▓█   ▀▒██    ▒
    ▒██▒ ▄██░ ▓██▄   ▒██▒░██   █▌▒███  ░ ▓██▄
    ▒██░█▀    ▒   ██▒░██░░▓█▄   ▌▒▓█  ▄  ▒   ██▒
    ░▓█  ▀█▓▒██████▒▒░██░░▒████▓ ░▒████▒██████▒▒
    ░▒▓███▀▒▒ ▒▓▒ ▒ ░░▓   ▒▒▓  ▒ ░░ ▒░ ▒ ▒▓▒ ▒ ░
    ▒░▒   ░ ░ ░▒  ░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░ ░▒  ░ ░
     ░    ░ ░  ░  ░   ▒ ░ ░ ░  ░    ░  ░  ░  ░
     ░            ░   ░     ░       ░  ░     ░
          ░                 ░
        """,
        """
    ┌─────────────────────────────────────┐
    │ █▀▀ █▄█ █▄▄ █▀▀ █▀█ █▀ █▀▀ █▀▀    │
    │ █▄▄  █  █▄█ ██▄ █▀▄ ▄█ ██▄ █▄▄    │
    │                                     │
    │       PITTSBURGH 2025 🔒            │
    └─────────────────────────────────────┘
        """,
    ]

    CYBER_WORDS = [
        "HACK",
        "SECURE",
        "ENCRYPT",
        "DECODE",
        "FIREWALL",
        "EXPLOIT",
        "PATCH",
        "PENTEST",
        "CRYPTO",
        "NETWORK",
        "BINARY",
        "PAYLOAD",
        "MALWARE",
        "DEFENSE",
        "AUDIT",
        "FORENSIC",
        "REVERSE",
        "SHELLCODE",
        "ROOTKIT",
        "SANDBOX",
    ]

    VIBE_MESSAGES = [
        "✨ Vibing with security! ✨",
        "🔐 Encrypted vibes only 🔐",
        "🚀 Launching cyber vibes 🚀",
        "💻 Hacking the mainframe... of good vibes 💻",
        "🛡️ Firewall activated: Bad vibes blocked 🛡️",
        "⚡ Electric security vibes ⚡",
        "🌐 Network secured, vibes amplified 🌐",
        "🔍 Scanning for maximum vibes... Found! 🔍",
    ]

    def __init__(self):
        """Initialize the vibe generator."""
        self.vibe_count = 0

    def generate_random_pattern(self) -> str:
        """Generate a random ASCII art pattern.

        Returns:
            A randomly selected ASCII art pattern.
        """
        return random.choice(self.ASCII_PATTERNS)

    def generate_cyber_matrix(self, width: int = 40, height: int = 10) -> str:
        """Generate a matrix-style cyber pattern.

        Args:
            width: Width of the matrix pattern.
            height: Height of the matrix pattern.

        Returns:
            A matrix-style ASCII pattern.
        """
        chars = "01╬═║╔╗╚╝░▓█"
        lines = []

        for _ in range(height):
            line = "".join(random.choice(chars) for _ in range(width))
            lines.append(line)

        return "\n".join(lines)

    def generate_word_art(self) -> str:
        """Generate random cyber word art.

        Returns:
            ASCII art featuring a random cyber word.
        """
        word = random.choice(self.CYBER_WORDS)
        border = "─" * (len(word) + 4)

        return f"""
    ┌{border}┐
    │  {word}  │
    └{border}┘
        """

    def get_vibe_message(self) -> str:
        """Get a random vibe message.

        Returns:
            A random vibe message string.
        """
        return random.choice(self.VIBE_MESSAGES)

    def generate_full_vibe(self) -> Tuple[str, str]:
        """Generate a complete vibe with art and message.

        Returns:
            Tuple of (ascii_art, vibe_message).
        """
        self.vibe_count += 1

        art_type = random.choice(["pattern", "matrix", "word"])

        if art_type == "pattern":
            art = self.generate_random_pattern()
        elif art_type == "matrix":
            art = self.generate_cyber_matrix()
        else:
            art = self.generate_word_art()

        message = self.get_vibe_message()

        return art, message

    def get_stats(self) -> dict:
        """Get vibe generation statistics.

        Returns:
            Dictionary containing vibe statistics.
        """
        return {
            "vibes_generated": self.vibe_count,
            "patterns_available": len(self.ASCII_PATTERNS),
            "cyber_words_available": len(self.CYBER_WORDS),
            "messages_available": len(self.VIBE_MESSAGES),
        }

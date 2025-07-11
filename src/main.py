#!/usr/bin/env python3
"""
bsidespgh25 script entrypoint
"""

import argparse
import time

from bsidespgh25 import config
from bsidespgh25.vibe_generator import VibeGenerator


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser with vibe-specific options.

    Returns:
        Configured argument parser.
    """
    parser = config.create_arg_parser()

    parser.add_argument(
        "--vibe", action="store_true", help="Generate a cybersecurity vibe"
    )

    parser.add_argument(
        "--vibe-type",
        choices=["pattern", "matrix", "word", "random"],
        default="random",
        help="Type of vibe to generate (default: random)",
    )

    parser.add_argument(
        "--continuous", action="store_true", help="Continuously generate vibes"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Delay between continuous vibes in seconds (default: 2.0)",
    )

    parser.add_argument(
        "--stats", action="store_true", help="Show vibe generation statistics"
    )

    return parser


def generate_vibe(vibe_gen: VibeGenerator, vibe_type: str) -> tuple[str, str]:
    """Generate a vibe based on the specified type.

    Args:
        vibe_gen: The vibe generator instance.
        vibe_type: Type of vibe to generate.

    Returns:
        Tuple of (ascii_art, message).
    """
    if vibe_type == "pattern":
        art = vibe_gen.generate_random_pattern()
        message = vibe_gen.get_vibe_message()
    elif vibe_type == "matrix":
        art = vibe_gen.generate_cyber_matrix()
        message = vibe_gen.get_vibe_message()
    elif vibe_type == "word":
        art = vibe_gen.generate_word_art()
        message = vibe_gen.get_vibe_message()
    else:  # random
        art, message = vibe_gen.generate_full_vibe()

    return art, message


def main():
    """Main entry point for the application."""
    # Parse arguments manually to avoid conflicts with config
    parser = create_parser()
    args = parser.parse_args()

    # Setup logging
    log = config.setup_logging(args.loglevel)
    log.debug("Logging initialized with level: %s", log.level)

    # Create vibe generator
    vibe_gen = VibeGenerator()

    # Handle different modes
    if args.stats:
        stats = vibe_gen.get_stats()
        print("\n📊 Vibe Generator Statistics 📊")
        print("─" * 40)
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        return

    if args.vibe:
        if args.continuous:
            print("🎉 Starting continuous vibe mode! Press Ctrl+C to stop.")
            print("─" * 60)
            try:
                while True:
                    art, message = generate_vibe(vibe_gen, args.vibe_type)
                    print(art)
                    print(f"\n{message}\n")
                    print("─" * 60)
                    time.sleep(args.delay)
            except KeyboardInterrupt:
                print("\n\n✨ Vibe session ended! Stay secure! ✨")
                stats = vibe_gen.get_stats()
                print(f"Total vibes generated: {stats['vibes_generated']}")
        else:
            # Single vibe
            art, message = generate_vibe(vibe_gen, args.vibe_type)
            print(art)
            print(f"\n{message}\n")
    else:
        # Default behavior - show help
        parser.print_help()
        print("\n💡 Tip: Try running with --vibe to generate some cybersecurity vibes!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import os
import sys
from dotenv import load_dotenv
from prompts import gather_info
from generator import generate_readme

load_dotenv()

def parse_args():
    parser = argparse.ArgumentParser(
        description="🧠 README Generator — AI-powered README.md creator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                          # uses GEMINI_API_KEY env var
  python main.py --key your-key...        # pass key directly
  python main.py --output docs/README.md  # custom output path
        """,
    )
    parser.add_argument(
        "--key",
        type=str,
        help="Gemini API key (or set GEMINI_API_KEY env var)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="README.md",
        help="Output file path (default: README.md)",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Print the generated README to stdout instead of saving",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    api_key = args.key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ No API key found. Set GEMINI_API_KEY or pass --key <your-key>")
        sys.exit(1)

    info = gather_info()

    print("\n⏳ Generating your README...\n")
    readme = generate_readme(info, api_key)

    if args.print:
        print(readme)
    else:
        output_path = args.output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(readme)
        print(f"✅ README saved to: {output_path}")
        print("\n--- Preview (first 20 lines) ---\n")
        lines = readme.splitlines()
        print("\n".join(lines[:20]))
        if len(lines) > 20:
            print(f"\n... ({len(lines) - 20} more lines)")


if __name__ == "__main__":
    main()
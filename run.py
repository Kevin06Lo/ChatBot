import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.main import run_chat

if __name__ == "__main__":
    run_chat()
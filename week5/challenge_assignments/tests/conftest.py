import sys
from pathlib import Path

# Add the parent directory of the tests folder to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

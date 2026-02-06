
from pathlib import Path
import sys

# Add paths to sys.path locally to imitate app structure
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from integration.utils.resource_path import get_user_data_dir

data_dir = get_user_data_dir("Nexy")
print(f"Resolved Data Dir: {data_dir}")

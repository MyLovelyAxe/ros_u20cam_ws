import numpy as np
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_DATA_TYPE = np.float32

# device

U20CAM_720P_SOURCE = "/dev/video2"   # same device as your test script

# calibration

CALIB_PARAM_JSON = REPO_ROOT / "u20cam_calib.json"
try:
    from models.IRL import entry as irl_entry
except Exception:
    irl_entry = None

try:
    from models.Gazeformer import entry as gazeformer_entry
except Exception:
    gazeformer_entry = None

from models.demo import entry as demo_entry

# Optional: HAT depends on detectron2
try:
    from models.HAT import entry as hat_entry  # type: ignore
    _has_hat = True
except Exception:
    hat_entry = None  # type: ignore
    _has_hat = False

# Optional: Scanpaths depends on mmcv
try:
    from models.Scanpaths import entry as scanpaths_entry  # type: ignore
    _has_scanpaths = True
except Exception:
    scanpaths_entry = None  # type: ignore
    _has_scanpaths = False

try:
    from models.CLIPGaze import entry as clipgaze_entry
except Exception:
    clipgaze_entry = None

MODEL_REGISTRY = {
    'demo': demo_entry,
}
if irl_entry:
    MODEL_REGISTRY['irl'] = irl_entry
if gazeformer_entry:
    MODEL_REGISTRY['gazeformer'] = gazeformer_entry
if _has_hat and hat_entry:
    MODEL_REGISTRY['hat'] = hat_entry  # type: ignore
if _has_scanpaths and scanpaths_entry:
    MODEL_REGISTRY['scanpaths'] = scanpaths_entry  # type: ignore
if clipgaze_entry:
    MODEL_REGISTRY['clipgaze'] = clipgaze_entry


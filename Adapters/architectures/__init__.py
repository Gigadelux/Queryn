# Model specifications for the adapter pipelines. Pure nn.Module
# definitions only — no optimizer, loss, or training-loop logic lives here.
# Each pipeline (v0, v1, ...) owns its own training orchestration and
# imports whichever architectures it needs from this package.
from .linear import LinearMapper
from .deep import DeepMapper

# Ordered deliberately: v1_adapter_model_training.py iterates this dict to
# decide which architecture to train per pair, and breaks ties in favor of
# whichever key comes first — i.e. "linear" wins ties against "deep".
ARCHITECTURES = {
    "linear": LinearMapper,
    "deep":   DeepMapper,
}

__all__ = ["LinearMapper", "DeepMapper", "ARCHITECTURES"]

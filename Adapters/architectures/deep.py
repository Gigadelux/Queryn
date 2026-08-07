# %%
"""COMPRESSED-LATENT MLP MAPPER"""
import torch.nn as nn
import torch.nn.functional as F


class DeepMapper(nn.Module):
    """Two-layer MLP whose hidden layer is a compressed latent space —
    strictly smaller than both in_dim and out_dim — instead of the
    expand-then-project width used in v0 (`hidden = max(in_dim, out_dim)`).

    Forcing the bottleneck below both dimensions makes the mapper keep only
    the signal shared across the two embedding spaces rather than
    over-parameterizing on either side's idiosyncratic dimensions — the
    same reasoning that makes an autoencoder's code layer useful.

    No residual/skip connection: input and latent live in different,
    differently-shaped spaces, so there is no identity path to add back.

    Normalizes its own input and output to unit vectors — see
    LinearMapper's docstring for why; the same reasoning applies here.
    """

    def __init__(
        self,
        in_dim: int,
        out_dim: int,
        latent_ratio: float = 0.5,
        min_latent: int = 128,
    ) -> None:
        super().__init__()
        self.latent_dim = max(int(min(in_dim, out_dim) * latent_ratio), min_latent)
        self.net = nn.Sequential(
            nn.Linear(in_dim, self.latent_dim),
            nn.GELU(),
            nn.Linear(self.latent_dim, out_dim),
        )

    def forward(self, x):
        x = F.normalize(x, p=2, dim=-1, eps=1e-8)
        y = self.net(x)
        return F.normalize(y, p=2, dim=-1, eps=1e-8)

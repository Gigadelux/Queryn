# %%
"""LINEAR MODEL"""
import torch.nn as nn
import torch.nn.functional as F


class LinearMapper(nn.Module):
    """Plain linear projection — the Procrustes-style baseline every
    nonlinear mapper in this package is judged against. Some pairs
    (near-isomorphic, same-family embedding spaces) translate almost as
    well with a single matrix as with a deeper network; this makes that
    an honest, measured comparison instead of an assumption.

    Normalizes its own input and output to unit vectors. Training and
    evaluation both optimize/measure cosine similarity, which is
    invariant to input magnitude — normalizing here bakes that assumption
    into the saved model instead of leaving it as a contract the caller
    has to remember to uphold.
    """

    def __init__(self, in_dim: int, out_dim: int) -> None:
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, x):
        x = F.normalize(x, p=2, dim=-1, eps=1e-8)
        y = self.linear(x)
        return F.normalize(y, p=2, dim=-1, eps=1e-8)

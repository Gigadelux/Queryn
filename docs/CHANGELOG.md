# Changelog & Roadmap

## v0.01 — Current

- `Adapters/`: unified 349,674-row multi-domain corpus (`dataset_generator.py`), embedding pipeline across 8 models (`embedding_pipeline.py`), and two generations of per-pair mapper training:
  - **v0** — 56 directed pairs, single deep architecture, last-epoch checkpointing.
  - **v1** — 49 directed pairs (`ada-002` dropped as a target), linear vs. deep trained and compared per pair with the winner kept, best-epoch checkpointing, cosine-similarity loss with LR scheduling.
- `app/`: scaffolded, pre-development. Directory structure in place (`core/adapters/`, `core/connectors/`, `services/migrator.py`, `main.py`); no functional code yet.
- Project open-sourced under Apache 2.0.

## Roadmap (future)

- **Engine build-out, with a choice between re-embedding and adapters.** Build out `app/` into a working local program, giving customers the option to either translate via a trained adapter or fall back to re-embedding directly through their own model provider — so the engine remains useful even for pairs without a trained (or trustworthy) adapter yet.
- **Weak-adapter study and architecture iteration.** Systematically identify which model pairs perform worst under the current linear/deep architectures (using the v1 `architecture_comparison` ablation data as the starting point), and investigate architecture changes — beyond the current single-hidden-layer linear/deep choice — for the pairs that need it.

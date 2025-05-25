# Micron AI Challenge

## Current Progress
- Best model: GPU-accelerated ensemble (RMSE: 0.0270)
  - 2 XGBoost models (GPU-enabled)
  - 2 LightGBM models (CPU)
  - Equal weights (0.25 each)
  - 500 trees per model
  - 80:20 train-test split

## Future Improvements to Try
1. Weighted ensemble approach
2. Cross-fold prediction
3. Model-specific GPU optimizations
4. Stacking with meta-learner
5. Bagging the entire pipeline

## Environment Setup
- CUDA-enabled environment for GPU acceleration
- XGBoost using GPU
- LightGBM on CPU (GPU support needs separate installation)

## Branch Information
- `main`: Original implementation
- `enhanced-gpu-model`: Experiments with feature importance and model improvements


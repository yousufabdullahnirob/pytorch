import torch

try:
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    x = torch.rand(5, 3)
    print("Random tensor created successfully:")
    print(x)
except Exception as e:
    print(f"Error verification failed: {e}")

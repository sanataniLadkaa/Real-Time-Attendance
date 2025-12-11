# backend/training/wandb_setup.py
import os
try:
    import wandb
except Exception:
    wandb = None

def init_wandb(project_name: str = "attendance-system", run_name: str = None):
    api_key = os.getenv("WANDB_API_KEY")
    if wandb is None:
        print("wandb not installed. Run `pip install wandb` to enable experiment tracking.")
        return None
    wandb.login(key=api_key)
    run = wandb.init(project=project_name, name=run_name)
    return run

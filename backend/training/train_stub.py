# backend/training/train_stub.py
import argparse
import time
from wandb_setup import init_wandb

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--project", default="attendance-system")
    args = p.parse_args()

    run = init_wandb(project_name=args.project, run_name="week1-stub")
    for e in range(args.epochs):
        # mock metrics
        train_loss = 1.0 / (e + 1)
        val_acc = 0.5 + 0.1 * e
        print(f"Epoch {e}: loss={train_loss}, val_acc={val_acc}")
        if run:
            run.log({"epoch": e, "train_loss": train_loss, "val_acc": val_acc})
        time.sleep(1)
    if run:
        run.finish()

if __name__ == "__main__":
    main()

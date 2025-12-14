import wandb

def init_run(name):
    wandb.login()
    return wandb.init(
        project="attendance-system",
        name=name,
        config={"framework": "pytorch"}
    )

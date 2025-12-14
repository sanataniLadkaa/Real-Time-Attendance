from wandb_utils import init_run

run = init_run("voice-embedding-analysis")
run.log({"note": "Using ECAPA-TDNN pretrained embeddings"})
run.finish()

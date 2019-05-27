CONFIG=cat-mel_2bar_big
RUN_DIR=/tmp/music_vae
NUM_OUTPUTS=8
OUTPUT_DIR=/home/ubuntu/CVAE/generate/
CONTEXT="[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]"
music_vae_generate \
    --mode=sample \
    --config=$CONFIG \
    --run_dir=$RUN_DIR \
    --num_outputs=$NUM_OUTPUTS \
    --output_dir=$OUTPUT_DIR \
    --context=$CONTEXT
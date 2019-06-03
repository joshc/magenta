CONFIG=cat-mel_2bar_big
RUN_DIR=/tmp/music_vae
NUM_OUTPUTS=8
OUTPUT_DIR=/home/ubuntu/CVAE/generate/
CONTEXT="[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]"
INPUT_MIDI=/home/ubuntu/CVAE/generate/extracted/cat-mel_2bar_big_input1-extractions_2019-06-03_032212-000-of-013.mid
#INPUT_MIDI=/home/ubuntu/CVAE/lmd_matched/Z/Z/C/TRZZCUA128F93334E0/eb812e2e1a2cc4103be4639781a4235e.mid
music_vae_generate \
    --mode=sample \
    --config=$CONFIG \
    --run_dir=$RUN_DIR \
    --num_outputs=$NUM_OUTPUTS \
    --output_dir=$OUTPUT_DIR \
    --context=$CONTEXT \
    --input_translate=$INPUT_MIDI

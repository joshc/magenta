EXAMPLES_PATH=data/mynotesequences.tfrecord
SEQ_TO_FNAME_PATH=seq_to_fname.p

python music_vae_train.py --config=groovae_4bar --run_dir=/tmp/music_vae/ \
    --mode=train --examples_path=$EXAMPLES_PATH \
    --seq_to_fname_path=$SEQ_TO_FNAME_PATH

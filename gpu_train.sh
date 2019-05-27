CONFIG=cat-mel_2bar_big
EXAMPLES_PATH=/home/ubuntu/CVAE/mynotesequences.tfrecord
SEQ_TO_FNAME_PATH=/home/ubuntu/CVAE/seq_to_fname.p
GENRE_DICT_PATH=/home/ubuntu/CVAE/genre_data/genre_dict.p
CHECKPOINTS_TO_KEEP=3
#CONFIG=groovae_4bar
#EXAMPLES_PATH=/home/ubuntu/CVAE/testdata/mynotesequences.tfrecord
#SEQ_TO_FNAME_PATH=/home/ubuntu/CVAE/testdata/seq_to_fname.p

music_vae_train --config=$CONFIG \
                --run_dir=/tmp/music_vae/ \
                --mode=train \
                --examples_path=$EXAMPLES_PATH \
                --seq_to_fname_path=$SEQ_TO_FNAME_PATH \
                --genre_dict_path=$GENRE_DICT_PATH \
                --cache_dataset=True \
                --checkpoints_to_keep=$CHECKPOINTS_TO_KEEP
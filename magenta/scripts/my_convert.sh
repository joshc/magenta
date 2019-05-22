INPUT_DIRECTORY=A

# TFRecord file that will contain NoteSequence protocol buffers.
SEQUENCES_TFRECORD=mynotesequences.tfrecord

python convert_dir_to_note_sequences.py \
  --input_dir=$INPUT_DIRECTORY \
  --output_file=$SEQUENCES_TFRECORD \
  --recursive


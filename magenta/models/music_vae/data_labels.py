from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

class TensorLabeler:
  """
  Class that computes labels of a one-hot melody tensor.
  """
  def __init__(self, tensor, config):
    """
    Construct a one-hot melody labeler.
    tensor: One-hot encoded melody. Array of shape (nsteps, npitches) where
      the steps are 16th notes.
    config: Config that was used to encode the tensor.
    """
    # Undo one-hot encoding
    row_idxs, col_idxs = tensor.nonzero()
    # Assert the encoding was one-hot; each row has one nonzero element
    assert (row_idxs == np.arange(tensor.shape[0])).all()

    # Decode into melody events.
    self.events = [config.data_converter.encoder_decoder.decode_event(x)
                   for x in col_idxs]

    # Precompute pitches
    # These are the nonnegative events that represent actual notes (not
    # note-off or hold events)
    self.notes = [e for e in self.events if e >= 0]

  def note_density(self):
    """
    Return note density, which is the number of note onsets
    / total number of 16th note steps.
    """
    return len(self.notes) / len(self.events)

  def c_diatonic(self):
    """
    Return fraction of notes that are on the white keys of the piano
    (C, D, E, F, G, A, B).
    """
    # 0, 2, 4, 5, 7, 9, 11
    # C  D  E  F  G  A  B
    return sum((n % 12) in [0, 2, 4, 5, 7, 9, 11] for n in self.notes) \
           / len(self.notes)

  def average_interval(self):
    """
    Return average absolute number of semitones between consecutive notes.
    """
    total_pitch_interval = 0
    for n1, n2 in zip(self.notes[:-1], self.notes[1:]):
      total_pitch_interval += abs(n1 - n2)
    return total_pitch_interval / (len(self.notes) - 1)

  def syncopation_16th(self):
    """
    Return the fraction of (16th note) quantized note onsets landing on
    an odd 16th note position (1-indexed) with no note onset at
    the previous 16th note position.
    """
    # Syncopated 16th note positions are at 1, 3, 5, etc.
    num_sync = sum(self.events[i-1] < 0 <= self.events[i]
                   for i in range(1, len(self.events), 2))
    return num_sync / len(self.notes)

  def syncopation_8th(self):
    """
    Return the fraction of (16th note) quantized note onsets landing on
    an odd 8th note position (1-indexed) with no note onset at
    either the previous 16th or 8th note positions.
    """
    # Syncopated 8th note positions are at 2, 6, 10, etc.
    num_sync = sum(self.events[i-1] < 0 <= self.events[i]
                   and self.events[i-2] < 0
                   for i in range(2, len(self.events), 4))
    return num_sync / len(self.notes)

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import magenta.music as mm
from magenta.models.music_vae.configs import CONFIG_MAP
from magenta.models.music_vae.data import np_onehot
from magenta.models.music_vae.data_labels import TensorLabeler

# MIDI numbers of several pitches
# pylint: disable=invalid-name
Eb4 = 63
F4 = 65
G4 = 67
Bb4 = 70
# pylint: enable=invalid-name

# Config to use during test
CONFIG_NAME = 'cat-mel_2bar_big'

class TensorLabelerTest(tf.test.TestCase):
  def testSampleTensor(self):
    with self.test_session():
      # Mary had a little lamb, in 8th notes
      # 2 bars, each step is a 16th note
      melody = [
          G4, mm.MELODY_NO_EVENT, F4, mm.MELODY_NO_EVENT,
          Eb4, mm.MELODY_NO_EVENT, F4, mm.MELODY_NO_EVENT,
          G4, mm.MELODY_NO_EVENT, G4, mm.MELODY_NO_EVENT,
          G4, mm.MELODY_NO_EVENT, mm.MELODY_NOTE_OFF, mm.MELODY_NO_EVENT,
          # This half bar has 16th note syncopation
          mm.MELODY_NO_EVENT, F4, mm.MELODY_NO_EVENT, F4,
          mm.MELODY_NO_EVENT, F4, mm.MELODY_NO_EVENT, mm.MELODY_NOTE_OFF,
          # This half bar has 8th note syncopation
          mm.MELODY_NO_EVENT, mm.MELODY_NO_EVENT, G4, mm.MELODY_NO_EVENT,
          mm.MELODY_NOTE_OFF, mm.MELODY_NO_EVENT, Bb4, mm.MELODY_NO_EVENT
      ]
      config = CONFIG_MAP[CONFIG_NAME]
      # One-hot encode
      codes = [config.data_converter.encoder_decoder.encode_event(e)
               for e in melody]
      tensor = np_onehot(codes, config.data_converter.output_depth)

      # Create TensorLabeler
      tl = TensorLabeler(tensor, config)
      self.assertAlmostEqual(tl.note_density(), 12 / 32)
      self.assertAlmostEqual(tl.c_diatonic(), 10 / 12)
      self.assertAlmostEqual(tl.average_interval(), 15 / 11)
      self.assertAlmostEqual(tl.syncopation_16th(), 3 / 12)
      self.assertAlmostEqual(tl.syncopation_8th(), 2 / 12)

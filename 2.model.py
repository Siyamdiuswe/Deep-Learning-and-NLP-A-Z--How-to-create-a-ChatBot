########## PART 2 - BUILDING THE SEQ2SEQ MODEL ##########

import tensorflow as tf
# Creating placeholder for the inputs and the targets
def model_inputs():
    inputs = tf.placeholder(tf.int32, [None,None], name = 'input')
    targets = tf.placeholder(tf.int32, [None,None], name = 'targets')
    lr = tf.placeholder(tf.float32, name = 'learning_rate')
    keep_prob = tf.placeholder(tf.float32, name = 'keep_prob')
    return inputs, targets, lr, keep_prob

# Preprocess the targets
def preprocess_targets(targets, word2int, batch_size):
    left_side = tf.fill([batch_size, 1], word2int['<SOS>'])
    right_side = tf.strided_slice(targets, [0,0], [batch_size, -1], [1,1])
    preprocessed_targets = tf.concat([left_side, right_side], 1)
    return preprocessed_targets

# Creating the Encoder RNN Layer
def encoder_rnn_layer(rnn_input, rnn_size, num_layers, keep_prob, sequence_length):
    lstm = tf.contrib.rnn.BasicLSTMCell(rnn_size)
    lstm_dropout = tf.contrib.rnn.DropoutWrapper(lstm, input_keep_prob = keep_prob)
    encoder_cell = tf.contrib.rnn.MultiRNNCell([lstm_dropout] * num_layers)
    _, encoder_state = tf.nn.bidirectional_dynamic_rnn(cell_fw = encoder_cell,
                                                      cell_bw = encoder_cell,
                                                      sequence_length = sequence_length,
                                                      input = rnn_input,
                                                      dtype = tf.float32)
    return encoder_state

# Decoding the training set
def decode_training_set():
    


print(":-D")
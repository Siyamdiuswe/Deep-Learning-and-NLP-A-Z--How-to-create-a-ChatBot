########## PART 2 - BUILDING THE SEQ2SEQ MODEL ##########
import tensorflow as tf
# Creating placeholder for the inputs and the targets
def model_inputs():
    inputs = tf.placeholder(tf.int32, [None,None], name = 'input')
    targets = tf.placeholder(tf.int32, [None,None],name = 'target')
    lr = tf.placeholder(tf.float32, name = 'learning_rate')
    keep_prob = tf.placeholder(tf.float32, name= 'keep_prob')
    
    
    
print(":-D")
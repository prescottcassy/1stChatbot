import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout
from preprocessing import preprocess_data
import matplotlib.pyplot as plt


# Load data
words, labels, training_data = preprocess_data('intents.json')

# Prepare training data
training_x = []
training_y = []

for (pattern, tag) in training_data:
	# Create bag of words
	bag = [1 if w in [w.lower() for w in pattern] else 0 for w in words]

	# Create output vector
	output_row = [0] * len(labels)
	output_row[labels.index(tag)] = 1

	training_x.append(bag)
	training_y.append(output_row)

training_x = np.array(training_x)
training_y = np.array(training_y)

from tensorflow.keras.regularizers import l2
# Define the model
model = Sequential([
    Input(shape=(len(training_x[0]),)),
    Dense(128, activation='relu', kernel_regularizer=l2(0.01)),
    Dropout(0.3),
    Dense(64, activation='relu', kernel_regularizer=l2(0.01)),
    Dropout(0.3),
    Dense(len(labels), activation='sigmoid')
])

from tensorflow.keras.optimizers.schedules import ExponentialDecay
# Define learning rate schedule
lr_schedule = ExponentialDecay(
    initial_learning_rate=0.001, decay_steps=1000, decay_rate=0.95, staircase=True
)

# Apply to optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Reward function
def compute_reward(y_true, y_pred):
    """
    Computes reward based on classification accuracy and confidence.
    """
    reward = 0
    predicted_label = np.argmax(y_pred)
    actual_label = np.argmax(y_true)

    # Reward correct predictions
    if predicted_label == actual_label:
        reward += 1  
    else:
        reward -= 0.5  # Penalize incorrect classifications

    # Encourage high-confidence predictions
    max_confidence = np.max(y_pred)
    reward += max_confidence  

    return reward

# Initialize learning rate
new_lr = np.float32(0.001)  # Ensure correct data type

# Training loop with reward integration
for epoch in range(3):  
    history = model.fit(training_x, training_y, epochs=1, batch_size=4, verbose=1)

    # Compute rewards per sample
    rewards = []
    y_preds = model.predict(training_x)
    
    for i in range(len(training_x)):  # Iterate over samples
        reward = compute_reward(training_y[i], y_preds[i])
        rewards.append(reward)

    # Adjust learning rate dynamically based on average reward
    avg_reward = np.mean(rewards)
    new_lr = np.float32(0.001 * (1 + avg_reward))  # Ensure type safety

    # Properly set the learning rate
    model.optimizer.learning_rate.assign(new_lr)

# Save the model
model.save('my_model.keras')

def chatbot_response(message):
    # Example response logic
    return f"Echo: {message}"

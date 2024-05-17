import hashlib
import time
import os
import base64

collision_counts = 0  # Initialize the collision counter
lookup_table = {}  # Initialize the lookup table for detecting collisions
k = 6  # Number of nibbles (4 bits each) to compare for collisions (24 bits total)

# Function to generate a truncated SHA-1 hash (first 24 bits)
def sha24v(message):
    sha1_hash = hashlib.sha1(message.encode()).hexdigest()
    return sha1_hash[:6]  # Return the first 24 bits (6 hex digits) of the SHA-1 hash

# Function to generate a random, typable message
def generate_random_message():
    random_binary = os.urandom(8)  # Generate 8 random bytes
    random_message = base64.b64encode(random_binary).decode('utf-8')  # Encode to base64 string
    return random_message

start_time = time.time()  # Record the start time

# Infinite loop to find collisions using the birthday paradox
while True:
    random_message = generate_random_message()  # Generate a random message
    result = sha24v(random_message)  # Get the truncated hash of the message

    hash_value = result[:k]  # Get the hash value to check for collisions
    if hash_value in lookup_table:
        # Collision found
        print("Birthday Paradox Collision")
        print("Message 1:", lookup_table[hash_value]['message'])
        print("Message 2:", random_message)
        print("The Hash:", hash_value)
        collision_counts += 1
        break
    else:
        lookup_table[hash_value] = {'message': random_message, 'hash': result}  # Store the hash value and message in the lookup table

end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time  # Calculate the elapsed time
time_string = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))  # Format the elapsed time as HH:MM:SS

# Print the number of collisions and the time taken
print("Number of collisions:", collision_counts)
print("Time taken:", time_string)

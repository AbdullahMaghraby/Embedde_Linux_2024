#python program to access environment variables

import os

# Accessing a specific environment variable
print("Path directory:", os.environ.get('PATH'))

# Listing all environment variables
print("\nAll Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

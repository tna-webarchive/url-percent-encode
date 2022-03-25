"""
This module takes a crawl seed list and makes them URL-safe.
"""

import urllib.parse


####
# Functions
####
def encode(seed):
    """
    Encode a given seed URL.

    seed: A URL string
    """
    # First unencode the seed in case of pre-existing encoding
    unencoded_seed = urllib.parse.unquote(seed)

    # Encode the plain-text seed
    encoded_seed = urllib.parse.quote(unencoded_seed, safe="/:?=&")

    return encoded_seed

#### End of functions


####
# Main script
####
if __name__ == "__main__":
    # Prompt user for input file name
    print("Input txt file")
    input_file = input("> ")

    # Prompt user for output file name
    print("Output txt file name")
    output_file = input("> ")

    with open(input_file, "r") as seed_file, open(output_file, "w") as encoded_seed_file:
        # Add contents of input file to list
        seed_list = [item.rstrip("\n") for item in seed_file]

        # Encode each seed URL from the input file
        encoded_seed_list = [encode(item) for item in seed_list]

        # Write URL-safe seed URLs to the output file
        for item in encoded_seed_list:
            encoded_seed_file.write(f"{item}\n")



#### End of main script

#### End of module

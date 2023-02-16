# URL percent encode
A Python script used to make characters in seed lists "URL-safe" (e.g. encoding of unicode characters in URLs to their percent-encoded equivalent) for compatibility with crawlers such as Heritrix.

## Input
This script runs over an input list of URLs, formatted as a text file with one URL per line.  See `./example_seed_lists/bad.txt` and `./example_seed_lists/good.txt` for examples.

`bad.txt` - This file contains an example list of URLs that contain characters that are not URL-safe and so cannot be crawled.

`good.txt` - This file contains the same list of URLs but this time percent encoded so they can be crawled.

## To run:
When the `encode.py` script is run it will prompt the user for an input txt file name and an output txt file name.  No errors will be produced if all characters in seed URLs are URL-safe (so there's no need to check the input file before running).

Input txt - The txt file that needs to be encoded (with file path if relevant).

Output txt - The desired name of the file produced by this script (with file path if relevant).

## Output
The script will produce a txt file (named by the user) which will contain the same URLs from the input file but with any non-standard characters made URL-safe.

## Contributing
Pull requests are welcome.  For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

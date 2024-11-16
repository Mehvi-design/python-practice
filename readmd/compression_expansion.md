# File Compression and Expansion Challenge

## Objective
The goal of this challenge is to create two functions, `encodeFile` and `decodeFile`, that perform file compression and expansion on an ASCII art smiley face. The compression should reduce the file size, and the expansion should recover the original data.

## Task Requirements

1. **encodeFile:**
   - This function should open an existing file that contains an ASCII art smiley face.
   - Perform some modification or compression to the data in the file to reduce its size.
   - Write the modified, compressed data to a new file, with the goal of making the new file smaller than the original.
   - The original file size is 2,749 bytes, and the new file should ideally be no more than 2,748 bytes. The challenge is to make it even smaller if possible.

2. **decodeFile:**
   - This function should open the compressed file created by `encodeFile`.
   - Perform the reverse of the original modification (decompression) to expand the data back to its original form.
   - Return the original string that was in the original file, prior to compression.

## Parameters

- **filename**: The name of the original file that contains the ASCII art data (input to `encodeFile`).
- **newFilename**: The name of the file where the modified/compressed data will be saved (output from `encodeFile`).
  
## Expected Results

- **encodeFile**: Writes the compressed data to a new file, ideally reducing the size of the original file.
- **decodeFile**: Returns the original, uncompressed string from the compressed file.

## Example Flow

### Example 1
- **Original File (filename)**: An ASCII art smiley face with a size of 2,749 bytes.
- **Compressed File (newFilename)**: The file after being compressed with `encodeFile`. It should be smaller than the original (preferably less than 2,748 bytes).
- **Decoded String**: When the `decodeFile` function is used on the compressed file, it should return the exact original ASCII art smiley face string.

## Notes

- **Compression Goal**: The challenge is to reduce the file size while maintaining the ability to expand it back to the original size. Aim to achieve the smallest possible file size.
- **Reversibility**: Ensure that the decompression process (`decodeFile`) correctly reverses the compression done by `encodeFile` to return the exact original data.

## Conclusion

This challenge encourages exploration of file compression techniques while ensuring the ability to expand the file back to its original form. You'll be working with encoding and decoding strategies to optimize file storage and data retrieval.

#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_directory> <output_file>"
    exit 1
fi

SOURCE_DIR="$1"
OUTPUT_FILE="$2"

# Check if the input directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Input directory does not exist."
    exit 1
fi

# file evtx_dump from https://github.com/omerbenamram/evtx
# Check if evtx_dump is installed
command -v evtx_dump >/dev/null 2>&1 || { echo "evtx_dump is not installed. Exiting."; exit 1; }

# Check if the output file can be written to
if [ ! -w "$(dirname "$OUTPUT_FILE")" ]; then
    echo "Error: No write permission for output directory."
    exit 1
fi

# Initialize counters
total_files=0
processed_files=0

# Loop through each file in the input directory
for file in "$SOURCE_DIR"/*; do
    # Check if it is a regular file
    if [ -f "$file" ]; then
        ((total_files++))
        echo "Processing: \"$file\""
        evtx_dump "$file" -o jsonl >> "$OUTPUT_FILE" 2>&1
        if [ $? -eq 0 ]; then
            rm "$file"
            echo "File \"$file\" has been processed and deleted."
            ((processed_files++))
        else
            echo "Error processing \"$file\". Skipping deletion."
        fi
    fi
done

if [ "$total_files" -eq 0 ]; then
    echo "No files found in $SOURCE_DIR to process."
else
    echo "$processed_files out of $total_files files processed successfully."
fi

echo "Logs saved to $OUTPUT_FILE."

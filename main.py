import whisper
import csv
import json
import time

### Inputs ---------------------------------------------------------------------

# Model name
model_name = "small"

# Folder path
folder_path = "/Users/carlosyago/Espacio Creativo/Cuantica/24-01-27_Madre/"

# Audio file name
audio_file_name = "24-01-27_podcast_madre-1_madre.wav"

### -----------------------------------------------------------------------------


# Start the timer
start_time = time.time()


# Load the model
model = whisper.load_model(model_name)

# After loading the model time
loaded_time = time.time()

print("Model loaded in ", loaded_time - start_time, " seconds")

# Transcribe the audio file
audio_file_path = folder_path + audio_file_name
result = model.transcribe(audio_file_path)

# Stop the timer
end_time = time.time()

# Calculate the duration
duration = end_time - start_time
loading_duration = loaded_time - start_time
transcription_duration = end_time - loaded_time

# Add duration to the result
result["duration"] = duration
result["loading_duration"] = loading_duration
result["transcription_duration"] = transcription_duration
result["model_name"] = model_name


# Write the result to a file, just in case the rest fails
result_filename = folder_path + 'result.json'

with open(result_filename, 'a') as jsonfile:
    jsonfile.write(json.dumps(result))


segments = result["segments"]

# Filename for CSV output
csv_filename = folder_path + 'segments' + '-' +  model_name + '.csv'


# Open the CSV file in writing mode
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["start", "end", "text"])

    # Write the data rows
    for segment in segments:
        writer.writerow([segment["start"], segment["end"], segment["text"]])



print("Transcription completed in ", transcription_duration, " seconds")
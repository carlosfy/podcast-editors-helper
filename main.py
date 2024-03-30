import whisper
import csv
import json
import time
import os

from models import TranscriptionTask, TranslationRequest

def load_and_validate_input(filepath: str) -> TranslationRequest:
    with open(filepath, 'r') as file:
        data = json.load(file)

    # Convert the data to a TranslationRequest
    try:
        tasks = [TranscriptionTask(**task) for task in data["tasks"]]
    except Exception as e:
        raise Exception(f"Error while reading request.json: {e}")
    return TranslationRequest(tasks=tasks)


def validate_translation_request(translation_request: TranslationRequest):
    for task in translation_request.tasks:
        task.validate_paths()


def perform_transcription_task(task: TranscriptionTask):
    print("Performing transcription task: ", task)

    # Start the timer
    start_time = time.time()

    # Load the model
    model = whisper.load_model(task.model)

    # After loading the model time
    loaded_time = time.time()

    loading_duration = loaded_time - start_time

    print("Model loaded in ", loading_duration, " seconds")


    audio_file_path = os.path.join(task.folder, task.file) # folder_path + audio_file_name
    result = model.transcribe(audio_file_path)

    # Stop the timer
    end_time = time.time()

    # Calculate the duration
    duration = end_time - start_time
    loading_duration = loaded_time - start_time
    transcription_duration = end_time - loaded_time

    # Create log object
    log = {}
    log["task"] = json.dumps(task.__dict__)
    log["duration"] = duration
    log["loading_duration"] = loading_duration
    log["transcription_duration"] = transcription_duration

    # Write the result to a file, just in case the rest fails
    logs_filename = os.path.join(os.path.curdir, 'logs.txt')

    with open(logs_filename, 'a') as jsonfile:
        jsonfile.write(json.dumps(log) + "\n")

    segments = result["segments"]

    # Filename for CSV output
    csv_filename = os.path.join(task.folder, 'transcription' + '-' + task.speaker + '-' +  task.model  + '.csv')


    # Open the CSV file in writing mode
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["start", "end", "text"])

        # Write the data rows
        for segment in segments:
            writer.writerow([segment["start"], segment["end"], segment["text"]])
    
    print("Transcription completed in", transcription_duration, "seconds using model", task.model)



def main():
    # Load translation request
    translation_request = load_and_validate_input("request.json")

    # Validate the translation request
    validate_translation_request(translation_request)

    # Perform the transcription tasks
    tasks = translation_request.tasks
    for task in tasks:
        perform_transcription_task(task)


if __name__ == "__main__":
    main()
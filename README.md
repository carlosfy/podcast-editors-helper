# Podcast Editing Tool

This repository contains a tool designed to assist in editing podcasts by transcribing audio to text with time annotations, enabling efficient search and edit capabilities.

## Functionalities

- Transcription of audio into text, complete with time stamps, to facilitate easy searching and editing of podcast audio.

## How to Run

1. Create a `request.json` file in the root directory of the project.
2. Define your transcription tasks in `request.json` using the following format:

```json
{
    "tasks": [
        {
            "folder": "Path to the folder containing the audio file; outputs will be saved here as well",
            "file": "Name of the audio file to transcribe",
            "speaker": "Name of the speaker in the audio",
            "model": "Transcription model to use (options: tiny, small, medium, large)"
        }
        // Add more tasks as needed
    ]
}
```

## Current version
0.0.2


## Changelog

See the [Changelog](CHANGELOG.md) for a detailed history of changes between releases.

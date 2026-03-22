# Docker AI

This project has many offline AI workflows.

## from video to audio

[ffmpeg]()

## from video to images

[ffmpeg]()

## from video to text (transcription/extraction)

?

## from audio to text (speech)

?

## from text to text (speakking)

[espeak]()

## from text to text (translating)

[argostranslate]()

## from txt to audio (text-to-speech)

```bash
docker run -v .:/files -w /files -e input=file.txt -e output=file.wav tmvdl/ai:txt2wav
# In Portuguese
docker run -v .:/files -w /files -e voice=pt-br -e input=file.txt -e output=file.wav tmvdl/ai:txt2wav
```

## from pdf file to text

[Python PDFReader](#)

## license

[MIT](./LICENSE)

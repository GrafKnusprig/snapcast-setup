@echo off
ffmpeg -f dshow -i audio="Voicemeeter Out B3 (VB-Audio Voicemeeter VAIO)" -f s16le -acodec pcm_s16le -ac 2 -ar 48000 tcp://127.0.0.1:4953
pause

# Snapcast Server on Windows with Docker without WSL

**Things you need:**

- Docker
- ffmpeg
- a virtual device

> Why docker?

Keeps things easy. The script copies the script and the config to the right places.

> What's this?

fakeinput.py listens for incoming raw PCM audio over TCP and forwards it directly to Snapserver via stdout, pretending to be a live audio source.

> Why?

Because Snapserver doesn’t accept audio over TCP directly, so we fake it by tricking it into thinking our script is a live audio input.

> How?

Start the snapserver with the bat file. When started, start the ffmpeg bat. Adjust you path's and device accordingly.

> What devices do I have?

```
ffmpeg -list_devices true -f dshow -i dummy
```

gives you a list.

> How to listen?

On Android use:

https://github.com/badaix/snapdroid

On Raspberry use:

```sudo apt install snapclient```

Run this on your Snapserver:

```hostname -I```

returns something like 192.168.1.42

Find your USB soundcard ID

Run:

```aplay -l```

Look for something like:

```card 1: USB [USB Audio], device 0: USB Audio```

→ You'll use ```plughw:1,0```

```sudo systemctl edit snapclient```

```[Service]
ExecStart=
ExecStart=/usr/bin/snapclient --host 192.168.1.42 --latency 120 --clientname RPi-Kitchen --soundcard plughw:1,0
Nice=-5```

You can skip the latency, this is just if it is out of sync.

```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

```
sudo systemctl restart snapclient
```
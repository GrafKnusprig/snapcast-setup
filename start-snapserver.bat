@echo off
docker run --rm --name snapserver ^
 -v /tmp/snapcast:/tmp/snapcast ^
 -v D:\docker\snapserver-docker\snapserver.conf:/etc/snapserver.conf ^
 -v D:\docker\snapserver-docker\fakeinput.py:/app/fakeinput.py ^
 -p 1704:1704 -p 1705:1705 -p 1780:1780 -p 4953:4953 ^
 ivdata/snapserver
pause

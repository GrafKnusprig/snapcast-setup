## Connect direclty over LAN

Go to:
System Settings → General → Sharing → Internet Sharing
	•	Share your Wi-Fi connection to your Ethernet (enX or similar)
	•	Turn on “Internet Sharing”

ssh snap@snapbox.local

## Add wifi network

```bash

nmcli connection show

nmcli dev wifi list

nmcli dev wifi connect "MyWifiName" password "MyWifiPassword"

nmcli connection show MyWifiName

nmcli connection modify MyWifiName connection.autoconnect yes

sudo reboot

```

How to delete networks:

```bash
nmcli connection delete preconfigured
```

Connect while in range:

```bash
nmcli dev wifi connect "MyWifiName" password "MyWifiPassword"
```

Add when not in range:

```bash
nmcli connection add type wifi ifname wlan0 con-name Tech_D0053217 ssid "MyWifiName"
nmcli connection modify MyWifiName wifi-sec.key-mgmt wpa-psk wifi-sec.psk "MyWifiPassword"
nmcli connection modify MyWifiName connection.autoconnect yes
nmcli connection modify MyWifiName connection.autoconnect-priority 100
```

## Modify snapclient

```

sudo systemctl list-units --type=service

sudo systemctl edit snapclient
```
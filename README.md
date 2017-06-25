# Usage

## Production
- Enalble i2c
- Enable camera
- Run `sudo usermod -a -G video $(whoami)`
- Run `$HOME/Desktop/walky-client/lib/bootstrap.sh`
- Move `settings.py` from your local
- Run `python mqtt_client.py`

## Test
- Enalble i2c
- Run `python client_test.py`

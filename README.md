# skyblock-python

Initial stages currently, basic (to be async) package for iteracting with the skyblock.net API.

## Install

`pip install skyblock` (or maybe `python -m pip`, or `py -m pip` it depends.)

## Usage

### Get server

```python
from skyblock import * 

players = getPlayers('economy') # economy, skywars or survival
print(players)
```

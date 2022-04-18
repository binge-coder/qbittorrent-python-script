from decouple import config     #to get login details from .env 
import qbittorrentapi


qbt_client = qbittorrentapi.Client(host = "localhost:8080", username = config('USER'), password = config('PASSWORD'))

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)
'''
print(f'qBittorrent: {qbt_client.app.version}')
print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')
for k, v in qbt_client.app.build_info.items():
    print(f'{k}: {v}')
'''

'''
for torrent in qbt_client.torrents_info():
    print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})')
'''

'''
#pause all torrents
qbt_client.torrents.pause.all()

'''

qbt_client.log.main.warning()
qbt_client.log.main.normal()







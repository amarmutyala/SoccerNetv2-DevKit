import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/home/amar/Desktop/soccernet")

mySoccerNetDownloader.password = 's0cc3rn3t'


# mySoccerNetDownloader.downloadDataTask(task="calibration", split=["train","valid","test","challenge"])

# mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train", "test", "challenge"])
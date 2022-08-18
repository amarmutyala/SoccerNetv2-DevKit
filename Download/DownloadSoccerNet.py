import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/home/amar/Desktop/soccernet")

mySoccerNetDownloader.password = 's0cc3rn3t'

# mySoccerNetDownloader.downloadGames(files=["Labels-v2.json", "1_ResNET_TF2.npy", "2_ResNET_TF2.npy"], split=[
#                                     "train", "valid", "test", "challenge"])  # download Features


# mySoccerNetDownloader.downloadGames(files=["1_field_calib_ccbv.json", "2_field_calib_ccbv.json", "1_player_boundingbox_maskrcnn.json","2_player_boundingbox_maskrcnn.json"], split=[
#                                     "train", "valid", "test", "challenge"])  # download Features

# download only test dataset
mySoccerNetDownloader.downloadGames(files=["1_field_calib_ccbv.json", "2_field_calib_ccbv.json", "1_player_boundingbox_maskrcnn.json","2_player_boundingbox_maskrcnn.json"], split=[
                                    "test"])  # download Features

# mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv"], split=["train","valid","test","challenge"])
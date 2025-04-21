import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader=SoccerNetDownloader(LocalDirectory="D:\Final Thesis\Data\MVF\Action Spoting")
mySoccerNetDownloader.downloadGames(files=["Labels-cameras.json"], split=["train","valid","test"], task="frames")
from SoccerNet.utils import getListGames
# print(getListGames(split="train")) # return list of games recommended for training
# print(getListGames(split="valid")) # return list of games recommended for validation
print(*getListGames(split="test"), sep='\n') # return list of games recommended for testing
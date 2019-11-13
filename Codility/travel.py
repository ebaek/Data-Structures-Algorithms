from collections import defaultdict
from datetime import datetime

def solution(S):
    reorganized = ""
    
    locationDict = defaultdict(list)
    splitPhotos = S.split("\n")

    for photo in splitPhotos:
        photoParts = photo.split(",")
        photoType = photoParts[0].split(".")[1]
        
        location = photoParts[1].strip()
        timeInfo = photoParts[-1].strip()
        
        photoInfo = (timeInfo, photoType)
        locationDict[location].append(photoInfo)
    
    for key, photoInfos in locationDict.items():
        photoInfos.sort(key = lambda date: datetime.strptime(date[0], '%Y-%m-%d %H:%M:%S'))

    for photo in splitPhotos:
        photoParts = photo.split(",")
        
        location = photoParts[1].strip()
        timeInfo = photoParts[-1].strip()
        
        newName = location
        
        dates = locationDict[location]
        numZeroes = len(str(len(dates)))

        for idx, date in enumerate(dates):
            if date[0] == timeInfo:
                preZeroes = numZeroes - len(str(idx+1))
                
                for _ in range(preZeroes):
                    newName += "0"
                
                newName = newName + str(idx+1) + "." + date[-1]
                reorganized = reorganized + newName + "\n"
    
    return reorganized
                
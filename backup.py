FilePath = 'temp' 
modifiedTime = os.path.getmtime(FilePath)

timeStamp =  datetime.datetime.fromtimestamp(modifiedTime).strftime("")
os.rename(FilePath,FilePath+"_"+timeStamp)
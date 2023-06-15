import sys
import requests
import time
import wave

filename = sys.argv[1]
headers = {'Content-Type': "audio/wav",'authorization': "bd513036b6cf45bcb079aade18e1e18b"}
audob=wave.open(filename,"rb")
duration=audob.getnframes()/audob.getframerate()
#wait_dur=(10*duration)/100
wait_dur=0.5

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
response = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(filename))


print("File Uploaded  Successfully")


endpoint = "https://api.assemblyai.com/v2/transcript"
json = { "audio_url": response.json()["upload_url"] }

response = requests.post(endpoint, json=json, headers=headers)


print("The Request is",response.json()["status"])


transcript=endpoint+"/"+response.json()["id"]
print("The Request is",requests.get(transcript,headers=headers).json()["status"])


con=requests.get(transcript,headers=headers).json()["status"]
print("Waiting",end=" ",flush=True)
while con!="completed":
    print(".",end=" ",flush=True)
    time.sleep(wait_dur)
    con=requests.get(transcript,headers=headers).json()["status"]
    
print("Conversion Completed")
print(requests.get(transcript,headers=headers).json()["text"])
ob=open("check.txt","w")
ob.write(requests.get(transcript,headers=headers).json()["text"])
ob.close()




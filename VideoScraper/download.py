# imported the requests library
import requests
url = "https://content.jwplatform.com/videos/AsignbxN-1Tm7nwch.mp4"

# URL of the image to be downloaded is defined as image_url
r = requests.get(url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("AsignbxN-1Tm7nwch.mp4",'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)

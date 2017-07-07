Demo application to showcase Bring Your Own Storage on App Service Linux

About the app:
- This app is a single page application that constantly pings it's own endpoint to load images located within /tmp/test1 directory. 
- If there are non-image files located in the file share, the page will fail to load those specific files but it won't break anything.
- This site pings itself rapidly to show the low latency of updating Azure Files, so keep that in mind as your server will get flooded with requests.  

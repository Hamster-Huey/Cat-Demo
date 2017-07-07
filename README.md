Demo application to showcase Bring Your Own Storage on App Service Linux

About the app:
- This app is a single page application that constantly pings it's own endpoint to load images located within /tmp/test1 directory. 
- The images MUST be named as such: test0.jpg, test1.jpg, ..., testn.jpg
- The images within the storage account must be located in app/images

Script located in /demo
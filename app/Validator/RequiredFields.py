# DONT ADD TOKEN HERE
#AUTH
REGISTER_FIELDS=['name','email','age','gender','address','postalcode']
REGISTER_AUTH_FIELDS=['name','email','age','gender','address','postalcode','ministry_name','position','secret_code']
LOGIN_FIELDS=['email','password']
LOGOUT_FIELDS=['email']
FORGET_PASSWORD_FIELDS=['email']
GET_USER_FIELDS=['email']

#FEED
ADD_POST=['email','image_url','title','description']
VIEW_MY_POSTS=['email']
DELETE_MY_POSTS=['email','post_id']
VIEW_ALL_POSTS=[]

#NOTE
ADD_NOTE=['email','lat','lon','text']
VIEW_MY_NOTES=['email']
DELETE_MY_NOTE=['email','note_id']
VIEW_PUBLIC_NOTES=[]

#REPORT GENERATOR
GET_DATES=['lattitude','longitude']
GET_IMAGE=['lattitude','longitude','date']
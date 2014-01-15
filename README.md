pystorage
=========

A simple python file-storage solution using dropbox and google app engine 


###What services we use here###
* [Dropbox](dropbox.com) - to store your files.
* [Google App Engine](appengine.google.com) - python runtime where we implement this handler code.


###How we build our environment###
#####Dropbox#####
* Create a dropbox account.
* Create a folder inside your "Public" directory.
* Create a test file inside that folder, Right-click and view its public url and find out your user-id. (public url will be in the syntax: dl.dropboxusercontent.com/u/\<USERID\>/\<YOURFOLDER\>/testfile)
* Input user-id and folder-name as variable values in the code.


#####Google App Engine#####
* Create a Google App Engine account.
* register a unique app-id.
* now your application will run at \<app-id\>.appspot.com
* Dowload [Python](python.org/download/releases/2.7.4/) and [Google App Engine SDK](googleappengine.googlecode.com/files/GoogleAppEngine-1.8.9.msi)
* Download this project.
* Select "src" folder as the project folder in the GAE SDK.
* Deploy it to App Engine.

###Example###
http://py-storage.appspot.com/test

This serves the file 'test' that is located in the specified folder of my Dropbox's Public directory.



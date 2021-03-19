import dropbox
import cv2
import time 
import random
start_time = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    print(number)
    videoCaptureObject = cv2.VideoCapture(0)
    print("initialized") 
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        print("read")
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        print("write")
        start_time = time.time()
        result = False
    return image_name
    print("snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(image_name):
    access_token = "LRr9xiTEvh8AAAAAAAAAAeZdpO22feXDaqeSpHR7AJhgXhb2Gz4M8iEB5jgIIzpP"
    file = image_name
    file_from = file
    file_to = "/new-folder/" + image_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file_uploaded")
def main():
    take_pic = True
    while(True):
        while(take_pic):
            name = takeSnapshot()
            upload_file(name)
            take_pic = False
        if(30 <= time.time() - start_time <= 35):
            take_pic = True
        else:
            take_pic = False
main()
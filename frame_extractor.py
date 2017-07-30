import cv2

def extract(path_to_video,output_dir,num_images):
    cap = cv2.VideoCapture(path_to_video)

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(num_frames)
    increment = num_frames//num_images
    print(increment)

    frame = 0
    success = 1
    while(success):
        success,img = cap.read()
    # 		print(count)

        if(frame%increment == 0):
            print(frame)
            cv2.imwrite(output_dir+"/frame%d.jpg" % frame, img)  

        frame+=1


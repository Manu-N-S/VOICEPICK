from yolov5 import train, detect

if __name__ == '__main__':  
    train.run(imgsz=416, data='data.yaml', weights='runs/train/exp2/weights/best.pt',epochs=100,batch=64, workers = 4)
    detect.run(imgsz=416,weights='runs/train/exp3/weights/best.pt', 
    source ='test.jpg',
    view_img=True)
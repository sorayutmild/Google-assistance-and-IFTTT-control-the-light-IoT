import cv2, os, numpy as np
import requests
cap = cv2.VideoCapture(0)
path = './picture_cap/'
h = s = p = b = 0

def control_lights(state):
    requests.post("https://maker.ifttt.com/trigger/"+state+"/with/key/cqF-cJMQ_eO9pdu5S7u2tA")

while True:
    _,frame = cap.read()
    key = cv2.waitKey(1) & 0xFF
    if key == ord('h') : h+=1; cv2.imwrite(path + 'hammer_' + str(h) + '.png', frame)
    if key == ord('s'): s += 1; cv2.imwrite(path + 'scissors_' + str(s) + '.png', frame)
    if key == ord('p') : p +=1; cv2.imwrite(path + 'paper_' + str(p) + '.png', frame)
    if key == ord('b'): b += 1; cv2.imwrite(path + 'background_' + str(b) + '.png', frame)
    y = []; D =[]
    for fname in os.listdir(path):
        if '.png' in fname:
            x = cv2.imread(path + fname)
            y.append(fname.split('_')[0])
            D.append(np.sum((x - frame)**2))
    if len(D) > 0 :
        ans = y[D.index(min(D))]
        print(ans)
    cv2.imshow('frame',frame)
    if ans == "bye":
        exit()
    elif ans == "paper":
        control_lights("turn_ON")
    elif ans == "hammer":
        control_lights("turn_OFF")
    else:
        print("Try again")

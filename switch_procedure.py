switch_status = False #ปิด

def turnon(): #เปิดไฟ
    global switch_status
    switch_status = True
    print("ไฟเปิด")

def turnoff(): #ปิดไฟ
    global switch_status
    switch_status = False
    print("ไฟปิด")

if __name__=="__main__":    
print(f'สถานะไฟ: {switch_status}')
turnon()
turnoff()
turnon()


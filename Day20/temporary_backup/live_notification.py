live_notification=[]
n=int(input("Enter the no.of.messages"))
for i in range(n):
    msg=input("Enter message")
    live_notification.append(msg)
    print(live_notification)
    k=print(f"messages to be printed")
    print(f"Notification {i+1}: {k} Recent messages.")
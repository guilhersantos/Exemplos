from time import time,sleep
from multiprocessing import Process, SimpleQueue
from threading import Thread

var_tmp = {}

def pra_sempre(i, simp):
    a = 0
    x = i
    z = {}
    for i in range(100000000): a+=1 + x
    print('Resultado '+str(x)+' '+str(a))
    z[x] = a
    simp.put(z)


def fnc_proc(i, var_tmp):
    
    simp = SimpleQueue()
    p = Process(target=pra_sempre, args=(i, simp,))
    p.start()
    result = simp.get()
    print(result)
    p.join()
    var_tmp[i] = result

'#--------------Multiprocessing--------------#'
def Multiprocessing():
    global var_tmp 
    inicio = time()

    th = {}
    
    for i in range(10):
        var_tmp[i] = None
        th[i] = Thread(target=fnc_proc, args=(i,var_tmp), daemon=True) 
        th[i].start()
    
    while 1:
        cont = 0
        sleep(0.1)
        for i in range(10):
            if var_tmp[i] != None:
                cont += 1
            else:
                cont = 0
        if cont == 10:
            break

    print('Time Multiprocessing: ', time()-inicio) # 0.05443859100341797

if __name__ == '__main__':
    

    Multiprocessing()

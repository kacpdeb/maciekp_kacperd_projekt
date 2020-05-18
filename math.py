import math
import matplotlib.pyplot as plt

def spadek_swobodny():
    z = 0

    print('Podaj znane wartości:')

    print('*możesz wpisać nazwy planet układu słonecznego i księżyc')
    gs = input('przyspiesznie g = ')

    if ',' in gs:
        gs = list(gs)
        index = gs.index(',')
        gs.insert(index,'.')
        gs.remove(',')
        gs = ''.join(gs)

    if gs == 'ziemia':
        gs = '9.81'
    elif gs == 'księżyc':
        gs ='1.6'
    elif gs == 'merkury':
        gs ='3.701'
    elif gs == 'wenus':
        gs ='8.87'
    elif gs == 'mars':
        gs ='3.934'
    elif gs == 'jowisz':
        gs ='24.79'
    elif gs == 'saturn':
        gs ='8.96'
    elif gs == 'uran':
        gs ='8.69'
    elif gs == 'neptun':
        gs ='11'

    hs = input('wysokość H = ')

    if ',' in hs:
        hs = list(hs)
        index = hs.index(',')
        hs.insert(index,'.')
        hs.remove(',')
        hs = ''.join(hs)

    ts = input('czas spadania t = ')

    if ',' in ts:
        ts = list(ts)
        index = ts.index(',')
        ts.insert(index,'.')
        ts.remove(',')
        ts = ''.join(ts)

    ms = input('masa ciała m = ')

    if ',' in ms:
        ms = list(ms)
        index = ms.index(',')
        ms.insert(index,'.')
        ms.remove(',')
        ms = ''.join(ms)

    vs = input('prędkość w chwili uderzenia w ziemie v = ')

    if ',' in vs:
        vs = list(vs)
        index = vs.index(',')
        vs.insert(index,'.')
        vs.remove(',')
        vs = ''.join(vs)

    es = input('energia potencjalna na maksymalnej wysokości oraz energia kinetyczna na zerowej wysokości Ep = Ek = ')

    if ',' in es:
        es = list(es)
        index = es.index(',')
        es.insert(index,'.')
        es.remove(',')
        es = ''.join(es)

    print('\n')

    while z < 7:

        #liczenie g
        if bool(gs) == False and bool(hs) == True and bool(ts) == True:
            hs = float(hs)
            ts = float(ts)
            gs = (2*hs)/(ts*ts)
            print('przyspieszenie g = ',gs, '\n')
            hs = str(hs)
            ts = str(ts)
            gs = str(gs)

        if bool(gs) == False and bool(es) == True and bool(hs) == True and bool(ms) == True:
            es = float(es)
            hs = float(hs)
            ms = float(ms)
            gs = es/(ms*hs)
            print('przyspieszenie g = ', gs, '\n')
            es = str(es)
            hs = str(hs)
            ms = str(ms)
            gs = str(gs)

        if bool(gs) == False and bool(hs) == True and bool(vs) == True:
            hs = float(hs)
            vs = float(vs)
            gs = (vs*vs)/(2*hs)
            hs = str(hs)
            vs = str(vs)
            gs = str(gs)


        #liczenie h
        if bool(hs) == False and bool(gs) == True and bool(ts) == True:
            gs = float(gs)
            ts = float(ts)
            hs = (gs*ts*ts)/2
            print('wysokość H = ', hs, '\n')
            gs = str(gs)
            ts = str(ts)
            hs = str(hs)

        if bool(hs) == False and bool(es) == True and bool(ms) == True and bool(gs) == True:
            es = float(es)
            gs = float(gs)
            ms = float(ms)
            hs = es/(ms*gs)
            print('wysokość H = ', hs, '\n')
            es = str(es)
            gs = str(gs)
            ms = str(ms)
            hs = str(hs)

        if bool(hs) == False and bool(gs) == True and bool(vs) == True:
            gs = float(gs)
            vs = float(vs)
            hs = (vs*vs)/(2*gs)
            print('wysokość H = ', hs, '\n')
            gs = str(gs)
            vs = str(vs)
            hs = str(hs)

        #liczenie t
        if bool(ts) == False and bool(hs) == True and bool(gs) == True:
            hs = float(hs)
            gs = float(gs)
            ts = math.sqrt((2*hs)/gs)
            print('czas spadania t = ', ts, '\n')
            hs = str(hs)
            gs = str(gs)
            ts = str(ts)

        #liczenie m
        if bool(ms) == False and bool(es) == True and bool(gs) == True and bool(hs) == True:
            es = float(es)
            gs = float(gs)
            hs = float(hs)
            ms = es/(gs*hs)
            print('masa ciała m = ', ms, '\n')
            es = str(es)
            gs = str(gs)
            hs = str(hs)
            ms = str(ms)

        if bool(ms) == False and bool(es) == True and bool(vs) == True:
            es = float(es)
            vs = float(vs)
            ms = (es*vs*vs)/2
            print('masa ciała m = ', ms, '\n')
            es = str(es)
            vs = str(vs)
            ms = str(ms)

        #liczenie v
        if bool(vs) == False and bool(gs) == True and bool(ts) == True:
            gs = float(gs)
            ts = float(ts)
            vs = gs*ts
            print('prędkość w chwili uderzenia w ziemie v = ', vs, '\n')
            gs = str(gs)
            ts = str(ts)
            vs = str(vs)

        if bool(vs) == False and bool(gs) == True and bool(hs) == True:
            gs = float(gs)
            hs = float(hs)
            vs = math.sqrt(2*gs*hs)
            print('prędkość w chwili uderzenia w ziemie v = ', vs, '\n')
            gs = str(gs)
            hs = str(hs)
            vs = str(vs)

        #liczenie energii
        if bool(es) == False :          
            if bool(ms) == True and bool(gs) == True and bool(hs):
                ms = float(ms)
                gs = float(gs)
                hs = float(hs)
                es = ms*gs*hs
                print('energia potencjalna i kinetyczna wynoszą Ep = Ek = ', es, '\n')
                ms = str(ms)
                gs = str(gs)
                hs = str(hs)
                es = str(es)
            elif bool(vs) == True and bool(ms) == bool:
                vs = float(vs)
                ms = float(ms)
                es = (ms*vs*vs)/2
                print('energia potencjalna i kinetyczna wynoszą Ep = Ek = ', es, '\n')
                ms = str(ms)
                vs = str(vs)
                es = str(es)
        
        if bool(gs) == True and bool(hs) == True and bool(ts) == True and bool(ms) == True and bool(vs) == True and bool(es) == True:
            print('Wszystko wartości zostały obliczone')
            break
        
        z = z + 1

    print('\n')
    print('WYNIK: \n')
    if bool(gs) == True:
        print('przyspiesznie: \ng = ', gs, ' m/s2\n')
    if bool(hs) == True:
        print('wysokość: \nH = ', hs, ' m\n')
    if bool(ts) == True:
        print('czas spadania: \nt = ', ts, ' s\n')
    if bool(ms) == True:
        print('masa ciała: \nm = ', ms, ' kg\n')
    if bool(vs) == True:
        print('prędkość w chwili uderzenia w ziemie: \nv = ', vs, ' m/s\n')
    if bool(es) == True:
        print('energia potencjalna na maksymalnej wysokości oraz energia kinetyczna na zerowej wysokości: \nEp = Ek = ', es ,' J\n')

    if bool(ts) == True and bool(gs) == True:
        #zamiana wartości na int
        ts = float(ts)
        ts = ts*1000
        ts = str(ts)
        ts = list(ts)
        a = ts.index('.')
        b = list(ts[:(a)])
        ts = ''.join(b)
        ts = int(ts)

        #tworzenie wykresu
        w = range(0, ts, 1)
        y = []
        x = []

        for i in w:
            y.append(((float(gs)*i*i)/2)/1000000)
            x.append(i/1000)

        plt.plot(x, y)
        plt.title('Wykres drogi od czasu')
        plt.grid(True)
        plt.xlabel('s')
        plt.ylabel('m')
        plt.draw()
        plt.show()
















def ruch_postepowy():

    z = 0

    print('Podaj znane wartości:')

    ap = input('przyspiesznie a=')

    if ',' in ap:
        ap = list(ap)
        index = ap.index(',')
        ap.insert(index,'.')
        ap.remove(',')
        ap = ''.join(ap)

    v0p = input('prędkość początkowa vp=')

    if ',' in v0p:
        v0p = list(v0p)
        index = v0p.index(',')
        v0p.insert(index,'.')
        v0p.remove(',')
        v0p = ''.join(v0p)

    vp = input('prędkość końcowa v=')

    if ',' in vp:
        vp = list(vp)
        index = vp.index(',')
        vp.insert(index,'.')
        vp.remove(',')
        vp = ''.join(vp)

    x0p = input('położenie początkowe xp=')

    if ',' in x0p:
        x0p = list(x0p)
        index = x0p.index(',')
        x0p.insert(index,'.')
        x0p.remove(',')
        x0p = ''.join(x0p)

    xp = input('położenie końcowe x=')

    if ',' in xp:
        xp = list(xp)
        index = xp.index(',')
        xp.insert(index,'.')
        xp.remove(',')
        xp = ''.join(xp)

    fp = input('wypadkowa siła działająca na ciało F=')

    if ',' in fp:
        fp = list(fp)
        index = fp.index(',')
        fp.insert(index,'.')
        fp.remove(',')
        fp = ''.join(fp)

    mp = input('masa ciała m=')

    if ',' in mp:
        mp = list(mp)
        index = mp.index(',')
        mp.insert(index,'.')
        mp.remove(',')
        mp = ''.join(mp)

    tp = input('czas ruchu t=')

    if ',' in tp:
        tp = list(tp)
        index = tp.index(',')
        tp.insert(index,'.')
        tp.remove(',')
        tp = ''.join(tp)

    sp = input('pokonana droga s=')

    if ',' in sp:
        sp = list(sp)
        index = sp.index(',')
        sp.insert(index,'.')
        sp.remove(',')
        sp = ''.join(sp)

    print('\n')

    while z < 8:

        #liczenie F
        if bool(fp) == False and bool(mp) == True and bool(ap) == True:
            mp = float(mp)
            ap = float(ap)
            fp = mp*ap
            print('wypadkowa siła działająca na ciało F = ', fp, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie m
        if bool(mp) == False and bool(fp) == True and bool(ap) == True:
            fp = float(fp)
            ap = float(ap)
            mp = fp/ap
            print('masa ciała m = ', mp, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie a
        if bool(ap) == False and bool(fp) == True and bool(mp) == True:
            fp = float(fp)
            mp = float(mp)
            ap = fp/mp
            print('przyspieszenie a = ', ap, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie x
        if bool(xp) == False and bool(sp) == True and bool(x0p) == True :
            sp = float(sp)
            x0p = float(x0p)
            xp = x0p + sp
            print('położenie końcowe x = ', xp, '\n')
            sp = str(sp)
            x0p = str(x0p)
            xp = str(xp)

        #liczenie xp
        if bool(x0p) == False and bool(xp) == True and bool(sp) == True:
            sp = float(sp)
            xp = float(xp)
            x0p = xp - sp
            print('położenie początkowe xp = ', x0p, '\n')
            sp = str(sp)
            xp = str(xp)
            x0p = str(x0p)
    
        #liczenie a
        if bool(ap) == False and bool(vp) == True and bool(tp) == True and bool(v0p) == True:
            vp = float(vp)
            tp = float(tp)
            v0p = float(v0p)
            ap = (vp - v0p)/tp
            print('przyspieszenie a = ', ap, '\n')
            vp = str(vp)
            tp = str(tp)
            v0p = str(v0p)
            ap = str(ap)
   
        if bool(ap) == False and bool(xp) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True:
            xp = float(xp)
            x0p = float(x0p)
            v0p = float(v0p)
            tp = float(tp)
            ap = ((2*xp) - (2*x0p) - (2*v0p*tp))/(tp*tp)
            sp = xp - x0p
            print('przyspieszenie a = ', ap, '\n')
            xp = str(xp)
            x0p = str(x0p)
            v0p = str(v0p)
            tp = str(tp)
            ap = str(ap)
        
        #liczenie x
        if bool(xp) == False and bool(xp) == False and bool(ap) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True:
            ap = float(ap)
            x0p = float(x0p)
            v0p = float(v0p)
            tp = float(tp)
            xp = x0p + (v0p*tp) + ((ap*tp*tp)/2)
            print('położenie końcowe x = ', xp, '\n')
            ap = str(ap)
            x0p = str(x0p)
            v0p = str(v0p)
            tp = str(tp)
            xp = str(xp)

        #liczenie s
        if bool(sp) == False:
            if bool(x0p) == True and bool(xp) == True:
                x0p = float(x0p)
                xp = float(xp)
                sp = xp - x0p
                sp = math.fabs(sp)
                print('przebyta droga s = ', sp, '\n')
                x0p = str(x0p)
                xp = str(xp)
                sp = str(sp)
            elif bool(v0p) == True and bool(tp) == True and bool(ap) == True:
                v0p = float(v0p)
                tp = float(tp)
                ap = float(ap)
                sp = (v0p*tp)+((ap*tp*tp)/2)
                print('przebyta droga s = ', sp, '\n')
                v0p = str(v0p)
                tp = str(tp)
                ap = str(ap)
                sp = str(sp)

        #liczenie t
        if bool(tp) == False and bool(vp) == True and bool(v0p) == True and bool(ap) == True and float(ap) != 0:
            vp = float(vp)
            v0p = float(v0p)
            ap = float(ap)
            tp = (vp - v0p)/ap
            print('Czas ruchu t = ', tp, '\n')
            vp = str(vp)
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)

        if bool(tp) == False and bool(sp) == True and bool(v0p) == True and float(ap) == 0:
            sp = float(sp)
            v0p = float(v0p)
            tp = sp/v0p
            print('Czas ruchu t = ', tp, '\n')
            sp = str(sp)
            v0p = str(v0p)
            tp = str(tp)

        #liczenie t z równania kwadratowego
        if  bool(tp) == False and bool(ap) == True and bool(v0p) == True and bool(xp) == True and bool(x0p) == True:
            x0p = float(x0p)
            xp = float(xp)
            v0p = float(v0p)
            ap = float(ap)
            c = x0p - xp
            b = v0p
            a = ap/2
            delta = (b*b) - (4*a*c)
            x0p = str(x0p)
            xp = str(xp)
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)
            if delta > 0:
                pdelta = math.sqrt(delta)
                tp1 = (-b + pdelta)/(2*a)
                tp2 = (-b - pdelta)/(2*a)
                if tp1 > 0:
                    tp = tp1
                    print('czas ruchu t = ', tp, '\n')
                elif tp2 > 0:
                    tp = tp2
                    print('czas ruchu t = ', tp, '\n')
                else:
                    print('Nie da się obliczyć czasu trwania ruchu', '\n')
            elif delta == 0:
                tp = (-b)/(2*a)
                print('czas ruchu t = ', tp, '\n')
            else:
                print('Nie da się obliczyć czasu trwania ruchu', '\n')

        #liczenie v
        if bool(vp) == False and bool(v0p) == True and bool(ap) == True and bool(tp) == True:
            v0p = float(v0p)
            ap = float(ap)
            tp = float(tp)
            vp = v0p + (ap * tp)
            print('prędkość końcowa V = ', vp, '\n')
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)
            vp = str(vp)

        #liczenie vp
        if bool(v0p) == False and bool(vp) == True and bool(ap) == True and bool(tp) == True:
            vp = float(vp)
            ap = float(ap)
            tp = float(tp)
            v0p = vp - (ap * tp)
            print('prędkość początkowa Vp = ', v0p, '\n')
            vp = str(vp)
            ap = str(ap)
            tp = str(tp)
            v0p = str(v0p)

        if bool(v0p) == False and bool(xp) == True and bool(x0p) == True and bool(tp) == True and bool(ap) == True:
            xp = float(xp)
            x0p = float(x0p)
            tp = float(tp)
            ap = float(ap)
            v0p = ((xp - x0p)/tp)-((ap*tp)/2)
            print('prędkość początkowa Vp = ', v0p, '\n')
            xp = str(xp)
            x0p = str(x0p)
            tp = str(tp)
            ap = str(ap)
            v0p = str(v0p)

        #liczenie xp
        if bool(x0p) == False and  bool(sp) == True and bool(xp) == True:
            xp = float(xp)
            sp = float(sp)
            x0p = xp - sp
            print('położenie początkowe xp = ', x0p, '\n')
            xp = str(xp)
            sp = str(sp)
            x0p = str(x0p)


        if bool(ap) == True and bool(xp) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True and bool(vp) == True and bool(sp) == True and bool(fp) == True and bool(mp) == True:
            print('wszystkie wartości są policzone', )
            break

        z = z + 1
    
    print('\n')
    print('WYNIK:\n ')
    if bool(ap) == True:
        print('przyspiesznie: \na = ', ap , " m/s2\n")
    if bool(v0p) == True:
        print('prędkość początkowa: \nvp = ', v0p , ' m/s\n')
    if bool(vp) == True:
        print('prędkość końcowa: \nv = ', vp ,' m/s\n')
    if bool(x0p) == True:
        print('położenie początkowe: \nxp = ', x0p ,' m\n')
    if bool(xp) == True:
        print('położenie końcowe: \nx = ', xp ,' m\n')
    if bool(fp) == True:
        print('wypadkowa siła działająca na ciało: \nF = ', fp , ' N\n')
    if bool(mp) == True:
        print('masa ciała: \nm = ', mp , ' kg\n')
    if bool(tp) == True:
        print('czas ruchu: \nt = ', tp , ' s\n')
    if bool(sp) == True:
        print('pokonana droga: \ns = ', sp , ' m\n')

    if bool(tp) == True and bool(ap) == True: 
        #zamiana wartości na int
        tp = float(tp)
        tp = tp*1000
        tp = str(tp)
        tp = list(tp)
        a = tp.index('.')
        b = list(tp[:(a)])
        tp = ''.join(b)
        tp = int(tp)

        #tworzenie wykresu
        w = range(0, tp, 1)
        y = []
        x = []

        for i in w:
            y.append(((float(ap)*i*i)/2)/1000000)
            x.append(i/1000)

        plt.plot(x, y)
        plt.title('Wykres x(t)')
        plt.grid(True)
        plt.xlabel('s')
        plt.ylabel('m')
        plt.draw()
        plt.show()










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











def rownia_pochyla():

    print('Podaj znane wartości:')
    k = input('kąt między Q a Fx(N) k=')

    if ',' in k:
        k = list(k)
        index = k.index(',')
        k.insert(index,'.')
        k.remove(',')
        k = ''.join(k)

    l = input('kąt między Q a Fy l=')

    if ',' in l:
        l = list(l)
        index = l.index(',')
        l.insert(index,'.')
        l.remove(',')
        l = ''.join(l)

    q = input('siła grawitacji Q=')

    if ',' in q:
        q = list(q)
        index = q.index(',')
        q.insert(index,'.')
        q.remove(',')
        q = ''.join(q)

    fx = input('składowa siła pozioma Qx=')

    if ',' in fx:
        fx = list(fx)
        index = fx.index(',')
        fx.insert(index,'.')
        fx.remove(',')
        fx = ''.join(fx)

    fy = input('nacisk (składowa siła pionowa) N=')

    if ',' in fy:
        fy = list(fy)
        index = fy.index(',')
        fy.insert(index,'.')
        fy.remove(',')
        fy = ''.join(fy)

    print('*możesz wpisać "ziemia"')
    g = input('przyspiesznie grawitacyjne g=')

    if ',' in g:
        g = list(g)
        index = g.index(',')
        g.insert(index,'.')
        g.remove(',')
        g = ''.join(g)

    if g == 'ziemia':
        g = '9.81'

    m = input('masa ciała m=')

    if ',' in m:
        m = list(m)
        index = m.index(',')
        m.insert(index,'.')
        m.remove(',')
        m = ''.join(m)

    ft = input('siła tarcia T=')

    if ',' in ft:
        ft = list(ft)
        index = ft.index(',')
        ft.insert(index,'.')
        ft.remove(',')
        ft = ''.join(ft)

    u = input('współczynnik tarcia u=')

    if ',' in u:
        u = list(u)
        index = u.index(',')
        u.insert(index,'.')
        u.remove(',')
        u = ''.join(u)

    fw = False
    a = False

    d = input("długość równi d=")

    if ',' in d:
        d = list(d)
        index = d.index(',')
        d.insert(index,'.')
        d.remove(',')
        d = ''.join(d)

    h = input ("wysokość równi h=")
    if ',' in h:
        h = list(h)
        index = h.index(',')
        h.insert(index,'.')
        h.remove(',')
        h = ''.join(h)
        
    t = False


    if bool(k) == True:
        k = float(k)
        k = math.radians(k)
        k = str(k)

    if bool(l) == True:
        l = float(l)
        l = math.radians(l)
        l = str(l)

    print('\n')
    z = 0
    
    while z < 8:

        # liczenie l
        if bool(l) == False and bool(k) == True:
            k = float(k)
            l = math.radians(90) - k
            print('kąt między Fx a Q (radiany) k=', k)
            l = float(l)
            k = str(k)

        # liczenie k
        if bool(k) == False and bool(l) == True:
            l = float(l)
            k = math.radians(90) - l
            print('kąt między Fx a Q (radiany) k=', k)
            l = str(l)
            k = str(k)

        if bool(k) == False and bool(fy) == True and bool(fx) == True and float(fx) > 0:
            fy = float(fy)
            fx = float(fx)
            k = math.atan(fy/fx)
            print('kąt między Fx a Q (radiany) k=', k)
            fy = str(fy)
            fx = str(fx)
            k = str(k)

        if bool(k) == False and bool(fy) == True and bool(q) == True and float(q) > 0:
            fy = float(fy)
            q = float(q)
            k = math.asin(fy/q)
            print('kąt między Fx a Q (radiany) k=', k)
            fy = str(fy)
            q = str(q)
            k = str(k)

        if bool(k) == False and bool(fx) == True and bool(q) == True and float(q) > 0:
            fx = float(fx)
            q = float(q)
            k = math.acos(fx/q)
            print('kąt między Fx a Q (radiany) k=', k)
            fx = str(fx)
            q = str(q)
            k = str(k)

        # liczenie q
        if bool(q) == False and bool(m) == True and bool(g) == True:
            m = float(m)
            g = float(g)
            q = m*g
            print('siła grawitacji Q=', q)
            m = str(m)
            g = str(g)
            q = str(q)
            print(bool(q))

        if bool(q) == False and bool(fy) == True and bool(fx) == True:
            fy = float(fy)
            fx = float(fx)
            q = math.sqrt((fy*fy)+(fx*fx))
            print('siła grawitacji Q=', q)
            fy = str(fy)
            fx = str(fx)
            q = str(q)

        if bool(q) == False and bool(k) == True and bool(fx) == True:
            k = float(k)
            fx = float(fx)
            q = fx/(math.cos(k))
            print('siła grawitacji Q=', q)
            k = str(k)
            fx = str(fx)
            q = str(q)

        if bool(q) == False and bool(fy) == True and bool(k) == True:
            fy = float(fy)
            k = float(k)
            q = fy/(math.sin(k))
            print('siła grawitacji Q=', q)
            fy = str(fy)
            k = str(k)
            q = str(q)

        #liczenie fy
        if bool(fy) == False and bool(q) == True and bool(fx) == True:
            q = float(q)
            fx = float(fx)
            fy = math.sqrt((q*q)-(fx*fx))
            print('pionowa składowa siły N=', fy)  
            q = str(q)
            fx = str(fx)
            fy = str(fy)

        if bool(fy) == False and bool(q) == True and bool(k) == True:
            q = float(q)
            k = float(k)
            fy = q*(math.sin(k))
            print('pionowa składowa siły N=', fy) 
            q = str(q)
            k = str(k)
            fy = str(fy)

        if bool(fy) == False and bool(k) == True and bool(fx) == True:
            k = float(k)
            fx = float(fx)
            fy = fx*math.tan(k)
            print('pionowa składowa siły N=', fy)  
            k = str(k)
            fx = str(fx)
            fy = str(fy)

        #liczenie fx
        if bool(fx) == False and bool(q) == True and bool(fy) == True:
            q = float(q)
            fy = float(fy)
            fx = math.sqrt((q*q)-(fy*fy))
            print('pozioma składowa Qx=', fx)
            q = str(q)
            fy = str(fy)
            fx = str(fx)

        if bool(fx) == False and bool(q) == True and bool(k) == True:
            q = float(q)
            k = float(k)
            fx = q*(math.cos(k))
            print('pozioma składowa Qx', fx)
            q = str(q)
            k = str(k)
            fx = str(fx)

        if bool(fx) == False and bool(k) == True and bool(fy) == True:
            k = float(k)
            fy = float(fy)
            fx = fy/(math.tan(k))
            print('pozioma składowa Qx', fx)
            k = str(k)
            fy = str(fy)
            fx = str(fx)

        #liczenie ft
        if bool(ft) == False and bool(u) == True and bool(fy) == True:
            u = float(u)
            fy = float(fy)
            ft = u * fy
            print('siła tarcia T=', ft)
            u = str(u)
            fy = str(fy)
            ft = str(ft)

        #liczenie u
        if bool(u) == False and bool(ft) == True and bool(fy) == True:
            ft = float(ft)
            fy = float(fy)
            u = ft/fy
            print('współczynnik tarcia u=', u)
            ft = str(ft)
            fy = str(fy)
            u = str(u)
        
        #liczenie m
        if bool(m) == False and bool(q) == True and bool(g) == True:
            q = float(q)
            g = float(g)
            m = q/g
            print('masa ciała m=', m)
            q = str(q)
            g = str(g)
            m = str(m)

        #liczenie fw
        if bool(fw) == False and bool(fx) == True and bool(ft) == True:
            fx = float(fx)
            ft = float(ft)
            fw = fx-ft
            print('siła wypadkowa', fw)
            fx = str(fx)
            ft = str(ft)
            fw = str(fw)

        #liczenie a
        if bool(a) == False and bool(fw) == True and bool(m) == True:
            fw = float(fw)
            m = float(m)
            a = fw/m
            print('przyspieszenie a=', a)
            fw = str(fw)
            m = str(m)
            a = str(a)

        #liczenie d
        if bool(d) == False and bool(h) == True and bool(k) == True:
            h = float(h)
            k = float(k)
            d = h/math.cos(h)
            print('długość równi d=', d)
            h = str(h)
            k = str(k)
            d = str(h)

        #licznie h
        if bool(h) == False and bool(d) == True and bool(k) == True:
            d = float(d)
            k = float(k)
            h = d*math.cos(k)
            print('wysokość równi h=', h)
            d = str(d)
            k = str(k)
            h = str(h)

        #liczenie t
        if bool(t) == False and bool(d) == True and bool(a) == True:
            d = float(d)
            a = float(d)
            t = math.sqrt((2*d)/a)
            print('czas zsuwania się z równi t=', t)
            d = str(d)
            a = str(d)
            t = str(t)

        z = z + 1
    print('\n')
    print('WYNIKI:')
    if bool(k) == True:
        k = float(k)
        k = math.degrees(k)
        print('kąt między Q a Fx(N): \nk = ', k,' *\n')
        k = math.radians(k)
        k = str(k)
    if bool(l) == True:
        l = float(l)
        l = math.degrees(l)
        print('kąt między Q a Fy: \nl = ', l,' *\n')
        l = math.radians(l)
        l = str(l)
    if bool(q) == True:
        print('siła grawitacji: \nQ = ', q, ' N\n')
    if bool(fx) == True:
        print('składowa siła pozioma: \nQx = ', fx, ' N\n')
    if bool(fy) == True:
        print('nacisk (składowa siła pionowa): \nN = ', fy, 'N\n')
    if bool(g) == True:
        print('przyspiesznie grawitacyjne: \ng = ', g, ' m/s2\n')
    if bool(m) == True:
        print('masa ciała: \nm = ', m, ' kg\n')
    if bool(ft) == True:
        print('siła tarcia: \nT = ', ft, ' N\n')
    if bool(u) == True:
        print('współczynnik tarcia: \nu = ', u, '\n')
    if bool(fw) == True:
        print('siła wypadkowa: \nfw = ', fw, ' N\n')
    if bool(a) == True:
        print('przyspieszenie: \na = ', a, ' m/s2\n')
    if bool(d) == True:
        print("długość równi: \nd = ", d, ' m\n')
    if bool(h) == True:
        print("wysokość równi: \nh = ", h, ' m\n')
    if bool(t) == True:
        print('czas zsuwania się z równi: \nt = ', t, ' s\n')











def rzut_ukosny():

    k = 0

    print('Podaj znane wartości początkowe:')
    print('*możesz wpisać nazwy planet układu słonecznego i księżyc')
    g = input('przyspiesznie g=')

    if ',' in g:
        g = list(g)
        index = g.index(',')
        g.insert(index,'.')
        g.remove(',')
        g = ''.join(g)

    if g == 'ziemia':
        g = '9.81'
    elif g == 'księżyc':
        g ='1.6'
    elif g == 'merkury':
        g ='3.701'
    elif g == 'wenus':
        g ='8.87'
    elif g == 'mars':
        g ='3.934'
    elif g == 'jowisz':
        g ='24.79'
    elif g == 'saturn':
        g ='8.96'
    elif g == 'uran':
        g ='8.69'
    elif g == 'neptun':
        g ='11'

    h = input('wysokość początkowa h=')

    if ',' in h:
        h = list(h)
        index = h.index(',')
        h.insert(index,'.')
        h.remove(',')
        h = ''.join(h)

    v0 = input('prędkość początkowa vp=')

    if ',' in v0:
        v0 = list(v0)
        index = v0.index(',')
        v0.insert(index,'.')
        v0.remove(',')
        v0 = ''.join(v0)

    a = input('kąt rzutu w stopniach a=')

    if ',' in a:
        a = list(a)
        index = a.index(',')
        a.insert(index,'.')
        a.remove(',')
        a = ''.join(a)

    vx = input('prędkość pozioma vx=')

    if ',' in vx:
        vx = list(vx)
        index = vx.index(',')
        vx.insert(index,'.')
        vx.remove(',')
        vx = ''.join(vx)

    vy0 = input('prędkość początkowa pionowa vpy=')

    if ',' in vy0:
        vy0 = list(vy0)
        index = vy0.index(',')
        vy0.insert(index,'.')
        vy0.remove(',')
        vy0 = ''.join(vy0)
    
    hm = False
    t2 = False
    t1 = False
    tc = False
    z = False
    vyk = False
    vk = False
    ak = False

    if bool(a) == True:
        a = float(a)
        a = math.radians(a)
        a = str(a)

    print('\n')

    while k < 6:

        #liczenie a
        if bool(a) == False and bool(vy0) == True and bool(vx) == True and float(vx) > 0:
            vy0 = float(vy0)
            vx = float(vx)
            a = math.atan(vy0/vx)
            print('kąt rzutu w stopniach a=', a)
            vy0 = str(vy0)
            vx = str(vx)
            a = str(a)

        if bool(a) == False and bool(vy0) == True and bool(v0) == True and float(v0) > 0:
            vy0 = float(vy0)
            v0 = float(v0)
            a = math.asin(vy0/v0)
            print('kąt rzutu w stopniach a=', a)
            vy0 = str(vy0)
            v0 = str(v0)
            a = str(a)

        if bool(a) == False and bool(vx) == True and bool(v0) == True and float(v0) > 0:
            vx = float(vx)
            v0 = float(v0)
            a = math.acos(vx/v0)
            print('kąt rzutu w stopniach a=', a)
            vx = str(vx)
            v0 = str(v0)
            a = str(a)

        #liczenie h
        if bool(h) == False:
            h = '0'

        # liczenie v0
        if bool(v0) == False and bool(vy0) == True and bool(vx) == True:
            vy0 = float(vy0)
            vx = float(vx)
            v0 = math.sqrt((vy0*vy0)+(vx*vx))
            print('prędkość początkowa vp=', v0)
            vy0 = str(vy0)
            vx = str(vx)
            v0 = str(v0)

        if bool(v0) == False and bool(a) == True and bool(vx) == True:
            a = float(a)
            vx = float(vx)
            v0 = vx/(math.cos(a))
            print('prędkość początkowa vp=', v0)
            a = str(a)
            vx = str(vx)
            v0 = str(v0)

        if bool(v0) == False and bool(vy0) == True and bool(a) == True:
            vy0 = float(vy0)
            a = float(a)
            v0 = vy0/(math.sin(a))
            print('prędkość początkowa vp=', v0)
            vy0 = str(vy0)
            a = str(a)
            v0 = str(v0)

        #liczenie vy0
        if bool(vy0) == False and bool(v0) == True and bool(vx) == True:
            v0 = float(v0)
            vx = float(vx)
            vy0 = math.sqrt((v0*v0)-(vx*vx))
            print('prędkość początkowa pionowa vpy=', vy0)  
            v0 = str(v0)
            vx = str(vx)
            vy0 = str(vy0)

        if bool(vy0) == False and bool(v0) == True and bool(a) == True:
            v0 = float(v0)
            a = float(a)
            vy0 = v0*(math.sin(a))
            print('prędkość początkowa pionowa vpy=', vy0)
            v0 = str(v0)
            a = str(a)
            vy0 = str(vy0)

        if bool(vy0) == False and bool(a) == True and bool(vx) == True:
            a = float(a)
            vx = float(vx)
            vy0 = vx*math.tan(a)
            print('prędkość początkowa pionowa vpy=', vy0) 
            a = str(a)
            vx = str(vx)
            vy0 = str(vy0)

        #liczenie vx
        if bool(vx) == False and bool(v0) == True and bool(vy0) == True:
            v0 = float(v0)
            vy0 = float(vy0)
            vx = math.sqrt((v0*v0)-(vy0*vy0))
            print('prędkość pozioma vx=', vx)
            v0 = str(v0)
            vy0 = str(vy0)
            vx = str(vx)

        if bool(vx) == False and bool(v0) == True and bool(a) == True:
            v0 = float(v0)
            a = float(a)
            vx = v0*(math.cos(a))
            print('prędkość pozioma vx=', vx)
            v0 = str(v0)
            a = str(a)
            vx = str(vx)

        if bool(vx) == False and bool(a) == True and bool(vy0) == True:
            a = float(a)
            vy0 = float(vy0)
            vx = vy0/(math.tan(a))
            print('prędkość pozioma vx=', vx)
            a = str(a)
            vy0 = str(vy0)
            vx = str(vx)

        #liczenie hm
        if bool(hm) == False and bool(vy0) == True and bool(g) == True:
            h = float(h)
            vy0 = float(vy0)
            g = float(g)
            hm = ((vy0*vy0)/(2*g))+h
            print('maksymalna wysokość H=', hm)
            vy0 = str(vy0)
            g = str(g)
            hm = str(hm)
            h = str(h)

        #liczenie t2 czyli t spadania z hm
        if bool(t2) == False and bool(hm) == True and bool(g) == True:
            hm = float(hm)
            g = float(g)
            t2 = math.sqrt((2*hm)/g)
            print('czas spadania z maksymalnej wysokości wynosi t2=', t2)
            hm = str(hm)
            g = str(g)
            t2 = str(t2)

        #liczenie t1 czyli czasu między h a hm
        if bool(t1) == False and bool(vy0) == True and bool(g) == True:
            vy0 = float(vy0)
            g = float(g)
            t1 = vy0/g
            print('czas wznoszenia t1=', t1)
            vy0 = str(vy0)
            g = str(g)
            t1 = str(t1)

        #liczenie tc
        if bool(tc) == False and bool(t1) == True and bool(t2) == True:
            t1 = float(t1)
            t2 = float(t2)
            tc = t1 + t2
            print('całkowity czas ruchu tc=', tc)
            t1 = str(t1)
            t2 = str(t2)
            tc = str(tc)

        #liczenie z
        if bool(z) == False and bool(tc) == True and bool(vx) == True:
            tc = float(tc)
            vx = float(vx)
            z = vx*tc
            print('zasięg rzutu z=', z)
            tc = str(tc)
            vx = str(vx)
            z = str(z)

        #liczenie vyk
        if bool(vyk) == False and bool(vy0) == True and bool(g) == True and bool(tc) == True:
            vy0 = float(vy0)
            g = float(g)
            tc = float(tc)
            vyk = vy0-(g*tc)
            print('prędkość pionowa końcowa vky=', vyk)
            vy0 = str(vy0)
            g = str(g)
            tc = str(tc)
            vyk = str(vyk)

        #zliczanie końcowego kąta ak
        if bool(ak) == False and bool(vyk) == True and bool(vx) == True and float(vx) > 0:
            vyk = float(vyk)
            vx = float(vx)
            ak = math.atan(math.fabs(vyk)/vx)
            print('kąt nachylenia vk do płaszczyzny ak=', ak)
            vyk = str(vyk)
            vx = str(vx)
            ak = str(ak)

        #zliczanie vk
        if bool(vk) == False and bool(vyk) == True and bool(vx) == True:
            vyk = float(vyk)
            vx = float(vx)
            vk = math.sqrt((vx*vx)+(vyk*vyk))
            print('prędkość końcowa vk=', vk)
            vyk = str(vyk)
            vx = str(vx)
            vk = str(vk)

        #zerwanie pętli
        if bool(g) == True and bool(h) == True and bool(v0) == True and bool(a) == True and bool(vx) == True and bool(vy0) == True and bool(hm) == True and bool(tc) == True and bool(z) == True and bool(vyk) == True and bool(ak) == True and bool(vk) == True:
            print('wszystkie wielkości zostały obliczone')
            break

        k = k + 1

    print('\n')
    print('WYNIKI:\n')
    if bool(g) == True:
        print('przyspiesznie: \ng = ', g, ' m/s2\n')
    if bool(h) == True:
        print('wysokość początkowa: \nh = ', h, ' m\n')
    if bool(v0) == True:
        print('prędkość początkowa: \nvp = ', v0, ' m/s\n')
    if bool(a) == True:
        a = float(a)
        a = math.degrees(a)
        print('kąt rzutu w stopniach: \na = ', a,' *\n')
        a = math.radians(a)
        a = str(a)
    if bool(vx) == True:
        print('prędkość pozioma: \nvx = ', vx, ' m/sv\n')
    if bool(vy0) == True:
        print('prędkość początkowa pionowa: \nvpy = ', vy0, ' m/s\n')
    if bool(hm) == True:
        print('wysokość maksymalna: \nH = ', hm, ' m\n')
    if bool(tc) == True:
        print('czas ruchu: \ntc = ', tc, ' s\n')
    if bool(z) == True:
        print('zasięg rzutu: \nz = ', z, ' m\n')
    if bool(vyk) == True:
        print('prędkość pionowa końcowa: \nvky = ', vyk, ' m/s\n')
    if bool(ak) == True:
        ak = float(ak)
        ak = math.degrees(ak)
        print('kąt nachylenia vk do płaszczyzny: \nak = ', ak, ' *\n')
        ak = math.radians(ak)
        ak = str(ak)
    if bool(vk) == True:
        print('prędkość końcowa: \nvk = ', vk, ' m/s\n')

    #wykres y(x)
    if bool(tc) == True: 

        tc = float(tc)
        tc = tc*1000
        tc = str(tc)
        tc = list(tc)
        a = tc.index('.')
        b = list(tc[:(a)])
        tc = ''.join(b)
        tc = int(tc)

        x = []
        y = []
        w = range(0,tc,1)

        vx = float(vx)
        g = float(g)
        vy0 = float(vy0)
        h = float(h)

        for i in w:
            x.append((vx*i)/1000)
            y.append(h+((vy0*i)/1000)-(((g*i*i)/2)/1000000))

        plt.plot(x, y)
        plt.title('Wykres Y(x)')
        plt.grid(True)
        plt.xlabel('m')
        plt.ylabel('m')
        plt.draw()
        plt.show()








odp1 = False

while True:

    if odp1 == False:
        print('Witaj\nJakie zadanie chcesz rozwiązać?\n')
        print('-spadek swobodny [wpisz: "spadek"]\n-ruch postępowy [wpisz: "ruch"]\n-równia pochyła [wpisz: "rownia"]\n-rzut [wpisz: "rzut"]')
        odp1 = input()
    print('\n')
    if odp1 == 'spadek':
        spadek_swobodny()
    elif odp1 == 'ruch':
        ruch_postepowy()
    elif odp1 == 'rownia':
        rownia_pochyla()
    elif odp1 == 'rzut':
        rzut_ukosny()
    else:
        print('Nieprawidłowe polecenie')
        

    print('Czy chcesz liczyć ponownie?\ntak-"t"\ninne zadanie-"inne"')
    odp2 = input()


    if odp2 == 'inne':
        odp1 = False
    elif odp2 != 't':
        print('Zamykanie programu')
        break

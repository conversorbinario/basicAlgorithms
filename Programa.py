import sqlite3
# -*- coding: utf-8 -*-
"""
Histograma sinxelo lendo unha serie de arquivos. Neste caso
tratábase dunha serie de programas electorais en programa .txt
 (partido Mes.txt) pex, para o programa do PP das elecions de Abril de 2019:
 PP Abril.txt. 
 Creamos unha base de datos sinxela para almecenar o histograma, usanod algúns conpetos sinxelos
 tales como usar foreign keys, insert or ignore se se viola a condición de UNique etc
 
"""
"""https://gist.github.com/NiciusB/860b1e5b73f95fbb2c49 """
ruido="Y", "/", "así", "e", "entre", "sus", "o","la","ha", "-", ".", "que","de","no","a","la","el","es","y","en","lo","un","por","qué","me","una","te","los","se","con","para","mi","está","si","bien","pero","yo","eso","las","sí","su","tu","aquí","del","al","como","le","más","esto","ya","todo","esta","vamos","muy","hay","ahora","algo"
ruido_galego = ['·', 'co', 'é', 'tamén', 'a', 'a', 'agas', 'ante', 'ate', 'baixo', 'cabo', 'canda', 'cara a', 'con', 'contra', 'de', 'deica', 'desde', 'en', 'entre', 
                           'para', 'perante', 'por', 'segundo', 'sen', 'so', 'sobre', 'tras',
                            'consonte', 'diante', 'durante', 'menos', 'onda', 'salvo', 'senón', 'tirante','tamen',
                            'mais', 'un', 'unha', 'o', 'e', 'que', 'da', 'do', 'dos', 'das','como','no','l', 'os', 'as', 'na', 'ao', 'se', '*']

mes = ''
partido = '';
while partido !=0 and mes!=0:
    palabras = 0
    topado= False
    try:   
        partido = int(input('De que partido queres abrir o seu programa electoral?\n' 
                    '1-PSOE\n'
                    '2-UP\n'
                    '3-BNG\n'
                    '4-Cs\n'
                    '5-PP\n'
                    '0-Para finalizar\n'))
        partidos={1:'PSOE',2: 'UP', 3: 'BNG', 4:'Ciudadanos', 5: 'PP'}
        prog_partido=partidos[partido]
        mes = ''
        while mes!=1 and mes!=2 and mes!=0:
            try:
                mes = int(input('De abril ou novembro? 1- abril \n2- novembro \n0-Para sair\n'))
            except: 
                print('A opcion debe ser 0, 1 ou 2')
        meses={1:'Abril',2: 'Novembro'}
        mes_partido=meses[mes]
        arquivo= prog_partido + ' ' +mes_partido + '.txt' 
        print(arquivo)
        handler = open(arquivo, encoding="utf8")
        topado=True
    except:
        if partido==0 or mes==0:
            print('Fin do programa')
        else:
            print('Erro. O numero debe estar entre 0 e 5')
        
    
    histograma= dict()
    if topado:
        for row in handler:
            for word in row.split():
                if word.lower() not in ruido:
                    if partido==3:
                        if word.lower() not in ruido_galego:
                            histograma[word]=histograma.get(word, 0) + 1
                            palabras= palabras + 1
                            if palabras==100:
                                break
                    else:
                        histograma[word]=histograma.get(word, 0) + 1
                        palabras= palabras + 1
                        if palabras ==100:
                            break
        '''Esta sería unha forma sinxela de ordealos e mostralos, pero imos
        Ordeamos porque so imos meter as 100 primeiras palaras'''
        histograma_ordeado = list()
        for palabra, cantidade in histograma.items():
            histograma_ordeado.append((cantidade, palabra))
            histograma_ordeado.sort(reverse=True)
        handler.close()
        
        
        """bloque para a creacion da táboa de datos """
        conn = sqlite3.connect('histograma.sqlite')
        cur = conn.cursor()
        '''
		So para eliminar no caso de que queiramos
        cur.execute('DROP TABLE IF EXISTS Partidos')
        cur.execute('DROP TABLE IF EXISTS Programas')
        '''
        cur.execute('''CREATE TABLE IF NOT EXISTS Partidos
                    (id_partido INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(70), 
                    UNIQUE (nombre))''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Programas
                    (id_palabra INTEGER PRIMARY KEY AUTOINCREMENT, partido INT, palabra VARCHAR(70), frecuencia INTEGER,
                    mes VARCHAR(70), ano INTEGER, 
                    FOREIGN KEY (partido) REFERENCES Partidos(id_partido),
                    UNIQUE (partido, palabra, ano, mes))''')
        cur.execute('''INSERT OR IGNORE INTO Partidos (nombre) VALUES (?) ''', (prog_partido, ))
        print("ANALIZANDO PROGRAMA DO PARTIDO ", prog_partido)
    
        cur.execute('''SELECT id_partido FROM Partidos WHERE nombre= ? LIMIT 1 ''', (prog_partido, ))
        idpartido=cur.fetchone()[0]
        j = 0
        for tupla in histograma_ordeado:
            cur.execute('''INSERT OR IGNORE INTO Programas 
                        (partido, palabra, frecuencia, mes, ano) 
                        values (?, ?, ?, ?, ?)''', (idpartido, tupla[1], tupla[0], mes, 2019, ))
            j=j+1
            if j >=20:
                break
        conn.commit()
        
        
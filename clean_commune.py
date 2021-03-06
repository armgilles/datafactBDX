# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:11:59 2016

@author: babou
"""

import pandas as pd

print "Load file"
commune = pd.read_csv('data/correspondance-code-insee-code-postal.csv', sep=";")

# Select col to use
col_to_use = ['Code INSEE', 'Statut', 'Altitude Moyenne', 'Superficie']
commune = commune[col_to_use]

# Naming
commune.columns = ['COM', 'status', 'mean_altitude', 'superficie']

print "Improve status"

# Fix Paris status
paris_insee = ['75101', '75102', '75103','75104','75105','75106','75107','75108',
               '75109','75110','75111','75112','75113','75114','75115','75116',
               '75117','75118','75119','75120']

commune.loc[commune.COM.isin(paris_insee), 'status'] = u"Capitale d'\xe9tat"

# Fix Mareille status
marseille_insee = ['13201', '13202', '13203', '13204', '13205', '13206', '13207', '13208',
                   '13209', '13210', '13211', '13212', '13213', '13214', '13215', '13216']

commune.loc[commune.COM.isin(marseille_insee), 'status'] = u'Pr\xe9fecture de r\xe9gion'

# Fix Lyon status
lyon_insee = ['69001', '69002', '69003', '69004', '69005', '69006', '69007',
             '69008', '69009']
             
commune.loc[commune.COM.isin(lyon_insee), 'status'] = u'Pr\xe9fecture de r\xe9gion'

print "Add French metropole"

# initialize
commune['is_metropole'] = 0
commune['metropole_name'] = None

# list of all code insee city in metropole
insee_metropole = {'59350' : 'Lille',
                '59013' : 'Lille',
                '59017' : 'Lille',
                '59044' : 'Lille',
                '59051' : 'Lille',
                '59056' : 'Lille',
                '59090' : 'Lille',
                '59098' : 'Lille',
                '59106' : 'Lille',
                '59128' : 'Lille',
                '59143' : 'Lille',
                '59146' : 'Lille',
                '59152' : 'Lille',
                '59163' : 'Lille',
                '59173' : 'Lille',
                '59670' : 'Lille',
                '59193' : 'Lille',
                '59195' : 'Lille',
                '59196' : 'Lille',
                '59201' : 'Lille',
                '59202' : 'Lille',
                '59208' : 'Lille',
                '59220' : 'Lille',
                '59247' : 'Lille',
                '59250' : 'Lille',
                '59252' : 'Lille',
                '59256' : 'Lille',
                '59275' : 'Lille',
                '59278' : 'Lille',
                '59279' : 'Lille',
                '59281' : 'Lille',
                '59286' : 'Lille',
                '59299' : 'Lille',
                '59303' : 'Lille',
                '59316' : 'Lille',
                '59317' : 'Lille',
                '59320' : 'Lille',
                '59328' : 'Lille',
                '59332' : 'Lille',
                '59339' : 'Lille',
                '59343' : 'Lille',
                '59346' : 'Lille',
                '59352' : 'Lille',
                '59356' : 'Lille',
                '59360' : 'Lille',
                '59367' : 'Lille',
                '59368' : 'Lille',
                '59378' : 'Lille',
                '59386' : 'Lille',
                '59388' : 'Lille',
                '59410' : 'Lille',
                '59421' : 'Lille',
                '59426' : 'Lille',
                '59437' : 'Lille',
                '59457' : 'Lille',
                '59458' : 'Lille',
                '59470' : 'Lille',
                '59482' : 'Lille',
                '59507' : 'Lille',
                '59508' : 'Lille',
                '59512' : 'Lille',
                '59522' : 'Lille',
                '59523' : 'Lille',
                '59524' : 'Lille',
                '59527' : 'Lille',
                '59550' : 'Lille',
                '59553' : 'Lille',
                '59560' : 'Lille',
                '59566' : 'Lille',
                '59585' : 'Lille',
                '59598' : 'Lille',
                '59599' : 'Lille',
                '59602' : 'Lille',
                '59609' : 'Lille',
                '59611' : 'Lille',
                '59009' : 'Lille',
                '59636' : 'Lille',
                '59643' : 'Lille',
                '59646' : 'Lille',
                '59648' : 'Lille',
                '59650' : 'Lille',
                '59653' : 'Lille',
                '59656' : 'Lille',
                '59658' : 'Lille',
                '59660' : 'Lille',
                '33063' : 'Bordeaux',
                '33003' : 'Bordeaux',
                '33004' : 'Bordeaux',
                '33013' : 'Bordeaux',
                '33032' : 'Bordeaux',
                '33039' : 'Bordeaux',
                '33056' : 'Bordeaux',
                '33065' : 'Bordeaux',
                '33075' : 'Bordeaux',
                '33096' : 'Bordeaux',
                '33119' : 'Bordeaux',
                '33162' : 'Bordeaux',
                '33167' : 'Bordeaux',
                '33192' : 'Bordeaux',
                '33069' : 'Bordeaux',
                '33200' : 'Bordeaux',
                '33519' : 'Bordeaux',
                '33249' : 'Bordeaux',
                '33273' : 'Bordeaux',
                '33281' : 'Bordeaux',
                '33312' : 'Bordeaux',
                '33318' : 'Bordeaux',
                '33376' : 'Bordeaux',
                '33434' : 'Bordeaux',
                '33449' : 'Bordeaux',
                '33487' : 'Bordeaux',
                '33522' : 'Bordeaux',
                '33550' : 'Bordeaux',
                '31555' : 'Toulouse',
                '31003' : 'Toulouse',
                '31022' : 'Toulouse',
                '31032' : 'Toulouse',
                '31044' : 'Toulouse',
                '31053' : 'Toulouse',
                '31056' : 'Toulouse',
                '31069' : 'Toulouse',
                '31088' : 'Toulouse',
                '31091' : 'Toulouse',
                '31116' : 'Toulouse',
                '31149' : 'Toulouse',
                '31150' : 'Toulouse',
                '31157' : 'Toulouse',
                '31163' : 'Toulouse',
                '31182' : 'Toulouse',
                '31184' : 'Toulouse',
                '31186' : 'Toulouse',
                '31205' : 'Toulouse',
                '31230' : 'Toulouse',
                '31282' : 'Toulouse',
                '31293' : 'Toulouse',
                '31351' : 'Toulouse',
                '31352' : 'Toulouse',
                '31355' : 'Toulouse',
                '31389' : 'Toulouse',
                '31417' : 'Toulouse',
                '31418' : 'Toulouse',
                '31445' : 'Toulouse',
                '31467' : 'Toulouse',
                '31488' : 'Toulouse',
                '31490' : 'Toulouse',
                '31506' : 'Toulouse',
                '31541' : 'Toulouse',
                '31557' : 'Toulouse',
                '31561' : 'Toulouse',
                '31588' : 'Toulouse',
                '44109' : 'Nantes',
                '44009' : 'Nantes',
                '44018' : 'Nantes',
                '44020' : 'Nantes',
                '44024' : 'Nantes',
                '44026' : 'Nantes',
                '44035' : 'Nantes',
                '44047' : 'Nantes',
                '44074' : 'Nantes',
                '44094' : 'Nantes',
                '44101' : 'Nantes',
                '44114' : 'Nantes',
                '44120' : 'Nantes',
                '44143' : 'Nantes',
                '44150' : 'Nantes',
                '44162' : 'Nantes',
                '44166' : 'Nantes',
                '44171' : 'Nantes',
                '44190' : 'Nantes',
                '44172' : 'Nantes',
                '44194' : 'Nantes',
                '44198' : 'Nantes',
                '44204' : 'Nantes',
                '44215' : 'Nantes',
                '06088' : 'Nice',
                '06006' : 'Nice',
                '06009' : 'Nice',
                '06011' : 'Nice',
                '06013' : 'Nice',
                '06020' : 'Nice',
                '06021' : 'Nice',
                '06025' : 'Nice',
                '06027' : 'Nice',
                '06032' : 'Nice',
                '06033' : 'Nice',
                '06034' : 'Nice',
                '06042' : 'Nice',
                '06046' : 'Nice',
                '06055' : 'Nice',
                '06059' : 'Nice',
                '06060' : 'Nice',
                '06065' : 'Nice',
                '06064' : 'Nice',
                '06066' : 'Nice',
                '06072' : 'Nice',
                '06073' : 'Nice',
                '06074' : 'Nice',
                '06075' : 'Nice',
                '06080' : 'Nice',
                '06102' : 'Nice',
                '06103' : 'Nice',
                '06109' : 'Nice',
                '06110' : 'Nice',
                '06111' : 'Nice',
                '06114' : 'Nice',
                '06117' : 'Nice',
                '06119' : 'Nice',
                '06120' : 'Nice',
                '06121' : 'Nice',
                '06122' : 'Nice',
                '06123' : 'Nice',
                '06126' : 'Nice',
                '06127' : 'Nice',
                '06129' : 'Nice',
                '06144' : 'Nice',
                '06146' : 'Nice',
                '06147' : 'Nice',
                '06149' : 'Nice',
                '06151' : 'Nice',
                '06153' : 'Nice',
                '06156' : 'Nice',
                '06157' : 'Nice',
                '06159' : 'Nice',
                '76005' : 'Rouen',
                '76020' : 'Rouen',
                '76039' : 'Rouen',
                '76056' : 'Rouen',
                '76069' : 'Rouen',
                '76088' : 'Rouen',
                '76108' : 'Rouen',
                '76108' : 'Rouen',
                '76103' : 'Rouen',
                '76116' : 'Rouen',
                '76131' : 'Rouen',
                '76157' : 'Rouen',
                '76165' : 'Rouen',
                '76178' : 'Rouen',
                '76212' : 'Rouen',
                '76216' : 'Rouen',
                '76222' : 'Rouen',
                '76231' : 'Rouen',
                '76237' : 'Rouen',
                '76273' : 'Rouen',
                '76475' : 'Rouen',
                '76282' : 'Rouen',
                '76313' : 'Rouen',
                '76319' : 'Rouen',
                '76322' : 'Rouen',
                '76350' : 'Rouen',
                '76354' : 'Rouen',
                '76366' : 'Rouen',
                '76367' : 'Rouen',
                '76377' : 'Rouen',
                '76378' : 'Rouen',
                '76391' : 'Rouen',
                '76402' : 'Rouen',
                '76410' : 'Rouen',
                '76429' : 'Rouen',
                '76436' : 'Rouen',
                '76451' : 'Rouen',
                '76448' : 'Rouen',
                '76457' : 'Rouen',
                '76464' : 'Rouen',
                '76474' : 'Rouen',
                '76484' : 'Rouen',
                '76486' : 'Rouen',
                '76497' : 'Rouen',
                '76498' : 'Rouen',
                '76513' : 'Rouen',
                '76514' : 'Rouen',
                '76536' : 'Rouen',
                '76540' : 'Rouen',
                '76550' : 'Rouen',
                '76558' : 'Rouen',
                '76560' : 'Rouen',
                '76561' : 'Rouen',
                '76575' : 'Rouen',
                '76591' : 'Rouen',
                '76599' : 'Rouen',
                '76614' : 'Rouen',
                '76617' : 'Rouen',
                '76631' : 'Rouen',
                '76634' : 'Rouen',
                '76636' : 'Rouen',
                '76640' : 'Rouen',
                '76608' : 'Rouen',
                '76681' : 'Rouen',
                '76682' : 'Rouen',
                '76705' : 'Rouen',
                '76709' : 'Rouen',
                '76717' : 'Rouen',
                '76750' : 'Rouen',
                '76753' : 'Rouen',
                '76759' : 'Rouen',
                '67043' : 'Strasbourg',
                '67049' : 'Strasbourg',
                '67118' : 'Strasbourg',
                '67119' : 'Strasbourg',
                '67124' : 'Strasbourg',
                '67131' : 'Strasbourg',
                '67137' : 'Strasbourg',
                '67152' : 'Strasbourg',
                '67204' : 'Strasbourg',
                '67212' : 'Strasbourg',
                '67218' : 'Strasbourg',
                '67256' : 'Strasbourg',
                '67267' : 'Strasbourg',
                '67268' : 'Strasbourg',
                '67296' : 'Strasbourg',
                '67309' : 'Strasbourg',
                '67326' : 'Strasbourg',
                '67343' : 'Strasbourg',
                '67350' : 'Strasbourg',
                '67365' : 'Strasbourg',
                '67378' : 'Strasbourg',
                '67389' : 'Strasbourg',
                '67447' : 'Strasbourg',
                '67471' : 'Strasbourg',
                '67482' : 'Strasbourg',
                '67506' : 'Strasbourg',
                '67519' : 'Strasbourg',
                '67551' : 'Strasbourg',
                '38185' : 'Grenoble',
                '38057' : 'Grenoble',
                '38059' : 'Grenoble',
                '38068' : 'Grenoble',
                '38071' : 'Grenoble',
                '38111' : 'Grenoble',
                '38126' : 'Grenoble',
                '38150' : 'Grenoble',
                '38151' : 'Grenoble',
                '38158' : 'Grenoble',
                '38169' : 'Grenoble',
                '38170' : 'Grenoble',
                '38179' : 'Grenoble',
                '38187' : 'Grenoble',
                '38188' : 'Grenoble',
                '38200' : 'Grenoble',
                '38229' : 'Grenoble',
                '38235' : 'Grenoble',
                '38252' : 'Grenoble',
                '38258' : 'Grenoble',
                '38271' : 'Grenoble',
                '38277' : 'Grenoble',
                '38279' : 'Grenoble',
                '38281' : 'Grenoble',
                '38309' : 'Grenoble',
                '38317' : 'Grenoble',
                '38325' : 'Grenoble',
                '38328' : 'Grenoble',
                '38364' : 'Grenoble',
                '38382' : 'Grenoble',
                '38388' : 'Grenoble',
                '38421' : 'Grenoble',
                '38423' : 'Grenoble',
                '38436' : 'Grenoble',
                '38445' : 'Grenoble',
                '38471' : 'Grenoble',
                '38472' : 'Grenoble',
                '38474' : 'Grenoble',
                '38478' : 'Grenoble',
                '38485' : 'Grenoble',
                '38486' : 'Grenoble',
                '38516' : 'Grenoble',
                '38524' : 'Grenoble',
                '38528' : 'Grenoble',
                '38529' : 'Grenoble',
                '38533' : 'Grenoble',
                '38540' : 'Grenoble',
                '38545' : 'Grenoble',
                '38562' : 'Grenoble',
                '34172' : 'Montpellier',
                '34022' : 'Montpellier',
                '34027' : 'Montpellier',
                '34057' : 'Montpellier',
                '34058' : 'Montpellier',
                '34077' : 'Montpellier',
                '34087' : 'Montpellier',
                '34088' : 'Montpellier',
                '34090' : 'Montpellier',
                '34095' : 'Montpellier',
                '34116' : 'Montpellier',
                '34120' : 'Montpellier',
                '34123' : 'Montpellier',
                '34129' : 'Montpellier',
                '34134' : 'Montpellier',
                '34164' : 'Montpellier',
                '34169' : 'Montpellier',
                '34179' : 'Montpellier',
                '34198' : 'Montpellier',
                '34202' : 'Montpellier',
                '34217' : 'Montpellier',
                '34227' : 'Montpellier',
                '34244' : 'Montpellier',
                '34249' : 'Montpellier',
                '34256' : 'Montpellier',
                '34259' : 'Montpellier', #Saint-Georges-d'Orques(34680) from wiki -> 34259
                '34270' : 'Montpellier',
                '34295' : 'Montpellier',
                '34307' : 'Montpellier',
                '34327' : 'Montpellier',
                '34337' : 'Montpellier',
                '35238' : 'Rennes',
                '35001' : 'Rennes',
                '35022' : 'Rennes',
                '35024' : 'Rennes',
                '35032' : 'Rennes',
                '35039' : 'Rennes',
                '35047' : 'Rennes',
                '35051' : 'Rennes',
                '35055' : 'Rennes',
                '35058' : 'Rennes',
                '35059' : 'Rennes',
                '35065' : 'Rennes',
                '35066' : 'Rennes',
                '35076' : 'Rennes',
                '35079' : 'Rennes',
                '35080' : 'Rennes',
                '35081' : 'Rennes',
                '35088' : 'Rennes',
                '35120' : 'Rennes',
                '35131' : 'Rennes',
                '35139' : 'Rennes',
                '35144' : 'Rennes',
                '35180' : 'Rennes',
                '35189' : 'Rennes',
                '35196' : 'Rennes',
                '35204' : 'Rennes',
                '35206' : 'Rennes',
                '35208' : 'Rennes',
                '35210' : 'Rennes',
                '35216' : 'Rennes',
                '35363' : 'Rennes',
                '35240' : 'Rennes',
                '35245' : 'Rennes',
                '35250' : 'Rennes',
                '35266' : 'Rennes',
                '35275' : 'Rennes',
                '35278' : 'Rennes',
                '35281' : 'Rennes',
                '35315' : 'Rennes',
                '35334' : 'Rennes',
                '35351' : 'Rennes',
                '35352' : 'Rennes',
                '35353' : 'Rennes',
                '29019' : 'Brest',
                '29011' : 'Brest',
                '29061' : 'Brest',
                '29069' : 'Brest',
                '29075' : 'Brest',
                '29189' : 'Brest',
                '29212' : 'Brest',
                '29235' : 'Brest'}

# Find agglo_name with code insee                
commune['metropole_name'] = commune.COM.apply(lambda x: insee_metropole.get(x))

# Fill is_agglo
commune.loc[~pd.isnull(commune.metropole_name), 'is_metropole'] = 1 

print "Extract files in /data/commune_metropole.csv"
commune.to_csv('data/commune_metropole.csv', index=False, encoding='utf-8')
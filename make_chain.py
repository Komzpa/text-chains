# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

EDGE_FILTER = 4.9
NODE_FILTER = 10
SCALE_FACTOR = 1

def pairwise(thelist, size=2):
    return [ thelist[x:x+size] for x in range( len(thelist) - size + 1 ) ]

token_cache = {}
def normalize(token):
    if token not in token_cache:
        t = morph.parse(token)[0]
        v = t.normal_form.strip()
        #if 'LATN' in t.tag:
            #v = u''
        token_cache[token] = v
    return token_cache[token]

def tokenize(line):
    line = line.strip()
    line = line.strip('.')
    
    try:
        line = line.decode('utf-8', errors='ignore').lower()
    except:
        pass
    line = line.replace('_', ' ')
    line = line.replace('*', ' ')
    line = line.replace('«', ' " ')
    line = line.replace('»', ' " ')
    line = line.replace(',', ' ')
    line = line.replace('"', ' ')
    line = line.replace('–', ' ')
    line = line.replace('—', ' ')
    line = line.replace('|', ' ')
    line = line.replace('№', ' ')
    line = line.replace('/', ' ')
    line = line.replace('<', ' ')
    line = line.replace('>', ' ')
    line = line.replace(']', ' ')
    line = line.replace('[', ' ')
    line = line.replace('@', ' ')
    line = line.replace(';', ' ')
    line = line.replace('ё', 'е')
    line = line.replace('~', ' ')


    for separate_token  in ('(', ')', ',', '?', ':'):
        line = line.replace(separate_token, ' ' )
    #line = line.replace('')
    line = line.split()
    nline = []
    for token in line:
        token = normalize(token)
        #if token in (u'или', u'если', u'как',u'что',u'так', u'он',u'оно',u'она',u'они',u'с',u'т',u'это',u'того',u'эти',u'ее',u'не',u'другой',):
            #pass
        #elif token[-3:] in (u'ого',u'его',):
            #token = token[:-3]
        #elif token[-2:] in (u'ий', u'их', u'ют', u'ет', u'им', u'ие', u'ам', u'ой', u'ую', u'ый', u'ов', u'ым', u'ей', u'ое', u'ов', u'ые', u'ом', u'ия',u'ая',u'ие',u'ия',u'ка',u'ке',u'ки',u'ку',u'им',u'ом',u'ее',u'ых',u'ом',u'ах',u'ии',):
            #token = token[:-2]
        #elif token[-1] in (u'а', u'я', u'и', u'ы', u'у', u'ю', u'о', u'е',u'к',u's',):
            #token = token[:-1]
            
        #if token in (u'and',u'of',u'the', u'a', u'в', u'с', u'что', u'н', u'в',u'то', u'ег', u'эт',u'т',u'м',u'to',u'is',u'in',u'дл',u'эт',u'л',u'же',u'п',u'так',u'как',u'если',u'из',u'или',u'котор',u'к',u'it', u'that',u'все',u'сво',u'данн',u'это',u'об',u'о',u'есть',u'име',u'пр',u'we',u'this',u'as',u'with',u'are',u'for',u'an',u'даже',u'был',u'мож',u'чтоб',u'б',u'/',u'|', u'от',u'чем',u'когд',u'сам',u'тем',u'will',u'be',u'when',u'must',u'not',u'if',u'з',u'ж',u'вс',u'того',u'тогд',u'такж',u'own',u'why',u'д',u'г',u'thi',u'очень',u'над',u'являетс',u'-',u'fet',u'gen.bridgegarreth45',u'http',
                     
                     
                     ##u'не',
                     
                     
                     #):
            #continue
        #token = {u'ее': u'она', 'client': u'клиент', u'св': u'own', u'больш': u'more', u'эзотерическ': u'эзотери',u'эзотерик': u'эзотери',  u'люд': u'people', u'ем': u'он', u'можем': u'may', u'собственн': u'own', u'чувствовать': u'чувств', u'чувству': u'чувств', u'себ': u'self', u'соб': u'self', u'психологическ': u'психолог',u'кросскультурн': u'межкультурн',u'культурн': u'культур',u'психотерапевт': u'психотерап', u'мир': u'world',u'свет': u'world',u'традиционн': u'традиц',u'мн': u'I',u'мо': u'I',u'i': u'I', u'psychotherapy': u'психотерап', u'традици': u'традиц', u'they': u'они',u'their': u'они',u'их': u'они', u'transference': u'перенос', u'countertransference': u'контрперенос', u'должен': u'должн', u'ha': u'have', u'мог': u'may', u'смож': u'can', u'her': u'она', u'нее': u'она', u'she': u'она',u'могут': u'may',u'поэтом': u'because',u'master': u'мастер',u'he': u'он',u'hi': u'он',u'ваш': u'your',u'тар': u'tarot',u'мног': u'many',u'терапевт': u'терап',u'therapist': u'терап',u'карт': u'card',u'конц': u'end',u'маг': u'magic',u'магическ': u'magic',u'долг': u'должн',u'motive': u'мотив',u'люб': u'any',u'внутренн': u'inner',u'точ': u'point',u'not': u'не',u'бол': u'more',u'ещ': u'more',u'сказать': u'say',u'говорить': u'say',u'тольк': u'only',u'взгляд': u'view',u'манти': u'mantic',u'мантическ': u'mantic',u'буд': u'will be',u'высок': u'more',u'говор': u'say',u'говорит': u'say',u'him': u'он',u'уж': u'already',u'тенев': u'shadow',u'ведущ': u'leading',u'кт': u'who',u'картин': u'view',u'зрен': u'view',u'любить': u'love',u'любл': u'love',u'любовь': u'love',u'любв': u'love',u'komzpa': u'darafei',u'komяpa': u'darafei',u'теб': u'you',u'praliaskouski': u'darafei', u'my': u'I',u'помога': u'help', u'помож': u'help',  u'помочь': u'help',   u'считыван': u'считывать',  }.get(token, token)
        
        
        #if token in (u'эзотери',):
            #continue
        if token in (u'and',u'of',u'the', u'a',u'from',u'by',u'at',u'в', u'с', u'что', u'то', u'ег',u'м',u'to',u'is',u'in',u'для',u'ли',u'же',u'по',u'так',u'как',u'если',
                     u'из',u'или', 
                     u'который',u'к',u'it', u'that',u'все',u'свой',u'данный',u'это',u'об',u'о',u'есть',u'имеет',u'про',u'we',u'this',u'as',u'with',u'are',u'for',u'an',
                     u'даже',u'был',u'может',u'чтобы',u'бы',u'/',u'|', u'от',u'чем',u'когд',u'сам',u'тем',u'will',u'be',u'when',u'must',u'not',u'if',u'за',u'же',u'все',
                     u'того',u'тогда',u'также',u'own',u'why',u'thi',u'очень',u'над',u'являетс',u'-',u'fet',u'gen.bridgegarreth45',u'http',u'и',u'на',u'чаща',u'у',
                     u'а',u'не',u'тот',u'этот',u'уже',u'при',u'кой',u'такой',u'но',u'быть',u'и',u'a'):
            continue
        if token.isdigit():
            continue
        if token:
            nline.append(token)
    ##return nline
    ##line = nline     
    return ['START'] + nline + ['END', 'END']

model = {}
for line in sys.stdin:
    tokens = tokenize(line)
    for distance in range(2, len(tokens)+1):
        weight = 2. / 1.88 ** distance
        for row in pairwise(tokens, distance):
            t1 = row[0]
            t2 = row[-1]
            if distance > 2 and (t1 in ('START', 'END') or t2 in ('START', 'END')): 
                continue
            #print row, t1, t2
            if t1 not in model:
                model[t1] = {'SELF': weight}
            else:
                model[t1]['SELF'] += weight
            if t2 not in model[t1]:
                model[t1][t2] = weight
            else:
                model[t1][t2] += weight

for s in model.keys():
    if model[s]['SELF'] <= NODE_FILTER:
        del model[s]
    #else:
        #print model[s]['SELF'], s



def dot_node(name, size):
        node = {}
        node["label"] = name + '\\n' + str(round(size,1))+'\\r'
        node['fontsize'] = SCALE_FACTOR*max((size)**0.5, 10)
        node = ','.join(['%s="%s"'%(k, v) for k,v in node.iteritems()])
        return '"%s" [%s]'%(name, node)

treshold = EDGE_FILTER
#print 'source,target,weight'
#for k in sorted(model.keys()):
    #for v in sorted(model[k].keys()):
        #if v == 'SELF': 
            #continue
        #if model[k][v] > treshold:
            #if v in model:                
                #print '"%s","%s","%s"'%(k, v, model[k][v])
                
#exit()  
print """
    digraph G {
   #rankdir="TB"    
    ratio=0.5625
#ratio=0.7070707
#ratio=1.4142857142857144
    """
linked_nodes = set()
for k in sorted(model.keys()):
    if k == 'STAcRT':
        continue
    for v in sorted(model[k].keys()):
        if v in ('SELF', 'ENcD'): 
            continue        
        if model[k][v] > treshold:
            if v in model:
                #print model[k][v],100.* model[k][v] / model[k]['SELF'], k, v
                print '"%s" -> "%s" [color="0.0 0.0 %s",weight="%s"];'%(k, v, 1 - (1.*model[k][v] / model[k]['SELF'])**.5, int(round(model[k][v]*10)))
                #print '"%s" -> "%s" [color="0.0 0.0 %s"];'%(k, v, 1 - (1.*model[k][v] / model[k]['SELF'])**.5)
                linked_nodes.add(k)
                linked_nodes.add(v)                
for k in sorted(linked_nodes):
    print dot_node(k, model[k]['SELF'])
            
print "}"

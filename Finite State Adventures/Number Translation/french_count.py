import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)


def french_count():
    f = FST('french')

    # for 000 to 009
    f.add_state('s')
    f.add_state('01')
    f.add_state('001')
    f.add_state('000')
    f.initial_state = 's'
    f.set_final('001')
    f.set_final('000')

    f.add_arc('s', '01', [str(0)], [])
    f.add_arc('01', '001', [str(0)], [])
    f.add_arc('001','000', str(0),[kFRENCH_TRANS[0]])
    for i in xrange(1,10):
        f.add_arc('001', '001', [str(i)], [kFRENCH_TRANS[i]])

    #for 10
    f.add_state('00')
    f.add_state('10')
    f.set_final('10')

    f.add_arc('s', '00', [str(0)], [])
    f.add_arc('00', '10', [str(1)], [kFRENCH_TRANS[10]])
    f.add_arc('10','10',[str(0)], [])

    #for 11 to 16
    f.add_state('11')
    f.set_final('11')

    f.add_arc('00', '11', [str(1)], [])
    for i in xrange(1,7):
        f.add_arc('11','11', [str(i)], [kFRENCH_TRANS[10+i]])

    #for 17 to 19
    for i in [7,8,9]:
        f.add_arc('10', '10', [str(i)], [kFRENCH_TRANS[i]])

    #for 20
    f.add_state('20')
    f.set_final('20')

    f.add_arc('00','20',str(2),[kFRENCH_TRANS[20]])
    f.add_arc('20', '20', str(0), [])

    #for 21 to 29
    f.add_arc('20', '20', [str(1)], [kFRENCH_AND]+[kFRENCH_TRANS[1]])
    for i in xrange(2, 10):
        f.add_arc('20','20',[str(i)], [kFRENCH_TRANS[i]])

    # for 30
    f.add_state('30')
    f.set_final('30')

    f.add_arc('00', '30', str(3), [kFRENCH_TRANS[30]])
    f.add_arc('30', '30', str(0), [])

    # for 31 to 39
    f.add_arc('30', '30', [str(1)], [kFRENCH_AND] + [kFRENCH_TRANS[1]])
    for i in xrange(2, 10):
        f.add_arc('30', '30', [str(i)], [kFRENCH_TRANS[i]])

    # for 40
    f.add_state('40')
    f.set_final('40')

    f.add_arc('00', '40', str(4), [kFRENCH_TRANS[40]])
    f.add_arc('40', '40', str(0), [])

    # for 41 to 49
    f.add_arc('40', '40', [str(1)], [kFRENCH_AND] + [kFRENCH_TRANS[1]])
    for i in xrange(2, 10):
        f.add_arc('40', '40', [str(i)], [kFRENCH_TRANS[i]])

    # for 50
    f.add_state('50')
    f.set_final('50')

    f.add_arc('00', '50', str(5), [kFRENCH_TRANS[50]])
    f.add_arc('50', '50', str(0), [])

    # for 51 to 59
    f.add_arc('50', '50', [str(1)], [kFRENCH_AND] + [kFRENCH_TRANS[1]])
    for i in xrange(2, 10):
        f.add_arc('50', '50', [str(i)], [kFRENCH_TRANS[i]])

    # for 60
    f.add_state('60')
    f.set_final('60')

    f.add_arc('00', '60', str(6), [kFRENCH_TRANS[60]])
    f.add_arc('60', '60', str(0), [])

    # for 61 to 69
    f.add_arc('60', '60', [str(1)], [kFRENCH_AND] + [kFRENCH_TRANS[1]])
    for i in xrange(2, 10):
        f.add_arc('60', '60', [str(i)], [kFRENCH_TRANS[i]])

    #for 70
    f.add_state('70')
    f.set_final('70')

    f.add_arc('00', '70', str(7), [kFRENCH_TRANS[60]])
    f.add_arc('70', '70', str(0), [kFRENCH_TRANS[10]])

    #for 71 to 76
    f.add_arc('70', '70', [str(1)], [kFRENCH_AND] + [kFRENCH_TRANS[11]])
    for i in xrange(2,7):
        f.add_arc('70', '70', str(i), [kFRENCH_TRANS[10+i]])

    #for 77 to 79
    for i in xrange(7,10):
        f.add_arc('70', '70', str(i), [kFRENCH_TRANS[10]]+[kFRENCH_TRANS[i]])

    #for 80
    f.add_state('80')
    f.set_final('80')
    f.add_state('020')
    f.set_final('020')

    f.add_arc('00', '80', str(8), [kFRENCH_TRANS[4]])
    f.add_arc('80', '020', str(0), [kFRENCH_TRANS[20]])

    #for 80 to 89
    f.add_arc('80','80', str(1), [kFRENCH_TRANS[20]]+[kFRENCH_TRANS[1]])
    for i in xrange(2,10):
        f.add_arc('80', '020', str(i), [kFRENCH_TRANS[20]]+[kFRENCH_TRANS[i]])

    #for 90 to 96
    f.add_state('90')
    f.set_final('90')
    f.add_arc('00', '90', str(9), [kFRENCH_TRANS[4]])
    for i in xrange(0,7):
        f.add_arc('90', '90', str(i), [kFRENCH_TRANS[20]]+[kFRENCH_TRANS[10+i]])

    #for 97 to 99
    for i in xrange(7,10):
        f.add_arc('90', '90', str(i), [kFRENCH_TRANS[20]]+[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[i]])

    #for 100
    f.add_state('100')
    f.add_state('01a')
    f.set_final('01a')


    f.add_arc('s', '100',str(1),[kFRENCH_TRANS[100]])
    f.add_arc('100', '01a', str(0), [])
    f.add_arc('01a', '001', str(0), [])



    #for 101 to 109
    for i in xrange(1,10):
        f.add_arc('01a', '001', str(i), [kFRENCH_TRANS[i]])

    #for 110 to 119
    f.add_arc('100', '10', str(1), [kFRENCH_TRANS[10]])
    f.add_arc('100', '11', str(1), [])

    #for 120 to 129
    f.add_arc('100','20', str(2), [kFRENCH_TRANS[20]])

    # for 130 to 139
    f.add_arc('100', '30', str(3), [kFRENCH_TRANS[30]])

    # for 140 to 149
    f.add_arc('100', '40', str(4), [kFRENCH_TRANS[40]])

    # for 150 to 159
    f.add_arc('100', '50', str(5), [kFRENCH_TRANS[50]])

    # for 160 to 169
    f.add_arc('100', '60', str(6), [kFRENCH_TRANS[60]])

    # for 170 to 179
    f.add_arc('100', '70', str(7), [kFRENCH_TRANS[60]])

    # for 180 to 189
    f.add_arc('100', '80', str(8), [kFRENCH_TRANS[4]])

    # for 190 to 199
    f.add_arc('100', '90', str(9), [kFRENCH_TRANS[4]])

    #for 200 to 999
    for i in xrange(2,10):
        f.add_arc('s', '100', str(i), [kFRENCH_TRANS[i]]+[kFRENCH_TRANS[100]])

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))

        from fsmutils import trace
        trace(f, prepare_input(100))

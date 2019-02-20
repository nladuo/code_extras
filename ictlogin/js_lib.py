__all__ = ['js_lib']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['x_encode', 'b64_encode'])
@Js
def PyJsHoisted_b64_encode_(dat, this, arguments, var=var):
    var = Scope({'dat':dat, 'this':this, 'arguments':arguments}, var)
    var.registers(['dat', 'base64'])
    var.put('base64', var.get('Hashes').get('Base64').create())
    return var.get('base64').callprop('encode', var.get('dat'))
PyJsHoisted_b64_encode_.func_name = 'b64_encode'
var.put('b64_encode', PyJsHoisted_b64_encode_)
@Js
def PyJsHoisted_x_encode_(str, key, this, arguments, var=var):
    var = Scope({'str':str, 'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['d', 'str', 'l', 'v', 'y', 'm', 'p', 'n', 'z', 'k', 'e', 'q', 'key', 's', 'c'])
    @Js
    def PyJsHoisted_s_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'v', 'i', 'b', 'c'])
        var.put('c', var.get('a').get('length'))
        var.put('v', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('c')):
            try:
                var.get('v').put((var.get('i')>>Js(2.0)), (((var.get('a').callprop('charCodeAt', var.get('i'))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(1.0)))<<Js(8.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(2.0)))<<Js(16.0)))|(var.get('a').callprop('charCodeAt', (var.get('i')+Js(3.0)))<<Js(24.0))))
            finally:
                    var.put('i', Js(4.0), '+')
        if var.get('b'):
            var.get('v').put(var.get('v').get('length'), var.get('c'))
        return var.get('v')
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    @Js
    def PyJsHoisted_l_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'd', 'm', 'i', 'b', 'c'])
        var.put('d', var.get('a').get('length'))
        var.put('c', ((var.get('d')-Js(1.0))<<Js(2.0)))
        if var.get('b'):
            var.put('m', var.get('a').get((var.get('d')-Js(1.0))))
            if ((var.get('m')<(var.get('c')-Js(3.0))) or (var.get('m')>var.get('c'))):
                return var.get(u"null")
            var.put('c', var.get('m'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('d')):
            try:
                var.get('a').put(var.get('i'), var.get('String').callprop('fromCharCode', (var.get('a').get(var.get('i'))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(8.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(16.0))&Js(255)), (PyJsBshift(var.get('a').get(var.get('i')),Js(24.0))&Js(255))))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if var.get('b'):
            return var.get('a').callprop('join', Js('')).callprop('substring', Js(0.0), var.get('c'))
        else:
            return var.get('a').callprop('join', Js(''))
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    if (var.get('str')==Js('')):
        return Js('')
    var.put('v', var.get('s')(var.get('str'), Js(True)))
    var.put('k', var.get('s')(var.get('key'), Js(False)))
    if (var.get('k').get('length')<Js(4.0)):
        var.get('k').put('length', Js(4.0))
    var.put('n', (var.get('v').get('length')-Js(1.0)))
    var.put('z', var.get('v').get(var.get('n')))
    var.put('y', var.get('v').get('0'))
    var.put('c', (Js(2248228889)|Js(406206880)))
    var.put('q', var.get('Math').callprop('floor', (Js(6.0)+(Js(52.0)/(var.get('n')+Js(1.0))))))
    var.put('d', Js(0.0))
    while (Js(0.0)<(var.put('q',Js(var.get('q').to_number())-Js(1))+Js(1))):
        var.put('d', ((var.get('d')+var.get('c'))&(Js(2363546047)|Js(1931421248))))
        var.put('e', (PyJsBshift(var.get('d'),Js(2.0))&Js(3.0)))
        #for JS loop
        var.put('p', Js(0.0))
        while (var.get('p')<var.get('n')):
            try:
                var.put('y', var.get('v').get((var.get('p')+Js(1.0))))
                var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
                var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
                var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
                var.put('z', var.get('v').put(var.get('p'), ((var.get('v').get(var.get('p'))+var.get('m'))&(Js(4021866800)|Js(273100495)))))
            finally:
                    (var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1))
        var.put('y', var.get('v').get('0'))
        var.put('m', (PyJsBshift(var.get('z'),Js(5.0))^(var.get('y')<<Js(2.0))))
        var.put('m', ((PyJsBshift(var.get('y'),Js(3.0))^(var.get('z')<<Js(4.0)))^(var.get('d')^var.get('y'))), '+')
        var.put('m', (var.get('k').get(((var.get('p')&Js(3.0))^var.get('e')))^var.get('z')), '+')
        var.put('z', var.get('v').put(var.get('n'), ((var.get('v').get(var.get('n'))+var.get('m'))&(Js(3141076802)|Js(1153890493)))))
    pass
    pass
    return var.get('l')(var.get('v'), Js(False))
PyJsHoisted_x_encode_.func_name = 'x_encode'
var.put('x_encode', PyJsHoisted_x_encode_)
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['B', 'a', 't', 'h', 'r', 'D', 'n', 'f', 'i', 'e', 'o', 'u', 'l', 'c'])
    @Js
    def PyJsHoisted_e_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'r', 'n', 'f', 'e', 'o'])
        var.put('r', Js(''))
        var.put('o', (-Js(1.0)))
        if (var.get('n') and var.get('n').get('length')):
            var.put('f', var.get('n').get('length'))
            while (var.put('o', Js(1.0), '+')<var.get('f')):
                var.put('e', var.get('n').callprop('charCodeAt', var.get('o')))
                var.put('t', (var.get('n').callprop('charCodeAt', (var.get('o')+Js(1.0))) if ((var.get('o')+Js(1.0))<var.get('f')) else Js(0.0)))
                if ((((Js(55296.0)<=var.get('e')) and (var.get('e')<=Js(56319.0))) and (Js(56320.0)<=var.get('t'))) and (var.get('t')<=Js(57343.0))):
                    var.put('e', ((Js(65536.0)+((var.get('e')&Js(1023.0))<<Js(10.0)))+(var.get('t')&Js(1023.0))))
                    var.put('o', Js(1.0), '+')
                if (var.get('e')<=Js(127.0)):
                    var.put('r', var.get('String').callprop('fromCharCode', var.get('e')), '+')
                else:
                    if (var.get('e')<=Js(2047.0)):
                        var.put('r', var.get('String').callprop('fromCharCode', (Js(192.0)|(PyJsBshift(var.get('e'),Js(6.0))&Js(31.0))), (Js(128.0)|(var.get('e')&Js(63.0)))), '+')
                    else:
                        if (var.get('e')<=Js(65535.0)):
                            var.put('r', var.get('String').callprop('fromCharCode', (Js(224.0)|(PyJsBshift(var.get('e'),Js(12.0))&Js(15.0))), (Js(128.0)|(PyJsBshift(var.get('e'),Js(6.0))&Js(63.0))), (Js(128.0)|(var.get('e')&Js(63.0)))), '+')
                        else:
                            if (var.get('e')<=Js(2097151.0)):
                                var.put('r', var.get('String').callprop('fromCharCode', (Js(240.0)|(PyJsBshift(var.get('e'),Js(18.0))&Js(7.0))), (Js(128.0)|(PyJsBshift(var.get('e'),Js(12.0))&Js(63.0))), (Js(128.0)|(PyJsBshift(var.get('e'),Js(6.0))&Js(63.0))), (Js(128.0)|(var.get('e')&Js(63.0)))), '+')
        return var.get('r')
    PyJsHoisted_e_.func_name = 'e'
    var.put('e', PyJsHoisted_e_)
    @Js
    def PyJsHoisted_t_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'h', 'r', 'n', 'f', 'i', 'e', 'o'])
        var.put('i', Js([]))
        var.put('e', var.put('t', var.put('r', var.put('o', var.put('f', Js(0.0))))))
        if (var.get('n') and var.get('n').get('length')):
            var.put('h', var.get('n').get('length'))
            var.put('n', Js(''), '+')
            while (var.get('e')<var.get('h')):
                var.put('r', var.get('n').callprop('charCodeAt', var.get('e')))
                var.put('t', Js(1.0), '+')
                if (var.get('r')<Js(128.0)):
                    var.get('i').put(var.get('t'), var.get('String').callprop('fromCharCode', var.get('r')))
                    var.put('e', Js(1.0), '+')
                else:
                    if ((var.get('r')>Js(191.0)) and (var.get('r')<Js(224.0))):
                        var.put('o', var.get('n').callprop('charCodeAt', (var.get('e')+Js(1.0))))
                        var.get('i').put(var.get('t'), var.get('String').callprop('fromCharCode', (((var.get('r')&Js(31.0))<<Js(6.0))|(var.get('o')&Js(63.0)))))
                        var.put('e', Js(2.0), '+')
                    else:
                        var.put('o', var.get('n').callprop('charCodeAt', (var.get('e')+Js(1.0))))
                        var.put('f', var.get('n').callprop('charCodeAt', (var.get('e')+Js(2.0))))
                        var.get('i').put(var.get('t'), var.get('String').callprop('fromCharCode', ((((var.get('r')&Js(15.0))<<Js(12.0))|((var.get('o')&Js(63.0))<<Js(6.0)))|(var.get('f')&Js(63.0)))))
                        var.put('e', Js(3.0), '+')
        return var.get('i').callprop('join', Js(''))
    PyJsHoisted_t_.func_name = 't'
    var.put('t', PyJsHoisted_t_)
    @Js
    def PyJsHoisted_r_(n, e, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't', 'r'])
        var.put('t', ((var.get('n')&Js(65535.0))+(var.get('e')&Js(65535.0))))
        var.put('r', (((var.get('n')>>Js(16.0))+(var.get('e')>>Js(16.0)))+(var.get('t')>>Js(16.0))))
        return ((var.get('r')<<Js(16.0))|(var.get('t')&Js(65535.0)))
    PyJsHoisted_r_.func_name = 'r'
    var.put('r', PyJsHoisted_r_)
    @Js
    def PyJsHoisted_o_(n, e, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'n'])
        return ((var.get('n')<<var.get('e'))|PyJsBshift(var.get('n'),(Js(32.0)-var.get('e'))))
    PyJsHoisted_o_.func_name = 'o'
    var.put('o', PyJsHoisted_o_)
    @Js
    def PyJsHoisted_f_(n, e, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'r', 'n', 'i', 'f', 'o', 'e'])
        var.put('t', (Js('0123456789ABCDEF') if var.get('e') else Js('0123456789abcdef')))
        var.put('r', Js(''))
        var.put('f', Js(0.0))
        var.put('i', var.get('n').get('length'))
        #for JS loop
        
        while (var.get('f')<var.get('i')):
            try:
                var.put('o', var.get('n').callprop('charCodeAt', var.get('f')))
                var.put('r', (var.get('t').callprop('charAt', (PyJsBshift(var.get('o'),Js(4.0))&Js(15.0)))+var.get('t').callprop('charAt', (var.get('o')&Js(15.0)))), '+')
            finally:
                    var.put('f', Js(1.0), '+')
        return var.get('r')
    PyJsHoisted_f_.func_name = 'f'
    var.put('f', PyJsHoisted_f_)
    @Js
    def PyJsHoisted_i_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't', 'r'])
        var.put('t', var.get('n').get('length'))
        var.put('r', Js(''))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', (var.get('n').callprop('charCodeAt', var.get('e'))&Js(255.0)), (PyJsBshift(var.get('n').callprop('charCodeAt', var.get('e')),Js(8.0))&Js(255.0))), '+')
            finally:
                    var.put('e', Js(1.0), '+')
        return var.get('r')
    PyJsHoisted_i_.func_name = 'i'
    var.put('i', PyJsHoisted_i_)
    @Js
    def PyJsHoisted_h_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't', 'r'])
        var.put('t', var.get('n').get('length'))
        var.put('r', Js(''))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('n').callprop('charCodeAt', var.get('e')),Js(8.0))&Js(255.0)), (var.get('n').callprop('charCodeAt', var.get('e'))&Js(255.0))), '+')
            finally:
                    var.put('e', Js(1.0), '+')
        return var.get('r')
    PyJsHoisted_h_.func_name = 'h'
    var.put('h', PyJsHoisted_h_)
    @Js
    def PyJsHoisted_u_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't', 'r'])
        var.put('t', (var.get('n').get('length')*Js(32.0)))
        var.put('r', Js(''))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('n').get((var.get('e')>>Js(5.0))),(Js(24.0)-(var.get('e')%Js(32.0))))&Js(255.0))), '+')
            finally:
                    var.put('e', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_u_.func_name = 'u'
    var.put('u', PyJsHoisted_u_)
    @Js
    def PyJsHoisted_a_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't', 'r'])
        var.put('t', (var.get('n').get('length')*Js(32.0)))
        var.put('r', Js(''))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('n').get((var.get('e')>>Js(5.0))),(var.get('e')%Js(32.0)))&Js(255.0))), '+')
            finally:
                    var.put('e', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_a_.func_name = 'a'
    var.put('a', PyJsHoisted_a_)
    @Js
    def PyJsHoisted_c_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'r', 'n', 'e', 'o'])
        var.put('t', (var.get('n').get('length')*Js(8.0)))
        var.put('r', var.get('Array')((var.get('n').get('length')>>Js(2.0))))
        var.put('o', var.get('r').get('length'))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('o')):
            try:
                var.get('r').put(var.get('e'), Js(0.0))
            finally:
                    var.put('e', Js(1.0), '+')
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.get('r').put((var.get('e')>>Js(5.0)), ((var.get('n').callprop('charCodeAt', (var.get('e')/Js(8.0)))&Js(255.0))<<(var.get('e')%Js(32.0))), '|')
            finally:
                    var.put('e', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_c_.func_name = 'c'
    var.put('c', PyJsHoisted_c_)
    @Js
    def PyJsHoisted_l_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'r', 'n', 'e', 'o'])
        var.put('t', (var.get('n').get('length')*Js(8.0)))
        var.put('r', var.get('Array')((var.get('n').get('length')>>Js(2.0))))
        var.put('o', var.get('r').get('length'))
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('o')):
            try:
                var.get('r').put(var.get('e'), Js(0.0))
            finally:
                    var.put('e', Js(1.0), '+')
        #for JS loop
        var.put('e', Js(0.0))
        while (var.get('e')<var.get('t')):
            try:
                var.get('r').put((var.get('e')>>Js(5.0)), ((var.get('n').callprop('charCodeAt', (var.get('e')/Js(8.0)))&Js(255.0))<<(Js(24.0)-(var.get('e')%Js(32.0)))), '|')
            finally:
                    var.put('e', Js(8.0), '+')
        return var.get('r')
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    @Js
    def PyJsHoisted_D_(n, e, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 't', 'h', 'r', 'n', 'i', 'f', 'o', 'e', 'u', 'l', 'c'])
        var.put('t', var.get('e').get('length'))
        var.put('r', var.get('Array')())
        var.put('a', var.get('Array')(var.get('Math').callprop('ceil', (var.get('n').get('length')/Js(2.0)))))
        var.put('h', var.get('a').get('length'))
        #for JS loop
        var.put('o', Js(0.0))
        while (var.get('o')<var.get('h')):
            try:
                var.get('a').put(var.get('o'), ((var.get('n').callprop('charCodeAt', (var.get('o')*Js(2.0)))<<Js(8.0))|var.get('n').callprop('charCodeAt', ((var.get('o')*Js(2.0))+Js(1.0)))))
            finally:
                    var.put('o', Js(1.0), '+')
        while (var.get('a').get('length')>Js(0.0)):
            var.put('u', var.get('Array')())
            var.put('i', Js(0.0))
            #for JS loop
            var.put('o', Js(0.0))
            while (var.get('o')<var.get('a').get('length')):
                try:
                    var.put('i', ((var.get('i')<<Js(16.0))+var.get('a').get(var.get('o'))))
                    var.put('f', var.get('Math').callprop('floor', (var.get('i')/var.get('t'))))
                    var.put('i', (var.get('f')*var.get('t')), '-')
                    if ((var.get('u').get('length')>Js(0.0)) or (var.get('f')>Js(0.0))):
                        var.get('u').put(var.get('u').get('length'), var.get('f'))
                finally:
                        var.put('o', Js(1.0), '+')
            var.get('r').put(var.get('r').get('length'), var.get('i'))
            var.put('a', var.get('u'))
        var.put('c', Js(''))
        #for JS loop
        var.put('o', (var.get('r').get('length')-Js(1.0)))
        while (var.get('o')>=Js(0.0)):
            try:
                var.put('c', var.get('e').callprop('charAt', var.get('r').get(var.get('o'))), '+')
            finally:
                    (var.put('o',Js(var.get('o').to_number())-Js(1))+Js(1))
        var.put('l', var.get('Math').callprop('ceil', ((var.get('n').get('length')*Js(8.0))/(var.get('Math').callprop('log', var.get('e').get('length'))/var.get('Math').callprop('log', Js(2.0))))))
        #for JS loop
        var.put('o', var.get('c').get('length'))
        while (var.get('o')<var.get('l')):
            try:
                var.put('c', (var.get('e').get('0')+var.get('c')))
            finally:
                    var.put('o', Js(1.0), '+')
        return var.get('c')
    PyJsHoisted_D_.func_name = 'D'
    var.put('D', PyJsHoisted_D_)
    @Js
    def PyJsHoisted_B_(n, e, this, arguments, var=var):
        var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'h', 'r', 'n', 'i', 'f', 'o', 'e'])
        var.put('t', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
        var.put('r', Js(''))
        var.put('o', var.get('n').get('length'))
        var.put('e', (var.get('e') or Js('=')))
        #for JS loop
        var.put('f', Js(0.0))
        while (var.get('f')<var.get('o')):
            try:
                var.put('h', (((var.get('n').callprop('charCodeAt', var.get('f'))<<Js(16.0))|((var.get('n').callprop('charCodeAt', (var.get('f')+Js(1.0)))<<Js(8.0)) if ((var.get('f')+Js(1.0))<var.get('o')) else Js(0.0)))|(var.get('n').callprop('charCodeAt', (var.get('f')+Js(2.0))) if ((var.get('f')+Js(2.0))<var.get('o')) else Js(0.0))))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<Js(4.0)):
                    try:
                        if (((var.get('f')*Js(8.0))+(var.get('i')*Js(6.0)))>(var.get('n').get('length')*Js(8.0))):
                            var.put('r', var.get('e'), '+')
                        else:
                            var.put('r', var.get('t').callprop('charAt', (PyJsBshift(var.get('h'),(Js(6.0)*(Js(3.0)-var.get('i'))))&Js(63.0))), '+')
                    finally:
                            var.put('i', Js(1.0), '+')
            finally:
                    var.put('f', Js(3.0), '+')
        return var.get('r')
    PyJsHoisted_B_.func_name = 'B'
    var.put('B', PyJsHoisted_B_)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    @Js
    def PyJs_anonymous_2_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'r', 'n', 'f'])
        var.put('n', Js('LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'))
        var.put('r', Js('='))
        var.put('o', Js(False))
        var.put('f', Js(False))
        @Js
        def PyJs_anonymous_3_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'h', 'i', 'o', 'u'])
            var.put('u', Js(''))
            var.put('a', var.get('t').get('length'))
            var.put('r', (var.get('r') or Js('=')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('f') else var.get('t')))
            #for JS loop
            var.put('o', Js(0.0))
            while (var.get('o')<var.get('a')):
                try:
                    var.put('h', (((var.get('t').callprop('charCodeAt', var.get('o'))<<Js(16.0))|((var.get('t').callprop('charCodeAt', (var.get('o')+Js(1.0)))<<Js(8.0)) if ((var.get('o')+Js(1.0))<var.get('a')) else Js(0.0)))|(var.get('t').callprop('charCodeAt', (var.get('o')+Js(2.0))) if ((var.get('o')+Js(2.0))<var.get('a')) else Js(0.0))))
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<Js(4.0)):
                        try:
                            if (((var.get('o')*Js(8.0))+(var.get('i')*Js(6.0)))>(var.get('a')*Js(8.0))):
                                var.put('u', var.get('r'), '+')
                            else:
                                var.put('u', var.get('n').callprop('charAt', (PyJsBshift(var.get('h'),(Js(6.0)*(Js(3.0)-var.get('i'))))&Js(63.0))), '+')
                        finally:
                                var.put('i', Js(1.0), '+')
                finally:
                        var.put('o', Js(3.0), '+')
            return var.get('u')
        PyJs_anonymous_3_._set_name('anonymous')
        var.get(u"this").put('encode', PyJs_anonymous_3_)
        @Js
        def PyJs_anonymous_4_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['B', 'a', 'h', 'D', 'i', 'o', 'e', 'A', 'u', 'C', 's', 'l', 'c'])
            var.put('A', Js(''))
            var.put('s', Js([]))
            if var.get('e').neg():
                return var.get('e')
            var.put('o', var.put('C', Js(0.0)))
            var.put('e', var.get('e').callprop('replace', var.get('RegExp').create((Js('\\')+var.get('r')), Js('gi')), Js('')))
            while 1:
                var.put('a', var.get('n').callprop('indexOf', var.get('e').callprop('charAt', var.put('o', Js(1.0), '+'))))
                var.put('c', var.get('n').callprop('indexOf', var.get('e').callprop('charAt', var.put('o', Js(1.0), '+'))))
                var.put('l', var.get('n').callprop('indexOf', var.get('e').callprop('charAt', var.put('o', Js(1.0), '+'))))
                var.put('D', var.get('n').callprop('indexOf', var.get('e').callprop('charAt', var.put('o', Js(1.0), '+'))))
                var.put('B', ((((var.get('a')<<Js(18.0))|(var.get('c')<<Js(12.0)))|(var.get('l')<<Js(6.0)))|var.get('D')))
                var.put('i', ((var.get('B')>>Js(16.0))&Js(255.0)))
                var.put('h', ((var.get('B')>>Js(8.0))&Js(255.0)))
                var.put('u', (var.get('B')&Js(255.0)))
                var.put('C', Js(1.0), '+')
                if PyJsStrictEq(var.get('l'),Js(64.0)):
                    var.get('s').put(var.get('C'), var.get('String').callprop('fromCharCode', var.get('i')))
                else:
                    if PyJsStrictEq(var.get('D'),Js(64.0)):
                        var.get('s').put(var.get('C'), var.get('String').callprop('fromCharCode', var.get('i'), var.get('h')))
                    else:
                        var.get('s').put(var.get('C'), var.get('String').callprop('fromCharCode', var.get('i'), var.get('h'), var.get('u')))
                if not (var.get('o')<var.get('e').get('length')):
                    break
            var.put('A', var.get('s').callprop('join', Js('')))
            var.put('A', (var.get('t')(var.get('A')) if var.get('f') else var.get('A')))
            return var.get('A')
        PyJs_anonymous_4_._set_name('anonymous')
        var.get(u"this").put('decode', PyJs_anonymous_4_)
        @Js
        def PyJs_anonymous_5_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('r', (var.get('n') or var.get('r')))
            return var.get(u"this")
        PyJs_anonymous_5_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_5_)
        @Js
        def PyJs_anonymous_6_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            var.put('n', (var.get('e') or var.get('n')))
            return var.get(u"this")
        PyJs_anonymous_6_._set_name('anonymous')
        var.get(u"this").put('setTab', PyJs_anonymous_6_)
        @Js
        def PyJs_anonymous_7_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('f', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_7_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_7_)
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_8_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'h', 'r', 'n', 'i', 'f', 'o'])
        var.put('t', Js(0.0))
        var.put('r', Js(0.0))
        var.put('o', Js(0.0))
        var.put('n', var.get('e')(var.get('n')))
        def PyJs_LONG_9_(var=var):
            return Js([Js('00000000 77073096 EE0E612C 990951BA 076DC419 706AF48F E963A535 9E6495A3 0EDB8832 '), Js('79DCB8A4 E0D5E91E 97D2D988 09B64C2B 7EB17CBD E7B82D07 90BF1D91 1DB71064 6AB020F2 F3B97148 '), Js('84BE41DE 1ADAD47D 6DDDE4EB F4D4B551 83D385C7 136C9856 646BA8C0 FD62F97A 8A65C9EC 14015C4F '), Js('63066CD9 FA0F3D63 8D080DF5 3B6E20C8 4C69105E D56041E4 A2677172 3C03E4D1 4B04D447 D20D85FD '), Js('A50AB56B 35B5A8FA 42B2986C DBBBC9D6 ACBCF940 32D86CE3 45DF5C75 DCD60DCF ABD13D59 26D930AC '), Js('51DE003A C8D75180 BFD06116 21B4F4B5 56B3C423 CFBA9599 B8BDA50F 2802B89E 5F058808 C60CD9B2 '), Js('B10BE924 2F6F7C87 58684C11 C1611DAB B6662D3D 76DC4190 01DB7106 98D220BC EFD5102A 71B18589 '), Js('06B6B51F 9FBFE4A5 E8B8D433 7807C9A2 0F00F934 9609A88E E10E9818 7F6A0DBB 086D3D2D 91646C97 '), Js('E6635C01 6B6B51F4 1C6C6162 856530D8 F262004E 6C0695ED 1B01A57B 8208F4C1 F50FC457 65B0D9C6 '), Js('12B7E950 8BBEB8EA FCB9887C 62DD1DDF 15DA2D49 8CD37CF3 FBD44C65 4DB26158 3AB551CE A3BC0074 '), Js('D4BB30E2 4ADFA541 3DD895D7 A4D1C46D D3D6F4FB 4369E96A 346ED9FC AD678846 DA60B8D0 44042D73 '), Js('33031DE5 AA0A4C5F DD0D7CC9 5005713C 270241AA BE0B1010 C90C2086 5768B525 206F85B3 B966D409 '), Js('CE61E49F 5EDEF90E 29D9C998 B0D09822 C7D7A8B4 59B33D17 2EB40D81 B7BD5C3B C0BA6CAD EDB88320 '), Js('9ABFB3B6 03B6E20C 74B1D29A EAD54739 9DD277AF 04DB2615 73DC1683 E3630B12 94643B84 0D6D6A3E '), Js('7A6A5AA8 E40ECF0B 9309FF9D 0A00AE27 7D079EB1 F00F9344 8708A3D2 1E01F268 6906C2FE F762575D '), Js('806567CB 196C3671 6E6B06E7 FED41B76 89D32BE0 10DA7A5A 67DD4ACC F9B9DF6F 8EBEEFF9 17B7BE43 '), Js('60B08ED5 D6D6A3E8 A1D1937E 38D8C2C4 4FDFF252 D1BB67F1 A6BC5767 3FB506DD 48B2364B D80D2BDA '), Js('AF0A1B4C 36034AF6 41047A60 DF60EFC3 A867DF55 316E8EEF 4669BE79 CB61B38C BC66831A 256FD2A0 '), Js('5268E236 CC0C7795 BB0B4703 220216B9 5505262F C5BA3BBE B2BD0B28 2BB45A92 5CB36A04 C2D7FFA7 '), Js('B5D0CF31 2CD99E8B 5BDEAE1D 9B64C2B0 EC63F226 756AA39C 026D930A 9C0906A9 EB0E363F 72076785 '), Js('05005713 95BF4A82 E2B87A14 7BB12BAE 0CB61B38 92D28E9B E5D5BE0D 7CDCEFB7 0BDBDF21 86D3D2D4 '), Js('F1D4E242 68DDB3F8 1FDA836E 81BE16CD F6B9265B 6FB077E1 18B74777 88085AE6 FF0F6A70 66063BCA '), Js('11010B5C 8F659EFF F862AE69 616BFFD3 166CCF45 A00AE278 D70DD2EE 4E048354 3903B3C2 A7672661 '), Js('D06016F7 4969474D 3E6E77DB AED16A4A D9D65ADC 40DF0B66 37D83BF0 A9BCAE53 DEBB9EC5 47B2CF7F '), Js('30B5FFE9 BDBDF21C CABAC28A 53B39330 24B4A3A6 BAD03605 CDD70693 54DE5729 23D967BF B3667A2E '), Js('C4614AB8 5D681B02 2A6F2B94 B40BBE37 C30C8EA1 5A05DF1B 2D02EF8D')]).callprop('join', Js(''))
        var.put('f', PyJs_LONG_9_())
        var.put('t', (var.get('t')^(-Js(1.0))))
        #for JS loop
        PyJsComma(var.put('i', Js(0.0)),var.put('h', var.get('n').get('length')))
        while (var.get('i')<var.get('h')):
            try:
                var.put('o', ((var.get('t')^var.get('n').callprop('charCodeAt', var.get('i')))&Js(255.0)))
                var.put('r', (Js('0x')+var.get('f').callprop('substr', (var.get('o')*Js(9.0)), Js(8.0))))
                var.put('t', (PyJsBshift(var.get('t'),Js(8.0))^var.get('r')))
            finally:
                    var.put('i', Js(1.0), '+')
        return PyJsBshift((var.get('t')^(-Js(1.0))),Js(0.0))
    PyJs_anonymous_8_._set_name('anonymous')
    @Js
    def PyJs_anonymous_10_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['w', 't', 'h', 'n', 'i', 'A', 'F', 'u', 'C', 's', 'E', 'l'])
        @Js
        def PyJsHoisted_u_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            return var.get('a')(var.get('C')(var.get('c')(var.get('n')), (var.get('n').get('length')*Js(8.0))))
        PyJsHoisted_u_.func_name = 'u'
        var.put('u', PyJsHoisted_u_)
        @Js
        def PyJsHoisted_l_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'i', 'f', 'o', 'u'])
            pass
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('h') else var.get('t')))
            var.put('r', var.get('c')(var.get('n')))
            if (var.get('r').get('length')>Js(16.0)):
                var.put('r', var.get('C')(var.get('r'), (var.get('n').get('length')*Js(8.0))))
            PyJsComma(var.put('o', var.get('Array')(Js(16.0))),var.put('f', var.get('Array')(Js(16.0))))
            #for JS loop
            var.put('u', Js(0.0))
            while (var.get('u')<Js(16.0)):
                try:
                    var.get('o').put(var.get('u'), (var.get('r').get(var.get('u'))^Js(909522486.0)))
                    var.get('f').put(var.get('u'), (var.get('r').get(var.get('u'))^Js(1549556828.0)))
                finally:
                        var.put('u', Js(1.0), '+')
            var.put('i', var.get('C')(var.get('o').callprop('concat', var.get('c')(var.get('t'))), (Js(512.0)+(var.get('t').get('length')*Js(8.0)))))
            return var.get('a')(var.get('C')(var.get('f').callprop('concat', var.get('i')), (Js(512.0)+Js(128.0))))
        PyJsHoisted_l_.func_name = 'l'
        var.put('l', PyJsHoisted_l_)
        @Js
        def PyJsHoisted_C_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'h', 'n', 'i', 'f', 'o', 'e', 'u', 'l', 'c'])
            var.put('u', Js(1732584193.0))
            var.put('a', (-Js(271733879.0)))
            var.put('c', (-Js(1732584194.0)))
            var.put('l', Js(271733878.0))
            var.get('n').put((var.get('e')>>Js(5.0)), (Js(128.0)<<(var.get('e')%Js(32.0))), '|')
            var.get('n').put(((PyJsBshift((var.get('e')+Js(64.0)),Js(9.0))<<Js(4.0))+Js(14.0)), var.get('e'))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<var.get('n').get('length')):
                try:
                    var.put('o', var.get('u'))
                    var.put('f', var.get('a'))
                    var.put('i', var.get('c'))
                    var.put('h', var.get('l'))
                    var.put('u', var.get('s')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(0.0))), Js(7.0), (-Js(680876936.0))))
                    var.put('l', var.get('s')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(1.0))), Js(12.0), (-Js(389564586.0))))
                    var.put('c', var.get('s')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(2.0))), Js(17.0), Js(606105819.0)))
                    var.put('a', var.get('s')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))
                    var.put('u', var.get('s')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(4.0))), Js(7.0), (-Js(176418897.0))))
                    var.put('l', var.get('s')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(5.0))), Js(12.0), Js(1200080426.0)))
                    var.put('c', var.get('s')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))
                    var.put('a', var.get('s')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(7.0))), Js(22.0), (-Js(45705983.0))))
                    var.put('u', var.get('s')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(8.0))), Js(7.0), Js(1770035416.0)))
                    var.put('l', var.get('s')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))
                    var.put('c', var.get('s')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(10.0))), Js(17.0), (-Js(42063.0))))
                    var.put('a', var.get('s')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))
                    var.put('u', var.get('s')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(12.0))), Js(7.0), Js(1804603682.0)))
                    var.put('l', var.get('s')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(13.0))), Js(12.0), (-Js(40341101.0))))
                    var.put('c', var.get('s')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))
                    var.put('a', var.get('s')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(15.0))), Js(22.0), Js(1236535329.0)))
                    var.put('u', var.get('w')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(1.0))), Js(5.0), (-Js(165796510.0))))
                    var.put('l', var.get('w')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))
                    var.put('c', var.get('w')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(11.0))), Js(14.0), Js(643717713.0)))
                    var.put('a', var.get('w')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(0.0))), Js(20.0), (-Js(373897302.0))))
                    var.put('u', var.get('w')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(5.0))), Js(5.0), (-Js(701558691.0))))
                    var.put('l', var.get('w')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(10.0))), Js(9.0), Js(38016083.0)))
                    var.put('c', var.get('w')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(15.0))), Js(14.0), (-Js(660478335.0))))
                    var.put('a', var.get('w')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(4.0))), Js(20.0), (-Js(405537848.0))))
                    var.put('u', var.get('w')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(9.0))), Js(5.0), Js(568446438.0)))
                    var.put('l', var.get('w')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))
                    var.put('c', var.get('w')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(3.0))), Js(14.0), (-Js(187363961.0))))
                    var.put('a', var.get('w')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(8.0))), Js(20.0), Js(1163531501.0)))
                    var.put('u', var.get('w')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))
                    var.put('l', var.get('w')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(2.0))), Js(9.0), (-Js(51403784.0))))
                    var.put('c', var.get('w')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(7.0))), Js(14.0), Js(1735328473.0)))
                    var.put('a', var.get('w')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))
                    var.put('u', var.get('F')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(5.0))), Js(4.0), (-Js(378558.0))))
                    var.put('l', var.get('F')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))
                    var.put('c', var.get('F')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(11.0))), Js(16.0), Js(1839030562.0)))
                    var.put('a', var.get('F')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(14.0))), Js(23.0), (-Js(35309556.0))))
                    var.put('u', var.get('F')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))
                    var.put('l', var.get('F')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(4.0))), Js(11.0), Js(1272893353.0)))
                    var.put('c', var.get('F')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(7.0))), Js(16.0), (-Js(155497632.0))))
                    var.put('a', var.get('F')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))
                    var.put('u', var.get('F')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(13.0))), Js(4.0), Js(681279174.0)))
                    var.put('l', var.get('F')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(0.0))), Js(11.0), (-Js(358537222.0))))
                    var.put('c', var.get('F')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(3.0))), Js(16.0), (-Js(722521979.0))))
                    var.put('a', var.get('F')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(6.0))), Js(23.0), Js(76029189.0)))
                    var.put('u', var.get('F')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(9.0))), Js(4.0), (-Js(640364487.0))))
                    var.put('l', var.get('F')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(12.0))), Js(11.0), (-Js(421815835.0))))
                    var.put('c', var.get('F')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(15.0))), Js(16.0), Js(530742520.0)))
                    var.put('a', var.get('F')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(2.0))), Js(23.0), (-Js(995338651.0))))
                    var.put('u', var.get('E')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(0.0))), Js(6.0), (-Js(198630844.0))))
                    var.put('l', var.get('E')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(7.0))), Js(10.0), Js(1126891415.0)))
                    var.put('c', var.get('E')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))
                    var.put('a', var.get('E')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(5.0))), Js(21.0), (-Js(57434055.0))))
                    var.put('u', var.get('E')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(12.0))), Js(6.0), Js(1700485571.0)))
                    var.put('l', var.get('E')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))
                    var.put('c', var.get('E')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(10.0))), Js(15.0), (-Js(1051523.0))))
                    var.put('a', var.get('E')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))
                    var.put('u', var.get('E')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(8.0))), Js(6.0), Js(1873313359.0)))
                    var.put('l', var.get('E')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(15.0))), Js(10.0), (-Js(30611744.0))))
                    var.put('c', var.get('E')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))
                    var.put('a', var.get('E')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(13.0))), Js(21.0), Js(1309151649.0)))
                    var.put('u', var.get('E')(var.get('u'), var.get('a'), var.get('c'), var.get('l'), var.get('n').get((var.get('t')+Js(4.0))), Js(6.0), (-Js(145523070.0))))
                    var.put('l', var.get('E')(var.get('l'), var.get('u'), var.get('a'), var.get('c'), var.get('n').get((var.get('t')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))
                    var.put('c', var.get('E')(var.get('c'), var.get('l'), var.get('u'), var.get('a'), var.get('n').get((var.get('t')+Js(2.0))), Js(15.0), Js(718787259.0)))
                    var.put('a', var.get('E')(var.get('a'), var.get('c'), var.get('l'), var.get('u'), var.get('n').get((var.get('t')+Js(9.0))), Js(21.0), (-Js(343485551.0))))
                    var.put('u', var.get('r')(var.get('u'), var.get('o')))
                    var.put('a', var.get('r')(var.get('a'), var.get('f')))
                    var.put('c', var.get('r')(var.get('c'), var.get('i')))
                    var.put('l', var.get('r')(var.get('l'), var.get('h')))
                finally:
                        var.put('t', Js(16.0), '+')
            return var.get('Array')(var.get('u'), var.get('a'), var.get('c'), var.get('l'))
        PyJsHoisted_C_.func_name = 'C'
        var.put('C', PyJsHoisted_C_)
        @Js
        def PyJsHoisted_A_(n, e, t, f, i, h, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'f':f, 'i':i, 'h':h, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'h', 'n', 'i', 'f', 'e'])
            return var.get('r')(var.get('o')(var.get('r')(var.get('r')(var.get('e'), var.get('n')), var.get('r')(var.get('f'), var.get('h'))), var.get('i')), var.get('t'))
        PyJsHoisted_A_.func_name = 'A'
        var.put('A', PyJsHoisted_A_)
        @Js
        def PyJsHoisted_s_(n, e, t, r, o, f, i, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'f':f, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'f', 'i', 'e', 'o'])
            return var.get('A')(((var.get('e')&var.get('t'))|((~var.get('e'))&var.get('r'))), var.get('n'), var.get('e'), var.get('o'), var.get('f'), var.get('i'))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        @Js
        def PyJsHoisted_w_(n, e, t, r, o, f, i, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'f':f, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'f', 'i', 'e', 'o'])
            return var.get('A')(((var.get('e')&var.get('r'))|(var.get('t')&(~var.get('r')))), var.get('n'), var.get('e'), var.get('o'), var.get('f'), var.get('i'))
        PyJsHoisted_w_.func_name = 'w'
        var.put('w', PyJsHoisted_w_)
        @Js
        def PyJsHoisted_F_(n, e, t, r, o, f, i, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'f':f, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'f', 'i', 'e', 'o'])
            return var.get('A')(((var.get('e')^var.get('t'))^var.get('r')), var.get('n'), var.get('e'), var.get('o'), var.get('f'), var.get('i'))
        PyJsHoisted_F_.func_name = 'F'
        var.put('F', PyJsHoisted_F_)
        @Js
        def PyJsHoisted_E_(n, e, t, r, o, f, i, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'f':f, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'f', 'i', 'e', 'o'])
            return var.get('A')((var.get('t')^(var.get('e')|(~var.get('r')))), var.get('n'), var.get('e'), var.get('o'), var.get('f'), var.get('i'))
        PyJsHoisted_E_.func_name = 'E'
        var.put('E', PyJsHoisted_E_)
        var.put('t', (var.get('n').get('uppercase') if (var.get('n') and PyJsStrictEq(var.get('n').get('uppercase').typeof(),Js('boolean'))) else Js(False)))
        var.put('i', (var.get('n').get('pda') if (var.get('n') and PyJsStrictEq(var.get('n').get('pad').typeof(),Js('string'))) else Js('=')))
        var.put('h', (var.get('n').get('utf8') if (var.get('n') and PyJsStrictEq(var.get('n').get('utf8').typeof(),Js('boolean'))) else Js(True)))
        @Js
        def PyJs_anonymous_11_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('f')(var.get('u')(var.get('n'), var.get('h')), var.get('t'))
        PyJs_anonymous_11_._set_name('anonymous')
        var.get(u"this").put('hex', PyJs_anonymous_11_)
        @Js
        def PyJs_anonymous_12_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('B')(var.get('u')(var.get('n')), var.get('i'))
        PyJs_anonymous_12_._set_name('anonymous')
        var.get(u"this").put('b64', PyJs_anonymous_12_)
        @Js
        def PyJs_anonymous_13_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('D')(var.get('u')(var.get('n'), var.get('h')), var.get('e'))
        PyJs_anonymous_13_._set_name('anonymous')
        var.get(u"this").put('any', PyJs_anonymous_13_)
        @Js
        def PyJs_anonymous_14_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('u')(var.get('n'), var.get('h'))
        PyJs_anonymous_14_._set_name('anonymous')
        var.get(u"this").put('raw', PyJs_anonymous_14_)
        @Js
        def PyJs_anonymous_15_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('f')(var.get('l')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_15_._set_name('anonymous')
        var.get(u"this").put('hex_hmac', PyJs_anonymous_15_)
        @Js
        def PyJs_anonymous_16_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('B')(var.get('l')(var.get('n'), var.get('e')), var.get('i'))
        PyJs_anonymous_16_._set_name('anonymous')
        var.get(u"this").put('b64_hmac', PyJs_anonymous_16_)
        @Js
        def PyJs_anonymous_17_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return var.get('D')(var.get('l')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_17_._set_name('anonymous')
        var.get(u"this").put('any_hmac', PyJs_anonymous_17_)
        @Js
        def PyJs_anonymous_18_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get('hex')(Js('abc')).callprop('toLowerCase'),Js('900150983cd24fb0d6963f7d28e17f72'))
        PyJs_anonymous_18_._set_name('anonymous')
        var.get(u"this").put('vm_test', PyJs_anonymous_18_)
        @Js
        def PyJs_anonymous_19_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('t', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_19_._set_name('anonymous')
        var.get(u"this").put('setUpperCase', PyJs_anonymous_19_)
        @Js
        def PyJs_anonymous_20_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('i', (var.get('n') or var.get('i')))
            return var.get(u"this")
        PyJs_anonymous_20_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_20_)
        @Js
        def PyJs_anonymous_21_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('h', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_21_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_21_)
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    PyJs_anonymous_10_._set_name('anonymous')
    @Js
    def PyJs_anonymous_22_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 't', 'h', 'n', 'i', 'A', 'C', 's', 'c'])
        @Js
        def PyJsHoisted_a_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            return var.get('u')(var.get('C')(var.get('l')(var.get('n')), (var.get('n').get('length')*Js(8.0))))
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        @Js
        def PyJsHoisted_c_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'r', 'n', 'i', 'f', 'o'])
            pass
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('h') else var.get('t')))
            var.put('r', var.get('l')(var.get('n')))
            if (var.get('r').get('length')>Js(16.0)):
                var.put('r', var.get('C')(var.get('r'), (var.get('n').get('length')*Js(8.0))))
            PyJsComma(var.put('o', var.get('Array')(Js(16.0))),var.put('f', var.get('Array')(Js(16.0))))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(16.0)):
                try:
                    var.get('o').put(var.get('i'), (var.get('r').get(var.get('i'))^Js(909522486.0)))
                    var.get('f').put(var.get('i'), (var.get('r').get(var.get('i'))^Js(1549556828.0)))
                finally:
                        var.put('i', Js(1.0), '+')
            var.put('a', var.get('C')(var.get('o').callprop('concat', var.get('l')(var.get('t'))), (Js(512.0)+(var.get('t').get('length')*Js(8.0)))))
            return var.get('u')(var.get('C')(var.get('f').callprop('concat', var.get('a')), (Js(512.0)+Js(160.0))))
        PyJsHoisted_c_.func_name = 'c'
        var.put('c', PyJsHoisted_c_)
        @Js
        def PyJsHoisted_C_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['w', 'B', 'a', 't', 'h', 'D', 'n', 'i', 'f', 'e', 'F', 'u', 'C', 'E', 'l', 'c'])
            var.put('D', var.get('Array')(Js(80.0)))
            var.put('B', Js(1732584193.0))
            var.put('C', (-Js(271733879.0)))
            var.put('w', (-Js(1732584194.0)))
            var.put('F', Js(271733878.0))
            var.put('E', (-Js(1009589776.0)))
            var.get('n').put((var.get('e')>>Js(5.0)), (Js(128.0)<<(Js(24.0)-(var.get('e')%Js(32.0)))), '|')
            var.get('n').put(((((var.get('e')+Js(64.0))>>Js(9.0))<<Js(4.0))+Js(15.0)), var.get('e'))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<var.get('n').get('length')):
                try:
                    PyJsComma(var.put('h', var.get('B')),var.put('u', var.get('C')))
                    var.put('a', var.get('w'))
                    var.put('c', var.get('F'))
                    var.put('l', var.get('E'))
                    #for JS loop
                    var.put('f', Js(0.0))
                    while (var.get('f')<Js(80.0)):
                        try:
                            if (var.get('f')<Js(16.0)):
                                var.get('D').put(var.get('f'), var.get('n').get((var.get('t')+var.get('f'))))
                            else:
                                var.get('D').put(var.get('f'), var.get('o')((((var.get('D').get((var.get('f')-Js(3.0)))^var.get('D').get((var.get('f')-Js(8.0))))^var.get('D').get((var.get('f')-Js(14.0))))^var.get('D').get((var.get('f')-Js(16.0)))), Js(1.0)))
                            var.put('i', var.get('r')(var.get('r')(var.get('o')(var.get('B'), Js(5.0)), var.get('A')(var.get('f'), var.get('C'), var.get('w'), var.get('F'))), var.get('r')(var.get('r')(var.get('E'), var.get('D').get(var.get('f'))), var.get('s')(var.get('f')))))
                            var.put('E', var.get('F'))
                            var.put('F', var.get('w'))
                            var.put('w', var.get('o')(var.get('C'), Js(30.0)))
                            var.put('C', var.get('B'))
                            var.put('B', var.get('i'))
                        finally:
                                var.put('f', Js(1.0), '+')
                    var.put('B', var.get('r')(var.get('B'), var.get('h')))
                    var.put('C', var.get('r')(var.get('C'), var.get('u')))
                    var.put('w', var.get('r')(var.get('w'), var.get('a')))
                    var.put('F', var.get('r')(var.get('F'), var.get('c')))
                    var.put('E', var.get('r')(var.get('E'), var.get('l')))
                finally:
                        var.put('t', Js(16.0), '+')
            return var.get('Array')(var.get('B'), var.get('C'), var.get('w'), var.get('F'), var.get('E'))
        PyJsHoisted_C_.func_name = 'C'
        var.put('C', PyJsHoisted_C_)
        @Js
        def PyJsHoisted_A_(n, e, t, r, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't', 'n'])
            if (var.get('n')<Js(20.0)):
                return ((var.get('e')&var.get('t'))|((~var.get('e'))&var.get('r')))
            if (var.get('n')<Js(40.0)):
                return ((var.get('e')^var.get('t'))^var.get('r'))
            if (var.get('n')<Js(60.0)):
                return (((var.get('e')&var.get('t'))|(var.get('e')&var.get('r')))|(var.get('t')&var.get('r')))
            return ((var.get('e')^var.get('t'))^var.get('r'))
        PyJsHoisted_A_.func_name = 'A'
        var.put('A', PyJsHoisted_A_)
        @Js
        def PyJsHoisted_s_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return (Js(1518500249.0) if (var.get('n')<Js(20.0)) else (Js(1859775393.0) if (var.get('n')<Js(40.0)) else ((-Js(1894007588.0)) if (var.get('n')<Js(60.0)) else (-Js(899497514.0)))))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        var.put('t', (var.get('n').get('uppercase') if (var.get('n') and PyJsStrictEq(var.get('n').get('uppercase').typeof(),Js('boolean'))) else Js(False)))
        var.put('i', (var.get('n').get('pda') if (var.get('n') and PyJsStrictEq(var.get('n').get('pad').typeof(),Js('string'))) else Js('=')))
        var.put('h', (var.get('n').get('utf8') if (var.get('n') and PyJsStrictEq(var.get('n').get('utf8').typeof(),Js('boolean'))) else Js(True)))
        @Js
        def PyJs_anonymous_23_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('f')(var.get('a')(var.get('n'), var.get('h')), var.get('t'))
        PyJs_anonymous_23_._set_name('anonymous')
        var.get(u"this").put('hex', PyJs_anonymous_23_)
        @Js
        def PyJs_anonymous_24_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('B')(var.get('a')(var.get('n'), var.get('h')), var.get('i'))
        PyJs_anonymous_24_._set_name('anonymous')
        var.get(u"this").put('b64', PyJs_anonymous_24_)
        @Js
        def PyJs_anonymous_25_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('D')(var.get('a')(var.get('n'), var.get('h')), var.get('e'))
        PyJs_anonymous_25_._set_name('anonymous')
        var.get(u"this").put('any', PyJs_anonymous_25_)
        @Js
        def PyJs_anonymous_26_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('a')(var.get('n'), var.get('h'))
        PyJs_anonymous_26_._set_name('anonymous')
        var.get(u"this").put('raw', PyJs_anonymous_26_)
        @Js
        def PyJs_anonymous_27_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('f')(var.get('c')(var.get('n'), var.get('e')))
        PyJs_anonymous_27_._set_name('anonymous')
        var.get(u"this").put('hex_hmac', PyJs_anonymous_27_)
        @Js
        def PyJs_anonymous_28_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('B')(var.get('c')(var.get('n'), var.get('e')), var.get('i'))
        PyJs_anonymous_28_._set_name('anonymous')
        var.get(u"this").put('b64_hmac', PyJs_anonymous_28_)
        @Js
        def PyJs_anonymous_29_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return var.get('D')(var.get('c')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_29_._set_name('anonymous')
        var.get(u"this").put('any_hmac', PyJs_anonymous_29_)
        @Js
        def PyJs_anonymous_30_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get('hex')(Js('abc')).callprop('toLowerCase'),Js('900150983cd24fb0d6963f7d28e17f72'))
        PyJs_anonymous_30_._set_name('anonymous')
        var.get(u"this").put('vm_test', PyJs_anonymous_30_)
        @Js
        def PyJs_anonymous_31_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('t', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_31_._set_name('anonymous')
        var.get(u"this").put('setUpperCase', PyJs_anonymous_31_)
        @Js
        def PyJs_anonymous_32_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('i', (var.get('n') or var.get('i')))
            return var.get(u"this")
        PyJs_anonymous_32_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_32_)
        @Js
        def PyJs_anonymous_33_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('h', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_33_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_33_)
        pass
        pass
        pass
        pass
        pass
    PyJs_anonymous_22_._set_name('anonymous')
    @Js
    def PyJs_anonymous_34_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['w', 'a', 't', 'h', 'd', 'y', 'v', 'm', 'p', 'n', 'i', 'o', 'A', 'F', 'C', 'g', 'E', 's', 'b', 'c'])
        @Js
        def PyJsHoisted_a_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'n'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('t') else var.get('n')))
            return var.get('u')(var.get('m')(var.get('l')(var.get('n')), (var.get('n').get('length')*Js(8.0))))
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        @Js
        def PyJsHoisted_c_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'h', 'r', 'n', 'f', 'o'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('i') else var.get('n')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('i') else var.get('t')))
            var.put('o', Js(0.0))
            var.put('f', var.get('l')(var.get('n')))
            var.put('h', var.get('Array')(Js(16.0)))
            var.put('a', var.get('Array')(Js(16.0)))
            if (var.get('f').get('length')>Js(16.0)):
                var.put('f', var.get('m')(var.get('f'), (var.get('n').get('length')*Js(8.0))))
            #for JS loop
            
            while (var.get('o')<Js(16.0)):
                try:
                    var.get('h').put(var.get('o'), (var.get('f').get(var.get('o'))^Js(909522486.0)))
                    var.get('a').put(var.get('o'), (var.get('f').get(var.get('o'))^Js(1549556828.0)))
                finally:
                        var.put('o', Js(1.0), '+')
            var.put('r', var.get('m')(var.get('h').callprop('concat', var.get('l')(var.get('t'))), (Js(512.0)+(var.get('t').get('length')*Js(8.0)))))
            return var.get('u')(var.get('m')(var.get('a').callprop('concat', var.get('r')), (Js(512.0)+Js(256.0))))
        PyJsHoisted_c_.func_name = 'c'
        var.put('c', PyJsHoisted_c_)
        @Js
        def PyJsHoisted_C_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return (PyJsBshift(var.get('n'),var.get('e'))|(var.get('n')<<(Js(32.0)-var.get('e'))))
        PyJsHoisted_C_.func_name = 'C'
        var.put('C', PyJsHoisted_C_)
        @Js
        def PyJsHoisted_A_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return PyJsBshift(var.get('n'),var.get('e'))
        PyJsHoisted_A_.func_name = 'A'
        var.put('A', PyJsHoisted_A_)
        @Js
        def PyJsHoisted_s_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return ((var.get('n')&var.get('e'))^((~var.get('n'))&var.get('t')))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        @Js
        def PyJsHoisted_w_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return (((var.get('n')&var.get('e'))^(var.get('n')&var.get('t')))^(var.get('e')&var.get('t')))
        PyJsHoisted_w_.func_name = 'w'
        var.put('w', PyJsHoisted_w_)
        @Js
        def PyJsHoisted_F_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(2.0))^var.get('C')(var.get('n'), Js(13.0)))^var.get('C')(var.get('n'), Js(22.0)))
        PyJsHoisted_F_.func_name = 'F'
        var.put('F', PyJsHoisted_F_)
        @Js
        def PyJsHoisted_E_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(6.0))^var.get('C')(var.get('n'), Js(11.0)))^var.get('C')(var.get('n'), Js(25.0)))
        PyJsHoisted_E_.func_name = 'E'
        var.put('E', PyJsHoisted_E_)
        @Js
        def PyJsHoisted_d_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(7.0))^var.get('C')(var.get('n'), Js(18.0)))^var.get('A')(var.get('n'), Js(3.0)))
        PyJsHoisted_d_.func_name = 'd'
        var.put('d', PyJsHoisted_d_)
        @Js
        def PyJsHoisted_g_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(17.0))^var.get('C')(var.get('n'), Js(19.0)))^var.get('A')(var.get('n'), Js(10.0)))
        PyJsHoisted_g_.func_name = 'g'
        var.put('g', PyJsHoisted_g_)
        @Js
        def PyJsHoisted_p_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(28.0))^var.get('C')(var.get('n'), Js(34.0)))^var.get('C')(var.get('n'), Js(39.0)))
        PyJsHoisted_p_.func_name = 'p'
        var.put('p', PyJsHoisted_p_)
        @Js
        def PyJsHoisted_y_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(14.0))^var.get('C')(var.get('n'), Js(18.0)))^var.get('C')(var.get('n'), Js(41.0)))
        PyJsHoisted_y_.func_name = 'y'
        var.put('y', PyJsHoisted_y_)
        @Js
        def PyJsHoisted_b_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(1.0))^var.get('C')(var.get('n'), Js(8.0)))^var.get('A')(var.get('n'), Js(7.0)))
        PyJsHoisted_b_.func_name = 'b'
        var.put('b', PyJsHoisted_b_)
        @Js
        def PyJsHoisted_v_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return ((var.get('C')(var.get('n'), Js(19.0))^var.get('C')(var.get('n'), Js(61.0)))^var.get('A')(var.get('n'), Js(6.0)))
        PyJsHoisted_v_.func_name = 'v'
        var.put('v', PyJsHoisted_v_)
        @Js
        def PyJsHoisted_m_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['B', 'a', 't', 'y', 'D', 'p', 'n', 'i', 'f', 'o', 'e', 'A', 'u', 'C', 'l', 'c'])
            var.put('t', Js([Js(1779033703.0), (-Js(1150833019.0)), Js(1013904242.0), (-Js(1521486534.0)), Js(1359893119.0), (-Js(1694144372.0)), Js(528734635.0), Js(1541459225.0)]))
            var.put('o', var.get('Array').create(Js(64.0)))
            pass
            pass
            var.get('n').put((var.get('e')>>Js(5.0)), (Js(128.0)<<(Js(24.0)-(var.get('e')%Js(32.0)))), '|')
            var.get('n').put(((((var.get('e')+Js(64.0))>>Js(9.0))<<Js(4.0))+Js(15.0)), var.get('e'))
            #for JS loop
            var.put('C', Js(0.0))
            while (var.get('C')<var.get('n').get('length')):
                try:
                    var.put('f', var.get('t').get('0'))
                    var.put('i', var.get('t').get('1'))
                    var.put('u', var.get('t').get('2'))
                    var.put('a', var.get('t').get('3'))
                    var.put('c', var.get('t').get('4'))
                    var.put('l', var.get('t').get('5'))
                    var.put('D', var.get('t').get('6'))
                    var.put('B', var.get('t').get('7'))
                    #for JS loop
                    var.put('A', Js(0.0))
                    while (var.get('A')<Js(64.0)):
                        try:
                            if (var.get('A')<Js(16.0)):
                                var.get('o').put(var.get('A'), var.get('n').get((var.get('A')+var.get('C'))))
                            else:
                                var.get('o').put(var.get('A'), var.get('r')(var.get('r')(var.get('r')(var.get('g')(var.get('o').get((var.get('A')-Js(2.0)))), var.get('o').get((var.get('A')-Js(7.0)))), var.get('d')(var.get('o').get((var.get('A')-Js(15.0))))), var.get('o').get((var.get('A')-Js(16.0)))))
                            var.put('p', var.get('r')(var.get('r')(var.get('r')(var.get('r')(var.get('B'), var.get('E')(var.get('c'))), var.get('s')(var.get('c'), var.get('l'), var.get('D'))), var.get('h').get(var.get('A'))), var.get('o').get(var.get('A'))))
                            var.put('y', var.get('r')(var.get('F')(var.get('f')), var.get('w')(var.get('f'), var.get('i'), var.get('u'))))
                            var.put('B', var.get('D'))
                            var.put('D', var.get('l'))
                            var.put('l', var.get('c'))
                            var.put('c', var.get('r')(var.get('a'), var.get('p')))
                            var.put('a', var.get('u'))
                            var.put('u', var.get('i'))
                            var.put('i', var.get('f'))
                            var.put('f', var.get('r')(var.get('p'), var.get('y')))
                        finally:
                                var.put('A', Js(1.0), '+')
                    var.get('t').put('0', var.get('r')(var.get('f'), var.get('t').get('0')))
                    var.get('t').put('1', var.get('r')(var.get('i'), var.get('t').get('1')))
                    var.get('t').put('2', var.get('r')(var.get('u'), var.get('t').get('2')))
                    var.get('t').put('3', var.get('r')(var.get('a'), var.get('t').get('3')))
                    var.get('t').put('4', var.get('r')(var.get('c'), var.get('t').get('4')))
                    var.get('t').put('5', var.get('r')(var.get('l'), var.get('t').get('5')))
                    var.get('t').put('6', var.get('r')(var.get('D'), var.get('t').get('6')))
                    var.get('t').put('7', var.get('r')(var.get('B'), var.get('t').get('7')))
                finally:
                        var.put('C', Js(16.0), '+')
            return var.get('t')
        PyJsHoisted_m_.func_name = 'm'
        var.put('m', PyJsHoisted_m_)
        var.put('t', (var.get('n').get('uppercase') if (var.get('n') and PyJsStrictEq(var.get('n').get('uppercase').typeof(),Js('boolean'))) else Js(False)))
        var.put('o', (var.get('n').get('pda') if (var.get('n') and PyJsStrictEq(var.get('n').get('pad').typeof(),Js('string'))) else Js('=')))
        var.put('i', (var.get('n').get('utf8') if (var.get('n') and PyJsStrictEq(var.get('n').get('utf8').typeof(),Js('boolean'))) else Js(True)))
        @Js
        def PyJs_anonymous_35_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('f')(var.get('a')(var.get('n'), var.get('i')))
        PyJs_anonymous_35_._set_name('anonymous')
        var.get(u"this").put('hex', PyJs_anonymous_35_)
        @Js
        def PyJs_anonymous_36_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('B')(var.get('a')(var.get('n'), var.get('i')), var.get('o'))
        PyJs_anonymous_36_._set_name('anonymous')
        var.get(u"this").put('b64', PyJs_anonymous_36_)
        @Js
        def PyJs_anonymous_37_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('D')(var.get('a')(var.get('n'), var.get('i')), var.get('e'))
        PyJs_anonymous_37_._set_name('anonymous')
        var.get(u"this").put('any', PyJs_anonymous_37_)
        @Js
        def PyJs_anonymous_38_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('a')(var.get('n'), var.get('i'))
        PyJs_anonymous_38_._set_name('anonymous')
        var.get(u"this").put('raw', PyJs_anonymous_38_)
        @Js
        def PyJs_anonymous_39_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('f')(var.get('c')(var.get('n'), var.get('e')))
        PyJs_anonymous_39_._set_name('anonymous')
        var.get(u"this").put('hex_hmac', PyJs_anonymous_39_)
        @Js
        def PyJs_anonymous_40_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('B')(var.get('c')(var.get('n'), var.get('e')), var.get('o'))
        PyJs_anonymous_40_._set_name('anonymous')
        var.get(u"this").put('b64_hmac', PyJs_anonymous_40_)
        @Js
        def PyJs_anonymous_41_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return var.get('D')(var.get('c')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_41_._set_name('anonymous')
        var.get(u"this").put('any_hmac', PyJs_anonymous_41_)
        @Js
        def PyJs_anonymous_42_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get('hex')(Js('abc')).callprop('toLowerCase'),Js('900150983cd24fb0d6963f7d28e17f72'))
        PyJs_anonymous_42_._set_name('anonymous')
        var.get(u"this").put('vm_test', PyJs_anonymous_42_)
        @Js
        def PyJs_anonymous_43_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('t', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_43_._set_name('anonymous')
        var.get(u"this").put('setUpperCase', PyJs_anonymous_43_)
        @Js
        def PyJs_anonymous_44_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('o', (var.get('n') or var.get('o')))
            return var.get(u"this")
        PyJs_anonymous_44_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_44_)
        @Js
        def PyJs_anonymous_45_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('i', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_45_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_45_)
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        def PyJs_LONG_46_(var=var):
            return var.put('h', Js([Js(1116352408.0), Js(1899447441.0), (-Js(1245643825.0)), (-Js(373957723.0)), Js(961987163.0), Js(1508970993.0), (-Js(1841331548.0)), (-Js(1424204075.0)), (-Js(670586216.0)), Js(310598401.0), Js(607225278.0), Js(1426881987.0), Js(1925078388.0), (-Js(2132889090.0)), (-Js(1680079193.0)), (-Js(1046744716.0)), (-Js(459576895.0)), (-Js(272742522.0)), Js(264347078.0), Js(604807628.0), Js(770255983.0), Js(1249150122.0), Js(1555081692.0), Js(1996064986.0), (-Js(1740746414.0)), (-Js(1473132947.0)), (-Js(1341970488.0)), (-Js(1084653625.0)), (-Js(958395405.0)), (-Js(710438585.0)), Js(113926993.0), Js(338241895.0), Js(666307205.0), Js(773529912.0), Js(1294757372.0), Js(1396182291.0), Js(1695183700.0), Js(1986661051.0), (-Js(2117940946.0)), (-Js(1838011259.0)), (-Js(1564481375.0)), (-Js(1474664885.0)), (-Js(1035236496.0)), (-Js(949202525.0)), (-Js(778901479.0)), (-Js(694614492.0)), (-Js(200395387.0)), Js(275423344.0), Js(430227734.0), Js(506948616.0), Js(659060556.0), Js(883997877.0), Js(958139571.0), Js(1322822218.0), Js(1537002063.0), Js(1747873779.0), Js(1955562222.0), Js(2024104815.0), (-Js(2067236844.0)), (-Js(1933114872.0)), (-Js(1866530822.0)), (-Js(1538233109.0)), (-Js(1090935817.0)), (-Js(965641998.0))]))
        PyJs_LONG_46_()
        pass
    PyJs_anonymous_34_._set_name('anonymous')
    @Js
    def PyJs_anonymous_47_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['w', 'a', 't', 'h', 'r', 'd', 'n', 'i', 'o', 'A', 'F', 'C', 'g', 'E', 's', 'c'])
        @Js
        def PyJsHoisted_h_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('o') else var.get('n')))
            return var.get('u')(var.get('c')(var.get('l')(var.get('n')), (var.get('n').get('length')*Js(8.0))))
        PyJsHoisted_h_.func_name = 'h'
        var.put('h', PyJsHoisted_h_)
        @Js
        def PyJsHoisted_a_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'h', 'r', 'n', 'i', 'f'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('o') else var.get('n')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('o') else var.get('t')))
            var.put('f', Js(0.0))
            var.put('i', var.get('l')(var.get('n')))
            var.put('h', var.get('Array')(Js(32.0)))
            var.put('a', var.get('Array')(Js(32.0)))
            if (var.get('i').get('length')>Js(32.0)):
                var.put('i', var.get('c')(var.get('i'), (var.get('n').get('length')*Js(8.0))))
            #for JS loop
            
            while (var.get('f')<Js(32.0)):
                try:
                    var.get('h').put(var.get('f'), (var.get('i').get(var.get('f'))^Js(909522486.0)))
                    var.get('a').put(var.get('f'), (var.get('i').get(var.get('f'))^Js(1549556828.0)))
                finally:
                        var.put('f', Js(1.0), '+')
            var.put('r', var.get('c')(var.get('h').callprop('concat', var.get('l')(var.get('t'))), (Js(1024.0)+(var.get('t').get('length')*Js(8.0)))))
            return var.get('u')(var.get('c')(var.get('a').callprop('concat', var.get('r')), (Js(1024.0)+Js(512.0))))
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        @Js
        def PyJsHoisted_c_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['M', 't', 'j', 'm', '_', 'U', 'c', 'h', 'r', 'S', 'D', 'e', 'x', 'l', 'a', 'y', 'f', 'u', 'b', 'B', 'T', 'v', 'p', 'n', 'o'])
            var.put('f', var.get('Array').create(Js(80.0)))
            var.put('h', var.get('Array').create(Js(16.0)))
            var.put('u', Js([var.get('C').create(Js(1779033703.0), (-Js(205731576.0))), var.get('C').create((-Js(1150833019.0)), (-Js(2067093701.0))), var.get('C').create(Js(1013904242.0), (-Js(23791573.0))), var.get('C').create((-Js(1521486534.0)), Js(1595750129.0)), var.get('C').create(Js(1359893119.0), (-Js(1377402159.0))), var.get('C').create((-Js(1694144372.0)), Js(725511199.0)), var.get('C').create(Js(528734635.0), (-Js(79577749.0))), var.get('C').create(Js(1541459225.0), Js(327033209.0))]))
            var.put('a', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('c', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('l', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('D', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('B', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('p', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('y', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('b', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('v', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('m', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('x', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('_', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('S', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('U', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('j', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('M', var.get('C').create(Js(0.0), Js(0.0)))
            var.put('T', var.get('C').create(Js(0.0), Js(0.0)))
            if PyJsStrictEq(var.get('i'),var.get('undefined')):
                def PyJs_LONG_59_(var=var):
                    return var.put('i', Js([var.get('C').create(Js(1116352408.0), (-Js(685199838.0))), var.get('C').create(Js(1899447441.0), Js(602891725.0)), var.get('C').create((-Js(1245643825.0)), (-Js(330482897.0))), var.get('C').create((-Js(373957723.0)), (-Js(2121671748.0))), var.get('C').create(Js(961987163.0), (-Js(213338824.0))), var.get('C').create(Js(1508970993.0), (-Js(1241133031.0))), var.get('C').create((-Js(1841331548.0)), (-Js(1357295717.0))), var.get('C').create((-Js(1424204075.0)), (-Js(630357736.0))), var.get('C').create((-Js(670586216.0)), (-Js(1560083902.0))), var.get('C').create(Js(310598401.0), Js(1164996542.0)), var.get('C').create(Js(607225278.0), Js(1323610764.0)), var.get('C').create(Js(1426881987.0), (-Js(704662302.0))), var.get('C').create(Js(1925078388.0), (-Js(226784913.0))), var.get('C').create((-Js(2132889090.0)), Js(991336113.0)), var.get('C').create((-Js(1680079193.0)), Js(633803317.0)), var.get('C').create((-Js(1046744716.0)), (-Js(815192428.0))), var.get('C').create((-Js(459576895.0)), (-Js(1628353838.0))), var.get('C').create((-Js(272742522.0)), Js(944711139.0)), var.get('C').create(Js(264347078.0), (-Js(1953704523.0))), var.get('C').create(Js(604807628.0), Js(2007800933.0)), var.get('C').create(Js(770255983.0), Js(1495990901.0)), var.get('C').create(Js(1249150122.0), Js(1856431235.0)), var.get('C').create(Js(1555081692.0), (-Js(1119749164.0))), var.get('C').create(Js(1996064986.0), (-Js(2096016459.0))), var.get('C').create((-Js(1740746414.0)), (-Js(295247957.0))), var.get('C').create((-Js(1473132947.0)), Js(766784016.0)), var.get('C').create((-Js(1341970488.0)), (-Js(1728372417.0))), var.get('C').create((-Js(1084653625.0)), (-Js(1091629340.0))), var.get('C').create((-Js(958395405.0)), Js(1034457026.0)), var.get('C').create((-Js(710438585.0)), (-Js(1828018395.0))), var.get('C').create(Js(113926993.0), (-Js(536640913.0))), var.get('C').create(Js(338241895.0), Js(168717936.0)), var.get('C').create(Js(666307205.0), Js(1188179964.0)), var.get('C').create(Js(773529912.0), Js(1546045734.0)), var.get('C').create(Js(1294757372.0), Js(1522805485.0)), var.get('C').create(Js(1396182291.0), (-Js(1651133473.0))), var.get('C').create(Js(1695183700.0), (-Js(1951439906.0))), var.get('C').create(Js(1986661051.0), Js(1014477480.0)), var.get('C').create((-Js(2117940946.0)), Js(1206759142.0)), var.get('C').create((-Js(1838011259.0)), Js(344077627.0)), var.get('C').create((-Js(1564481375.0)), Js(1290863460.0)), var.get('C').create((-Js(1474664885.0)), (-Js(1136513023.0))), var.get('C').create((-Js(1035236496.0)), (-Js(789014639.0))), var.get('C').create((-Js(949202525.0)), Js(106217008.0)), var.get('C').create((-Js(778901479.0)), (-Js(688958952.0))), var.get('C').create((-Js(694614492.0)), Js(1432725776.0)), var.get('C').create((-Js(200395387.0)), Js(1467031594.0)), var.get('C').create(Js(275423344.0), Js(851169720.0)), var.get('C').create(Js(430227734.0), (-Js(1194143544.0))), var.get('C').create(Js(506948616.0), Js(1363258195.0)), var.get('C').create(Js(659060556.0), (-Js(544281703.0))), var.get('C').create(Js(883997877.0), (-Js(509917016.0))), var.get('C').create(Js(958139571.0), (-Js(976659869.0))), var.get('C').create(Js(1322822218.0), (-Js(482243893.0))), var.get('C').create(Js(1537002063.0), Js(2003034995.0)), var.get('C').create(Js(1747873779.0), (-Js(692930397.0))), var.get('C').create(Js(1955562222.0), Js(1575990012.0)), var.get('C').create(Js(2024104815.0), Js(1125592928.0)), var.get('C').create((-Js(2067236844.0)), (-Js(1578062990.0))), var.get('C').create((-Js(1933114872.0)), Js(442776044.0)), var.get('C').create((-Js(1866530822.0)), Js(593698344.0)), var.get('C').create((-Js(1538233109.0)), (-Js(561857047.0))), var.get('C').create((-Js(1090935817.0)), (-Js(1295615723.0))), var.get('C').create((-Js(965641998.0)), (-Js(479046869.0))), var.get('C').create((-Js(903397682.0)), (-Js(366583396.0))), var.get('C').create((-Js(779700025.0)), Js(566280711.0)), var.get('C').create((-Js(354779690.0)), (-Js(840897762.0))), var.get('C').create((-Js(176337025.0)), (-Js(294727304.0))), var.get('C').create(Js(116418474.0), Js(1914138554.0)), var.get('C').create(Js(174292421.0), (-Js(1563912026.0))), var.get('C').create(Js(289380356.0), (-Js(1090974290.0))), var.get('C').create(Js(460393269.0), Js(320620315.0)), var.get('C').create(Js(685471733.0), Js(587496836.0)), var.get('C').create(Js(852142971.0), Js(1086792851.0)), var.get('C').create(Js(1017036298.0), Js(365543100.0)), var.get('C').create(Js(1126000580.0), (-Js(1676669620.0))), var.get('C').create(Js(1288033470.0), (-Js(885112138.0))), var.get('C').create(Js(1501505948.0), (-Js(60457430.0))), var.get('C').create(Js(1607167915.0), Js(987167468.0)), var.get('C').create(Js(1816402316.0), Js(1246189591.0))]))
                PyJs_LONG_59_()
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<Js(80.0)):
                try:
                    var.get('f').put(var.get('r'), var.get('C').create(Js(0.0), Js(0.0)))
                finally:
                        var.put('r', Js(1.0), '+')
            var.get('n').put((var.get('e')>>Js(5.0)), (Js(128.0)<<(Js(24.0)-(var.get('e')&Js(31.0)))), '|')
            var.get('n').put(((((var.get('e')+Js(128.0))>>Js(10.0))<<Js(5.0))+Js(31.0)), var.get('e'))
            var.put('o', var.get('n').get('length'))
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<var.get('o')):
                try:
                    var.get('A')(var.get('l'), var.get('u').get('0'))
                    var.get('A')(var.get('D'), var.get('u').get('1'))
                    var.get('A')(var.get('B'), var.get('u').get('2'))
                    var.get('A')(var.get('p'), var.get('u').get('3'))
                    var.get('A')(var.get('y'), var.get('u').get('4'))
                    var.get('A')(var.get('b'), var.get('u').get('5'))
                    var.get('A')(var.get('v'), var.get('u').get('6'))
                    var.get('A')(var.get('m'), var.get('u').get('7'))
                    #for JS loop
                    var.put('t', Js(0.0))
                    while (var.get('t')<Js(16.0)):
                        try:
                            var.get('f').get(var.get('t')).put('h', var.get('n').get((var.get('r')+(Js(2.0)*var.get('t')))))
                            var.get('f').get(var.get('t')).put('l', var.get('n').get(((var.get('r')+(Js(2.0)*var.get('t')))+Js(1.0))))
                        finally:
                                var.put('t', Js(1.0), '+')
                    #for JS loop
                    var.put('t', Js(16.0))
                    while (var.get('t')<Js(80.0)):
                        try:
                            var.get('s')(var.get('j'), var.get('f').get((var.get('t')-Js(2.0))), Js(19.0))
                            var.get('w')(var.get('M'), var.get('f').get((var.get('t')-Js(2.0))), Js(29.0))
                            var.get('F')(var.get('T'), var.get('f').get((var.get('t')-Js(2.0))), Js(6.0))
                            var.get('_').put('l', ((var.get('j').get('l')^var.get('M').get('l'))^var.get('T').get('l')))
                            var.get('_').put('h', ((var.get('j').get('h')^var.get('M').get('h'))^var.get('T').get('h')))
                            var.get('s')(var.get('j'), var.get('f').get((var.get('t')-Js(15.0))), Js(1.0))
                            var.get('s')(var.get('M'), var.get('f').get((var.get('t')-Js(15.0))), Js(8.0))
                            var.get('F')(var.get('T'), var.get('f').get((var.get('t')-Js(15.0))), Js(7.0))
                            var.get('x').put('l', ((var.get('j').get('l')^var.get('M').get('l'))^var.get('T').get('l')))
                            var.get('x').put('h', ((var.get('j').get('h')^var.get('M').get('h'))^var.get('T').get('h')))
                            var.get('d')(var.get('f').get(var.get('t')), var.get('_'), var.get('f').get((var.get('t')-Js(7.0))), var.get('x'), var.get('f').get((var.get('t')-Js(16.0))))
                        finally:
                                var.put('t', Js(1.0), '+')
                    #for JS loop
                    var.put('t', Js(0.0))
                    while (var.get('t')<Js(80.0)):
                        try:
                            var.get('S').put('l', ((var.get('y').get('l')&var.get('b').get('l'))^((~var.get('y').get('l'))&var.get('v').get('l'))))
                            var.get('S').put('h', ((var.get('y').get('h')&var.get('b').get('h'))^((~var.get('y').get('h'))&var.get('v').get('h'))))
                            var.get('s')(var.get('j'), var.get('y'), Js(14.0))
                            var.get('s')(var.get('M'), var.get('y'), Js(18.0))
                            var.get('w')(var.get('T'), var.get('y'), Js(9.0))
                            var.get('_').put('l', ((var.get('j').get('l')^var.get('M').get('l'))^var.get('T').get('l')))
                            var.get('_').put('h', ((var.get('j').get('h')^var.get('M').get('h'))^var.get('T').get('h')))
                            var.get('s')(var.get('j'), var.get('l'), Js(28.0))
                            var.get('w')(var.get('M'), var.get('l'), Js(2.0))
                            var.get('w')(var.get('T'), var.get('l'), Js(7.0))
                            var.get('x').put('l', ((var.get('j').get('l')^var.get('M').get('l'))^var.get('T').get('l')))
                            var.get('x').put('h', ((var.get('j').get('h')^var.get('M').get('h'))^var.get('T').get('h')))
                            var.get('U').put('l', (((var.get('l').get('l')&var.get('D').get('l'))^(var.get('l').get('l')&var.get('B').get('l')))^(var.get('D').get('l')&var.get('B').get('l'))))
                            var.get('U').put('h', (((var.get('l').get('h')&var.get('D').get('h'))^(var.get('l').get('h')&var.get('B').get('h')))^(var.get('D').get('h')&var.get('B').get('h'))))
                            var.get('g')(var.get('a'), var.get('m'), var.get('_'), var.get('S'), var.get('i').get(var.get('t')), var.get('f').get(var.get('t')))
                            var.get('E')(var.get('c'), var.get('x'), var.get('U'))
                            var.get('A')(var.get('m'), var.get('v'))
                            var.get('A')(var.get('v'), var.get('b'))
                            var.get('A')(var.get('b'), var.get('y'))
                            var.get('E')(var.get('y'), var.get('p'), var.get('a'))
                            var.get('A')(var.get('p'), var.get('B'))
                            var.get('A')(var.get('B'), var.get('D'))
                            var.get('A')(var.get('D'), var.get('l'))
                            var.get('E')(var.get('l'), var.get('a'), var.get('c'))
                        finally:
                                var.put('t', Js(1.0), '+')
                    var.get('E')(var.get('u').get('0'), var.get('u').get('0'), var.get('l'))
                    var.get('E')(var.get('u').get('1'), var.get('u').get('1'), var.get('D'))
                    var.get('E')(var.get('u').get('2'), var.get('u').get('2'), var.get('B'))
                    var.get('E')(var.get('u').get('3'), var.get('u').get('3'), var.get('p'))
                    var.get('E')(var.get('u').get('4'), var.get('u').get('4'), var.get('y'))
                    var.get('E')(var.get('u').get('5'), var.get('u').get('5'), var.get('b'))
                    var.get('E')(var.get('u').get('6'), var.get('u').get('6'), var.get('v'))
                    var.get('E')(var.get('u').get('7'), var.get('u').get('7'), var.get('m'))
                finally:
                        var.put('r', Js(32.0), '+')
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<Js(8.0)):
                try:
                    var.get('h').put((Js(2.0)*var.get('r')), var.get('u').get(var.get('r')).get('h'))
                    var.get('h').put(((Js(2.0)*var.get('r'))+Js(1.0)), var.get('u').get(var.get('r')).get('l'))
                finally:
                        var.put('r', Js(1.0), '+')
            return var.get('h')
        PyJsHoisted_c_.func_name = 'c'
        var.put('c', PyJsHoisted_c_)
        @Js
        def PyJsHoisted_C_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            var.get(u"this").put('h', var.get('n'))
            var.get(u"this").put('l', var.get('e'))
        PyJsHoisted_C_.func_name = 'C'
        var.put('C', PyJsHoisted_C_)
        @Js
        def PyJsHoisted_A_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            var.get('n').put('h', var.get('e').get('h'))
            var.get('n').put('l', var.get('e').get('l'))
        PyJsHoisted_A_.func_name = 'A'
        var.put('A', PyJsHoisted_A_)
        @Js
        def PyJsHoisted_s_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            var.get('n').put('l', (PyJsBshift(var.get('e').get('l'),var.get('t'))|(var.get('e').get('h')<<(Js(32.0)-var.get('t')))))
            var.get('n').put('h', (PyJsBshift(var.get('e').get('h'),var.get('t'))|(var.get('e').get('l')<<(Js(32.0)-var.get('t')))))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        @Js
        def PyJsHoisted_w_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            var.get('n').put('l', (PyJsBshift(var.get('e').get('h'),var.get('t'))|(var.get('e').get('l')<<(Js(32.0)-var.get('t')))))
            var.get('n').put('h', (PyJsBshift(var.get('e').get('l'),var.get('t'))|(var.get('e').get('h')<<(Js(32.0)-var.get('t')))))
        PyJsHoisted_w_.func_name = 'w'
        var.put('w', PyJsHoisted_w_)
        @Js
        def PyJsHoisted_F_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            var.get('n').put('l', (PyJsBshift(var.get('e').get('l'),var.get('t'))|(var.get('e').get('h')<<(Js(32.0)-var.get('t')))))
            var.get('n').put('h', PyJsBshift(var.get('e').get('h'),var.get('t')))
        PyJsHoisted_F_.func_name = 'F'
        var.put('F', PyJsHoisted_F_)
        @Js
        def PyJsHoisted_E_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'i', 'f', 'o', 'e'])
            var.put('r', ((var.get('e').get('l')&Js(65535.0))+(var.get('t').get('l')&Js(65535.0))))
            var.put('o', ((PyJsBshift(var.get('e').get('l'),Js(16.0))+PyJsBshift(var.get('t').get('l'),Js(16.0)))+PyJsBshift(var.get('r'),Js(16.0))))
            var.put('f', (((var.get('e').get('h')&Js(65535.0))+(var.get('t').get('h')&Js(65535.0)))+PyJsBshift(var.get('o'),Js(16.0))))
            var.put('i', ((PyJsBshift(var.get('e').get('h'),Js(16.0))+PyJsBshift(var.get('t').get('h'),Js(16.0)))+PyJsBshift(var.get('f'),Js(16.0))))
            var.get('n').put('l', ((var.get('r')&Js(65535.0))|(var.get('o')<<Js(16.0))))
            var.get('n').put('h', ((var.get('f')&Js(65535.0))|(var.get('i')<<Js(16.0))))
        PyJsHoisted_E_.func_name = 'E'
        var.put('E', PyJsHoisted_E_)
        @Js
        def PyJsHoisted_d_(n, e, t, r, o, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'h', 'r', 'n', 'i', 'f', 'e', 'o', 'u'])
            var.put('f', ((((var.get('e').get('l')&Js(65535.0))+(var.get('t').get('l')&Js(65535.0)))+(var.get('r').get('l')&Js(65535.0)))+(var.get('o').get('l')&Js(65535.0))))
            var.put('i', ((((PyJsBshift(var.get('e').get('l'),Js(16.0))+PyJsBshift(var.get('t').get('l'),Js(16.0)))+PyJsBshift(var.get('r').get('l'),Js(16.0)))+PyJsBshift(var.get('o').get('l'),Js(16.0)))+PyJsBshift(var.get('f'),Js(16.0))))
            var.put('h', (((((var.get('e').get('h')&Js(65535.0))+(var.get('t').get('h')&Js(65535.0)))+(var.get('r').get('h')&Js(65535.0)))+(var.get('o').get('h')&Js(65535.0)))+PyJsBshift(var.get('i'),Js(16.0))))
            var.put('u', ((((PyJsBshift(var.get('e').get('h'),Js(16.0))+PyJsBshift(var.get('t').get('h'),Js(16.0)))+PyJsBshift(var.get('r').get('h'),Js(16.0)))+PyJsBshift(var.get('o').get('h'),Js(16.0)))+PyJsBshift(var.get('h'),Js(16.0))))
            var.get('n').put('l', ((var.get('f')&Js(65535.0))|(var.get('i')<<Js(16.0))))
            var.get('n').put('h', ((var.get('h')&Js(65535.0))|(var.get('u')<<Js(16.0))))
        PyJsHoisted_d_.func_name = 'd'
        var.put('d', PyJsHoisted_d_)
        @Js
        def PyJsHoisted_g_(n, e, t, r, o, f, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'o':o, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'h', 'r', 'n', 'i', 'f', 'e', 'o', 'u'])
            var.put('i', (((((var.get('e').get('l')&Js(65535.0))+(var.get('t').get('l')&Js(65535.0)))+(var.get('r').get('l')&Js(65535.0)))+(var.get('o').get('l')&Js(65535.0)))+(var.get('f').get('l')&Js(65535.0))))
            var.put('h', (((((PyJsBshift(var.get('e').get('l'),Js(16.0))+PyJsBshift(var.get('t').get('l'),Js(16.0)))+PyJsBshift(var.get('r').get('l'),Js(16.0)))+PyJsBshift(var.get('o').get('l'),Js(16.0)))+PyJsBshift(var.get('f').get('l'),Js(16.0)))+PyJsBshift(var.get('i'),Js(16.0))))
            var.put('u', ((((((var.get('e').get('h')&Js(65535.0))+(var.get('t').get('h')&Js(65535.0)))+(var.get('r').get('h')&Js(65535.0)))+(var.get('o').get('h')&Js(65535.0)))+(var.get('f').get('h')&Js(65535.0)))+PyJsBshift(var.get('h'),Js(16.0))))
            var.put('a', (((((PyJsBshift(var.get('e').get('h'),Js(16.0))+PyJsBshift(var.get('t').get('h'),Js(16.0)))+PyJsBshift(var.get('r').get('h'),Js(16.0)))+PyJsBshift(var.get('o').get('h'),Js(16.0)))+PyJsBshift(var.get('f').get('h'),Js(16.0)))+PyJsBshift(var.get('u'),Js(16.0))))
            var.get('n').put('l', ((var.get('i')&Js(65535.0))|(var.get('h')<<Js(16.0))))
            var.get('n').put('h', ((var.get('u')&Js(65535.0))|(var.get('a')<<Js(16.0))))
        PyJsHoisted_g_.func_name = 'g'
        var.put('g', PyJsHoisted_g_)
        var.put('t', (var.get('n').get('uppercase') if (var.get('n') and PyJsStrictEq(var.get('n').get('uppercase').typeof(),Js('boolean'))) else Js(False)))
        var.put('r', (var.get('n').get('pda') if (var.get('n') and PyJsStrictEq(var.get('n').get('pad').typeof(),Js('string'))) else Js('=')))
        var.put('o', (var.get('n').get('utf8') if (var.get('n') and PyJsStrictEq(var.get('n').get('utf8').typeof(),Js('boolean'))) else Js(True)))
        @Js
        def PyJs_anonymous_48_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('f')(var.get('h')(var.get('n')))
        PyJs_anonymous_48_._set_name('anonymous')
        var.get(u"this").put('hex', PyJs_anonymous_48_)
        @Js
        def PyJs_anonymous_49_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('B')(var.get('h')(var.get('n')), var.get('r'))
        PyJs_anonymous_49_._set_name('anonymous')
        var.get(u"this").put('b64', PyJs_anonymous_49_)
        @Js
        def PyJs_anonymous_50_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('D')(var.get('h')(var.get('n')), var.get('e'))
        PyJs_anonymous_50_._set_name('anonymous')
        var.get(u"this").put('any', PyJs_anonymous_50_)
        @Js
        def PyJs_anonymous_51_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('h')(var.get('n'), var.get('o'))
        PyJs_anonymous_51_._set_name('anonymous')
        var.get(u"this").put('raw', PyJs_anonymous_51_)
        @Js
        def PyJs_anonymous_52_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('f')(var.get('a')(var.get('n'), var.get('e')))
        PyJs_anonymous_52_._set_name('anonymous')
        var.get(u"this").put('hex_hmac', PyJs_anonymous_52_)
        @Js
        def PyJs_anonymous_53_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('B')(var.get('a')(var.get('n'), var.get('e')), var.get('r'))
        PyJs_anonymous_53_._set_name('anonymous')
        var.get(u"this").put('b64_hmac', PyJs_anonymous_53_)
        @Js
        def PyJs_anonymous_54_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return var.get('D')(var.get('a')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_54_._set_name('anonymous')
        var.get(u"this").put('any_hmac', PyJs_anonymous_54_)
        @Js
        def PyJs_anonymous_55_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get('hex')(Js('abc')).callprop('toLowerCase'),Js('900150983cd24fb0d6963f7d28e17f72'))
        PyJs_anonymous_55_._set_name('anonymous')
        var.get(u"this").put('vm_test', PyJs_anonymous_55_)
        @Js
        def PyJs_anonymous_56_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('t', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_56_._set_name('anonymous')
        var.get(u"this").put('setUpperCase', PyJs_anonymous_56_)
        @Js
        def PyJs_anonymous_57_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('r', (var.get('n') or var.get('r')))
            return var.get(u"this")
        PyJs_anonymous_57_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_57_)
        @Js
        def PyJs_anonymous_58_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('o', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_58_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_58_)
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    PyJs_anonymous_47_._set_name('anonymous')
    @Js
    def PyJs_anonymous_60_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['w', 'a', 't', 'h', 'd', 'g', 'n', 'i', 'A', 'F', 'u', 'C', 's', 'E', 'l'])
        @Js
        def PyJsHoisted_A_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            return var.get('w')(var.get('F')(var.get('c')(var.get('n')), (var.get('n').get('length')*Js(8.0))))
        PyJsHoisted_A_.func_name = 'A'
        var.put('A', PyJsHoisted_A_)
        @Js
        def PyJsHoisted_s_(n, t, this, arguments, var=var):
            var = Scope({'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'r', 'n', 'i', 'f', 'o', 'u'])
            var.put('n', (var.get('e')(var.get('n')) if var.get('h') else var.get('n')))
            var.put('t', (var.get('e')(var.get('t')) if var.get('h') else var.get('t')))
            var.put('f', var.get('c')(var.get('n')))
            var.put('i', var.get('Array')(Js(16.0)))
            var.put('u', var.get('Array')(Js(16.0)))
            if (var.get('f').get('length')>Js(16.0)):
                var.put('f', var.get('F')(var.get('f'), (var.get('n').get('length')*Js(8.0))))
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<Js(16.0)):
                try:
                    var.get('i').put(var.get('r'), (var.get('f').get(var.get('r'))^Js(909522486.0)))
                    var.get('u').put(var.get('r'), (var.get('f').get(var.get('r'))^Js(1549556828.0)))
                finally:
                        var.put('r', Js(1.0), '+')
            var.put('o', var.get('F')(var.get('i').callprop('concat', var.get('c')(var.get('t'))), (Js(512.0)+(var.get('t').get('length')*Js(8.0)))))
            return var.get('w')(var.get('F')(var.get('u').callprop('concat', var.get('o')), (Js(512.0)+Js(160.0))))
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        @Js
        def PyJsHoisted_w_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n', 'e', 't', 'r'])
            var.put('t', Js(''))
            var.put('r', (var.get('n').get('length')*Js(32.0)))
            #for JS loop
            var.put('e', Js(0.0))
            while (var.get('e')<var.get('r')):
                try:
                    var.put('t', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('n').get((var.get('e')>>Js(5.0))),(var.get('e')%Js(32.0)))&Js(255.0))), '+')
                finally:
                        var.put('e', Js(8.0), '+')
            return var.get('t')
        PyJsHoisted_w_.func_name = 'w'
        var.put('w', PyJsHoisted_w_)
        @Js
        def PyJsHoisted_F_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['w', 't', 'm', '_', 'c', 'h', 'S', 'D', 'e', 'x', 'A', 's', 'y', 'i', 'f', 'b', 'B', 'v', 'p', 'n', 'F'])
            var.put('c', Js(1732584193.0))
            var.put('D', Js(4023233417.0))
            var.put('B', Js(2562383102.0))
            var.put('A', Js(271733878.0))
            var.put('s', Js(3285377520.0))
            var.get('n').put((var.get('e')>>Js(5.0)), (Js(128.0)<<(var.get('e')%Js(32.0))), '|')
            var.get('n').put(((PyJsBshift((var.get('e')+Js(64.0)),Js(9.0))<<Js(4.0))+Js(14.0)), var.get('e'))
            var.put('h', var.get('n').get('length'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('h')):
                try:
                    var.put('w', var.put('v', var.get('c')))
                    var.put('F', var.put('m', var.get('D')))
                    var.put('p', var.put('x', var.get('B')))
                    var.put('y', var.put('_', var.get('A')))
                    var.put('b', var.put('S', var.get('s')))
                    #for JS loop
                    var.put('f', Js(0.0))
                    while (var.get('f')<=Js(79.0)):
                        try:
                            var.put('t', var.get('r')(var.get('w'), var.get('E')(var.get('f'), var.get('F'), var.get('p'), var.get('y'))))
                            var.put('t', var.get('r')(var.get('t'), var.get('n').get((var.get('i')+var.get('u').get(var.get('f'))))))
                            var.put('t', var.get('r')(var.get('t'), var.get('d')(var.get('f'))))
                            var.put('t', var.get('r')(var.get('o')(var.get('t'), var.get('l').get(var.get('f'))), var.get('b')))
                            var.put('w', var.get('b'))
                            var.put('b', var.get('y'))
                            var.put('y', var.get('o')(var.get('p'), Js(10.0)))
                            var.put('p', var.get('F'))
                            var.put('F', var.get('t'))
                            var.put('t', var.get('r')(var.get('v'), var.get('E')((Js(79.0)-var.get('f')), var.get('m'), var.get('x'), var.get('_'))))
                            var.put('t', var.get('r')(var.get('t'), var.get('n').get((var.get('i')+var.get('a').get(var.get('f'))))))
                            var.put('t', var.get('r')(var.get('t'), var.get('g')(var.get('f'))))
                            var.put('t', var.get('r')(var.get('o')(var.get('t'), var.get('C').get(var.get('f'))), var.get('S')))
                            var.put('v', var.get('S'))
                            var.put('S', var.get('_'))
                            var.put('_', var.get('o')(var.get('x'), Js(10.0)))
                            var.put('x', var.get('m'))
                            var.put('m', var.get('t'))
                        finally:
                                var.put('f', Js(1.0), '+')
                    var.put('t', var.get('r')(var.get('D'), var.get('r')(var.get('p'), var.get('_'))))
                    var.put('D', var.get('r')(var.get('B'), var.get('r')(var.get('y'), var.get('S'))))
                    var.put('B', var.get('r')(var.get('A'), var.get('r')(var.get('b'), var.get('v'))))
                    var.put('A', var.get('r')(var.get('s'), var.get('r')(var.get('w'), var.get('m'))))
                    var.put('s', var.get('r')(var.get('c'), var.get('r')(var.get('F'), var.get('x'))))
                    var.put('c', var.get('t'))
                finally:
                        var.put('i', Js(16.0), '+')
            return Js([var.get('c'), var.get('D'), var.get('B'), var.get('A'), var.get('s')])
        PyJsHoisted_F_.func_name = 'F'
        var.put('F', PyJsHoisted_F_)
        @Js
        def PyJsHoisted_E_(n, e, t, r, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't', 'n'])
            def PyJs_LONG_72_(var=var):
                return (((var.get('e')&var.get('t'))|((~var.get('e'))&var.get('r'))) if ((Js(16.0)<=var.get('n')) and (var.get('n')<=Js(31.0))) else (((var.get('e')|(~var.get('t')))^var.get('r')) if ((Js(32.0)<=var.get('n')) and (var.get('n')<=Js(47.0))) else (((var.get('e')&var.get('r'))|(var.get('t')&(~var.get('r')))) if ((Js(48.0)<=var.get('n')) and (var.get('n')<=Js(63.0))) else ((var.get('e')^(var.get('t')|(~var.get('r')))) if ((Js(64.0)<=var.get('n')) and (var.get('n')<=Js(79.0))) else Js('rmd160_f: j out of range')))))
            return (((var.get('e')^var.get('t'))^var.get('r')) if ((Js(0.0)<=var.get('n')) and (var.get('n')<=Js(15.0))) else PyJs_LONG_72_())
        PyJsHoisted_E_.func_name = 'E'
        var.put('E', PyJsHoisted_E_)
        @Js
        def PyJsHoisted_d_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            def PyJs_LONG_73_(var=var):
                return (Js(0.0) if ((Js(0.0)<=var.get('n')) and (var.get('n')<=Js(15.0))) else (Js(1518500249.0) if ((Js(16.0)<=var.get('n')) and (var.get('n')<=Js(31.0))) else (Js(1859775393.0) if ((Js(32.0)<=var.get('n')) and (var.get('n')<=Js(47.0))) else (Js(2400959708.0) if ((Js(48.0)<=var.get('n')) and (var.get('n')<=Js(63.0))) else (Js(2840853838.0) if ((Js(64.0)<=var.get('n')) and (var.get('n')<=Js(79.0))) else Js('rmd160_K1: j out of range'))))))
            return PyJs_LONG_73_()
        PyJsHoisted_d_.func_name = 'd'
        var.put('d', PyJsHoisted_d_)
        @Js
        def PyJsHoisted_g_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            def PyJs_LONG_74_(var=var):
                return (Js(1352829926.0) if ((Js(0.0)<=var.get('n')) and (var.get('n')<=Js(15.0))) else (Js(1548603684.0) if ((Js(16.0)<=var.get('n')) and (var.get('n')<=Js(31.0))) else (Js(1836072691.0) if ((Js(32.0)<=var.get('n')) and (var.get('n')<=Js(47.0))) else (Js(2053994217.0) if ((Js(48.0)<=var.get('n')) and (var.get('n')<=Js(63.0))) else (Js(0.0) if ((Js(64.0)<=var.get('n')) and (var.get('n')<=Js(79.0))) else Js('rmd160_K2: j out of range'))))))
            return PyJs_LONG_74_()
        PyJsHoisted_g_.func_name = 'g'
        var.put('g', PyJsHoisted_g_)
        var.put('t', (var.get('n').get('uppercase') if (var.get('n') and PyJsStrictEq(var.get('n').get('uppercase').typeof(),Js('boolean'))) else Js(False)))
        var.put('i', (var.get('n').get('pda') if (var.get('n') and PyJsStrictEq(var.get('n').get('pad').typeof(),Js('string'))) else Js('=')))
        var.put('h', (var.get('n').get('utf8') if (var.get('n') and PyJsStrictEq(var.get('n').get('utf8').typeof(),Js('boolean'))) else Js(True)))
        var.put('u', Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(7.0), Js(4.0), Js(13.0), Js(1.0), Js(10.0), Js(6.0), Js(15.0), Js(3.0), Js(12.0), Js(0.0), Js(9.0), Js(5.0), Js(2.0), Js(14.0), Js(11.0), Js(8.0), Js(3.0), Js(10.0), Js(14.0), Js(4.0), Js(9.0), Js(15.0), Js(8.0), Js(1.0), Js(2.0), Js(7.0), Js(0.0), Js(6.0), Js(13.0), Js(11.0), Js(5.0), Js(12.0), Js(1.0), Js(9.0), Js(11.0), Js(10.0), Js(0.0), Js(8.0), Js(12.0), Js(4.0), Js(13.0), Js(3.0), Js(7.0), Js(15.0), Js(14.0), Js(5.0), Js(6.0), Js(2.0), Js(4.0), Js(0.0), Js(5.0), Js(9.0), Js(7.0), Js(12.0), Js(2.0), Js(10.0), Js(14.0), Js(1.0), Js(3.0), Js(8.0), Js(11.0), Js(6.0), Js(15.0), Js(13.0)]))
        var.put('a', Js([Js(5.0), Js(14.0), Js(7.0), Js(0.0), Js(9.0), Js(2.0), Js(11.0), Js(4.0), Js(13.0), Js(6.0), Js(15.0), Js(8.0), Js(1.0), Js(10.0), Js(3.0), Js(12.0), Js(6.0), Js(11.0), Js(3.0), Js(7.0), Js(0.0), Js(13.0), Js(5.0), Js(10.0), Js(14.0), Js(15.0), Js(8.0), Js(12.0), Js(4.0), Js(9.0), Js(1.0), Js(2.0), Js(15.0), Js(5.0), Js(1.0), Js(3.0), Js(7.0), Js(14.0), Js(6.0), Js(9.0), Js(11.0), Js(8.0), Js(12.0), Js(2.0), Js(10.0), Js(0.0), Js(4.0), Js(13.0), Js(8.0), Js(6.0), Js(4.0), Js(1.0), Js(3.0), Js(11.0), Js(15.0), Js(0.0), Js(5.0), Js(12.0), Js(2.0), Js(13.0), Js(9.0), Js(7.0), Js(10.0), Js(14.0), Js(12.0), Js(15.0), Js(10.0), Js(4.0), Js(1.0), Js(5.0), Js(8.0), Js(7.0), Js(6.0), Js(2.0), Js(13.0), Js(14.0), Js(0.0), Js(3.0), Js(9.0), Js(11.0)]))
        var.put('l', Js([Js(11.0), Js(14.0), Js(15.0), Js(12.0), Js(5.0), Js(8.0), Js(7.0), Js(9.0), Js(11.0), Js(13.0), Js(14.0), Js(15.0), Js(6.0), Js(7.0), Js(9.0), Js(8.0), Js(7.0), Js(6.0), Js(8.0), Js(13.0), Js(11.0), Js(9.0), Js(7.0), Js(15.0), Js(7.0), Js(12.0), Js(15.0), Js(9.0), Js(11.0), Js(7.0), Js(13.0), Js(12.0), Js(11.0), Js(13.0), Js(6.0), Js(7.0), Js(14.0), Js(9.0), Js(13.0), Js(15.0), Js(14.0), Js(8.0), Js(13.0), Js(6.0), Js(5.0), Js(12.0), Js(7.0), Js(5.0), Js(11.0), Js(12.0), Js(14.0), Js(15.0), Js(14.0), Js(15.0), Js(9.0), Js(8.0), Js(9.0), Js(14.0), Js(5.0), Js(6.0), Js(8.0), Js(6.0), Js(5.0), Js(12.0), Js(9.0), Js(15.0), Js(5.0), Js(11.0), Js(6.0), Js(8.0), Js(13.0), Js(12.0), Js(5.0), Js(12.0), Js(13.0), Js(14.0), Js(11.0), Js(8.0), Js(5.0), Js(6.0)]))
        var.put('C', Js([Js(8.0), Js(9.0), Js(9.0), Js(11.0), Js(13.0), Js(15.0), Js(15.0), Js(5.0), Js(7.0), Js(7.0), Js(8.0), Js(11.0), Js(14.0), Js(14.0), Js(12.0), Js(6.0), Js(9.0), Js(13.0), Js(15.0), Js(7.0), Js(12.0), Js(8.0), Js(9.0), Js(11.0), Js(7.0), Js(7.0), Js(12.0), Js(7.0), Js(6.0), Js(15.0), Js(13.0), Js(11.0), Js(9.0), Js(7.0), Js(15.0), Js(11.0), Js(8.0), Js(6.0), Js(6.0), Js(14.0), Js(12.0), Js(13.0), Js(5.0), Js(14.0), Js(13.0), Js(13.0), Js(7.0), Js(5.0), Js(15.0), Js(5.0), Js(8.0), Js(11.0), Js(14.0), Js(14.0), Js(6.0), Js(14.0), Js(6.0), Js(9.0), Js(12.0), Js(9.0), Js(12.0), Js(5.0), Js(15.0), Js(8.0), Js(8.0), Js(5.0), Js(12.0), Js(9.0), Js(12.0), Js(5.0), Js(14.0), Js(6.0), Js(8.0), Js(13.0), Js(6.0), Js(5.0), Js(15.0), Js(13.0), Js(11.0), Js(11.0)]))
        @Js
        def PyJs_anonymous_61_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('f')(var.get('A')(var.get('n'), var.get('h')))
        PyJs_anonymous_61_._set_name('anonymous')
        var.get(u"this").put('hex', PyJs_anonymous_61_)
        @Js
        def PyJs_anonymous_62_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('B')(var.get('A')(var.get('n'), var.get('h')), var.get('i'))
        PyJs_anonymous_62_._set_name('anonymous')
        var.get(u"this").put('b64', PyJs_anonymous_62_)
        @Js
        def PyJs_anonymous_63_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('D')(var.get('A')(var.get('n'), var.get('h')), var.get('e'))
        PyJs_anonymous_63_._set_name('anonymous')
        var.get(u"this").put('any', PyJs_anonymous_63_)
        @Js
        def PyJs_anonymous_64_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get('A')(var.get('n'), var.get('h'))
        PyJs_anonymous_64_._set_name('anonymous')
        var.get(u"this").put('raw', PyJs_anonymous_64_)
        @Js
        def PyJs_anonymous_65_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('f')(var.get('s')(var.get('n'), var.get('e')))
        PyJs_anonymous_65_._set_name('anonymous')
        var.get(u"this").put('hex_hmac', PyJs_anonymous_65_)
        @Js
        def PyJs_anonymous_66_(n, e, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'n'])
            return var.get('B')(var.get('s')(var.get('n'), var.get('e')), var.get('i'))
        PyJs_anonymous_66_._set_name('anonymous')
        var.get(u"this").put('b64_hmac', PyJs_anonymous_66_)
        @Js
        def PyJs_anonymous_67_(n, e, t, this, arguments, var=var):
            var = Scope({'n':n, 'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'n'])
            return var.get('D')(var.get('s')(var.get('n'), var.get('e')), var.get('t'))
        PyJs_anonymous_67_._set_name('anonymous')
        var.get(u"this").put('any_hmac', PyJs_anonymous_67_)
        @Js
        def PyJs_anonymous_68_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get('hex')(Js('abc')).callprop('toLowerCase'),Js('900150983cd24fb0d6963f7d28e17f72'))
        PyJs_anonymous_68_._set_name('anonymous')
        var.get(u"this").put('vm_test', PyJs_anonymous_68_)
        @Js
        def PyJs_anonymous_69_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('t', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_69_._set_name('anonymous')
        var.get(u"this").put('setUpperCase', PyJs_anonymous_69_)
        @Js
        def PyJs_anonymous_70_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n',throw=False).typeof(),Js('undefined')):
                var.put('i', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_70_._set_name('anonymous')
        var.get(u"this").put('setPad', PyJs_anonymous_70_)
        @Js
        def PyJs_anonymous_71_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('boolean')):
                var.put('h', var.get('n'))
            return var.get(u"this")
        PyJs_anonymous_71_._set_name('anonymous')
        var.get(u"this").put('setUTF8', PyJs_anonymous_71_)
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    PyJs_anonymous_60_._set_name('anonymous')
    PyJs_Object_1_ = Js({'VERSION':Js('1.0.5'),'Base64':PyJs_anonymous_2_,'CRC32':PyJs_anonymous_8_,'MD5':PyJs_anonymous_10_,'SHA1':PyJs_anonymous_22_,'SHA256':PyJs_anonymous_34_,'SHA512':PyJs_anonymous_47_,'RMD160':PyJs_anonymous_60_})
    var.put('n', PyJs_Object_1_)
    @Js
    def PyJs_anonymous_75_(e, t, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 't', 'r'])
        var.put('r', Js(False))
        if PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')):
            var.put('r', var.get('exports'))
            if (((var.get('exports') and PyJsStrictEq(var.get('global',throw=False).typeof(),Js('object'))) and var.get('global')) and PyJsStrictEq(var.get('global'),var.get('global').get('global'))):
                var.put('e', var.get('global'))
        if ((PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and PyJsStrictEq(var.get('define').get('amd').typeof(),Js('object'))) and var.get('define').get('amd')):
            @Js
            def PyJs_anonymous_76_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return var.get('n')
            PyJs_anonymous_76_._set_name('anonymous')
            var.get('define')(PyJs_anonymous_76_)
        else:
            if var.get('r'):
                if ((PyJsStrictEq(var.get('module',throw=False).typeof(),Js('object')) and var.get('module')) and PyJsStrictEq(var.get('module').get('exports'),var.get('r'))):
                    var.get('module').put('exports', var.get('n'))
                else:
                    var.get('r').put('Hashes', var.get('n'))
            else:
                var.get('e').put('Hashes', var.get('n'))
    PyJs_anonymous_75_._set_name('anonymous')
    PyJs_anonymous_75_(var.get(u"this"))
PyJs_anonymous_0_._set_name('anonymous')
PyJs_anonymous_0_()
pass
pass
pass


# Add lib to the module scope
js_lib = var.to_python()
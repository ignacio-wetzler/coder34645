import string

class Clave():    
    def __init__(self,clave):
        self.clave = self.clave_valida(clave)
    
    def __str__(self):
        return self.clave

    def clave_valida(self, clave):
        check_minl = 6
        check_maxl = 10 
        check_uppc = set(string.ascii_uppercase) 
        check_lowc = set(string.ascii_lowercase) 
        check_symc = set(string.punctuation) 
        check_numb = set(string.digits) 
        b_chk_minl = len(clave) >= check_minl 
        b_chk_maxl = len(clave) <= check_maxl 
        b_chk_uppc = not set(clave).isdisjoint(check_uppc)  
        b_chk_lowc = not set(clave).isdisjoint(check_lowc)
        b_chk_numc = not set(clave).isdisjoint(check_numb)
        b_chk_symc = not set(clave).isdisjoint(check_symc)
        d_es_valid = {}
        d_es_valid["Cantidad Minima de Caracteres"] = b_chk_minl
        d_es_valid["Cantidad Maxima de Caracteres"] = b_chk_maxl
        d_es_valid["Contiene Mayusculas"] = b_chk_uppc
        d_es_valid["Contiene Minusculas"] = b_chk_lowc
        d_es_valid["Contiene Numeros"] = b_chk_numc
        d_es_valid["Contiene Simbolos"] = b_chk_symc
        b_es_valid = True

        for i in d_es_valid:
            print(f"{i}: {d_es_valid[i]}")
            if d_es_valid[i] == True and b_es_valid == True:
                b_es_valid = True
            else:
                b_es_valid = False
        print(f"La clave es valida: {b_es_valid}")
        
        if b_es_valid == True:
            return(clave)
        else:
            return("------")
        
               
pass1 = Clave("!26etz03")
print(pass1)
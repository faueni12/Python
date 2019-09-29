import tkinter as tk
from urllib.request import Request, urlopen

class App():
    def __init__(self, toplan):
        self.vulneraveis = []
        self.cont = 0

        self.fontenormal = ('Verdana', '10')
        self.fonteexemplo = ('Verdana', '8')
        self.fontetitulo = ('Verdana', '12', 'bold')
        self.fontebutton = ('Verdana', '10', 'bold')
        
        self.configuracoes_label = {'font': self.fontenormal, 'bg':bg_retangulo}
        self.config_asterisco = {'fg':'red', 'font':('Verdana','8','bold'), 'bg':bg_retangulo, 'bd':0.5, 'text':'*'}
        
        self.widget1 = tk.Frame(toplan)
        self.widget1['bg'] = '#1E90FF'
        self.widget1.place(x=124, y=44, width=546, height=406, anchor='nw')

        self.retangulo = tk.Frame(self.widget1)
        self.retangulo['bg'] = bg_retangulo
        self.retangulo.place(x=3, y=3, width=540, height=400, anchor='nw')
        
        self.menu = tk.Menubutton(self.retangulo, text='Menu', bg='#1E90FF', font=('Verdana', '10', 'bold'))
        self.menu_ = tk.Menu(self.menu)
        self.menu['menu'] = self.menu_

        self.menu_.add_command(label='Search for vulnerable sites', command=self.Radios_search)
        self.menu.place(x=0, y=0)

    def Radios_search(self):
        one = tk.StringVar()
        y_1 = 50
        self.x_3 = 20
        self.y_3 = 120
        Radio1 = tk.Radiobutton(self.retangulo, bg='#6495ED', text='I have the URL here', variable=one, value=True, command=self.have_url)
        Radio2 = tk.Radiobutton(self.retangulo, bg='#6495ED', text='I want to do it manually', variable=one, value=False, command=self.nohave_url)
        Radio1.place(x=20, y=y_1)
        Radio2.place(x=20, y=y_1+30)

    def have_url(self):
        try:
            self.lista_destroy = [self.label_formulary, self.formulary_search, self.label_site, self.site, self.label_inurl, self.inurl, self.label_intervalo, self.intervalo,
                                  self.asterisco_intervalo,
                                self.label_tempo, self.asterisco_tempo]
            for radios in self.radio:
                self.lista_destroy.append(radios)
                
            self.Destroy_components(self.lista_destroy)
        except:
            pass
        try:
            self.btn_confirm.destroy()
        except:
            pass
        
        self.label_url = tk.Label(self.retangulo, self.configuracoes_label, text='Url:')
        self.label_url.place(x=x_1+90, y=y_1, anchor='ne')
        tk.Label(self.retangulo, self.config_asterisco).place(x=x_1+84.5, y=y_1)
        self.url = tk.Entry(self.retangulo)
        self.url.place(x=x_1+95, y=y_1)
    
        self.x_1 = x_1
        
        self.ListaSites()

        #---Create-Botão-Confirmar---
        self.btn_confirm = tk.Button(self.retangulo, text='Start',padx=20, font=self.fontebutton, bg='#00BFFF', command=self.Verificar_haveurl)
        self.btn_confirm.place(x=x_1+86, y=y_1+45, anchor='nw')
                
    def nohave_url(self):
        try:
            self.lista_destroy = [self.url, self.label_url, self.label_formulary, self.formulary_search, self.label_site, self.site, self.label_inurl, self.inurl,
                                  self.label_intervalo, self.intervalo, self.asterisco_intervalo,
                                  self.label_tempo, self.asterisco_tempo]
            for radios in self.radio:
                self.lista_destroy.append(radios)
            
            self.Destroy_components(self.lista_destroy)
        except:
            pass
        try:
            self.btn_confirm.destroy()
        except:
            pass

        self.label_formulary = tk.Label(self.retangulo, self.configuracoes_label, text='Formulary search:')
        self.label_formulary.place(x=x_1-35, y=y_1, anchor='nw')
        tk.Label(self.retangulo, self.config_asterisco).place(x=x_1+84.5, y=y_1)
        
        self.formulary_search = tk.Entry(self.retangulo)
        self.formulary_search.place(x=x_1+95, y=y_1, anchor='nw')

        self.label_site = tk.Label(self.retangulo, self.configuracoes_label,  text='Site:')
        self.site = tk.Entry(self.retangulo)
        self.label_site.place(x=x_1+50, y=y_1+30, anchor='nw')
        self.site.place(x=x_1+95, y=y_1+30)

        self.label_inurl = tk.Label(self.retangulo, self.configuracoes_label,  text='Inurl:')
        self.inurl = tk.Entry(self.retangulo)
        self.label_inurl.place(x=x_1+50, y=y_1+60, anchor='nw')
        self.inurl.place(x=x_1+95, y=y_1+60)

        self.label_intervalo = tk.Label(self.retangulo, self.configuracoes_label,  text='Interval:')
        self.intervalo = tk.Entry(self.retangulo)
        self.label_intervalo.place(x=x_1+20, y=y_1+90, anchor='nw')
        self.intervalo.place(x=x_1+95, y=y_1+90)
        self.asterisco_intervalo = tk.Label(self.retangulo, self.config_asterisco)
        self.asterisco_intervalo.place(x=x_1+84.5, y=y_1+90)

        tempos = [('Any date','&tbs=qdr'), ('In last hour', '&tbs=qdr:h'),
                  ('In last day', '&tbs=qdr:d'), ('In last week', '&tbs=qdr:w'),
                  ('In last month', '&tbs=qdr:m'), ('In last year', '&tbs=qdr:y')]
        self.tempo = tk.StringVar()
        self.radio = list(range(0,6))
        i = 0
        y_2 = y_1+150
        x_2 = x_1
        for texto, valor in tempos:
            self.radio[i] = tk.Radiobutton(self.retangulo, text=texto, variable=self.tempo, value=valor, bg=bg_retangulo)
            if i%2 == 1:
                self.radio[i].place(x=x_2+100, y=y_2)
                y_2 += 30
            else:
                self.radio[i].place(x=x_2, y=y_2)
            i += 1
        self.y_2 = y_2
        self.x_2 = x_2
        
        self.label_tempo = tk.Label(self.retangulo, self.configuracoes_label, text='Time')
        self.label_tempo.place(x=x_2+100, y=y_1+130, anchor='center')
        self.asterisco_tempo = tk.Label(self.retangulo, self.config_asterisco, bd=0.1)
        self.asterisco_tempo.place(x=x_2+120, y=y_1+130, anchor='center')

        self.ListaSites()

        self.btn_confirm = tk.Button(self.retangulo, text='Start',padx=20, font=self.fontebutton, bg='#00BFFF', command=self.Verificar_no_haveurl)
        self.btn_confirm.place(x=x_2, y=y_2+45, anchor='nw')

    
    def Destroy_components(self, lista):
        for i in lista:
            i.destroy()

    def ListaSites(self):
        if self.cont != 1:
            self.label_sb = tk.Label(self.retangulo, font=self.fontebutton, text='Vulnerable sites', bg=bg_retangulo)
            self.label_sb.place(x=self.x_3+38, y=self.y_3+8)
            self.sb = tk.Scrollbar(self.retangulo)
            self.sb.place(x=self.x_3+218.5, y=self.y_3+40, anchor='nw')
            self.lista = tk.Listbox(self.retangulo, yscrollcommand=self.sb.set, width=36)

            self.lista.place(x=self.x_3, y=self.y_3+40,anchor='nw')
            self.sb.config(command=self.lista.yview)
            self.cont = 1

    def Verificar_haveurl(self):
        self.sites = []
        self.url_completa = self.url.get()
        self.req = Request(self.url_completa, headers={'User-Agent': 'Mozilla/5.0'})
        self.web_page = urlopen(self.req).read()
        self.webpage = self.web_page.decode('utf-8')

        self.tag_inicio = '<a href="/url?q='
        self.tag_final = '&amp'
        self.caracteres_google = {'%3F':'?', '%3D':'='}
        self.lista_caracteres = list(self.caracteres_google.keys())
        self.inicio = self.webpage.find(self.tag_inicio)
        while self.inicio != -1:
            #------------pegar site-----------------
            self.final = self.webpage.find(self.tag_final, self.inicio)
            self.site_analise = (self.webpage[self.inicio+16:self.final])
            #------------------tirar caracteres_google do site-----------------
            if self.lista_caracteres[0] in self.site_analise or self.lista_caracteres[1] in self.site_analise:
                start = self.site_analise.find(self.lista_caracteres[0])
                while start != -1:
                    self.site_analise = self.site_analise[:start] + '?' + self.site_analise[start+len(self.lista_caracteres[0]):]
                    start = self.site_analise.find(self.lista_caracteres[0], start+1)
                start = self.site_analise.find(self.lista_caracteres[1])
                while start != -1:
                    self.site_analise = self.site_analise[:start] + '=' + self.site_analise[start+len(self.lista_caracteres[1]):]
                    start = self.site_analise.find(self.lista_caracteres[1], start+1)
                    #-----------------------------------------------------------------------
            self.sites += [self.site_analise]
            self.inicio = self.webpage.find(self.tag_inicio, self.inicio+1)
        self.mensagem_sqlerror = "You have an error in your SQL syntax; check the manual that corresponds to your"
        for i in range(0, len(self.sites)):
                try:
                    self.req = Request(self.sites[i]+"'")
                    self.html_site = str(urlopen(self.req).read())
                    if self.mensagem_sqlerror in self.html_site:
                        self.vulneraveis += [self.sites[i]]
                        self.lista.insert(tk.END, self.sites[i])
                except:
                    print('Not is possible analyze '+self.sites[i]+' :(')
                    i = i+1
        self.lista.insert(tk.END, '-------------------------------------------')
    

    def Verificar_no_haveurl(self):
        self.sites = []

        self.formulary_ = self.formulary_search.get().strip() #strip pra tirar os espaços
        
        self.site_ = self.site.get().strip()
        self.inurl_ = self.inurl.get().strip()
        self.time_ = self.tempo.get().strip()
        
        self.intervalo_ = self.intervalo.get()
        self.intervalo_ = self.intervalo_.split()
        self.intervaloinicial = (int(self.intervalo_[0])-1) * 10
        self.intervalofinal = (int(self.intervalo_[1])-1) * 10
            
        for paginas in range(self.intervaloinicial, self.intervalofinal, 10):
            if self.site_ != '':
                self.url_manual = (self.formulary_ + 'site:'+self.site_ +'%20'+'inurl:'+self.inurl_+self.time_)
            else:
                self.url_manual = (self.formulary_ +'inurl:'+self.inurl_+self.time_)
            self.url_manual += '&start='+str(paginas)
            self.req = Request(self.url_manual, headers={'User-Agent': 'Mozilla/5.0'})
            self.web_page = urlopen(self.req).read()
            self.webpage = self.web_page.decode('utf-8')
    
            self.tag_inicio = '<a href="/url?q='
            self.tag_final = '&amp'
            self.caracteres_google = {'%3F':'?', '%3D':'='}
            self.lista_caracteres = list(self.caracteres_google.keys())
            self.inicio = self.webpage.find(self.tag_inicio)
            while self.inicio != -1:
                #------------pegar site-----------------
                self.final = self.webpage.find(self.tag_final, self.inicio)
                self.site_analise = (self.webpage[self.inicio+16:self.final])
                #------------------tirar caracteres_google do site-----------------
                if self.lista_caracteres[0] in self.site_analise or self.lista_caracteres[1] in self.site_analise:
                    start = self.site_analise.find(self.lista_caracteres[0])
                    while start != -1:
                        self.site_analise = self.site_analise[:start] + '?' + self.site_analise[start+len(self.lista_caracteres[0]):]
                        start = self.site_analise.find(self.lista_caracteres[0], start+1)
                    start = self.site_analise.find(self.lista_caracteres[1])
                    while start != -1:
                        self.site_analise = self.site_analise[:start] + '=' + self.site_analise[start+len(self.lista_caracteres[1]):]
                        start = self.site_analise.find(self.lista_caracteres[1], start+1)
                        #-----------------------------------------------------------------------
                self.sites += [self.site_analise]
                self.inicio = self.webpage.find(self.tag_inicio, self.inicio+1)
        self.mensagem_sqlerror = "You have an error in your SQL syntax; check the manual that corresponds to your"
        for i in range(0, len(self.sites)):
                try:
                    self.req = Request(self.sites[i]+"'")
                    self.html_site = str(urlopen(self.req).read())
                    if self.mensagem_sqlerror in self.html_site:
                        self.vulneraveis += [self.sites[i]]
                        self.lista.insert(tk.END, self.sites[i])
                except:
                    print('Not is possible analyze '+self.sites[i]+' :(')
                    i = i+1
        self.lista.insert(tk.END, '-------------------------------------------')
    
    
window = tk.Tk()

y_1 = 50
x_1 = 300
bg_retangulo = '#F0F8FF'

window.title('Decodifer')
window.geometry('800x500+100+100')
window.maxsize(width=800, height=500)
window.minsize(width=800, height=500)

image_bg = tk.PhotoImage(file='fundo_.gif')
window_bg = tk.Label(window, image=image_bg)
window_bg.pack()

App(window)
window.tk.mainloop()

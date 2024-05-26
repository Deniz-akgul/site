from flask import Flask
import random

app = Flask(__name__)
facts_list=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.", "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.", "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.", "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.","Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

yazi_tura=["YAZI!!!","TURA!!!"]

@app.route("/")
def hello_world():    
    return '''<h1>Merhaba bu sayfada teknoloji hakkında rastgele gerçekler öğreniyorsun!</h1>
    <a href="/random_fact" >rastgele bir gerçeği görüntüle!</a>
    <a href="/yazi_tura" >Yazı tura at!</a>'''
@app.route("/random_fact")
def random_fact():
    return f'<h3>{random.choice(facts_list)}</h3>'

@app.route("/yazi_tura")
def yazitura():
    return f'<h1>{random.choice(yazi_tura)}</h1>'


app.run(debug=True

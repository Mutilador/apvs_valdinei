from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    date_register = models.DateTimeField(auto_now=timezone.now())
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

tipo_carro = (
    ('CARRO', 'Carro'),
    ('MOTO', 'Moto'),
    ('CAMINHAO', 'Caminhão'),
    ('NAUTICO', 'Nautico'),
)

modelo_caminhao = (
    ("1","AGRALE"),("2","BEPOBUS"),
    ("3","CHEVROLET"),("4","CICCOBUS"),
    ("5","DAF"),("6","EFFA-JMC"),
    ("7","FIAT"),("8","FORD"),
    ("9","FOTON"),("10","GMC"),
    ("11","HYUNDAI"),("12","IVECO"),
    ("13","MAN"),("14","MARCOPOLO"),
    ("15","MASCARELLO"),("16","MAXIBUS"),
    ("17","MERCEDES-BENZ"),("18","NAVISTAR"),
    ("19","NEOBUS"),("20","PUMA-ALFA"),
    ("21","SAAB-SCANIA"),("22","SCANIA"),
    ("23","SHACMAN"),("24","SINOTRUK"),
    ("25","VOLKSWAGEN"),("26","VOLVO"),
    ("27","WALKBUS"),
)

modelo_carro = (
    ("1","Acura"),("2","Agrale"),
    ("3","Alfa Romeo"),("4","AM Gen"),
    ("5","Asia Motors"),("6","ASTON MARTIN"),
    ("7","Audi"),("8","BMW"),("9","BRM"),
    ("10","Buggy"),("11","Bugre"),
    ("12","Cadillac"),("13","CBT Jipe"),
    ("14","CHANA"),("15","CHANGAN"),
    ("16","CHERY"),("17","Chrysler"),
    ("18","Citroën"),("19","Cross Lander"),
    ("20","Daewoo"),("21","Daihatsu"),
    ("22","Dodge"),("23","EFFA"),
    ("24","Engesa"),("25","Envemo"),
    ("26","Ferrari"),("27","Fiat"),
    ("28","Fibravan"),("29","Ford"),
    ("30","FOTON"),("31","Fyber"),
    ("32","GEELY"),("33","GM - Chevrolet"),
    ("34","GREAT WALL"),("35","Gurgel"),
    ("36","HAFEI"),("37","Honda"),
    ("38","Hyundai"),("39","Isuzu"),
    ("40","JAC"),("41","Jaguar"),
    ("42","Jeep"),("43","JINBEI"),
    ("44","JPX"),("45","Kia Motors"),
    ("46","Lada"),("47","LAMBORGHINI"),
    ("48","Land Rover"),("49","Lexus"),
    ("50","LIFAN"),("51","LOBINI"),
    ("52","Lotus"),("53","Mahindra"),
    ("54","Maserati"),("55","Matra"),
    ("56","Mazda"),("57","Mercedes-Benz"),
    ("58","Mercury"),("59","MG"),
    ("60","MINI"),("61","Mitsubishi"),
    ("62","Miura"),("63","Nissan"),
    ("64","Peugeot"),("65","Plymouth"),
    ("66","Pontiac"),("67","Porsche"),
    ("68","RAM"),("69","RELY"),
    ("70","Renault"),("71","Rolls-Royce"),
    ("72","Rover"),("73","Saab"),
    ("74","Saturn"),("75","Seat"),
    ("76","SHINERAY"),("77","smart"),
    ("78","SSANGYONG"),("79","Subaru"),
    ("80","Suzuki"),("81","TAC"),
    ("82","Toyota"),("83","Troller"),
    ("84","Volvo"),("85","VW - VolksWagen"),
    ("86","Wake"),("87","Walk"),
)

modelo_moto = (
    ("60","ADLY"),("61","AGRALE"),
    ("131","AMAZONAS"),("62","APRILIA"),
    ("63","ATALA"),("64","BAJAJ"),
    ("205","BEE"),("162","Benelli"),
    ("65","BETA"),("66","BIMOTA"),
    ("67","BMW"),("68","BRANDY"),
    ("130","BRAVA"),("150","BRP"),
    ("117","BUELL"),("155","BUENO"),
    ("69","byCristo"),("70","CAGIVA"),
    ("71","CALOI"),("72","DAELIM"),
    ("145","DAFRA"),("137","DAYANG"),
    ("142","DAYUN"),("73","DERBI"),
    ("74","DUCATI"),("75","EMME"),
    ("132","FOX"),("128","FYM"),
    ("143","GARINNI"),("76","GAS GAS"),
    ("133","GREEN"),("138","HAOBAO"),
    ("203","HAOJUE"),("77","HARLEY-DAVIDSON"),
    ("78","HARTFORD"),("79","HERO"),
    ("80","HONDA"),("81","HUSABERG"),
    ("82","HUSQVARNA"),("202","INDIAN"),
    ("158","IROS"),("141","JIAPENG VOLCANO"),
    ("174","JOHNNYPAG"),("151","JONNY"),
    ("129","KAHENA"),("118","KASINSKI"),
    ("85","KAWASAKI"),("87","KTM"),
    ("204","KYMCO"),("159","LANDUM"),
    ("88","L'AQUILA"),("89","LAVRALE"),
    ("139","LERIVO"),("178","LIFAN"),
    ("148","Lon-V"),("175","MAGRÃO TRICICLOS"),
    ("146","Malaguti"),("126","MIZA"),
    ("90","MOTO GUZZI"),("201","MOTOCAR"),
    ("200","MOTORINO"),("160","MRX"),
    ("91","MV AGUSTA"),("92","MVK"),
    ("93","ORCA"),("164","PEGASSI"),
    ("94","PEUGEOT"),("95","PIAGGIO"),
    ("173","REGAL RAPTOR"),("198","RIGUETE"),
    ("192","Royal Enfield"),("96","SANYANG"),
    ("134","SHINERAY"),("97","SIAMOTO"),
    ("98","SUNDOWN"),("99","SUZUKI"),
    ("176","TARGOS"),("187","TIGER"),
    ("119","TRAXX"),("100","TRIUMPH"),
    ("180","VENTO"),("135","WUYANG"),
    ("101","YAMAHA"),
)
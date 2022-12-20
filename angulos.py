
class Azimute:
    pass

class Rumo:
    angulo: float

    def setByGms(self, graus: int=0, minutos: int=0, segundos: int=0) -> None:
        self.angulo = Angulos.gms2gd(graus, minutos, segundos)

    def setByGd(self, graus_decimais) -> None:
        self.angulo = graus_decimais

    def calcularComAzimute(azimute: float):
        match azimute:
            case (0 >= azimute and azimute < 90):
                pass


        

class Angulos:

    """Representação Básica da Classe que realiza calculos com angulos."""

    @staticmethod
    def gms2gd(graus: int=0, minutos: int=0, segundos: int=0, sinal: int=1) -> float:
        """Converte Graus Minutos e Segundos para Graus Decimais."""
        G, M, S = graus, minutos/60, segundos/(60*60)
        return (G + M + S) * (sinal)

    @staticmethod
    def gd2gms(graus_decimais: float=0.0) -> dict:
        """Graus Decimais e Segundos para Converte Graus Minutos."""
        G, g_resto = int(graus_decimais), graus_decimais - int(graus_decimais)
        M, m_resto = int(g_resto * 60), g_resto * 60 - int(g_resto * 60)
        S = m_resto * 60
        return  {"graus":G, "minutos":M, "segundos":S}


if __name__ == "__main__":
    print(3/5) # 0.6
    print((3/5)**2) # 9/25 ou 0.36
    print(Angulos.gms2gd(3, 37, 30))
    print(Angulos.gd2gms(3.625))
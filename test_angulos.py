from angulos import Angulos
import unittest

class TestAngulos(unittest.TestCase):
    
    """Classe de teste para a calsse Angulos."""
    
    def setUp(self):
        """Fixtures."""
        self.angs = Angulos()

    def test_gms2gd_return_float(self):
        """Testa se o valor recebi é do tipo float."""
        esperado = float
        self.assertIsInstance(self.angs.gms2gd(), esperado)

    def test_gms2gd_return_correct_value(self):
        recebido = {"graus":0, "minutos":30, "segundos":0}
        esperado = 0.5
        self.assertAlmostEqual(self.angs.gms2gd(**recebido), esperado)

    def test_gd2gms_return_dict(self):
        esperado = dict
        self.assertIsInstance(self.angs.gd2gms(), dict)

    def test_gd2gms_return_correct_value(self):
        recebido = 3.625
        esperado = {"graus":3, "minutos":37, "segundos":30}
        self.assertEqual(self.angs.gd2gms(recebido), esperado)


if __name__ == "__main__":
    unittest.main()
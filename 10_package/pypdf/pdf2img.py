"""Este módulo provee la funcionalidad de transformar el PDF a imágen"""

class Converter:
    """"Convertidor de PDF a imágen"""
    
    def convert(self, path):
        """
        Convierte PDF a imágen

        Parameters:
        path (str): Ruta del archivo PDF

        Returns:
        str: retorna el contenido del PDF en formato de imágen
        """
        print("pdf2img")
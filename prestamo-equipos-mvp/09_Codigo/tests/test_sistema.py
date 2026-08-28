"""
Pruebas automatizadas del Sistema de Préstamo de Equipos Tecnológicos.

Alcance del Sprint 1: HU01 (registrar equipos), HU02 (consultar equipos) y
HU03 (registrar estudiantes).

Se ejecutan con:
    python -m unittest discover -s tests        (desde la carpeta 09_Codigo)
o simplemente:
    python tests/test_sistema.py

Cada prueba trabaja sobre una carpeta de datos temporal, de modo que NO se
tocan los archivos JSON reales del proyecto.
"""

import os
import sys
import tempfile
import unittest

# Permite importar los módulos del proyecto aunque las pruebas estén en tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import archivos
import equipos
import estudiantes


class PruebaSistema(unittest.TestCase):
    """Verifica el registro y la consulta de equipos y estudiantes."""

    def setUp(self):
        """Antes de cada prueba: redirige el almacenamiento a una carpeta temporal."""
        self._dir_temporal = tempfile.mkdtemp()
        archivos.CARPETA_DATOS = self._dir_temporal

    def tearDown(self):
        """Después de cada prueba: elimina la carpeta temporal."""
        for nombre in os.listdir(self._dir_temporal):
            os.remove(os.path.join(self._dir_temporal, nombre))
        os.rmdir(self._dir_temporal)

    # ---- HU01 / HU02: Equipos ------------------------------------------- #

    def test_registrar_equipo(self):
        equipo = equipos.registrar_equipo("EQ001", "Portátil", "Lenovo", "E14")
        self.assertEqual(equipo["estado"], "disponible")
        self.assertEqual(len(equipos.listar_equipos()), 1)

    def test_no_permite_codigo_duplicado(self):
        equipos.registrar_equipo("EQ001", "Portátil", "Lenovo", "E14")
        with self.assertRaises(ValueError):
            equipos.registrar_equipo("EQ001", "Tablet", "Samsung", "Tab A")

    def test_listar_equipos_vacio(self):
        self.assertEqual(equipos.listar_equipos(), [])

    # ---- HU03: Estudiantes ---------------------------------------------- #

    def test_registrar_estudiante(self):
        estudiantes.registrar_estudiante(
            "100", "Ana Pérez", "ana@campus.edu", "Sistemas")
        self.assertEqual(len(estudiantes.listar_estudiantes()), 1)

    def test_no_permite_documento_duplicado(self):
        estudiantes.registrar_estudiante("100", "Ana", "ana@campus.edu", "Sistemas")
        with self.assertRaises(ValueError):
            estudiantes.registrar_estudiante("100", "Otro", "otro@campus.edu", "Sistemas")


if __name__ == "__main__":
    unittest.main(verbosity=2)

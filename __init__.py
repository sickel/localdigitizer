# -*- coding: utf-8 -*-
"""
/***************************************************************************
 localCoordinateDigitizer
                                 A QGIS plugin
 Digitizes in distances from a local reference point
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-08-02
        copyright            : (C) 2020 by Morten Sickel
        email                : morten@sickel.net
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load localCoordinateDigitizer class from file localCoordinateDigitizer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .localcoordinates import localCoordinateDigitizer
    return localCoordinateDigitizer(iface)

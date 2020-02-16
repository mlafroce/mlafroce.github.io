---
layout: post
title: Tutorial D-Bus
description: ¡Nuevo tutorial disponible!
tags: blog programación tutoriales C C++
---

# Nuevo tutorial de D-Bus

Hace muy poco, en la máquina del trabajo, decidí cambiar de gestor de escritorio. Usaba *Unity*, que por diversas razones no me agradaba, y decidí probar *LXDE*. El cambio fue muy positivo para mi, pero, nada podía ser perfecto, y algo que me llamó la atención es que había perdido los *bindings* de varias aplicaciones. Entre ellas, las teclas multimedia de *Spotify*. Rápidamente empecé a buscar como recuperar esta funcionalidad, y encontré un blog de *ArchLinux* donde, entre varias soluciones, sugieren utilizar de forma directa el sistema **D-Bus**.

**D-Bus** es un sistema de comunicación entre procesos, que permite notificar eventos y realizar llamadas a *procedimientos remotos* (RPC). En particular, *D-Bus*es parte del proyecto *freedesktop.org*, como intento de unificar los protocolos de comunicación entre *KDE* y *GNOME*. El mismo se basa en *sockets unix*, y tiene bindings en muchos lenguajes que facilitan su uso.

El tutorial se encuentra [aquí](https://github.com/mlafroce/tutorial-dbus), y muestra como implementar un "servidor" utilizando QDbus (módulo de dbus para Qt5, en C++) y un cliente usando la biblioteca libdbus en C.

Espero que les sea de utilidad para entender más en detalle el ecosistema unix.

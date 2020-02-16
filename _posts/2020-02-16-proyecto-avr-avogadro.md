---
layout: post
title: Proyecto AVR Avogadro
description: Presentando al proyecto AVR Avogadro
tags: blog programación electrónica Rust C++ AVR
---

Hace mucho que no escribo, poco más de medio año, que fue cuando comencé con el proyecto **AVR Avogadro**. No sé por qué elegí ese nombre, buscaba algo que contenga las letras A-V-R, aunque *Avocado* (palta en inglés) me gustaba más, pero ya estaba tomado.

Este proyecto de un simulador de microcontroladores AVR, cuyo núcleo está hecho en Rust, y su GUI en C++. El mismo fue pensado como una alternativa a los actuales simuladores implementados en C y C++, ya que se requería algo de alta performance pero los productos encontrados no era fáciles de utilizar y no me gustó como estaban implementados.
Rust fue elegido por su performance similar a C y C++, pero sobre todo por su estilo de pattern matching y modularización que no posee los lenguajes mencionados.
La GUI está hecha en C++ con Qt5, por el simple motivo de que conozco bastante la biblioteca y me gusta como está hecha y como funciona.

Pueden ver el avance del proyecto [aquí](https://mlafroce.github.io/avr-avogadro).

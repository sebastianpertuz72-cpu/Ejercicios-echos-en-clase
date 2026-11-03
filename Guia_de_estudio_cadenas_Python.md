# Guía de estudio: cadenas (`str`) en Python

Guía de apoyo para el *Taller de cadenas en Python*. Cubre los **30 métodos de las fichas**, las **funciones y conceptos auxiliares** del taller (`len`, `repr`, `enumerate`, `range`, índices, cortes) y una **tabla resumen** al final.

> Convención de los ejemplos: la línea `# → ...` muestra lo que devuelve o imprime Python.

---

## Índice

1. [Conceptos base](#1-conceptos-base)
2. [Funciones y herramientas auxiliares](#2-funciones-y-herramientas-auxiliares)
3. [Limpieza](#3-limpieza): `strip`, `lstrip`, `rstrip`
4. [Mayúsculas y minúsculas](#4-mayúsculas-y-minúsculas): `lower`, `upper`, `capitalize`, `title`, `swapcase`, `casefold`
5. [Búsqueda](#5-búsqueda): `find`, `rfind`, `index`, `count`
6. [Reemplazo](#6-reemplazo): `replace`
7. [Comprobación de extremos](#7-comprobación-de-extremos): `startswith`, `endswith`
8. [Separación y unión](#8-separación-y-unión): `split`, `rsplit`, `splitlines`, `join`, `partition`, `rpartition`
9. [Presentación](#9-presentación): `center`, `ljust`, `rjust`, `zfill`
10. [Clasificación](#10-clasificación): `isalpha`, `isdigit`, `isalnum`, `isspace`
11. [Recorridos (`for`, `enumerate`, `range`, `while`)](#11-recorridos)
12. [Tabla resumen](#12-tabla-resumen)
13. [Errores típicos y reglas de oro](#13-errores-típicos-y-reglas-de-oro)

---

## 1. Conceptos base

### 1.1 ¿Qué es una cadena?

Una cadena (`str`) es una **secuencia inmutable de puntos de código Unicode**. Se escribe entre comillas simples o dobles; ambas son equivalentes:

```python
a = 'Hola mundo'
b = "Hola mundo"
print(a == b)          # → True
```

Comillas dentro de comillas: usa el otro tipo, o escápalas con `\`.

```python
frase = "Ella dijo: 'hola'"      # comillas simples dentro de dobles
otra  = 'Ella dijo: "hola"'      # al revés
esc   = 'It\'s here'             # con barra invertida
```

Secuencias de escape más usadas:

| Escape | Significado |
|---|---|
| `\n` | salto de línea (baja al siguiente renglón) |
| `\t` | tabulador (espacio grande horizontal) |
| `\\` | una barra invertida literal |
| `\'` y `\"` | comilla literal |

```python
print("Línea 1\nLínea 2")
# → Línea 1
# → Línea 2
print("A\tB")
# → A       B
```

### 1.2 `25` no es `"25"`

```python
25 + 25        # → 50        (int: suma matemática)
"25" + "25"    # → '2525'    (str: concatenación)
25 + "25"      # → TypeError
```

Por eso los datos que **no se usan para calcular** (cédula, teléfono, código postal, "007") se guardan como texto, aunque tengan dígitos.

### 1.3 Cadena vacía vs. cadena con un espacio

```python
vacia  = ""     # len 0
espacio = " "   # len 1
len(vacia)      # → 0
len(espacio)    # → 1
"" == " "       # → False
```

### 1.4 Inmutabilidad (lo más importante del taller)

Una cadena **no se puede modificar** después de creada. Los métodos **no cambian la original**: devuelven **una cadena nueva**.

```python
texto = "sol"
texto[0] = "X"        # → TypeError: 'str' object does not support item assignment

texto = "Campus"
resultado = texto.upper()
print(resultado)      # → CAMPUS
print(texto)          # → Campus   (la original queda igual)
```

Si quieres "cambiar" una cadena, debes **guardar el resultado**:

```python
nombre = "  ana  "
nombre = nombre.strip()   # reasigno el nombre al resultado nuevo
print(nombre)             # → ana
```

> Error clásico: escribir `nombre.strip()` sin asignar. No pasa nada, porque el resultado se pierde.

### 1.5 Índices y cortes (slicing)

Los índices **empiezan en 0**. Los negativos cuentan desde el final.

```
 texto =  P   y   t   h   o   n
 índice:  0   1   2   3   4   5
 negativo:-6  -5  -4  -3  -2  -1
```

```python
t = "Python"
t[0]      # → 'P'
t[5]      # → 'n'
t[-1]     # → 'n'
t[6]      # → IndexError (fuera de rango)
```

Corte `[inicio:fin]`: incluye `inicio`, **excluye `fin`**. Un corte fuera de rango **no** da error:

```python
t[0:2]    # → 'Py'
t[2:]     # → 'thon'
t[:3]     # → 'Pyt'
t[2:100]  # → 'thon'  (no falla)
t[::-1]   # → 'nohtyP' (paso -1: al revés)
```

Diferencia clave: **un índice** fuera de rango lanza `IndexError`; **un corte** fuera de rango se ajusta en silencio.

### 1.6 Funciones vs. métodos

- **Función**: `len(texto)`. La entrada va **dentro de los paréntesis**.
- **Método**: `texto.upper()`. Se llama **sobre el objeto**, con punto. La cadena antes del punto es la **receptora**.

```python
len("hola")        # función integrada → 4
"hola".upper()     # método de str    → 'HOLA'
"hola".len()       # → AttributeError (len no es método de str)
```

### 1.7 Cómo leer una firma

Ejemplo: `str.replace(old, new, count=-1, /)`

| Parte | Significado |
|---|---|
| `old, new` | parámetros **obligatorios** (sin valor por defecto) |
| `count=-1` | parámetro **opcional**; si no lo das, vale `-1` (sin límite) |
| `/` | todo lo que está **antes** es **solo posicional**: no se puede pasar por nombre |
| `[, start[, end]]` | corchetes = opcionales (notación de la documentación) |
| `self` | la cadena receptora; no se escribe al llamar |

```python
"casa".replace("a", "o")            # old="a", new="o"
"casa".replace("a", "o", 1)         # count=1
"casa".replace(old="a", new="o")    # → TypeError por la barra /
```

### 1.8 Lista, tupla, iterable

```python
["a", "b"]   # lista  (corchetes, se puede modificar)
("a", "b")   # tupla  (paréntesis, inmutable)
```

**Iterable** = objeto que se puede recorrer elemento por elemento (cadenas, listas, tuplas, `range`...).

---

## 2. Funciones y herramientas auxiliares

### `len(objeto)`

Devuelve un `int` con la cantidad de elementos. En una cadena cuenta **puntos de código Unicode**, no "símbolos visibles" ni bytes.

```python
len("sol")        # → 3
len("")           # → 0
len("A B")        # → 3   (el espacio cuenta)
len("niño")       # → 4
```

Caso Unicode: dos cadenas que **se ven iguales** pueden tener distinto `len`.

```python
a = "é"            # U+00E9, un solo punto de código
b = "é"      # 'e' + acento combinado (dos puntos de código)
print(a, b)        # → é é   (se ven igual)
len(a), len(b)     # → (1, 2)
a == b             # → False
```

### `repr(objeto)`

Devuelve la representación **para depuración**, con comillas y escapes visibles. Sirve para "ver" espacios y saltos ocultos.

```python
print("A B\n")         # imprime A B y baja de línea (no se ve el \n)
print(repr("A B\n"))   # → 'A B\n'
print(repr(" "))       # → ' '
```

### `str(valor)`

Convierte a texto. Necesaria para concatenar números con cadenas.

```python
"Edad: " + str(25)     # → 'Edad: 25'
"Edad: " + 25          # → TypeError
```

### `int(texto)` e `input()`

`input()` **siempre devuelve `str`**. Si necesitas un número, conviértelo.

```python
n = int(input())       # si escribes 5 → n vale el entero 5
```

### `range(...)`

Genera una secuencia de enteros (el final **se excluye**).

```python
list(range(4))          # → [0, 1, 2, 3]
list(range(2, 5))       # → [2, 3, 4]
list(range(5, 0, -1))   # → [5, 4, 3, 2, 1]   (paso -1)
list(range(0))          # → []
```

### `enumerate(iterable)`

Entrega pares `(índice, elemento)`.

```python
for i, c in enumerate("A B"):
    print(i, repr(c))
# → 0 'A'
# → 1 ' '
# → 2 'B'
```

### Operadores útiles sobre cadenas

```python
"ab" + "cd"       # → 'abcd'   concatenación
"-" * 5           # → '-----'  repetición
"ol" in "hola"    # → True     contiene
"x" not in "hola" # → True
```

---

## 3. Limpieza

### `strip`

**Para qué sirve:** quita caracteres de **ambos extremos** (inicio y final). Por defecto, espacios en blanco.
**Firma:** `str.strip(chars=None, /)`
**Parámetro:** `chars` (opcional) es un **conjunto de caracteres** a quitar, **no una palabra**.
**Devuelve:** `str` nueva.

```python
"  hola  ".strip()           # → 'hola'
"\t  dato \n".strip()        # → 'dato'   (quita espacios, tabs y saltos)
"--mesa--".strip("-")        # → 'mesa'
"abHolaaba".strip("ab")      # → 'Hol'
```

Por qué `'abHolaaba'.strip('ab')` da `'Hol'`: desde la izquierda quita `a` y `b` mientras aparezcan (`ab`), se detiene en `H`. Desde la derecha quita `a`, `b`, `a`, `a` (`aaba`), se detiene en `l`. **No toca el interior.**

```python
"  hola mundo  ".strip()     # → 'hola mundo'   (el espacio del medio se conserva)
```

**Usos:** limpiar lo que escribe el usuario en un formulario, comparar entradas, leer líneas de archivos.
**Trampa:** `chars` es un conjunto: `strip("ab")` quita cualquier mezcla de `a` y `b`, no la palabra "ab".

---

### `lstrip`

**Para qué sirve:** igual que `strip` pero **solo el extremo izquierdo** (inicio).
**Firma:** `str.lstrip(chars=None, /)`

```python
"  hola  ".lstrip()          # → 'hola  '
"0007".lstrip("0")           # → '7'
"abHolaaba".lstrip("ab")     # → 'Holaaba'
```

**Usos:** quitar sangría de una línea copiada, quitar ceros a la izquierda.
**Trampa:** no quita un **prefijo exacto**, quita **cualquier carácter del conjunto**:

```python
"banana".lstrip("ban")       # → ''   (todo son b, a, n)
"banana".removeprefix("ban") # → 'ana' (para un prefijo exacto, Python 3.9+)
```

---

### `rstrip`

**Para qué sirve:** igual que `strip` pero **solo el extremo derecho** (final).
**Firma:** `str.rstrip(chars=None, /)`

```python
"  hola  ".rstrip()          # → '  hola'
"linea\n".rstrip()           # → 'linea'
"dato.txt".rstrip(".txt")    # → 'dato'
```

**Usos:** quitar el salto de línea al final de una línea leída.
**Trampa (muy preguntada):** quitar extensiones con `rstrip` es **incorrecto** porque `chars` es un conjunto:

```python
"test.txt".rstrip(".txt")    # → 'tes'   ¡borra también la 't' final de "test"!
"test.txt".removesuffix(".txt")   # → 'test'  (forma correcta, 3.9+)
```

---

## 4. Mayúsculas y minúsculas

Todos devuelven **cadena nueva**; los números y signos no cambian.

### `lower`

**Sirve para:** pasar todo a minúscula.
**Firma:** `str.lower()` (sin argumentos).

```python
"ÁRBOL 25!".lower()     # → 'árbol 25!'
"MiNombre".lower()      # → 'minombre'
"Straße".lower()        # → 'straße'   (la ß se conserva)
```

**Usos:** comparar correos (`correo.lower() == guardado.lower()`), normalizar entradas.

### `upper`

**Sirve para:** pasar todo a mayúscula.
**Firma:** `str.upper()`

```python
"niño".upper()          # → 'NIÑO'
"hola mundo".upper()    # → 'HOLA MUNDO'
"ß".upper()             # → 'SS'
len("ß"), len("ß".upper())   # → (1, 2)
```

**Dato clave:** el resultado **puede tener distinta longitud** (la alemana `ß` se vuelve `SS`).
**Usos:** carteles, siglas, códigos.

### `capitalize`

**Sirve para:** primer carácter en mayúscula y **el resto en minúscula**.
**Firma:** `str.capitalize()`

```python
"hOLA MUNDO".capitalize()      # → 'Hola mundo'
"python ES genial".capitalize()# → 'Python es genial'
" hola".capitalize()           # → ' hola'
```

El último caso: el primer carácter es un **espacio**, así que no hay nada que poner en mayúscula (y el resto queda en minúscula).
**Usos:** inicio de oraciones.

### `title`

**Sirve para:** primera letra de **cada palabra** en mayúscula, el resto en minúscula.
**Firma:** `str.title()`

```python
"hola mUNDO".title()           # → 'Hola Mundo'
"maría fernanda".title()       # → 'María Fernanda'
"they're here".title()         # → "They'Re Here"
```

Considera como límite de palabra **cualquier carácter que no sea letra** (espacio, guion, apóstrofo...). Por eso el apóstrofo rompe `they're`. Tampoco respeta `McDonald` ni partículas (`de`, `del`).
**Usos:** nombres propios sencillos, títulos.

### `swapcase`

**Sirve para:** invierte mayúsculas ↔ minúsculas.
**Firma:** `str.swapcase()`

```python
"Hola 7".swapcase()            # → 'hOLA 7'
"PyThOn".swapcase()            # → 'pYtHoN'
"straße".swapcase().swapcase() # → 'strasse'
```

**Trampa:** aplicarlo dos veces **no siempre** devuelve el original (`straße` → `STRASSE` → `strasse`).
**Usos:** efectos visuales, juegos.

### `casefold`

**Sirve para:** minúscula **agresiva** pensada para **comparar** sin distinguir mayúsculas.
**Firma:** `str.casefold()`

```python
"Straße".casefold()                         # → 'strasse'
"Hola".casefold() == "HOLA".casefold()      # → True
"Straße".casefold() == "STRASSE".casefold() # → True
"Straße".lower()  == "STRASSE".lower()      # → False
"Árbol".casefold()                          # → 'árbol'
```

**Aclaración:** **no** quita tildes ni normaliza todas las formas Unicode; solo "pliega" las mayúsculas/minúsculas.
**Regla práctica:** para **mostrar** usa `lower`; para **comparar** usa `casefold`.

---

## 5. Búsqueda

### `find`

**Sirve para:** posición de la **primera** aparición de una subcadena.
**Firma:** `str.find(sub[, start[, end]])` — `sub` obligatoria; `start` y `end` opcionales (se busca en `[start, end)`).
**Devuelve:** `int`; **`-1`** si no la encuentra (no lanza error).

```python
"banana".find("an")        # → 1
"banana".find("na", 3)     # → 4   (busca desde el índice 3)
"banana".find("x")         # → -1
"banana".find("a", 2, 4)   # → 3   (busca solo en texto[2:4] = "na")
"correo@x.com".find("@")   # → 6
```

**Trampa clásica:** `0` es una posición **válida** y `-1` es "no encontrado".

```python
texto = "hola"
if texto.find("h"):        # ¡MAL! find devuelve 0 → es falso
    ...
if texto.find("h") != -1:  # BIEN
    ...
if "h" in texto:           # BIEN y más simple si solo quieres saber si está
    ...
```

---

### `rfind`

**Sirve para:** posición de la **última** aparición.
**Firma:** `str.rfind(sub[, start[, end]])`
Los índices **siguen contándose desde la izquierda**; solo cambia que se escoge la última coincidencia.

```python
"banana".rfind("na")        # → 4
"banana".rfind("na", 0, 4)  # → 2   (busca solo en "bana")
"a/b/c.txt".rfind("/")      # → 3
"foto.final.jpg".rfind(".") # → 10
```

**Usos:** hallar el último punto (extensión) o la última barra (nombre de archivo).
```python
f = "foto.final.jpg"
f[f.rfind(".") + 1:]        # → 'jpg'
```

---

### `index`

**Sirve para:** igual que `find`, pero si no hay coincidencia **lanza `ValueError`** en vez de devolver `-1`.
**Firma:** `str.index(sub[, start[, end]])`

```python
"banana".index("na")        # → 2
"12:30".index(":")          # → 2
"banana".index("x")         # → ValueError: substring not found
```

**Cuándo usarlo:** cuando el separador **debe existir** y quieres que el programa falle (o lo capturas) si falta.

```python
try:
    pos = "1230".index(":")
except ValueError:
    print("Formato inválido")
```

---

### `count`

**Sirve para:** contar apariciones **no solapadas** de una subcadena.
**Firma:** `str.count(sub[, start[, end]])`
**Devuelve:** `int`.

```python
"banana".count("a")     # → 3
"aaaa".count("aa")      # → 2   (no 3: no cuenta solapadas)
"hola hola".count("hola") # → 2
"abc".count("")         # → 4   (len + 1)
"banana".count("a", 2)  # → 2   (desde el índice 2)
```

**Subcadena vacía:** `len(texto) + 1` porque la cadena vacía "cabe" antes de cada carácter y al final.
**Usos:** contar vocales (con cada vocal), palabras repetidas, comas de una línea.

---

## 6. Reemplazo

### `replace`

**Sirve para:** sustituir **subcadenas** por otra.
**Firma:** `str.replace(old, new, count=-1, /)` — `old` y `new` obligatorios; `count` limita cuántos reemplazos (de izquierda a derecha).

```python
"casa casa".replace("casa", "aula")       # → 'aula aula'
"casa casa".replace("casa", "aula", 1)    # → 'aula casa'
"casa".replace("a", "X", 0)               # → 'casa'  (count=0: no cambia nada)
"1,5".replace(",", ".")                   # → '1.5'
"ana y ana".replace("ana", "eva")         # → 'eva y eva'
"hola mundo".replace(" ", "")             # → 'holamundo'  (quitar espacios)
```

**Trampa:** reemplaza **subcadenas**, no palabras completas.

```python
"casas".replace("casa", "X")   # → 'Xs'  (cambió dentro de otra palabra)
```

Si no está `old`, devuelve la cadena igual. Recuerda: devuelve **nueva** cadena.

---

## 7. Comprobación de extremos

### `startswith`

**Sirve para:** ¿empieza por un prefijo? **Devuelve `bool`.**
**Firma:** `str.startswith(prefix[, start[, end]])` — `prefix` puede ser `str` **o tupla** de prefijos.

```python
"informe.txt".startswith("in")        # → True
"python".startswith("py")             # → True
"+573001234567".startswith("+57")     # → True
"pre_dato".startswith("dato", 4)      # → True  (compara desde el índice 4)
"hola".startswith(("ho", "he"))       # → True  (basta que coincida uno)
"Hola".startswith("ho")               # → False (distingue mayúsculas)
```

`start` y `end` limitan el tramo: se compara contra `texto[start:end]`, no contra el inicio real.

---

### `endswith`

**Sirve para:** ¿termina en un sufijo? **Devuelve `bool`.**
**Firma:** `str.endswith(suffix[, start[, end]])`

```python
"reporte.pdf".endswith(".pdf")                  # → True
"FOTO.JPG".endswith(".jpg")                     # → False (distingue mayúsculas)
"FOTO.JPG".lower().endswith(".jpg")             # → True
"dato.csv".endswith((".txt", ".csv"))           # → True  (varias terminaciones: TUPLA)
"dato.csv".endswith([".txt", ".csv"])           # → TypeError (una lista no vale)
```

**Usos:** validar extensiones de archivo.

---

## 8. Separación y unión

### `split`

**Sirve para:** partir una cadena en una **lista** de cadenas.
**Firma:** `str.split(sep=None, maxsplit=-1)`
- `sep=None`: separa por **cualquier espacio en blanco**, junta los repetidos y **descarta vacíos** de los extremos.
- `sep="x"`: corta en **cada** `x`; los separadores repetidos generan elementos vacíos `''`.
- `sep=""` → `ValueError: empty separator`.

```python
"uno,dos,tres".split(",")     # → ['uno', 'dos', 'tres']
"  a  b ".split()             # → ['a', 'b']
"  a  b ".split(" ")          # → ['', '', 'a', '', 'b', '']
"a-b-c".split("-", 1)         # → ['a', 'b-c']   (maxsplit=1: un solo corte)
"hola".split(",")             # → ['hola']       (sin coincidencia: lista de 1)
"".split()                    # → []
"".split(",")                 # → ['']
```

**Usos:** palabras de una frase, campos de un CSV.
**Receta típica:** `len(frase.split())` = cantidad de palabras.

---

### `rsplit`

**Sirve para:** como `split` pero los cortes se cuentan **desde la derecha**.
**Firma:** `str.rsplit(sep=None, maxsplit=-1)`

```python
"a-b-c".rsplit("-", 1)        # → ['a-b', 'c']
"a-b-c".split("-", 1)         # → ['a', 'b-c']
"a.b.c".rsplit(".", 1)        # → ['a.b', 'c']
"foto.final.jpg".rsplit(".", 1)  # → ['foto.final', 'jpg']
"a-b-c".rsplit("-")           # → ['a', 'b', 'c']   (sin límite = igual que split)
```

**Diferencia:** solo importa cuando hay `maxsplit`. Sin límite, ambos dan lo mismo.
**Uso:** separar nombre y extensión cuando el nombre tiene puntos.

---

### `splitlines`

**Sirve para:** partir por **saltos de línea** y devolver lista.
**Firma:** `str.splitlines(keepends=False)` — con `keepends=True` conserva los `\n`.

```python
"a\nb\n".splitlines()         # → ['a', 'b']
"a\nb\n".splitlines(True)     # → ['a\n', 'b\n']
"x\ny\nz".splitlines()        # → ['x', 'y', 'z']
"a\nb\n".split("\n")          # → ['a', 'b', '']   ← ¡último vacío!
```

**Diferencia con `split("\n")`:** un salto **final** no genera un elemento vacío en `splitlines`.
**Usos:** procesar texto de varias líneas, leer archivos completos.

---

### `join`

**Sirve para:** unir los elementos de un iterable de cadenas usando la **cadena receptora como separador**.
**Firma:** `str.join(iterable)`

```python
"-".join(["a", "b"])             # → 'a-b'
" ".join(["hola", "mundo"])      # → 'hola mundo'
"".join(["a", "b", "c"])         # → 'abc'
", ".join(["rojo", "azul"])      # → 'rojo, azul'
"-".join("sol")                  # → 's-o-l'   (una cadena también es iterable)
"-".join(["a", 2])               # → TypeError  (2 no es str)
"-".join(["a", str(2)])          # → 'a-2'
```

Ojo con la lectura: **el separador va ANTES del punto**, la lista va dentro del paréntesis.
**Inverso de `split`:**

```python
" ".join("uno dos  tres".split())   # → 'uno dos tres'  (normaliza espacios)
```

---

### `partition`

**Sirve para:** cortar en la **primera** aparición del separador, **conservándolo**.
**Firma:** `str.partition(sep)`
**Devuelve:** **tupla de 3**: `(antes, sep, después)`.

```python
"a=b=c".partition("=")                 # → ('a', '=', 'b=c')
"usuario@correo.com".partition("@")    # → ('usuario', '@', 'correo.com')
"abc".partition("=")                   # → ('abc', '', '')
```

Si `sep` no aparece: `(texto_original, '', '')` (el original queda en **primera** posición).

```python
usuario, arroba, dominio = "ana@mail.com".partition("@")
print(usuario)   # → ana
print(dominio)   # → mail.com
```

---

### `rpartition`

**Sirve para:** igual que `partition` pero en la **última** aparición.
**Firma:** `str.rpartition(sep)`

```python
"a=b=c".rpartition("=")          # → ('a=b', '=', 'c')
"a/b/c.txt".rpartition("/")      # → ('a/b', '/', 'c.txt')
"abc".rpartition("=")            # → ('', '', 'abc')
```

Si `sep` no aparece: `('', '', texto_original)` (el original queda en **tercera** posición).
**Uso:** obtener el nombre de archivo de una ruta: `ruta.rpartition("/")[2]`.

---

## 9. Presentación

Ninguno de estos **corta** el texto: si el ancho es menor o igual a la longitud, devuelven la cadena igual.
`width` es el **ancho final total**, no la cantidad de relleno. `fillchar` debe ser **un solo carácter**.

### `center`

**Firma:** `str.center(width, fillchar=' ', /)` — centra el texto.

```python
"sol".center(7, "-")     # → '--sol--'
"hi".center(6, "*")      # → '**hi**'
"sol".center(2, "-")     # → 'sol'      (ancho menor: no corta)
"sol".center(8, "-")     # → '--sol---' (con reparto impar, el sobrante queda a un lado)
"sol".center(7, "--")    # → TypeError  (fillchar de 2 caracteres)
```

**Uso:** títulos centrados en reportes.

### `ljust`

**Firma:** `str.ljust(width, fillchar=' ', /)` — texto a la **izquierda**, relleno a la **derecha**.

```python
"sol".ljust(5, ".")      # → 'sol..'
"ok".ljust(5, ".")       # → 'ok...'
"sol".ljust(2, ".")      # → 'sol'
"ana".ljust(8) + "|"     # → 'ana     |'
```

**Uso:** columnas de nombres alineadas a la izquierda.

### `rjust`

**Firma:** `str.rjust(width, fillchar=' ', /)` — texto a la **derecha**, relleno a la **izquierda**.

```python
"sol".rjust(5, ".")      # → '..sol'
"42".rjust(6, "0")       # → '000042'
"sol".rjust(3)           # → 'sol'
"7".rjust(4)             # → '   7'
```

**Uso:** columnas de números/precios alineados a la derecha.

Ejemplo de tabla alineada:

```python
for nombre, precio in [("Pan", 2500), ("Leche", 4200)]:
    print(nombre.ljust(10) + str(precio).rjust(8))
# → Pan           2500
# → Leche         4200
```

### `zfill`

**Firma:** `str.zfill(width)` — rellena con **ceros a la izquierda**; si hay signo `+`/`-`, los ceros van **después** del signo.

```python
"7".zfill(3)         # → '007'
"-42".zfill(5)       # → '-0042'
"+5".zfill(4)        # → '+005'
"12345".zfill(3)     # → '12345'   (no recorta)
"ab".zfill(5)        # → '000ab'   (funciona con cualquier texto, no convierte a número)
```

**Usos:** códigos `007`, horas `08:05`.

```python
h, m = 8, 5
str(h).zfill(2) + ":" + str(m).zfill(2)    # → '08:05'
```

---

## 10. Clasificación

Todos devuelven `bool`. **La cadena vacía siempre da `False`.**

### `isalpha`

**Sirve para:** ¿todos los caracteres son **letras** (y hay al menos uno)?
**Firma:** `str.isalpha()`

```python
"Hola".isalpha()     # → True
"niño".isalpha()     # → True    (ñ, á, ü cuentan: usa definición Unicode)
"ab c".isalpha()     # → False   (el espacio no es letra)
"abc1".isalpha()     # → False
"".isalpha()         # → False
```

**Uso:** validar que un nombre solo tenga letras (ojo: rechaza espacios y guiones).

### `isdigit`

**Sirve para:** ¿todos son **dígitos**?
**Firma:** `str.isdigit()`

```python
"2026".isdigit()     # → True
"-12".isdigit()      # → False   (el signo no es dígito)
"3.5".isdigit()      # → False   (el punto tampoco)
"²".isdigit()        # → True    (¡superíndice cuenta como dígito Unicode!)
int("²")             # → ValueError
```

**Trampa:** `True` **no garantiza** que `int()` acepte la cadena. No se limita a 0–9.
**Uso:** comprobar que una cédula o teléfono tenga solo dígitos antes de convertirlo.

### `isalnum`

**Sirve para:** ¿todos son letras **o** números (y hay al menos uno)?
**Firma:** `str.isalnum()`

```python
"user123".isalnum()    # → True
"Niño2".isalnum()      # → True
"dato_2".isalnum()     # → False  (el guion bajo no cuenta)
"a b".isalnum()        # → False  (espacio no)
"".isalnum()           # → False
```

**Uso:** validar nombres de usuario simples.

### `isspace`

**Sirve para:** ¿todos son **espacio en blanco** (espacio, `\t`, `\n`, etc.)?
**Firma:** `str.isspace()`

```python
"  \t".isspace()       # → True
" \t\n".isspace()      # → True
"".isspace()           # → False   (vacía: no tiene ningún carácter)
" a ".isspace()        # → False
```

**Uso:** ignorar líneas vacías o en blanco al leer un archivo.

```python
for linea in ["hola", "   ", "mundo", ""]:
    if linea.isspace() or linea == "":
        continue
    print(linea)
# → hola
# → mundo
```

---

## 11. Recorridos

Recorrer = visitar los elementos uno a uno. En un `str`, cada paso entrega **otra cadena de longitud 1**.

### Con `for` directo

```python
for c in "A B":
    print(repr(c))
# → 'A'
# → ' '
# → 'B'
```

`"sol"` → 3 vueltas. `""` → **0 vueltas** (el cuerpo no se ejecuta).

### Con `enumerate`

```python
for i, c in enumerate("A B"):
    print(i, repr(c))
# → 0 'A'
# → 1 ' '
# → 2 'B'
```

### Con índices y `range(len(...))`

```python
texto = "sol"
for i in range(len(texto)):
    print(i, repr(texto[i]))
# → 0 's'
# → 1 'o'
# → 2 'l'
```

El último índice válido es `len(texto) - 1` porque se cuenta desde 0.

### Con `while`

```python
texto = "sol"
i = 0                        # valor inicial
while i < len(texto):        # condición
    print(i, repr(texto[i]))
    i = i + 1                # actualización (¡sin esto, ciclo infinito!)
```

Con texto vacío: `0 < 0` es `False`, el cuerpo nunca corre y nunca se accede fuera de rango.

### Recorrer al revés

```python
texto = "abc"
inverso = ""
for i in range(len(texto) - 1, -1, -1):
    inverso = inverso + texto[i]
print(inverso)    # → cba
```

### Patrón acumulador (el que más se usa en los ejercicios)

```python
frase = "Más ü"
total = 0
for c in frase:
    if c in "aeiouáéíóúüAEIOUÁÉÍÓÚÜ":
        total = total + 1
print(total)      # → 2
```

---

## 12. Tabla resumen

| Método | Firma | Devuelve | Idea en una línea |
|---|---|---|---|
| `strip` | `strip(chars=None, /)` | `str` | quita **conjunto** de chars en ambos extremos |
| `lstrip` | `lstrip(chars=None, /)` | `str` | igual, solo a la izquierda |
| `rstrip` | `rstrip(chars=None, /)` | `str` | igual, solo a la derecha |
| `lower` | `lower()` | `str` | todo minúscula |
| `upper` | `upper()` | `str` | todo mayúscula (`ß`→`SS`) |
| `capitalize` | `capitalize()` | `str` | 1.er carácter mayúscula, resto minúscula |
| `title` | `title()` | `str` | cada palabra con inicial mayúscula |
| `swapcase` | `swapcase()` | `str` | invierte mayúsc./minúsc. |
| `casefold` | `casefold()` | `str` | minúscula agresiva para comparar |
| `find` | `find(sub[,start[,end]])` | `int` | 1.ª posición o `-1` |
| `rfind` | `rfind(sub[,start[,end]])` | `int` | última posición o `-1` |
| `index` | `index(sub[,start[,end]])` | `int` | como `find`, pero `ValueError` si no está |
| `count` | `count(sub[,start[,end]])` | `int` | apariciones no solapadas |
| `replace` | `replace(old,new,count=-1,/)` | `str` | sustituye subcadenas |
| `startswith` | `startswith(prefix[,start[,end]])` | `bool` | ¿empieza por? (acepta tupla) |
| `endswith` | `endswith(suffix[,start[,end]])` | `bool` | ¿termina en? (acepta tupla) |
| `split` | `split(sep=None, maxsplit=-1)` | `list` | parte desde la izquierda |
| `rsplit` | `rsplit(sep=None, maxsplit=-1)` | `list` | parte desde la derecha |
| `splitlines` | `splitlines(keepends=False)` | `list` | parte por saltos de línea |
| `join` | `join(iterable)` | `str` | une con la receptora como separador |
| `partition` | `partition(sep)` | `tuple` (3) | corta en la 1.ª aparición |
| `rpartition` | `rpartition(sep)` | `tuple` (3) | corta en la última aparición |
| `center` | `center(width, fillchar=' ', /)` | `str` | centra con relleno |
| `ljust` | `ljust(width, fillchar=' ', /)` | `str` | texto a la izq. |
| `rjust` | `rjust(width, fillchar=' ', /)` | `str` | texto a la der. |
| `zfill` | `zfill(width)` | `str` | ceros a la izq. (respeta signo) |
| `isalpha` | `isalpha()` | `bool` | ¿solo letras? |
| `isdigit` | `isdigit()` | `bool` | ¿solo dígitos? |
| `isalnum` | `isalnum()` | `bool` | ¿solo letras/números? |
| `isspace` | `isspace()` | `bool` | ¿solo espacio en blanco? |

### ¿Qué método uso para...?

| Necesito... | Uso |
|---|---|
| Limpiar espacios de lo que escribió el usuario | `strip()` |
| Comparar sin importar mayúsculas | `casefold()` (o `lower()`) |
| Saber si una palabra está dentro de un texto | `"x" in texto` o `find(...) != -1` |
| Contar cuántas veces aparece algo | `count()` |
| Cambiar una palabra por otra | `replace()` |
| Partir una frase en palabras | `split()` |
| Armar una frase desde una lista | `" ".join(lista)` |
| Separar usuario y dominio de un correo | `partition("@")` |
| Obtener la extensión de un archivo | `rpartition(".")[2]` o `rsplit(".", 1)[1]` |
| Poner ceros a la izquierda | `zfill(n)` |
| Validar solo letras / solo dígitos | `isalpha()` / `isdigit()` |

---

## 13. Errores típicos y reglas de oro

1. **Inmutabilidad:** los métodos devuelven **cadena nueva**. Si no guardas el resultado, no cambia nada.
   ```python
   t = " hola "
   t.strip()         # no hace nada útil
   t = t.strip()     # correcto
   ```
2. **`find` devuelve `-1`**, no `False`. Y `0` es posición válida.
3. **`strip/lstrip/rstrip` usan un conjunto de caracteres**, no una palabra ni un prefijo/sufijo exacto.
4. **`join`:** el separador va antes del punto, y todos los elementos deben ser `str`.
5. **`split()` ≠ `split(" ")`:** el primero agrupa espacios repetidos; el segundo genera `''`.
6. **`isdigit()` ≠ "se puede convertir con `int`"** (`"²"`, `"-12"`, `"3.5"`).
7. **Cadena vacía:** `isalpha`, `isdigit`, `isalnum`, `isspace` devuelven `False`; `for` sobre `""` no ejecuta nada; `split()` devuelve `[]`.
8. **Índice vs. corte:** `t[10]` lanza `IndexError`, `t[0:10]` no.
9. **`len` cuenta puntos de código**, no lo que "ves" ni bytes.
10. **`input()` devuelve `str`:** conviértelo con `int()` o `float()` si vas a calcular.
11. **Distingue** `texto.upper()` (método, con punto) de `len(texto)` (función, entre paréntesis).
12. **Tupla vs. lista:** `startswith`/`endswith` aceptan **tupla**, no lista.

---

### Cómo estudiar esto

1. Abre una consola de Python (`python` en la terminal) y **escribe cada ejemplo tú mismo**.
2. **Predice** el resultado antes de ejecutar (igual que en las fichas del taller).
3. Cuando falles, mira la sección *Trampa* de ese método.
4. Usa `help(str.split)` para leer la documentación oficial de cualquier método.

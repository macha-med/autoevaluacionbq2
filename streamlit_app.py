import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Autoevaluación de Bioquímica", layout="centered")

st.title("🧪 Autoevaluación de Bioquímica Médica")
st.write("Genera preguntas dinámicas adaptadas a los contenidos y nivel del tema.")

# Configurar clave de API
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Falta la clave de API. Por favor, configúrala en los secretos de Streamlit (GEMINI_API_KEY).")
    st.stop()

# --- APUNTES Y MATERIAL FIJO DEL TEMA (OPCIÓN B) ---
TEXTO_APUNTES = """
1. FUNCIONES DEL AGUA

El agua desempeña una serie de funciones vitales en el organismo humano: 

1. Excelente disolvente de sustancias iónicas y polares: debido a su polaridad y a su elevada permitividad relativa, el agua hidrata iones (solvatación) y establece interacciones con moléculas polares. Sin embargo, disuelve mal muchas sustancias apolares que necesitan mecanismos de transporte específicos. 
2. Función Bioquímica: Actúa como medio para reacciones metabólicas, participa en reacciones enzimáticas como sustrato y producto y en la regulación ácido-base. 

3. Función de Transporte: Facilita la distribución e incorporación de nutrientes y eliminación de desechos a través de la circulación sanguínea.

4. Función Termorreguladora: Ayuda a mantener la temperatura corporal equilibrada disipando el calor e impidiendo cambios bruscos. 

5. Contribuye a la organización y estabilidad de las macromoléculas: el agua forma capas de hidratación alrededor de grupos polares e interviene, directa o indirectamente, en puentes de hidrógeno, interacciones electrostáticas y efecto hidrofóbico. Estas interacciones influyen en el plegamiento de proteínas, la formación de membranas y la estructura de los ácidos nucleicos.
2. ESTRUCTURA DEL AGUA

image.png

El agua forma un dipolo eléctrico permanente

La molécula de agua es angular y presenta una distribución desigual o asimétrica de la carga electrónica. El oxígeno, más electronegativo, posee una carga parcial negativa, δ−, mientras que cada hidrógeno posee una carga parcial positiva, δ+. Aunque la molécula es eléctricamente neutra, la separación espacial de estas cargas genera un dipolo permanente, por lo tanto es una molécula polar.
La polaridad permite la formación de hasta 4 puentes de hidrógeno entre moléculas de agua y otras sustancias, fundamentales para la cohesión del agua. 

Además, el agua es un electrolito débil  con comportamiento anfótero ya que puede actuar como ácido o base (ceder-captar protones), lo que le permite participar en diversas reacciones biológicas. 

Puentes de Hidrógeno:

Los puentes de hidrógeno son interacciones no covalentes de carácter fundamentalmente electrostático y direccional. Aunque más débiles que los covalentes, son cruciales para la cohesión del agua y sus propiedades únicas. Un enlace por puente de H se efectúa entre un átomo electronegativo y el átomo de hidrógeno unido covalentemente a otro átomo electronegativo. Cada molécula de agua puede establecer puentes de hidrógeno con otras cuatro moléculas de agua en una disposición similar a un tetraedro. 
En estado líquido, cada molécula de agua establece puentes de hidrógeno en un número variable (una media de 3,5), creando una red dinámica que se reorganiza continuamente de forma que una misma molécula de agua crea y rompe puentes de hidrógeno continuamente. Al congelarse, las moléculas de agua forman una estructura cristalina tetraédrica estable (las moléculas se unen estableciendo 4 puentes de hidrógeno). Estos puentes confieren al agua alta cohesión y debido a la distancia entre las moléculas y las interacciones intermoleculares hacen que el agua líquida sea poco compresible en condiciones fisiológicas.
3. PROPIEDADES FÍSICO QUÍMICAS DEL AGUA

image.png

CARACTERÍSTICAS FÍSICO QUÍMICAS RELACIONADAS CON LA TERMOREGULACIÓN
El agua, gracias a sus propiedades únicas, desempeña un papel esencial en la regulación de la temperatura en nuestro planeta y en nuestros cuerpos. 
Densidad y Flotación del Hielo: El agua es más densa a 4°C, lo que permite que el hielo flote y proteja la vida marina en ambientes fríos. Las moléculas del hielo están dispuestas en una formación especialmente laxa tridimensional que tiene muchos huecos merced a los puentes de hidrógeno. En su caso, al calentarse y empezar a deslizarse las moléculas de agua, en vez de expandirse pasan a rellenar esos huecos o espacios intermoleculares, pasando a ocupar menos espacio en estado líquido que en sólido. Siendo, pues, menos denso el hielo que el agua. 
 Alta Temperatura de Ebullición: A una presión de 1 atm, el agua pura funde aproximadamente a 0 °C y hierve aproximadamente a 100 °C, luego se mantiene en estado líquido en un rango amplio de 0°C a 100°C. Esto permite la vida en lugares con climas extremos. 
Calor Específico: Se necesita mucha energía para elevar la temperatura del agua en comparación con otras sustancias (1cal/g/°C). Esto nos permite resistir cambios drásticos de temperatura externa sin que nuestra temperatura corporal varíe mucho. El agua actúa como un eficiente regulador de temperatura a través de la circulación sanguínea. 
Alto calor de Vaporización: para que el agua pase del estado líquido al gaseoso es necesario aportar una cantidad considerable de energía, porque deben debilitarse y romperse numerosas interacciones intermoleculares como los puentes de hidrógeno. Por ello, la evaporación del sudor extrae calor de la superficie corporal y constituye un mecanismo eficaz de termoregulación. 
Conductividad térmica relativamente elevada: el agua facilita la transferencia de calor entre regiones corporales. La circulación sanguínea contribuye además a redistribuir el calor producido por los tejidos.
 

image.png

 

CARACTERÍSTICAS FÍSICO QUÍMICAS RELACIONADAS CON LA CAPACIDAD COMO DISOLVENTE UNIVERSAL

ELEVADA CONSTANTE DIELÉCTRICA: es la medida de la capacidad de un medio para reducir las interacciones electrostáticas entre cargas. El agua presenta una constante dieléctrica elevada debido a su elevada polaridad, por lo que estabiliza eficazmente los iones y favorece la disolución de sustancias iónicas. Implica que el agua es un buen disolvente de compuestos iónicos y sales cristalizadas, se oponen a la atracción electrostática entre iones positivos y negativos debilitando dichas fuerzas de atracción. A 25ºC posee una constante dieléctrica muy alta (78,5),

ELECTROLITO DÉBIL. A una temperatura de 25ºC una cantidad muy pequeña de moléculas de agua aparecen disociadas en iones hidronio e hidroxilo. Puede actuar como ácido o como base: anfótera.  

EXCELENTE DISOLVENTE . En función a su solubilidad en agua los compuestos se clasifican como: 

- Apolares o hidrofóbicos- Los gases como el, O2 y N2 son muy apolares. Por ello en nuestro organismo el O2 requiere un transportador soluble específico (hemoglobina, mioglobina). El CO₂ también carece de dipolo neto por su geometría lineal, pero reacciona con el agua y tiene un comportamiento biológico diferente. En la sangre, el CO₂ se transporta disuelto, unido a proteínas en forma de compuestos carbamino y, principalmente, tras convertirse en bicarbonato mediante una reacción catalizada por la anhidrasa carbónica.

-Polares o hidrofílicos: El agua disuelve sales como el NaCl mediante hidratación y estabilización de los iones Na+ y Cl-, debilitando sus interacciones electrostáticas y contrarrestando su tendencia a asociarse.   

- Anfipáticos: Los compuestos anfipáticos contienen regiones polares y apolares. Las regiones apolares se agrupan para evitar el contacto con el agua y establecen entre sí interacciones hidrofóbicas. Muchas moléculas son anfipáticas: proteínas, pigmentos, fosfolípidos , vitaminas, esteroles, etc

Links to an external site.
4. EL AGUA COMO REACTIVO

REACTIVO.JPG

La mayoría de las reacciones metabólicas se producen en un medio acuoso. El agua permite:

la difusión de metabolitos;
la interacción entre enzimas y sustratos;
la movilidad de iones;
la transferencia de protones;
la organización de complejos macromoleculares.
Además, el agua puede participar en reacciones químicas como reactivo:   

Hidrólisis: El agua actúa como sustrato en reacciones de catabolismo, catalizadas por hidrolasas, donde se rompe un enlace mediante la incorporación de agua. 
image.png
Las hidrólisis son frecuentes en los procesos catabólicos. Ejemplos:

hidrólisis de enlaces peptídicos;
hidrólisis de enlaces glucosídicos;
hidrólisis de enlaces éster;
hidrólisis del ATP.
Condensación: 
En una reacción de condensación, se forma un enlace covalente y se libera una molécula pequeña, frecuentemente agua:
image.png
Las condensaciones son frecuentes en procesos biosintéticos. Ejemplos:

formación de enlaces peptídicos;
formación de determinados enlaces glucosídicos;
formación de enlaces éster.
EL AGUA COMO ELECTROLITO 

Repaso: Ácidos y Bases

Según Brönsted-Lowry, un ácido puede ceder protones y una base los acepta, formando pares conjugados que pueden revertir sus roles (ver ejemplo del HCl abajo) 

Ácido (disociación): AH---> A- + H+ 
Base disociación: B: + H+-->BH+ 
Los ácidos se clasifican en fuertes (ionización completa Ej. HCl) y débiles (ionización parcial, Ej. acido acético, agua). El agua es una sustancia anfótera o anfiprótica, actuando como ácido o base según el medio. 




 

5. EL AGUA COMO ÁCIDO DÉBIL. IONIZACIÓN DEL AGUA



El agua se considera un electrolito débil porque la mayor parte de sus moléculas se encuentran en su forma neutra, H₂O, y solo una pequeñísima fracción se ioniza. La ionización ocurre cuando dos moléculas de agua, que interaccionan entre sí mediante puentes de hidrógeno, debido a ciertas inestabilidades en el entorno molecular, uno de los hidrógenos covalentes puede transferirse de una molécula a la otra (autoionización o autoprotólisis del agua). Como consecuencia, se forman dos especies cargadas: el ión hidronio (H₃O⁺), que resulta de la ganancia de un protón, y el ión hidroxilo (OH⁻), que queda al perderlo. La reacción global puede expresarse de la siguiente manera:



Aunque esta reacción se resume a menudo de forma simplificada como:


es importante recordar que, en realidad, el protón libre se encuentra hidratado formando el ión hidronio.

Cada vez que se produce una ionización, se generan en el mismo número iones hidronio e iones hidroxilo. Esto significa que sus concentraciones son siempre iguales en el agua pura. La concentración de cada uno de ellos es de 1 × 10⁻⁷ M.

El producto de estas concentraciones se denomina constante de ionización del agua (Kw), y tiene un valor de:


Este valor es constante y no tiene unidades. Por tanto, cualquier variación en una de las concentraciones debe compensarse con un cambio inverso en la otra, de manera que el producto se mantenga igual. Así, si disminuye la concentración de iones hidronio, aumenta la de iones hidroxilo, y viceversa.

A partir de estas cifras se construye la escala de pH, que evita el uso de exponentes tan pequeños mediante la aplicación del logaritmo en base 10. De este modo, el agua pura, con una concentración de iones hidronio de 1 × 10⁻⁷ M, tiene un pH de 7. 

EL AGUA Y LA ESCALA DE pH

El pH mide la acidez o alcalinidad de una solución; un pH de 7 es neutro, menor de 7 es ácido (aumentan los H+) y mayor de 7 es básico (disminuyen los H+). La escala es logarítmica (pH es abreviatura de Potencial Hidrógeno), lo que implica cambios exponenciales en la concentración de protones. A 25º, el pH del agua pura y de cualquier solución acuosa  que contenga concentraciones de H+ y OH- iguales es de 7. Este es un estado neutro. El intervalo 0–14 es una representación habitual para disoluciones acuosas relativamente diluidas a 25 °C, pero no constituye un límite absoluto. En determinadas disoluciones concentradas pueden existir valores de pH inferiores a 0 y valores de pH superiores a 14.

pH.JPG
 

6. TAMPONES

Los Tampones en Nuestro Organismo: Manteniendo el Equilibrio Ácido-Base
Importancia de los Tampones:

Los tampones biológicos amortiguan variaciones de pH producidas por la adición moderada de ácido o base para mantener la homeostasis. Son esenciales para evitar daños celulares y funcionales causados por fluctuaciones en el pH. Un tampón no mantiene el pH completamente constante. Solo reduce la magnitud del cambio y posee una capacidad limitada. A consecuencia del metabolismo celular se generan compuestos de carácter ácido, que , cuando son vertidos a la sangre, pueden alterar el pH y alterar la homeostasis de la sangre. Es por ello que el papel de los tampones es esencial. En la imagen puedes observar los productos ácidos procedentes del metabolismo:

image.png

El equilibrio ácido-base del organismo depende de tres niveles de actuación:

sistemas tampón químicos;
regulación respiratoria fisiológica: Ayuda a eliminar CO₂, reduciendo la acidez en el cuerpo.
regulación renal fisiológica: Regulan el pH excretando o conservando iones de hidrógeno y bicarbonato.
Tampones Químicos: Bicarbonato, Fosfato y Proteínas

Un tampón químico es un sistema acuoso cuya función principal es amortiguar las variaciones del pH, evitando cambios bruscos que podrían alterar el equilibrio de los procesos biológicos. Está constituido por un par conjugado, es decir, por un ácido débil y su base conjugada, o bien por una base débil y su ácido conjugado. En el siguiente vídeo se explica qué son los pares de compuestos tamponadores:


En el caso más habitual, un tampón está formado por un ácido débil (HA) y su base conjugada (A⁻). Cuando el ácido débil se encuentra en un medio acuoso, puede ceder un protón (H⁺) al agua:



En esta reacción, el ácido débil (HA) pierde un protón y se transforma en su base conjugada (A⁻), mientras que el agua, al recibir el protón, se convierte en un catión hidronio (H₃O⁺).

También es posible que un tampón esté constituido de forma inversa, a partir de una base débil (B). En ese caso, la base es capaz de captar un protón del agua:



Aquí, la base (B) se convierte en su ácido conjugado (BH⁺) al aceptar el protón, y el agua actúa como donador de protón transformándose en su base conjugada, el ion hidroxilo (OH⁻).

En la práctica, cuando estudiamos sistemas tampón fisiológicos, el caso más frecuente y relevante es el primero: el de un ácido débil y su base conjugada. Esta reacción de disociación está regulada por una constante de equilibrio denominada Ka, la constante de disociación ácida.

La Ka refleja la tendencia del ácido débil a disociarse en un medio acuoso y, por tanto, nos permite predecir el comportamiento del tampón en las condiciones fisiológicas. Esta constante, se expresa en escala logarítmica en base 10 como la pKa, como describiremos más adelante

Los tampones más destacados son el bicarbonato, los fosfatos y las proteínas.

Bicarbonato: es el más representativo del LEC. Amortigua cambios en la sangre y está conectado con los sistemas respiratorio y renal, es un sistema abierto. La interconversión entre CO₂ y ácido carbónico es acelerada por la anhidrasa carbónica y consta de las siguientes reacciones:
 
image.png

Cada una de las reacciones que componen este sistema están dirigidas por una constante, pKa (cte de disociación de un ácido débil), que como veremos en el próximo capítulo, nos indica entre otras cosas a qué pH esa reacción será buen tampón.

2. Fosfato: Regula el pH en el citosol (Intracelular), orina y en los túbulos renales. La imagen siguiente describe las reacciones que componen este tampón. 

image.png

3. Proteínas y Hemoglobina: Actúan tamponando el pH en diferentes compartimentos del cuerpo gracias a que en su estructura, las proteínas contienen aminoácidos con grupos ácidos (COOH), básicos (NH2) y cadenas laterales ionizables que pueden actuar tamponando a determinados intervalos fisiológicos. En el caso de la hemoglobina, la capacidad tamponadora de algunas histidinas está relacionada con su capacidad para transportar y ceder oxígeno a los tejidos.

image.pngimage.png

image.png

Los Tampones en Nuestro Organismo: Ecuación de Henderson- Hasselbalch
En los apartados anteriores del tema hemos hablado del comportamiento del agua como ión, de la relación que esto tiene con la escala de pH y de la importancia de los distintos tipos de tampones para mantener el pH de los fluidos corporales amortiguando las variaciones. la ecuación de H-H es importante a la hora de describir la acción de los tampones o de cualquier ácido débil en general (ya que es una sustancia que va a poder tamponar)

image.png

La ecuación de Henderson-Hasselbalch es una herramienta importante en la química y la bioquímica que se utiliza para calcular el pH de una solución buffer o amortiguadora. Esta ecuación relaciona el pH de una solución con la concentración de un ácido débil (HA) y su base conjugada (A⁻) en dicha solución. La ecuación se expresa de la siguiente manera:
pH = pKa + log([A⁻]/[HA])
Donde:
pH es el valor de acidez o alcalinidad de la solución.
pKa es la constante de acidez (logaritmo negativo de la constante de equilibrio de ionización del ácido débil).
[A⁻] es la concentración de la base conjugada.
[HA] es la concentración del ácido débil.
La ecuación de Henderson-Hasselbalch es útil para predecir cómo cambiará el pH de una solución buffer cuando se agregan ácidos o bases fuertes o cuando se diluye la solución. Algunas aplicaciones comunes incluyen la preparación de soluciones buffer para experimentos de laboratorio y la comprensión de cómo los sistemas biológicos mantienen el pH en rangos específicos para un funcionamiento óptimo. También se utiliza para analizar y comprender cómo se comportan los sistemas biológicos en condiciones ácidas o alcalinas, como la sangre en el cuerpo humano, que se mantiene en un estrecho rango de pH para garantizar su funcionamiento adecuado. Es muy útil también en el diseño de fármacos para poder predecir su comportamiento, o diseñarlos para que se absorban mejor.
El pKa, o constante de acidez, es una medida que se utiliza en química y bioquímica para describir la acidez o basicidad de un ácido débil (HA). Es el logaritmo negativo (base 10) de la constante de equilibrio de ionización ácido-base para el ácido débil. En otras palabras, el pKa nos indica la tendencia de un ácido débil a perder un protón (H⁺) en una solución acuosa. Un pKa más bajo indica que el ácido débil es más fuerte, es decir, tiene una mayor tendencia a liberar protones y, por lo tanto, es más ácido. Por otro lado, un pKa más alto indica que el ácido débil es más débil y tiene una menor tendencia a liberar protones en una solución acuosa, lo que significa que es menos ácido. 
El pKa es importante porque determina en qué rango de pH una solución buffer es más efectiva para resistir cambios en la acidez o alcalinidad cuando se agregan ácidos o bases fuertes, es decir para comportarse como un buen tampón.
Los Tampones en Nuestro Organismo: Titulación de un ácido débil


La titulación de un ácido débil consiste en añadir progresivamente una base fuerte de concentración conocida para determinar la cantidad de ácido presente. Por ejemplo, al titular ácido acético (CH₃COOH) con NaOH, tiene lugar la reacción de neutralización:

CH₃COOH + OH⁻ → CH₃COO⁻ + H₂O

A diferencia de un ácido fuerte, el ácido acético no está completamente disociado en disolución, por lo que durante la titulación coexisten CH₃COOH y CH₃COO⁻, formando un sistema tampón que amortigua los cambios de pH. En el punto de equivalencia, todo el ácido acético inicial ha reaccionado y queda principalmente acetato (CH₃COO⁻), por lo que el pH es > 7 debido a la hidrólisis básica del acetato. El punto de equivalencia se identifica experimentalmente mediante un indicador adecuado o mediante una curva de titulación.

Para obtener la curva de titulación de un ácido débil, como el ácido acético, se mide inicialmente el pH de una disolución de concentración conocida y se añade progresivamente una base fuerte, como NaOH, registrando el pH después de cada adición. Al representar el pH frente al volumen de base añadido, se obtiene una curva característica: inicialmente el pH aumenta lentamente; en la zona previa al punto de equivalencia se forma un tampón ácido acético/acetato, y en el punto de equivalencia se produce un cambio más pronunciado del pH, aunque este es superior a 7. A partir de la curva puede determinarse, entre otros parámetros, el punto de equivalencia y el pKa del ácido.

La gasometría para el diagnótico de las alteraciones del pH
image.png

La gasometría arterial es una prueba que permite valorar el equilibrio ácido-base y el intercambio gaseoso, especialmente útil en pacientes con alteraciones respiratorias o metabólicas. Los principales parámetros son el pH (7,35–7,45), la PaCO₂ (35–45 mmHg), que refleja el componente respiratorio, y el HCO₃⁻ (22–26 mmol/L), que refleja principalmente el componente metabólico; también se determinan la PaO₂ y la saturación de O₂ para valorar la oxigenación. Cuando el pH es < 7,35 hablamos de acidemia y cuando es > 7,45, de alcalemia. Si la alteración primaria se debe a un aumento o disminución de la PaCO₂, se trata de una alteración respiratoria; si se debe principalmente a un cambio del HCO₃⁻, es metabólica: ↑PaCO₂ → acidosis respiratoria; ↓PaCO₂ → alcalosis respiratoria; ↓HCO₃⁻ → acidosis metabólica; ↑HCO₃⁻ → alcalosis metabólica.

1. OSMOLARIDAD. ÓSMOSIS Y PRESIÓN OSMÓTICA
El agua se distribuye entre los diferentes compartimentos del organismo de acuerdo con la concentración de solutos presente en cada uno de ellos. Para comprender cómo se produce esta distribución necesitamos introducir tres conceptos relacionados: osmolaridad, ósmosis y presión osmótica.

OSMOLARIDAD
La osmolaridad expresa la concentración total de partículas osmóticamente activas presentes en una solución. Se expresa habitualmente en mOsm/L de solución. A diferencia de la molaridad, que indica el número de moles de una sustancia por litro de solución (mol/L), la osmolaridad tiene en cuenta el número de partículas presentes en la solución. Las  concentraciones se expresan habitualmente como Molaridad (M), que se define como un número de moles disuelto por litro de solución (mol/L).  Sin embargo,  en soluciones biológicas utilizamos la Osmolaridad que se refiere al número de partículas en un determinado volumen, debido a que algunas moléculas se disocian en iones cuando se disuelven en una solución (por ejemplo: 1 mol de glucosa → aproximadamente 1 mol de partículas mientras que 1 mol de NaCl → aproximadamente 2 moles de partículas porque, en solución, el NaCl se disocia principalmente en Na⁺ y Cl⁻).  El número de partículas en solución no es siempre igual al número de moléculas. La osmolaridad normal del cuerpo humano oscila entre 280 y 300 mOsm/L

OSMOLARIDAD.JPG

IDEA CLAVE: La osmolaridad nos dice cuántas partículas osmóticamente activas hay en una solución.

ÓSMOSIS 
Imaginemos ahora dos compartimentos separados por una membrana con permeabilidad selectiva. La membrana permite el paso de agua, pero restringe el paso de determinados solutos. Si la concentración efectiva de solutos es diferente a ambos lados de la membrana, se producirá un movimiento neto de agua. El agua se desplaza hacia el compartimento que presenta una mayor concentración de solutos que no pueden atravesar la membrana hasta alcanzar el equilibrio osmótico. Este movimiento neto de agua a través de una membrana debido a una diferencia de concentración de solutos se denomina ósmosis.

osmosis-gif.gif

Una forma sencilla de visualizarlo es imaginar una célula: Pocos solutos efectivos fuera → muchos solutos efectivos dentro → el agua entra en la célula. Por el contrario: Muchos solutos efectivos fuera → pocos solutos efectivos dentro → el agua sale de la célula. Es importante recordar que las moléculas de agua continúan desplazándose en ambas direcciones. Lo que nos interesa es el movimiento neto de agua.

PRESIÓN OSMÓTICA
La presión osmótica es la presión que sería necesario aplicar para impedir el movimiento neto de agua a través de una membrana semipermeable debido a una diferencia de concentración de solutos. La presión osmótica depende fundamentalmente del número de partículas presentes en la solución y no del tamaño de esas partículas.

Por ejemplo, una molécula grande y una molécula pequeña pueden ejercer una contribución similar a la presión osmótica si ambas representan una única partícula en solución y se encuentran en la misma concentración molar.

Esto permite entender por qué una macromolécula como el glucógeno tiene un efecto osmótico mucho menor que una cantidad equivalente de glucosa libre. Aunque el glucógeno esté formado por numerosas unidades de glucosa, estas están unidas covalentemente y forman una única macromolécula.

IDEA CLAVE: La presión osmótica depende del número de partículas, no del número de átomos o de unidades que contiene cada molécula.

¿CÓMO ATRAVIESA EL AGUA LAS MEMBRANAS?
El agua puede atravesar las membranas celulares por difusión a través de la bicapa lipídica, pero en muchas células su paso está enormemente facilitado por proteínas especializadas denominadas acuaporinas.

Las acuaporinas son proteínas integrales de membrana que forman canales altamente selectivos para el agua. Muchas de ellas se organizan como tetrámeros, y cada subunidad contiene un poro que permite el paso de agua.


  ACUAPORINA.jpg

Las propiedades estructurales del canal permiten el paso rápido y selectivo de moléculas de agua, dificultando el paso de iones y protones.

Por tanto, las acuaporinas son fundamentales para que las células puedan responder rápidamente a cambios en el equilibrio osmótico.

COMPARACIÓN ENTRE SOLUCIONES: HIPEROSMÓTICA, ISOOSMÓTICA E HIPOOSMÓTICA
Cuando comparamos dos soluciones podemos describirlas en función de su osmolaridad:

Una solución es hiperosmótica respecto a otra cuando contiene una mayor concentración total de partículas osmóticamente activas.
Una solución es hipoosmótica cuando contiene una menor concentración total de partículas.
Dos soluciones son isoosmóticas cuando presentan una osmolaridad equivalente.
Hasta aquí estamos simplemente contando partículas.

Pero si queremos saber qué ocurrirá con una célula cuando la pongamos en contacto con una solución, necesitamos un concepto adicional:

2. TONICIDAD
La tonicidad nos permite predecir qué ocurrirá con el volumen de una célula cuando esta se encuentra en una determinada solución.

Dependiendo de las características del medio, una célula puede:

aumentar de volumen,
disminuir de volumen,
o mantener aproximadamente su volumen.
En función de este efecto, describimos la solución como:

hipotónica,
hipertónica,
isotónica.
Pero aquí aparece una diferencia fundamental:

La osmolaridad tiene en cuenta todas las partículas presentes en la solución, mientras que la tonicidad depende fundamentalmente de los solutos que no pueden atravesar la membrana y que, por tanto, mantienen un gradiente osmótico efectivo.

¿QUÉ SON LOS SOLUTOS PENETRANTES Y NO PENETRANTES?
Para entender la tonicidad tenemos que preguntarnos qué ocurre con cada soluto cuando existe una membrana entre dos compartimentos.

Solutos penetrantes
Son aquellos que pueden atravesar la membrana celular. Si un soluto atraviesa la membrana y alcanza una concentración similar a ambos lados, deja de mantener un gradiente osmótico efectivo.

Solutos no penetrantes
Son aquellos que no pueden atravesar libremente la membrana, o lo hacen de manera suficientemente lenta como para mantener un gradiente osmótico efectivo. Estos solutos son los que tienen una mayor importancia para determinar la tonicidad.

Por tanto:

Para saber hacia dónde se desplazará el agua, no basta con saber cuántos solutos hay. Hay que saber qué solutos pueden atravesar la membrana.

3. ¿QUÉ LE OCURRE A UNA CÉLULA EN UNA SOLUCIÓN HIPOTÓNICA, ISOTÓNICA O HIPERTÓNICA?
Vamos a utilizar como ejemplo un eritrocito, ya que es una célula especialmente sencilla para visualizar estos cambios.

MEDIO HIPOTÓNICO
Imaginemos que colocamos un eritrocito en agua prácticamente pura. Dentro de la célula existe una elevada concentración de solutos que no pueden atravesar libremente la membrana, mientras que fuera hay muy pocos solutos. El medio externo es hipotónico respecto al interior celular. Por tanto: medio hipotónico → entra agua → aumenta el volumen celular

Si la entrada de agua es suficientemente importante, el eritrocito puede llegar a romperse. Este fenómeno se denomina hemólisis.

MEDIO HIPERTÓNICO
Ahora imaginemos que colocamos el eritrocito en una solución con una elevada concentración de solutos efectivos. En este caso, la concentración de solutos no penetrantes es mayor fuera de la célula. Por tanto: medio hipertónico → sale agua → disminuye el volumen celular

El eritrocito se encoge y adopta una morfología característica denominada crenación.

MEDIO ISOTÓNICO
Finalmente, imaginemos que colocamos el eritrocito en una solución cuya concentración efectiva de solutos es equivalente a la del interior celular.No existe un movimiento neto de agua hacia dentro o hacia fuera. El volumen celular permanece aproximadamente constante.

medio isotónico → no hay cambio neto de volumen

Esto no significa que no exista movimiento de agua: las moléculas de agua continúan atravesando la membrana en ambos sentidos. Lo que ocurre es que el movimiento está equilibrado y, por tanto, no existe un cambio neto de volumen.

TONICITY.gif

4. OSMOLARIDAD Y TONICIDAD NO SON LO MISMO
Esta es una de las diferencias conceptuales más importantes de este tema. Podemos resumirlo de la siguiente manera:

OSMOLARIDAD = número total de partículas.

TONICIDAD = efecto de los solutos efectivos sobre el volumen celular.

Por tanto, una solución puede ser isoosmótica y no ser isotónica. ¿Por qué? Porque una solución puede contener muchas partículas que sean capaces de atravesar la membrana. Imaginemos, por ejemplo, una solución que contiene urea. La urea contribuye a la osmolaridad de la solución. Sin embargo, puede atravesar determinadas membranas celulares. Si la urea entra en la célula, deja de mantener un gradiente osmótico efectivo entre el interior y el exterior. El agua puede entonces seguir a la urea y modificar el volumen celular. Por tanto isoosmótico ≠ necesariamente isotónico

Ejemplo: Imagina dos soluciones que tienen exactamente la misma osmolaridad. Podríamos pensar: “Si tienen la misma osmolaridad, producirán el mismo efecto sobre una célula”. Pero esto no tiene por qué ser cierto. Supongamos que: Solución A contiene principalmente un soluto que no atraviesa la membrana. Solución B contiene principalmente un soluto que puede atravesar la membrana. Aunque ambas soluciones tengan inicialmente la misma osmolaridad, su efecto sobre el volumen celular puede ser diferente. Por eso, ante cualquier problema de tonicidad, debemos hacernos siempre esta pregunta: ¿Qué solutos pueden atravesar la membrana?

5. TONICIDAD: UNA FORMA DE RAZONAR
Cuando nos encontremos ante un problema de tonicidad podemos seguir siempre los mismos pasos.

PASO 1. Identifica los compartimentos
¿Qué hay a cada lado de la membrana?

Por ejemplo:

interior celular ↔ líquido extracelular

PASO 2. Identifica los solutos
¿Qué sustancias hay dentro y fuera?

PASO 3. Pregunta qué solutos pueden atravesar la membrana
Los solutos penetrantes pueden redistribuirse entre ambos compartimentos.

Los solutos no penetrantes son los que mantienen un gradiente osmótico efectivo.

PASO 4. Compara la concentración de solutos efectivos
Pregunta:

¿Dónde hay más solutos no penetrantes?

PASO 5. Predice el movimiento de agua
El agua se desplazará hacia el compartimento que presenta una mayor concentración de solutos efectivos.

PASO 6. Predice el cambio de volumen
Si entra agua → la célula se hincha.
Si sale agua → la célula se encoge.
Si no existe movimiento neto → el volumen se mantiene.
6. ¿POR QUÉ ES IMPORTANTE LA TONICIDAD EN MEDICINA?
Las células necesitan mantener un volumen relativamente estable para conservar su estructura y función. El organismo dispone de mecanismos muy precisos para regular la composición de los líquidos corporales. Entre ellos se encuentran el transporte activo de iones, los canales y transportadores de membrana y la regulación del agua corporal. Un papel especialmente importante corresponde a la Na⁺/K⁺-ATPasa, que mantiene los gradientes de Na⁺ y K⁺ entre el interior y el exterior celular. Estos gradientes contribuyen al equilibrio osmótico y a la regulación del volumen celular.

La relación entre tonicidad y volumen celular adquiere especial importancia en el sistema nervioso. Si el líquido extracelular se vuelve excesivamente hipotónico, el agua puede entrar en las células. En el cerebro, el aumento del volumen celular puede contribuir al edema cerebral, que puede tener consecuencias neurológicas importantes. Por el contrario, si el líquido extracelular se vuelve excesivamente hipertónico, el agua sale de las células y estas disminuyen de volumen.

El sodio es el principal catión del líquido extracelular y tiene un papel fundamental en la determinación de la tonicidad del líquido extracelular. Por ello, las alteraciones importantes de la concentración de sodio pueden producir cambios en el movimiento de agua entre los compartimentos corporales. Por ejemplo, en determinadas situaciones de hiponatremia, la disminución de la concentración efectiva de solutos del líquido extracelular puede favorecer la entrada de agua en las células. En el sistema nervioso, esto puede producir aumento del volumen cerebral y manifestaciones neurológicas. En determinadas situaciones de hipernatremia, el líquido extracelular puede presentar una tonicidad elevada, favoreciendo la salida de agua de las células. La repercusión clínica dependerá, entre otros factores, de la magnitud de la alteración, de la rapidez con la que se produzca y de la situación clínica del paciente.

Por tanto, conocer la tonicidad permite conectar un concepto biofísico con una situación clínica real.

7. TONICIDAD Y SOLUCIONES INTRAVENOSAS
La tonicidad también es fundamental para comprender por qué diferentes soluciones administradas por vía intravenosa pueden producir efectos diferentes sobre las células y sobre la distribución del agua corporal.

Cuando administramos una solución intravenosa no debemos preguntarnos únicamente:

¿Cuántas partículas contiene?

También debemos preguntarnos:

¿Qué partículas contiene?

¿Pueden atravesar las membranas celulares?

¿Qué efecto tendrán sobre el movimiento de agua?

Esto permite comprender por qué una solución con una determinada osmolaridad puede tener un comportamiento diferente al de otra solución con una osmolaridad similar.

La composición de los líquidos administrados a los pacientes debe, por tanto, interpretarse teniendo en cuenta tanto la cantidad de partículas como su comportamiento frente a las membranas biológicas.
"""

# --- SECCIÓN DE CONFIGURACIÓN DE CRITERIOS EN LA SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Opciones de Evaluación")
    
    tipo_pregunta = st.selectbox(
        "Formato de Pregunta:",
        [
            "Aleatorio",
            "Test de opción múltiple (4 opciones)",
            "Verdadero / Falso (con justificación)",
            "Rellenar espacios en blanco",
            "Emparejar / Conectar conceptos",
            "Pregunta abierta de respuesta corta"
        ]
    )
    
    nivel_bloom = st.selectbox(
        "Nivel Cognitivo (Taxonomía de Bloom):",
        [
            "Aleatorio (Niveles 1-4)",
            "Nivel 1: Recordar (Datos, definiciones, estructuras)",
            "Nivel 2: Comprender (Explicación de mecanismos y rutas)",
            "Nivel 3: Aplicar (Cálculos y casos prácticos)",
            "Nivel 4: Analizar (Interpretación de datos y contextos)"
        ]
    )

    contexto = st.multiselect(
        "Contextos prioritarios:",
        ["Nutricional", "Fisiológico", "Farmacológico", "Biomédico", "Clínico"],
        default=["Nutricional", "Clínico", "Biomédico"]
    )

# --- PROMPT DEL SISTEMA Y GENERACIÓN ---
SYSTEM_PROMPT = f"""
Eres un docente e investigador experto en Bioquímica y Biología Celular para estudiantes de 1º de Medicina.
Tu tarea es generar preguntas de autoevaluación adaptadas estrictamente al material de referencia proporcionado.

REGLAS OBLIGATORIAS:
1. FUENTE ÚNICA DEL CONTENIDO:
   - Basarás TODAS las preguntas e ítems EXCLUSIVAMENTE en el "Material de Estudio" proporcionado a continuación.
   - No debes incluir conceptos o datos fuera del texto de referencia a menos que sean deducciones lógicas directas.

2. TIPOS DE PREGUNTA:
   - Opción múltiple: 4 opciones (A, B, C, D) con solo una correcta.
   - Verdadero/Falso: Declaración detallada indicando si es V o F y la explicación del porqué.
   - Rellenar espacios en blanco: Frase con conceptos clave indicados con [____].
   - Emparejar/Conectar: Dos columnas de conceptos para relacionar.
   - Respuesta corta: Pregunta abierta orientada a conceptos o razonamiento sintético.

3. NIVELES DE BLOOM (Niveles 1 a 4):
   - Nivel 1 (Recordar): Conocer términos, estructuras, enzimas clave.
   - Nivel 2 (Comprender): Explicar la lógica de una ruta o mecanismo.
   - Nivel 3 (Aplicar): Aplicar el concepto a una situación fisiológica, nutricional o clínica concreta.
   - Nivel 4 (Analizar): Desglosar causas-efectos, alteraciones metabólicas o contexto biomédico/farmacológico.

4. CONTEXTO INTEGRADO:
   - Siempre que sea posible, enmarca la pregunta en contextos: {', '.join(contexto)}.

5. ESTRUCTURA DE LA RESPUESTA:
   - Muestra primero la pregunta/ejercicio de forma clara.
   - Coloca la solución al final dentro de un bloque desplegable (usando HTML/Markdown o un formato bien delimitado), ofreciendo una explicación pedagógica completa de la respuesta correcta y del posible error.

MATERIAL DE ESTUDIO DEL TEMA:
---
{TEXTO_APUNTES}
---
"""

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = None

if st.button("🎲 Generar nueva pregunta", type="primary", use_container_width=True):
    prompt_usuario = f"""
    Genera una pregunta con los siguientes parámetros:
    - Formato solicitado: {tipo_pregunta}
    - Nivel de Bloom solicitado: {nivel_bloom}
    """

    with st.spinner("Diseñando pregunta de autoevaluación..."):
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=f"{SYSTEM_PROMPT}\n\n{prompt_usuario}",
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        st.session_state.pregunta_actual = response.text
                    break
                except Exception:
                    if intento == 0:
                        import time
                        time.sleep(5)

            if pregunta_generada:
                break

        if pregunta_generada:
            st.session_state.pregunta_actual = pregunta_generada
        else:
            st.error(
                "No se ha podido generar la pregunta en este momento. "
                "Vuelve a intentarlo dentro de unos minutos."
            )

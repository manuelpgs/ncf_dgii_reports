# NCF DGII Reports

Este módulo para ODOO 10 (por lo pronto) implementa los reportes de los números de comprobantes fiscales (NCF) para el cumplimento de la norma 06-18 de la Dirección de Impuestos Internos (DGII) en la República Dominicana.

Este repositorio tiene como objetivo que este módulo sea integrado en https://github.com/odoo-dominicana/l10n-dominicana y que sea mantenido por la comunidad de ODOO Dominicana.  Mientras tanto todo aquel que desee colaborar, puede hacer un Pull Request aquí.

## CONFIGURAR IMPUESTOS
Se debe configurar correctamente los impuestos, para ello ir al listado de impuestos y en la opción de Tipo de Impuesto de Compra (Cuando el Ámbito del Impuesto es Compra) seleccionar la opción adecuada para cada caso.

## CONFIGURAR CORRECTAMENTE LOS TIPOS DE PRODUCTOS
En cada producto, se debe configurar correctamente el "Tipo de Producto" para poder filtrar el "Monto Facturado en Servicios" y el "Monto Facturado en Bienes".  Actualmente si un producto es del tipo "Servicio" pues se suma al Monto Facturado en Servicios y si es otra cosa como puede ser Consumible o Almacenable, entonces lo sumamos al Monto Facturado en Bienes.  OJO que si venden productos digitales (como libros, fotos, etc..) en teoría serían servicios al no ser algo mateiral pero esto tampoco lo estamos filtrado en la actualidad y en dado caso de ponerlo caerían como Bienes.


### ESTADO ACTUAL:  En desarrollo, no funcional para declaraciones aún.  Faltan agregar nuevas columnas en los reportes y hacer las pruebas de lugar.

## ISSUES AND PENDING STUFF

- Ver todos los #TODO en el código.
- Al crear una Nota de Crédito para una factura de proveedor con estado pagada y escogiendo la primera opción y única opción para estos casos que da la localización "Crear una Nota de Crédito en Borrador"; El sistema deja la nota de crédito en estado "abierta" y si le damos a la opción de pagar, entonces nos pide diario de pago.   Aquí queda pendiente de aclarar si es que en estos casos la Nota de Crédito se deja en estado abierta y no se registra ningún pago (por su naturaleza que no necesita pago) o es algo a reparar en la localización.
- OJO al registrar un pago de una factura de un proveedor.  En agosto registre un pago a una factura de proveedor de fecha de junio y quería poner que el pago fue en junio pero me equivoque y deje la fecha contable en agosto.  Luego cancele el asiento contable y lo edite para ponerle la fecha correcta de junio (y así figura en el asiento contable) pero en el modelo AccountPayment sigue teniendo la fecha de agosto (payment_date) y por eso en el reporte del 606 de junio esa factura sale sin fecha de pago pues el sistema sigue viendo que el pago fue en agosto.  Este punto hay que validar si es algo a corregir en la localización o es un tema de ODOO o validar la fecha de pago por otra vía en estos reportes.
- Hay que validar como se comportan las Notas de Créditos cuando recibes una NC en un mes posterior a la factura que recibe la NC.  Aquí se debe validar con los contables que sucede en estos casos; por ahora el sistema en ese mes posterior muestra la NC y a la factura que afecta.  La fecha de pago le pone el mismo día de la NC y la Forma de Pago le pone "NOTA DE CREDITO".


### Créditos:  Basado en el trabajo de Eneldo Serrata para Marcos Organizador de Negocios SRL. (https://marcos.do/) 

### Autor: Manuel Gonzalez para SOFTNET TEAM SRL (https://www.softnet.do)

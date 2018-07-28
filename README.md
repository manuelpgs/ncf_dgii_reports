# NCF DGII Reports

Este módulo para ODOO 10 (por lo pronto) implementa los reportes de los números de comprobantes fiscales (NCF) para el cumplimento de la norma 06-18 de la Dirección de Impuestos Internos (DGII) en la República Dominicana.

Este repositorio tiene como objetivo que este módulo sea integrado en https://github.com/odoo-dominicana/l10n-dominicana y que sea mantenido por la comunidad de ODOO Dominicana.  Mientras tanto todo aquel que desee colaborar, puede hacer un Pull Request aquí.

# CONFIGURAR IMPUESTOS
Se debe configurar correctamente los impuestos, para ello ir al listado de impuestos y colocarle a cada uno la cuenta que afecta.
Las cuentas:

* 11080101 = ITBIS Pagado en Compras Locales (usada para filtrar ITBIS Bienes)
* 11080102 = ITBIS Pagado en Servicios Locales (usada para filtrar ITBIS Servicios)

En sus facturas de proveedor, a cada línea de la factura se le debe asignar correctamente el ITBIS que lleva y ese ITBIS debe tener una cuenta a la cual alimenta.

# ESTADO ACTUAL:  En desarrollo, no funcional para declaraciones aún.  Faltan agregar nuevas columnas en los reportes y hacer las pruebas de lugar.

### Créditos:  Basado en el trabajo de Eneldo Serrata para Marcos Organizador de Negocios SRL. (https://marcos.do/) 

### Autor: Manuel Gonzalez para SOFTNET TEAM SRL (https://www.softnet.do)

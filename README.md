
# API Creación de facturas

Sistema para la creación de facturas y calculo de IVA según los productos de la factura.

- En el proyecto se usaron patrones de diseño: **(Factory, Strategy)** los cuales nos permiten la creación de los tipos de facturas y su comportamiento propio para el calculo del IVA para los productos de la factura.


## ¿Como usar?

1. `Clone repository`
2. `python3 -m venv .env`
3. `source .env/bin/activate`
4. `pip install requirements.txt`
5. `python main.py`


### Documentación API:
http://127.0.0.1:8083/docs


### Ejecutar tests
`cd src/`

`python -m unittest`


## Endpoints

```
POST -> /invoices/
```
##### Body de entrada:
```
{
    "type": "A", 
    "details": [
        {"product": "Product X", "quantity": 2, "unit_price": 250.0}, 
        {"product": "Service Y", "quantity": 1, "unit_price": 500.0}
    ]
}
```
##### Respuesta con los calculos
```
{
    "type": "A",
    "subtotal": 1000,
    "applied_tax": {
        "percentage": 21,
        "amount": 210
    },
    "total": 1210,
    "details": [
        {
            "product": "Product X",
            "quantity": 2,
            "unit_price": 250
        },
        {
            "product": "Service Y",
            "quantity": 1,
            "unit_price": 500
        }
    ]
}
```
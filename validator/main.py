from pycsvschema.checker import Validator

def main():
    schema = {
        'exactFields': True,
        'fields': [
            {
                'name': 'Columna 1',
                'type': 'number',
                'minimum': 100,
                'maximum': 999999999 
            },
            {
                'name': 'Columna 2',
                'type': 'string',
                'format' : 'email'
            },
            {
                'name': 'Columna 3',
                'type': 'string',
                'enum' : ['CC', 'TI']
            },
            {
                'name': 'Columna 4',
                'type': 'number',
                'minimum': 500000,
                'maximum': 1500000
            },
            {
                'name': 'Columna 5',
                'type': 'string'
            }
        ]
    }
    v = Validator(csvfile='./data/invalido.txt', schema=schema, errors='coerce')
    try: 
        v.validate()
    except IndexError:
        print("Tienes mas columnas de las esperadas (esperadas: 5)")

if __name__ == "__main__":
    main()

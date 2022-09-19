from flask import Flask, request, jsonify

recetario = {
    "recetas":[
        {
            "nombre":"postre con platano macho horneado",
            "ingredientes":[
                "4 plátanos macho cortados por la mitad",
                "3 cdas. de azúcar mascabada",
                "½ taza de nuez picada",
                "2 cdas. de mantequilla",
                "1 cda. de extracto de vainilla"
            ],
            "instrucciones":[
                "1 - Funde el azúcar en una sartén, agrega la mantequilla y el extracto de vainilla.",
                "2 - Coloca los plátanos en una charola con papel encerado, vierte el caramelo sobre ellos y distribuye encima la nuez.",
                "3 - Hornea a 200 grados C durante 8 minutos. Sírvelos calientes."
            ]
        },
        {
            "nombre":"PASTA ALFREDO CON CAMARONES",
            "ingredientes":[
                "250 g de pasta tipo fettuccini",
                "1 taza de crema entera",
                "1 taza de mantequilla",
                "20 g de queso parmesano rallado",
                "3 dientes de ajo machacados",
                "Sal y pimienta",
                "1/2 cebolla picada",
                "100 g de camarones limpios y pelados"
            ],
            "instrucciones":[
                "1 - En una olla calienta un poco de agua con sal, cuando comience a hervir añade el fettuccini y deja cocinar hasta que la paste este al dente. Reserva.",
                "2 - Aparte en una cacerola a fuego medio vierte a crema 1/2 taza de mantequilla, cuando la mantequilla se derrita, agreda el queso parmesano, 1 diente de ajo, sal pimienta y mezcla hasta que el quesos se derrita y tenga una consistencia un poco espesa. Retira del fuego.",
                "3 - Calienta el resto de a mantequilla en una sartén, agrega la cebolla y sofríe, moviendo constantemente por 2 minutos, añade el resto del ajo y los camarones. Cocina a fuego medio hasta que los camarones tengan un color rosado.",
                "4 - Mezcla la pasta con la salsa Alfredo, sirve y añade los camarones."
            ]
        },
        {
            "nombre":"TINGA DE POLLO",
            "ingredientes":[
                "1 pechuga de pollo cocida y desmenuzada",
                "2 cebollas fileteadas",
                "2 jitomates picados",
                "2 chiles chipotles adobados",
                "Sal al gusto",
                "Aceite vegetal",
            ],
            "instrucciones":[
                "1 - En una cacerola con aceite caliente acitrona la cebolla.",
                "2 - Agrega el pollo y el jitomate y el chile, sazona con sal y cocina a fuego medio hasta que se seque.",
            ]
        }


    ]
}

app = Flask(__name__)
@app.route('/', methods=['POST'])

def webhook():
    print(request.json)
    peticion = request.json
    if peticion['queryResult']['intent']['displayName'] == 'Receta':
        return jsonify({
            'fulfillmentText':recetario['recetas'][0]['nombre'],
            'fulfillmentMessages':[
                {
                    'text':{
                        'text':[recetario['recetas'][0]['nombre']]
                    }
                },
                {
                    'text': {
                        'text': ['Ingredientes: ']
                    }
                },
                {
                    'text': {
                        'text':recetario["recetas"][0]['ingredientes']
                    }
                },
                {
                    'text': {
                        'text': ['Pasos a seguir: ']
                    }
                },
                {
                    'text': {
                        'text': recetario["recetas"][0]['instrucciones']
                    }
                }
            ]})

    return 'HOLA'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=4000)

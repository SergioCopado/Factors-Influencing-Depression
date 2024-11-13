import numpy as np
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, CSV
import matplotlib.pyplot as plt
from io import StringIO
import seaborn as sn


def query(v1, v2):
    if v1 == "ValorDemocracia":
        return '''PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?x ?y WHERE{}
                ?c a dbo:Pais .
                ?c dbo:posee ?m1 .
                ?m1 a dbo:{} .
                ?m1 dbo:valor ?x .
                ?m1 dbo:ano "2021"^^xsd:int .
                ?c dbo:posee ?m2 .
                ?m2 a dbo:{} .
                ?m2 dbo:valor ?y .
            {}'''.format('{', v1, v2, '}')
    elif v2 == "ValorDemocracia":
        return '''PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?x ?y WHERE{}
                ?c a dbo:Pais .
                ?c dbo:posee ?m1 .
                ?m1 a dbo:{} .
                ?m1 dbo:valor ?y .
                ?m1 dbo:ano "2021"^^xsd:int .
                ?c dbo:posee ?m2 .
                ?m2 a dbo:{} .
                ?m2 dbo:valor ?x .
            {}'''.format('{', v2, v1, '}')
    return '''PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
    SELECT ?x ?y WHERE{}
        ?c a dbo:Pais .
        ?c dbo:posee ?m1 .
        ?m1 a dbo:{} .
        ?m1 dbo:valor ?x .
        ?c dbo:posee ?m2 .
        ?m2 a dbo:{} .
        ?m2 dbo:valor ?y .
    {}'''.format('{', v1, v2, '}')


print("""
1 - visualizar datos generales
2 - obtener datos por país
3 - visualizar relación entre dos variables
4 - ver correlación entre todas las variables
5 - ver lista de países
99 - salir""")
choice = input()

while choice != "99":
    if choice == "1":
        print("""
1 - mostrar número de países por tipo de régimen
2 - mostrar número de países por índice democrático
3 - mostrar número de países por zona geográfica
4 - mostrar número de países por prevalencia de depresión
5 - mostrar número de países por tamaño de población
6 - mostrar número de países por número de casos de depresión
7 - mostrar número de países por PIB per cápita
8 - mostrar número de países por densidad de población
9 - mostrar número de países por coeficiente de gini
10 - mostrar número de países por índice de desarrollo humano
99 - volver""")
        choice = input()
        while choice != "99":
            if choice == "1":
                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                SELECT ?regimen WHERE{
                      ?c a dbo:Pais .
                      ?c dbo:posee ?n .
                      ?n a dbo:TipoRegimen .
                      ?n dbo:tipo ?regimen .
                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = list(set(df.regimen))
                y = [list(df.regimen).count(i) for i in x]
                ax.bar(x, y)
                plt.xlabel("Tipo de régimen")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "2":
                valores = {"0-1": 0, "1-2": 0, "2-3": 0, "3-4": 0, "4-5": 0, "5-6": 0, "6-7": 0, "7-8": 0, "8-9": 0,
                           "9-10": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                SELECT ?valor WHERE{
                                      ?c a dbo:Pais .
                                      ?c dbo:posee ?n .
                                      ?n a dbo:ValorDemocracia .
                                      ?n dbo:valor ?valor .
                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 1:
                        valores[list(valores.keys())[0]] += 1
                    elif 1 <= float(i) < 2:
                        valores[list(valores.keys())[1]] += 1
                    elif 2 <= float(i) < 3:
                        valores[list(valores.keys())[2]] += 1
                    elif 3 <= float(i) < 4:
                        valores[list(valores.keys())[3]] += 1
                    elif 4 <= float(i) < 5:
                        valores[list(valores.keys())[4]] += 1
                    elif 5 <= float(i) < 6:
                        valores[list(valores.keys())[5]] += 1
                    elif 6 <= float(i) < 7:
                        valores[list(valores.keys())[6]] += 1
                    elif 7 <= float(i) < 8:
                        valores[list(valores.keys())[7]] += 1
                    elif 8 <= float(i) < 9:
                        valores[list(valores.keys())[8]] += 1
                    elif 9 <= float(i) <= 10:
                        valores[list(valores.keys())[9]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xlabel("Índice de democracia")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "3":
                zonas = []

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                    PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                    SELECT ?zona WHERE{
                                        ?c a dbo:Pais .
                                        ?c dbo:estaEn ?z .
                                        ?z dbo:nombre ?zona .
                                    }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.zona):
                    zonas.append(str(i))

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = list(set(zonas))
                y = [zonas.count(i) for i in x]
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("Zona geográfica")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "4":
                valores = {"2.5-3": 0, "3-3.5": 0, "3.5-4": 0, "4-4.5": 0, "4.5-5": 0, "5-5.5": 0, "5.5-6": 0,
                           "6-6.5": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                                SELECT ?valor WHERE{
                                                      ?c a dbo:Pais .
                                                      ?c dbo:posee ?n .
                                                      ?n a dbo:IndiceDepresion .
                                                      ?n dbo:valor ?valor .
                                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 3:
                        valores[list(valores.keys())[0]] += 1
                    elif 3 <= float(i) < 3.5:
                        valores[list(valores.keys())[1]] += 1
                    elif 3.5 <= float(i) < 4:
                        valores[list(valores.keys())[2]] += 1
                    elif 4 <= float(i) < 4.5:
                        valores[list(valores.keys())[3]] += 1
                    elif 4.5 <= float(i) < 5:
                        valores[list(valores.keys())[4]] += 1
                    elif 5 <= float(i) < 5.5:
                        valores[list(valores.keys())[5]] += 1
                    elif 5.5 <= float(i) < 6:
                        valores[list(valores.keys())[6]] += 1
                    elif 6 <= float(i) < 6.5:
                        valores[list(valores.keys())[7]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xlabel("Prevalencia de depresión (%)")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "5":
                valores = {"<1.000.000": 0, "1.000.000-9.000.000": 0, "9.000.000-17.000.000": 0,
                           "17.000.000-25.000.000": 0, "25.000.000-33.000.000": 0, ">33.000.000": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                                                SELECT ?valor WHERE{
                                                                      ?c a dbo:Pais .
                                                                      ?c dbo:posee ?n .
                                                                      ?n a dbo:Poblacion .
                                                                      ?n dbo:valor ?valor .
                                                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 1000000:
                        valores[list(valores.keys())[0]] += 1
                    elif 1000000 <= float(i) < 9000000:
                        valores[list(valores.keys())[1]] += 1
                    elif 9000000 <= float(i) < 17000000:
                        valores[list(valores.keys())[2]] += 1
                    elif 17000000 <= float(i) < 25000000:
                        valores[list(valores.keys())[3]] += 1
                    elif 25000000 <= float(i) < 33000000:
                        valores[list(valores.keys())[4]] += 1
                    elif float(i) >= 33000000:
                        valores[list(valores.keys())[5]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("Tamaño de población")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "6":
                valores = {"<125.000": 0, "125.000-375.000": 0, "375.000-625.000": 0, "625.000-875.000": 0,
                           "875.000-1.125.000": 0, ">1.125.000": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                SELECT ?valor WHERE{
                    ?c a dbo:Pais .
                    ?c dbo:posee ?n .
                    ?n a dbo:IndiceDepresion .
                    ?n dbo:numeroCasos ?valor .
                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if int(i) < 125000:
                        valores[list(valores.keys())[0]] += 1
                    elif 125000 <= int(i) < 375000:
                        valores[list(valores.keys())[1]] += 1
                    elif 375000 <= int(i) < 625000:
                        valores[list(valores.keys())[2]] += 1
                    elif 625000 <= int(i) < 875000:
                        valores[list(valores.keys())[3]] += 1
                    elif 875000 <= int(i) < 1125000:
                        valores[list(valores.keys())[4]] += 1
                    elif int(i) >= 1125000:
                        valores[list(valores.keys())[5]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("Número de casos de depresión")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "7":
                valores = {"<1000": 0, "1000-2500": 0, "2500-5000": 0, "5000-7500": 0, "7500-10000": 0,
                           "10000-12500": 0,
                           "12500-15000": 0, "15000-17500": 0, "17500-20000": 0, "20000-22500": 0, "22500-25000": 0,
                           "25000-27500": 0, "27500-30000": 0, ">30000": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                SELECT ?valor WHERE{
                    ?c a dbo:Pais .
                    ?c dbo:posee ?n .
                    ?n a dbo:PibPerCapita .
                    ?n dbo:valor ?valor .
                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 1000:
                        valores[list(valores.keys())[0]] += 1
                    elif 1000 <= float(i) < 2500:
                        valores[list(valores.keys())[1]] += 1
                    elif 2500 <= float(i) < 5000:
                        valores[list(valores.keys())[2]] += 1
                    elif 5000 <= float(i) < 7500:
                        valores[list(valores.keys())[3]] += 1
                    elif 7500 <= float(i) < 10000:
                        valores[list(valores.keys())[4]] += 1
                    elif 10000 <= float(i) < 12500:
                        valores[list(valores.keys())[5]] += 1
                    elif 12500 <= float(i) < 15000:
                        valores[list(valores.keys())[6]] += 1
                    elif 15000 <= float(i) < 17500:
                        valores[list(valores.keys())[7]] += 1
                    elif 17500 <= float(i) < 20000:
                        valores[list(valores.keys())[8]] += 1
                    elif 20000 <= float(i) < 22500:
                        valores[list(valores.keys())[9]] += 1
                    elif 22500 <= float(i) < 25000:
                        valores[list(valores.keys())[10]] += 1
                    elif 25000 <= float(i) < 27500:
                        valores[list(valores.keys())[11]] += 1
                    elif 27500 <= float(i) < 30000:
                        valores[list(valores.keys())[12]] += 1
                    elif float(i) >= 30000:
                        valores[list(valores.keys())[13]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("PIB per cápita")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "8":
                valores = {"<150": 0, "150-300": 0, "300-450": 0, "450-600": 0, "600-750": 0,
                           ">750": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                SELECT ?valor WHERE{
                                    ?c a dbo:Pais .
                                    ?c dbo:posee ?n .
                                    ?n a dbo:DensidadPoblacion .
                                    ?n dbo:valor ?valor .
                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 50:
                        valores[list(valores.keys())[0]] += 1
                    elif 50 <= float(i) < 100:
                        valores[list(valores.keys())[1]] += 1
                    elif 100 <= float(i) < 150:
                        valores[list(valores.keys())[2]] += 1
                    elif 150 <= float(i) < 200:
                        valores[list(valores.keys())[3]] += 1
                    elif 200 <= float(i) < 250:
                        valores[list(valores.keys())[4]] += 1
                    elif float(i) >= 250:
                        valores[list(valores.keys())[5]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("Densidad de población")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "9":
                valores = {"<25": 0, "25-30": 0, "30-35": 0, "35-40": 0, "40-45": 0,
                           "45-50": 0, "50-55": 0, "55-60": 0, ">60": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                                SELECT ?valor WHERE{
                                                      ?c a dbo:Pais .
                                                      ?c dbo:posee ?n .
                                                      ?n a dbo:CoeficienteGini .
                                                      ?n dbo:valor ?valor .
                                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 25:
                        valores[list(valores.keys())[0]] += 1
                    elif 25 <= float(i) < 30:
                        valores[list(valores.keys())[1]] += 1
                    elif 30 <= float(i) < 35:
                        valores[list(valores.keys())[2]] += 1
                    elif 35 <= float(i) < 40:
                        valores[list(valores.keys())[3]] += 1
                    elif 40 <= float(i) < 45:
                        valores[list(valores.keys())[4]] += 1
                    elif 45 <= float(i) < 50:
                        valores[list(valores.keys())[5]] += 1
                    elif 50 <= float(i) < 30:
                        valores[list(valores.keys())[6]] += 1
                    elif 55 <= float(i) < 60:
                        valores[list(valores.keys())[7]] += 1
                    elif float(i) >= 60:
                        valores[list(valores.keys())[8]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xticks(rotation=90)
                plt.xlabel("Coeficiente Gini")
                plt.ylabel("Número de países")
                plt.show()

            elif choice == "10":
                valores = {"0-0.1": 0, "0.1-0.2": 0, "0.2-0.3": 0, "0.3-0.4": 0, "0.4-0.5": 0, "0.5-0.6": 0,
                           "0.6-0.7": 0, "0.7-0.8": 0, "0.8-0.9": 0, "0.9-1": 0}

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery("""
                                PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                SELECT ?valor WHERE{
                                      ?c a dbo:Pais .
                                      ?c dbo:posee ?n .
                                      ?n a dbo:IndiceDesarrolloHumano .
                                      ?n dbo:valor ?valor .
                                }""")
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                for i in list(df.valor):
                    if float(i) < 0.1:
                        valores[list(valores.keys())[0]] += 1
                    elif 0.1 <= float(i) < 0.2:
                        valores[list(valores.keys())[1]] += 1
                    elif 0.2 <= float(i) < 0.3:
                        valores[list(valores.keys())[2]] += 1
                    elif 0.3 <= float(i) < 0.4:
                        valores[list(valores.keys())[3]] += 1
                    elif 0.4 <= float(i) < 0.5:
                        valores[list(valores.keys())[4]] += 1
                    elif 0.5 <= float(i) < 0.6:
                        valores[list(valores.keys())[5]] += 1
                    elif 0.6 <= float(i) < 0.7:
                        valores[list(valores.keys())[6]] += 1
                    elif 0.7 <= float(i) < 0.8:
                        valores[list(valores.keys())[7]] += 1
                    elif 0.8 <= float(i) < 0.9:
                        valores[list(valores.keys())[8]] += 1
                    elif float(i) >= 0.9:
                        valores[list(valores.keys())[9]] += 1

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                x = valores.keys()
                y = valores.values()
                ax.bar(x, y)
                plt.xlabel("Índice de desarrollo humano")
                plt.ylabel("Número de países")
                plt.show()

            print("""
1 - mostrar número de países por tipo de régimen
2 - mostrar número de países por índice democrático
3 - mostrar número de países por zona geográfica
4 - mostrar número de países por prevalencia de depresión
5 - mostrar número de países por tamaño de población
6 - mostrar número de países por número de casos de depresión
7 - mostrar número de países por PIB per cápita
8 - mostrar número de países por densidad de población
9 - mostrar número de países por coeficiente de gini
10 - mostrar número de países por índice de desarrollo humano
99 - volver""")
            choice = input()

    elif choice == "2":
        print("Introduzca el nombre del país (Spain, Cameroon, Germany, United States...)")
        pais = input().replace(" ", "_")
        sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
        sparql.setReturnFormat(CSV)
        sparql.setQuery('''
                            PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                            SELECT DISTINCT ?regimen ?indice ?zona ?prevalencia ?casos ?poblacion ?pib ?densidad ?gini ?desarrollo WHERE{}
                              ?c a dbo:Pais .
                              ?c dbo:nombre "{}" .
                              OPTIONAL {}?c dbo:posee ?n1 .
                                        ?n1 a dbo:TipoRegimen .
                                        ?n1 dbo:tipo ?regimen .
                                        {} .
                              OPTIONAL {}?c dbo:posee ?n2 .
                                        ?n2 a dbo:ValorDemocracia .
                                        ?n2 dbo:ano "2021"^^xsd:int .
                                        ?n2 dbo:valor ?indice .
                                        {} .
                              OPTIONAL {}?c dbo:estaEn ?z .
                                        ?z dbo:nombre ?zona .{} .
                              OPTIONAL {}?c dbo:posee ?n3 .
                                        ?n3 a dbo:IndiceDepresion .
                                        ?n3 dbo:valor ?prevalencia .
                                        ?n3 dbo:numeroCasos ?casos.
                                        {} .
                              OPTIONAL {}?c dbo:posee ?n4 .
                                        ?n4 a dbo:Poblacion .
                                        ?n4 dbo:valor ?poblacion .
                                        {} .
                              OPTIONAL {}?c dbo:posee ?n5 .
                                        ?n5 a dbo:PibPerCapita .
                                        ?n5 dbo:valor ?pib .
                                        {} .
                              OPTIONAL{}?c dbo:posee ?n6 .
                                       ?n6 a dbo:DensidadPoblacion .
                                       ?n6 dbo:valor ?densidad .
                                       {} .
                              OPTIONAL{}?c dbo:posee ?n7 .
                                       ?n7 a dbo:CoeficienteGini .
                                       ?n7 dbo:valor ?gini .
                                       {} .
                              OPTIONAL{}?c dbo:posee ?n8 .
                                       ?n8 a dbo:IndiceDesarrolloHumano .
                                       ?n8 dbo:valor ?desarrollo .
                                       {} .
                        {} LIMIT 1'''.format("{", pais, "{", "}", "{", "}", "{", "}", "{", "}", "{", "}", "{", "}", "{",
                                             "}", "{", "}", "{", "}", "}"))
        results = sparql.queryAndConvert().decode(encoding='UTF8')
        csvStringIO = StringIO(results)
        df = pd.read_csv(csvStringIO)
        if not df.empty:
            datos = df.iloc[0, :]
            print(
                "\nTipo de régimen: {}\nÍndice democrático de 2021: {}\nZona geográfica: {}\nPrevalencia de depresión: "
                "{}\nNúmero de casos de depresión: {}\nTamaño de población: {}\nDensidad de población: {}\nPIB "
                "per capita: {}\nCoeficiente de Gini: {}\nÍndice de desarrollo humano: {}".format(datos.regimen,
                                                                                                  datos.indice,
                                                                                                  datos.zona,
                                                                                                  datos.prevalencia,
                                                                                                  datos.casos,
                                                                                                  datos.poblacion,
                                                                                                  datos.densidad,
                                                                                                  datos.pib, datos.gini,
                                                                                                  datos.desarrollo))

            sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
            sparql.setReturnFormat(CSV)
            sparql.setQuery('''
                            PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                            SELECT DISTINCT ?2006 ?2008 ?2010 ?2011 ?2012 ?2013 ?2014 ?2015 ?2016 ?2017 ?2018 ?2019 ?2020 ?2021 WHERE{}
                                  ?c a dbo:Pais .
                                  ?c dbo:nombre "{}" .
                                  OPTIONAL {}?c dbo:posee ?v1 .
                                            ?v1 a dbo:ValorDemocracia .
                                            ?v1 dbo:ano "2006"^^xsd:int .
                                            ?v1 dbo:valor ?2006 .{} .
                                  OPTIONAL {}?c dbo:posee ?v2 .
                                            ?v2 a dbo:ValorDemocracia .
                                            ?v2 dbo:ano "2008"^^xsd:int .
                                            ?v2 dbo:valor ?2008 .{} .
                                  OPTIONAL {}?c dbo:posee ?v3 .
                                            ?v3 a dbo:ValorDemocracia .
                                            ?v3 dbo:ano "2010"^^xsd:int .
                                            ?v3 dbo:valor ?2010 .{} .
                                  OPTIONAL {}?c dbo:posee ?v4 .
                                            ?v4 a dbo:ValorDemocracia .
                                            ?v4 dbo:ano "2011"^^xsd:int .
                                            ?v4 dbo:valor ?2011 .{} .
                                  OPTIONAL {}?c dbo:posee ?v5 .
                                            ?v5 a dbo:ValorDemocracia .
                                            ?v5 dbo:ano "2012"^^xsd:int .
                                            ?v5 dbo:valor ?2012 .{} .
                                  OPTIONAL {}?c dbo:posee ?v6 .
                                            ?v6 a dbo:ValorDemocracia .
                                            ?v6 dbo:ano "2013"^^xsd:int .
                                            ?v6 dbo:valor ?2013 .{} .
                                  OPTIONAL {}?c dbo:posee ?v7 .
                                            ?v7 a dbo:ValorDemocracia .
                                            ?v7 dbo:ano "2014"^^xsd:int .
                                            ?v7 dbo:valor ?2014 .{} .
                                  OPTIONAL {}?c dbo:posee ?v8 .
                                            ?v8 a dbo:ValorDemocracia .
                                            ?v8 dbo:ano "2015"^^xsd:int .
                                            ?v8 dbo:valor ?2015 .{} .
                                  OPTIONAL {}?c dbo:posee ?v9 .
                                            ?v9 a dbo:ValorDemocracia .
                                            ?v9 dbo:ano "2016"^^xsd:int .
                                            ?v9 dbo:valor ?2016 .{} .
                                  OPTIONAL {}?c dbo:posee ?v10 .
                                            ?v10 a dbo:ValorDemocracia .
                                            ?v10 dbo:ano "2017"^^xsd:int .
                                            ?v10 dbo:valor ?2017 .{} .
                                  OPTIONAL {}?c dbo:posee ?v11 .
                                            ?v11 a dbo:ValorDemocracia .
                                            ?v11 dbo:ano "2018"^^xsd:int .
                                            ?v11 dbo:valor ?2018 .{} .
                                  OPTIONAL {}?c dbo:posee ?v12 .
                                            ?v12 a dbo:ValorDemocracia .
                                            ?v12 dbo:ano "2019"^^xsd:int .
                                            ?v12 dbo:valor ?2019 .{} .
                                  OPTIONAL {}?c dbo:posee ?v13 .
                                            ?v13 a dbo:ValorDemocracia .
                                            ?v13 dbo:ano "2020"^^xsd:int .
                                            ?v13 dbo:valor ?2020 .{} .
                                  OPTIONAL {}?c dbo:posee ?v14 .
                                            ?v14 a dbo:ValorDemocracia .
                                            ?v14 dbo:ano "2021"^^xsd:int .
                                            ?v14 dbo:valor ?2021 .{} .
                              
                            {} LIMIT 1'''.format("{", pais, "{", "}", "{", "}", "{", "}", "{", "}", "{", "}", "{", "}", "{",
                                             "}", "{", "}", "{", "}", "{",
                                             "}", "{", "}", "{", "}", "{", "}", "{", "}", "}"))
            results = sparql.queryAndConvert().decode(encoding='UTF8')
            csvStringIO = StringIO(results)
            df = pd.read_csv(csvStringIO)
            df.fillna(0)

            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            x = ["2006", "2008", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
                 "2021"]
            y = list(df.iloc[0, :])
            ax.plot(x, y)
            plt.ylim(0, 10)
            plt.xlabel("Año")
            plt.ylabel("Índice de democracia")
            plt.title("Evolución del índice democrático de {}".format(pais))
            plt.show()
        else:
            print("No se han podido obtener valores")
            print("Introduzca el nombre del país (Spain, Cameroon, Germany...)")
            pais = input()
            continue

    elif choice == "3":
        vars = ["prevalencia de depresión", "índice de democracia", "tamaño de población", "PIB per capita",
                "coeficiente de Gini", "índice de desarrollo humano"]
        cods = ["IndiceDepresion", "ValorDemocracia", "Poblacion", "PibPerCapita", "CoeficienteGini",
                "IndiceDesarrolloHumano"]
        print("\nElija la primera variable:")
        for i in range(len(vars)):
            print("{} - {}".format(i + 1, vars[i]))
        choice = input()
        if choice in "123456":
            if choice == "1":
                v1 = cods[0]
                n1 = vars[0]
                vars.pop(0)
                cods.pop(0)
            elif choice == "2":
                v1 = cods[1]
                n1 = vars[1]
                vars.pop(1)
                cods.pop(1)
            elif choice == "3":
                v1 = cods[2]
                n1 = vars[2]
                vars.pop(2)
                cods.pop(2)
            elif choice == "4":
                v1 = cods[3]
                n1 = vars[3]
                vars.pop(3)
                cods.pop(3)
            elif choice == "5":
                v1 = cods[4]
                n1 = vars[4]
                vars.pop(4)
                cods.pop(4)
            elif choice == "6":
                v1 = cods[5]
                n1 = vars[5]
                vars.pop(5)
                cods.pop(5)

            print("\nElija la segunda variable:")
            for i in range(len(vars)):
                print("{} - {}".format(i + 1, vars[i]))
            choice = input()
            if choice in "12345":
                if choice == "1":
                    v2 = cods[0]
                    n2 = vars[0]
                elif choice == "2":
                    v2 = cods[1]
                    n2 = vars[1]
                elif choice == "3":
                    v2 = cods[2]
                    n2 = vars[2]
                elif choice == "4":
                    v2 = cods[3]
                    n2 = vars[3]
                elif choice == "5":
                    v2 = cods[4]
                    n2 = vars[4]
                elif choice == "6":
                    v2 = cods[5]
                    n2 = vars[5]

                sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
                sparql.setReturnFormat(CSV)
                sparql.setQuery(query(v1, v2))
                results = sparql.queryAndConvert().decode(encoding='UTF8')
                csvStringIO = StringIO(results)
                df = pd.read_csv(csvStringIO)
                x = list(df.x)
                y = list(df.y)

                upper1 = np.percentile(x, 75)
                lower1 = np.percentile(x, 25)
                iqr1 = (upper1 - lower1) * 1.5
                upper2 = np.percentile(y, 75)
                lower2 = np.percentile(y, 25)
                iqr2 = (upper2 - lower2) * 1.5
                for i in range(len(x)):
                    if x[i] < lower1 - iqr1 or y[i] < lower2 - iqr2 or x[i] > upper1 + iqr1 or y[i] > upper2 + iqr2:
                        x[i] = None
                        y[i] = None
                x = [i for i in x if i is not None]
                y = [i for i in y if i is not None]

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                ax.scatter(x, y, s=60, alpha=0.7, edgecolors="k")
                b, a = np.polyfit(x, y, deg=1)
                ax.plot(np.array(x), a + b * np.array(x), color="k", lw=2.5)
                plt.xlim(min(x) - 0.25 * np.std(x), max(x) + 0.25 * np.std(x))
                plt.ylim(min(y) - 0.25 * np.std(y), max(y) + 0.25 * np.std(y))
                plt.xlabel(n1)
                plt.ylabel(n2)
                plt.title("{} vs {}".format(n1, n2))
                plt.show()

            else:
                print("\nHa introducido un número incorrecto")
        else:
            print("\nHa introducido un número incorrecto")

    elif choice == "4":
        sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
        sparql.setReturnFormat(CSV)
        sparql.setQuery('''
                                    PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                                    SELECT DISTINCT ?nombre ?indice ?prevalencia ?casos ?poblacion ?pib ?densidad ?gini ?desarrollo WHERE{}
                                      ?c a dbo:Pais .
                                      ?c dbo:nombre ?nombre .
                                      OPTIONAL {}?c dbo:posee ?n2 .
                                                ?n2 a dbo:ValorDemocracia .
                                                ?n2 dbo:ano "2021"^^xsd:int .
                                                ?n2 dbo:valor ?indice .
                                                {} .
                                      OPTIONAL {}?c dbo:posee ?n3 .
                                                ?n3 a dbo:IndiceDepresion .
                                                ?n3 dbo:valor ?prevalencia .
                                                ?n3 dbo:numeroCasos ?casos.
                                                {} .
                                      OPTIONAL {}?c dbo:posee ?n4 .
                                                ?n4 a dbo:Poblacion .
                                                ?n4 dbo:valor ?poblacion .
                                                {} .
                                      OPTIONAL {}?c dbo:posee ?n5 .
                                                ?n5 a dbo:PibPerCapita .
                                                ?n5 dbo:valor ?pib .
                                                {} .
                                      OPTIONAL{}?c dbo:posee ?n6 .
                                               ?n6 a dbo:DensidadPoblacion .
                                               ?n6 dbo:valor ?densidad .
                                               {} .
                                      OPTIONAL{}?c dbo:posee ?n7 .
                                               ?n7 a dbo:CoeficienteGini .
                                               ?n7 dbo:valor ?gini .
                                               {} .
                                      OPTIONAL{}?c dbo:posee ?n8 .
                                               ?n8 a dbo:IndiceDesarrolloHumano .
                                               ?n8 dbo:valor ?desarrollo .
                                               {} .
                                {}'''.format("{", "{", "}", "{", "}", "{", "}", "{", "}", "{",
                                             "}", "{", "}", "{",
                                             "}", "}"))
        results = sparql.queryAndConvert().decode(encoding='UTF8')
        csvStringIO = StringIO(results)
        df = pd.read_csv(csvStringIO)
        df = df.dropna(axis=0)
        df.drop_duplicates(['nombre'], inplace=True)
        df = df.iloc[:, 1:]

        corr_matrix = df.corr()
        sn.heatmap(corr_matrix, annot=True)
        plt.show()

    elif choice == "5":
        sparql = SPARQLWrapper("http://localhost:7200/repositories/trabajo-web-semantica")
        sparql.setReturnFormat(CSV)
        sparql.setQuery("""
                        PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
                        SELECT ?pais WHERE{
                              ?c a dbo:Pais .
                              ?c dbo:nombre ?pais .
                        }""")
        results = sparql.queryAndConvert().decode(encoding='UTF8')
        csvStringIO = StringIO(results)
        df = pd.read_csv(csvStringIO)

        for i in list(df.pais):
            print("- {}".format(i))

    print("""
1 - visualizar datos generales
2 - obtener datos por país
3 - visualizar relación entre dos variables
4 - ver correlación entre todas las variables
5 - ver lista de países
99 - salir""")
    choice = input()

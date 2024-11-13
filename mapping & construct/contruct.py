from SPARQLWrapper import SPARQLWrapper, RDFXML
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

sparql.setQuery("""
    PREFIX dbo: <http://www.semanticweb.org/34620/ontologies/2022/11/ontology-Sergio#>
    PREFIX dbp: <http://dbpedia.org/property/> 
    PREFIX schema: <http://schema.org/>
    PREFIX db: <http://dbpedia.org/ontology/>

    CONSTRUCT {
        ?countryUriNuestra a dbo:Pais .
        ?countryUriNuestra dbo:posee ?giniCoefficientURI .
        ?giniCoefficientURI a dbo:CoeficienteGini .
        ?giniCoefficientURI  dbo:valor ?giniCoefficient .
        ?giniCoefficientURI dbo:descripcion "Coeficiente que mide la desigualdad en los ingresos de las personas de un país" .
        ?giniCoefficientURI dbo:ano 2020 .

        ?countryUriNuestra dbo:posee ?humanDevelopmentIndexURI .
        ?humanDevelopmentIndexURI a dbo:IndiceDesarrolloHumano .
        ?humanDevelopmentIndexURI  dbo:valor ?humanDevelopmentIndex .
        ?humanDevelopmentIndexURI dbo:descripcion "Indice usado para medir el desarrollo humano de los países" .
        ?humanDevelopmentIndexURI dbo:ano 2020 .

        ?countryUriNuestra dbo:posee ?populationDensityURI .
        ?populationDensityURI a dbo:DensidadPoblacion .
        ?populationDensityURI dbo:valor ?populationDensityFloat .
        ?populationDensityURI dbo:descripcion "Cantidad de personas que en promedio habitan por por kilómetro cuadrado" .
        ?populationDensityURI dbo:ano 2020 .

        ?countryUriNuestra dbo:posee ?gdpNominalPerCapitaURI .
        ?gdpNominalPerCapitaURI a dbo:PibPerCapita .
        ?gdpNominalPerCapitaURI  dbo:valor ?gdpNominalPerCapitaFloat .
        ?gdpNominalPerCapitaURI dbo:descripcion "Indicador macroeconómico que mide la produccion de un país en relación con su número de habitantes" .
        ?gdpNominalPerCapitaURI dbo:ano 2020 .

    }


    WHERE {
        ?country a db:Country .
        ?country db:giniCoefficient ?giniCoefficient .
        ?country db:humanDevelopmentIndex ?humanDevelopmentIndex .
        ?country <http://dbpedia.org/ontology/PopulatedPlace/populationDensity> ?populationDensity .
        ?country dbp:gdpNominalPerCapita ?gdpNominalPerCapita .
        ?country dbp:commonName ?c .


        BIND (URI(REPLACE(CONCAT("http://www.semanticweb.org/data/giniCoefficient/2022/", STR(?c)), " ", "_")) AS ?giniCoefficientURI)

        BIND (URI(REPLACE(CONCAT("http://www.semanticweb.org/data/humanDevelopmentIndex/2022/", STR(?c)), " ", "_")) AS ?humanDevelopmentIndexURI)

        BIND (URI(REPLACE(CONCAT("http://www.semanticweb.org/data/populationDensity/2022/", STR(?c)), " ", "_")) AS ?populationDensityURI)
        BIND (xsd:float(?populationDensity) AS ?populationDensityFloat)

        BIND (xsd:float(?gdpNominalPerCapita) AS ?gdpNominalPerCapitaFloat)
        BIND (URI(REPLACE(CONCAT("http://www.semanticweb.org/data/gdpNominalPerCapita/2022/", STR(?c)), " ", "_")) AS ?gdpNominalPerCapitaURI)


        BIND (URI(REPLACE(CONCAT("http://www.semanticweb.org/data/", STR(?c)), " ", "_")) AS ?countryUriNuestra)

    }
""")
sparql.setReturnFormat(RDFXML)
results = sparql.query().convert()
results.parse('/content/output_mapping_final.ttl')
results.serialize('mapping_y_construct.ttl', format='ttl')
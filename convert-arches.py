import sys
import os
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import requests

class ArchesToRdfConverter:
    def __init__(self, hostUrl):
        self.host = hostUrl

    def fetch_arches_resource_jsonld(self, resourceinstanceid=None):
        
        if resourceinstanceid == None:
            raise ValueError('No resourceinstanceid provided')
        
        reqUrl = f"{ self.host }/resources/{ str(resourceinstanceid) }"
        print(f"... ... fetching data {reqUrl}")
        r = requests.get(reqUrl)
        if r.status_code == 200:
            print(f"... ... ... status code {r.status_code}")
            return r.text
        else:
            raise ValueError(f'Arches responded with {r.statuscode} response code')


    def convert_arches_resource_to_rdf(self, resourceinstanceid=None):
        record_data = self.fetch_arches_resource_jsonld(resourceinstanceid)
        g = Graph().parse(data=record_data, format='json-ld')
        rdf = g.serialize(format='turtle')
        return rdf


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise ValueError('Incorrect input arguments - Expecting 0. Arches hostname (e.g. https://www.example-arches.com); 1. Resourceinstanceid guid; 2. output directory path')

    host = str(sys.argv[1])
    inResids = str(sys.argv[2])
    resid_list = inResids.split(',')
    outdir = str(sys.argv[3])

    if not os.path.exists(outdir):
        raise ValueError("Incorrect input argument - Output directory does not exist ")
    
    print("== Arches RDF generator ==")
    print("")
    
    converter = ArchesToRdfConverter(host)

    for resid in resid_list:
        outfile = f'{outdir}\\{resid}.rdf'
        rdf_string = None
        print(f"... starting {resid}")
        try:
            rdf_string = converter.convert_arches_resource_to_rdf(resid)
        except Exception as ex:
            print(f'... ERROR: Could not generate rdf data from record - {str(ex)}')

        if rdf_string != None:
            try:
                rdf = open(outfile,'w')
                try:
                    rdf.write(rdf_string.decode("utf-8") )
                    print(f"... generated file for {resid}")
                    
                finally:
                    rdf.close()
                    
            except Exception as e:
                print(str(e))
    print("")            
    print("=== Complete ===")

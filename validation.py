from tripoli import IIIFValidator
from rede_iiif_manifest.manifest import Manifest, Sequence, Canvas


m = Manifest(label="My manifest", id_="localhost/ex/1", sequences=[])

# mm = Manifest(label="my second manifest", id_="sd")

x = """
{ "@context": "http://iiif.io/api/presentation/2/context.json", "@id": "http://localhost:10000//wenkerboegen/24903/manifest", "@type": "sc:Manifest", "label": "my first maninfest for 24903", "sequences": [ { "@id": "http://localhost:10000//wenkerboegen/24903/sequence/normal", "@type": "sc:Sequence", "canvases": [ { "@id": "http://localhost:10000//wenkerboegen/24903/canvas/a", "@type": "sc:Canvas", "height": 1000, "images": [ { "@id": "http://localhost:10000//wenkerboegen/24903/annotation/a", "@type": "oa:Annotation", "motivation": "sc:painting", "on": "http://localhost:10000//wenkerboegen/24903/canvas/a", "resource": { "@id": "http://localhost/iiif/2/12345c.jp2/info.json", "@type": "dctypes:Image", "height": 1000, "service": { "@context": "http://iiif.io/api/image/2/context.json", "@id": "http://localhost/iiif/2/12345c.jp2/info.json", "profile": "http://iiif.io/api/image/2/level2.json" }, "width": 1000 } } ], "label": "my first canvas", "otherContent": [], "width": 1000 } ] } ] }
"""
print("json:", m.as_json)
print("dict:", m.as_dict)

iv = IIIFValidator()

iv.validate(x)

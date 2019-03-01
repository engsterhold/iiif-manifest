import related


@related.mutable
class base_:
    id_ = related.URLField(key="@id")

    @property
    def as_json(self):
        return related.to_json(self)

    @property
    def as_dict(self):
        return related.to_dict(self)


@related.mutable
class Annotation(base_):
    type_ = related.StringField(default="oa:Annotation", key="@type")


@related.mutable
class AnnotationList(base_):

    resources = related.SequenceField(cls=Annotation)
    type_ = related.StringField(default="sc:AnnotationList", key="@type")


@related.mutable
class ImageService(base_):
    context_ = related.URLField(
        default="http:iiif.io/api/image/2/context.json", key="@context")
    profile = related.URLField(
        default="http://iiif.io/api/image/2/level2.json")


@related.mutable
class ImageResource(base_):
    service = related.ChildField(ImageService)
    height = related.IntegerField(required=False)
    width = related.IntegerField(required=False)

    type_ = related.StringField(default="dctypes:Image", key="@type")


@related.mutable
class Image(Annotation):

    resource = related.ChildField(ImageResource)
    on = related.URLField()
    motivation = related.StringField(default="sc:painting")
    type_ = related.StringField(default="oa:Annotation", key="@type")


@related.mutable
class Canvas(base_):
    label = related.StringField()
    width = related.IntegerField()
    height = related.IntegerField()
    images = related.SequenceField(cls=Annotation, required=False)
    otherContent = related.SequenceField(cls=list, required=False)
    type_ = related.StringField(default="sc:Canvas", key="@type")


@related.mutable
class Sequence(base_):

    canvases = related.SequenceField(cls=Canvas)
    type_ = related.StringField(default="sc:Sequence", key="@type")


@related.mutable
class Manifest(base_):
    label = related.StringField()
    sequences = related.SequenceField(cls=Sequence, required=False)
    type_ = related.StringField(default="sc:Manifest", key="@type")


if __name__ == "__main__":
    m = Manifest(label="My manifest", id_="1", sequences=[Sequence(id_="3", canvases=[
        Canvas(label="my canvas", id_="2", width=1, height=1), Canvas(label="my canvas 2", id_="3", width=1, height=1)])])

    # mm = Manifest(label="my second manifest", id_="sd")

    print("json:", m.as_json)
    print("dict:", m.as_dict)

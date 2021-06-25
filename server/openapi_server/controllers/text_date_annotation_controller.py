import connexion
from openapi_server.annotator.annotate import Annotator
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_date_annotation_request import \
    TextDateAnnotationRequest  # noqa: E501
from openapi_server.models.text_date_annotation import TextDateAnnotation
from openapi_server.models.text_date_annotation_response import \
    TextDateAnnotationResponse  # noqa: E501


annotator: Annotator = Annotator.load(
    'openapi_server/annotator/cached/annotator_model.joblib')


def create_text_date_annotations():  # noqa: E501
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note # noqa: E501

    :rtype: TextDateAnnotations
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextDateAnnotationRequest.from_dict(
                connexion.request.get_json())  # noqa: E501
            note = annotation_request.note
            annotation_set, = annotator.annotate([note.text])
            annotations = [TextDateAnnotation(
                start=annotation['start'],
                length=annotation['end'] - annotation['start'],
                text=annotation['text'],
                confidence=95.0
            ) for annotation in annotation_set]

            res = TextDateAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    return res, status

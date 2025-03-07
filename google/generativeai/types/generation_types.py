from typing import Optional, Sequence, Union

from google.ai.generativelanguage_v1beta.types import safety as protos


class ContentFilter:
    r"""Content filter.

    Attributes:
        reason (``str``):
            The reason the content was filtered.
        index (``int``):
            The index of the content that was filtered.
    """

    def __init__(self, reason: str, index: int):
        self.reason = reason
        self.index = index


class GenerationResponse:
    r"""Generation response.

    Attributes:
        text (``str``):
            The generated text.
        prompt_feedback (``Optional[PromptFeedback]``):
            Information about the prompt feedback, if any.
        safety_ratings (``Sequence[SafetyRating]``):
            Safety ratings for the generated text.
        citation_metadata (``Optional[CitationMetadata]``):
            Citation metadata for the generated text.
    """

    def __init__(
        self,
        text: str,
        prompt_feedback: Optional["PromptFeedback"] = None,
        safety_ratings: Sequence["SafetyRating"] = (),
        citation_metadata: Optional["CitationMetadata"] = None,
    ):
        self.text = text
        self.prompt_feedback = prompt_feedback
        self.safety_ratings = safety_ratings
        self.citation_metadata = citation_metadata


class PromptFeedback:
    r"""Prompt feedback.

    Attributes:
        safety_ratings (``Sequence[SafetyRating]``):
            Safety ratings for the prompt.
    """

    def __init__(
        self,
        safety_ratings: Sequence["SafetyRating"],
    ):
        self.safety_ratings = safety_ratings


class SafetyRating:
    r"""Safety rating.

    Attributes:
        category (``str``):
            The category of the safety rating.
        probability (``str``):
            The probability of the safety rating.
    """

    def __init__(self, category: str, probability: str):
        self.category = category
        self.probability = probability


class CitationMetadata:
    r"""Citation metadata.

    Attributes:
        citation_sources (``Sequence[CitationSource]``):
            Citation sources for the generated text.
    """

    def __init__(
        self,
        citation_sources: Sequence["CitationSource"],
    ):
        self.citation_sources = citation_sources


class CitationSource:
    r"""Citation source.

    Attributes:
        start_index (``int``):
            The start index of the citation.
        end_index (``int``):
            The end index of the citation.
        uri (``str``):
            The URI of the citation.
        license (``str``):
            The license of the citation.
    """

    def __init__(self, start_index: int, end_index: int, uri: str, license: str):
        self.start_index = start_index
        self.end_index = end_index
        self.uri = uri
        self.license = license


class StreamingGenerationChunk:
    r"""Streaming generation chunk.

    Attributes:
        text (``str``):
            The generated text chunk.
        safety_ratings (``Sequence[SafetyRating]``):
            Safety ratings for the generated text chunk.
        citation_metadata (``Optional[CitationMetadata]``):
            Citation metadata for the generated text chunk.
    """

    def __init__(
        self,
        text: str,
        safety_ratings: Sequence["SafetyRating"] = (),
        citation_metadata: Optional["CitationMetadata"] = None,
    ):
        self.text = text
        self.safety_ratings = safety_ratings
        self.citation_metadata = citation_metadata


class ToolCall:
    r"""Tool call.

    Attributes:
        name (``str``):
            The name of the tool.
        arguments (``Dict[str, Any]``):
            The arguments to the tool.
    """

    def __init__(self, name: str, arguments: dict):
        self.name = name
        self.arguments = arguments


class FunctionResponse:
    r"""Function response.

    Attributes:
        name (``str``):
            The name of the function.
        response (``Dict[str, Any]``):
            The response from the function.
    """

    def __init__(self, name: str, response: dict):
        self.name = name
        self.response = response


class Part:
    r"""A part of a turn.

    Attributes:
        text (``Optional[str]``):
            The text of the part.
        inline_data (``Optional[Blob]``):
            The inline data of the part.
        tool_call (``Optional[ToolCall]``):
            The tool call of the part.
        function_response (``Optional[FunctionResponse]``):
            The function response of the part.
    """

    def __init__(
        self,
        text: Optional[str] = None,
        inline_data: Optional["Blob"] = None,
        tool_call: Optional[ToolCall] = None,
        function_response: Optional[FunctionResponse] = None,
    ):
        self.text = text
        self.inline_data = inline_data
        self.tool_call = tool_call
        self.function_response = function_response

    @property
    def text(self) -> Optional[str]:
        return self._pb.text

    @text.setter
    def text(self, text: Optional[str]) -> None:
        self._pb.text = text

    @property
    def inline_data(self) -> Optional["Blob"]:
        if not self._pb.HasField("inline_data"):
            return None
        return Blob.from_pb(self._pb.inline_data)

    @inline_data.setter
    def inline_data(self, inline_data: Optional["Blob"]):
        if inline_data is None:
            self._pb.ClearField("inline_data")
            return
        self._pb.inline_data = inline_data._pb

    @property
    def tool_call(self) -> Optional[ToolCall]:
        if not self._pb.HasField("tool_call"):
            return None
        return ToolCall(self._pb.tool_call.name, self._pb.tool_call.args)

    @tool_call.setter
    def tool_call(self, tool_call: Optional[ToolCall]):
        if tool_call is None:
            self._pb.ClearField("tool_call")
            return
        self._pb.tool_call.name = tool_call.name
        self._pb.tool_call.args = tool_call.arguments

    @property
    def function_response(self) -> Optional[FunctionResponse]:
        if not self._pb.HasField("function_response"):
            return None
        return FunctionResponse(
            self._pb.function_response.name, self._pb.function_response.result
        )

    @function_response.setter
    def function_response(self, function_response: Optional[FunctionResponse]):
        if function_response is None:
            self._pb.ClearField("function_response")
            return
        self._pb.function_response.name = function_response.name
        self._pb.function_response.result = function_response.response

    @classmethod
    def from_pb(cls, pb: protos.Part) -> "Part":
        result = cls.__new__(cls)
        result._pb = pb
        return result

    def __repr__(self) -> str:
        return f"Part(text={self.text}, inline_data={self.inline_data})"


class Blob:
    r"""Inline data.

    Attributes:
        mime_type (``str``):
            The MIME type of the data.
        data (``bytes``):
            The data itself.
    """

    def __init__(self, mime_type: str, data: bytes):
        self.mime_type = mime_type
        self.data = data

    @classmethod
    def from_pb(cls, pb: protos.Blob) -> "Blob":
        return cls(mime_type=pb.mime_type, data=pb.data)


class Candidate:
    r"""A candidate from the model.

    Attributes:
        parts (``Sequence[Part]``):
            The parts of the candidate.
        safety_ratings (``Sequence[SafetyRating]``):
            Safety ratings for the candidate.
        citation_metadata (``Optional[CitationMetadata]``):
            Citation metadata for the candidate.
        finish_reason (``str``):
            The reason the model stopped generating.
        finish_message (``str``):
            The message associated with the finish reason.
        index (``int``):
            The index of the candidate.
    """

    def __init__(
        self,
        parts: Sequence[Part],
        safety_ratings: Sequence[SafetyRating],
        citation_metadata: Optional[CitationMetadata],
        finish_reason: str,
        finish_message: str,
        index: int,
    ):
        self.parts = parts
        self.safety_ratings = safety_ratings
        self.citation_metadata = citation_metadata
        self.finish_reason = finish_reason
        self.finish_message = finish_message
        self.index = index


class StreamingCandidate:
    r"""A candidate from the model.

    Attributes:
        parts (``Sequence[Part]``):
            The parts of the candidate.
        safety_ratings (``Sequence[SafetyRating]``):
            Safety ratings for the candidate.
        citation_metadata (``Optional[CitationMetadata]``):
            Citation metadata for the candidate.
    """

    def __init__(
        self,
        parts: Sequence[Part],
        safety_ratings: Sequence[SafetyRating],
        citation_metadata: Optional[CitationMetadata],
    ):
        self.parts = parts
        self.safety_ratings = safety_ratings
        self.citation_metadata = citation_metadata


class HarmCategory(str):
    HARM_CATEGORY_UNSPECIFIED = "HARM_CATEGORY_UNSPECIFIED"
    HARM_CATEGORY_DEROGATORY = "HARM_CATEGORY_DEROGATORY"
    HARM_CATEGORY_TOXICITY = "HARM_CATEGORY_TOXICITY"
    HARM_CATEGORY_VIOLENCE = "HARM_CATEGORY_VIOLENCE"
    HARM_CATEGORY_SEXUAL = "HARM_CATEGORY_SEXUAL"
    HARM_CATEGORY_HATE_SPEECH = "HARM_CATEGORY_HATE_SPEECH"
    HARM_CATEGORY_HARASSMENT = "HARM_CATEGORY_HARASSMENT"
    HARM_CATEGORY_DANGEROUS_CONTENT = "HARM_CATEGORY_DANGEROUS_CONTENT"


class HarmProbability(str):
    HARM_PROBABILITY_UNSPECIFIED = "HARM_PROBABILITY_UNSPECIFIED"
    NEGLIGIBLE = "NEGLIGIBLE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


def _ranking_from_safety_feedback(feedback: protos.SafetyFeedback) -> str:
    return feedback.rating


def _safety_rating_from_proto(rating: protos.SafetyRating) -> SafetyRating:
    return SafetyRating(
        category=rating.category.name,
        probability=rating.probability.name,
    )


def _citation_metadata_from_proto(
    metadata: protos.CitationMetadata,
) -> CitationMetadata:
    return CitationMetadata(
        citation_sources=[
            CitationSource(
                start_index=source.start_index,
                end_index=source.end_index,
                uri=source.uri,
                license=source.license,
            )
            for source in metadata.citation_sources
        ]
    )


def _candidate_from_proto(candidate: protos.Candidate) -> Candidate:
    return Candidate(
        parts=[Part.from_pb(part) for part in candidate.content.parts],
        safety_ratings=[
            _safety_rating_from_proto(rating)
            for rating in candidate.safety_ratings
        ],
        citation_metadata=(
            _citation_metadata_from_proto(candidate.citation_metadata)
            if candidate.HasField("citation_metadata")
            else None
        ),
        finish_reason=candidate.finish_reason.name,
        finish_message=candidate.finish_message,
        index=candidate.index,
    )


def _streaming_candidate_from_proto(candidate: protos.Candidate) -> StreamingCandidate:
    return StreamingCandidate(
        parts=[Part.from_pb(part) for part in candidate.content.parts],
        safety_ratings=[
            _safety_rating_from_proto(rating)
            for rating in candidate.safety_ratings
        ],
        citation_metadata=(
            _citation_metadata_from_proto(candidate.citation_metadata)
            if candidate.HasField("citation_metadata")
            else None
        ),
    )


def _content_filter_from_proto(filter: protos.ContentFilter) -> ContentFilter:
    return ContentFilter(reason=filter.reason.name, index=filter.index)


class HarmBlockThreshold(str):
    BLOCK_NONE = "BLOCK_NONE"
    BLOCK_LOW_AND_ABOVE = "BLOCK_LOW_AND_ABOVE"
    BLOCK_MEDIUM_AND_ABOVE = "BLOCK_MEDIUM_AND_ABOVE"
    BLOCK_ONLY_HIGH = "BLOCK_ONLY_HIGH"


class Response:
    def __init__(
        self,
        response: protos.GenerateContentResponse,
        raw: Optional[protos.GenerateContentResult] = None,
    ):
        self._response = response
        self._raw = raw

    @property
    def prompt_feedback(self) -> Optional[PromptFeedback]:
        if not self._response.prompt_feedback:
            return None

        return PromptFeedback(
            safety_ratings=[
                _safety_rating_from_proto(rating)
                for rating in self._response.prompt_feedback.safety_ratings
            ]
        )

    @property
    def candidates(self) -> Sequence[Candidate]:
        return [_candidate_from_proto(candidate) for candidate in self._response.candidates]

    @property
    def filters(self) -> Sequence[ContentFilter]:
        return [_content_filter_from_proto(filter) for filter in self._response.filters]


class ChatSessionResponse:
    def __init__(self, response: protos.GenerateContentResponse):
        self._response = response

    @property
    def prompt_feedback(self) -> Optional[PromptFeedback]:
        if not self._response.prompt_feedback:
            return None

        return PromptFeedback(
            safety_ratings=[
                _safety_rating_from_proto(rating)
                for rating in self._response.prompt_feedback.safety_ratings
            ]
        )

    @property
    def last(self) -> Optional[Candidate]:
        if not self._response.candidates:
            return None
        return _candidate_from_proto(self._response.candidates[-1])

    @property
    def filters(self) -> Sequence[ContentFilter]:
        return [_content_filter_from_proto(filter) for filter in self._response.filters]


class StreamResponse:
    def __init__(
        self,
        iter: Union[
            Sequence[protos.GenerateContentResponse],
            Sequence[protos.GenerateContentResult],
        ],
    ):
        self._iter = iter

    def __iter__(self):
        return self

    def __next__(self) -> StreamingGenerationChunk:
        try:
            chunk = next(self._iter)
        except StopIteration:
            raise StopIteration

        if isinstance(chunk, protos.GenerateContentResponse):
            if not chunk.candidates:
                return StreamingGenerationChunk(text="")

            candidate = chunk.candidates[0]

            if not candidate.content.parts:
                return StreamingGenerationChunk(text="")

            return StreamingGenerationChunk(
                text=candidate.content.parts[0].text,
                safety_ratings=[
                    _safety_rating_from_proto(rating)
                    for rating in candidate.safety_ratings
                ],
                citation_metadata=(
                    _citation_metadata_from_proto(candidate.citation_metadata)
                    if candidate.HasField("citation_metadata")
                    else None
                ),
            )

        # Handle streaming streaming, only used by the REST backend.
        candidate = chunk.generation_result
        part = candidate.content.parts[0]

        # This is because some protos come back without this field being set.
        # See b/300889781.
        part_type = protos.Part.pb(part).WhichOneof("data")
        if part_type == "text":
            text = part.text
        else:
            text = ""

        return StreamingGenerationChunk(
            text=text,
            safety_ratings=[
                _safety_rating_from_proto(rating)
                for rating in candidate.safety_ratings
            ],
            citation_metadata=(
                _citation_metadata_from_proto(candidate.citation_metadata)
                if candidate.HasField("citation_metadata")
                else None
            ),
        )
